# Notas de Rendimiento de ARS

> **Modelo recomendado: Claude Opus 4.7** con **plan Max** (o configuración equivalente). Opus 4.7 utiliza pensamiento adaptativo; ya no es necesario establecer un presupuesto de pensamiento fijo.
>
> El pipeline académico completo (10 etapas) consume una **gran cantidad de tokens** — una sola ejecución de extremo a extremo puede superar los 200K tokens de entrada + 100K de salida, dependiendo de la longitud del artículo y las rondas de corrección. Planifica tu presupuesto en consecuencia.
>
> Las habilidades individuales (ej. `investigacion-profunda` sola, o `articulo-academico-revisor` solo) consumen significativamente menos.

## Uso estimado de tokens por modo

| Habilidad / Modo | Tokens de Entrada | Tokens de Salida | Costo Estimado (Opus 4.7) |
|---|---|---|---|
| `investigacion-profunda` socrático | ~30K | ~15K | ~$0.60 |
| `investigacion-profunda` completo | ~60K | ~30K | ~$1.20 |
| `investigacion-profunda` revision-sistematica | ~100K | ~50K | ~$2.00 |
| `articulo-academico` plan | ~40K | ~20K | ~$0.80 |
| `articulo-academico` completo | ~80K | ~50K | ~$1.80 |
| `articulo-academico-revisor` completo | ~50K | ~30K | ~$1.10 |
| `articulo-academico-revisor` rapido | ~15K | ~8K | ~$0.30 |
| **Pipeline completo (10 etapas)** | **~200K+** | **~100K+** | **~$4-6** |
| + Verificación multi-modelo | +~10K (ext) | +~5K (ext) | +~$0.60-1.10 |

*Estimaciones basadas en un artículo de ~15,000 palabras con ~60 referencias. El uso real varía con la longitud del artículo, las rondas de corrección y la profundidad del diálogo. Costos según precios de la API de Anthropic a abril de 2026.*

## Configuraciones recomendadas de Claude Code

| Ajuste | Qué hace | Cómo habilitarlo | Docs |
|---|---|---|---|
| **Equipo de Agentes** (opcional) | Habilita herramientas `TeamCreate` / `SendMessage` para coordinación manual multi-agente. **La paralelización interna de ARS no requiere esta bandera** — las habilidades generan subagentes vía la herramienta `Agent` directamente. | Establecer `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` | Característica experimental |
| **Omitir Permisos** | Omite las solicitudes de confirmación por herramienta, permitiendo una ejecución autónoma ininterrumpida en todas las etapas del pipeline. | Iniciar con `claude --dangerously-skip-permissions` | [Permisos](https://docs.anthropic.com/en/docs/claude-code/cli-reference) |

> **⚠️ Omitir Permisos**: Esta bandera desactiva todos los diálogos de confirmación de uso de herramientas. Úsalo bajo tu propia discreción — es conveniente para pipelines de larga duración, pero elimina la red de seguridad de la aprobación manual. Solo habilítalo en entornos donde te sientas cómodo con que Claude ejecute lecturas, escrituras y comandos de shell sin preguntar primero.

## Gestión de sesiones de larga duración

El pipeline académico completo está diseñado para la ejecución con humano-en-el-ciclo, con confirmación obligatoria del usuario en cada etapa. En la práctica, una ejecución completa a menudo abarca de horas a días — más tiempo que el TTL del caché de prompts de Anthropic (5 minutos). Dos consecuencias:

1. **Los fallos de caché entre puntos de control son normales.** Cuando un punto de control de etapa se pausa por más de 5 minutos, la siguiente etapa lee su contexto sin caché. Este es un costo inevitable de los pipelines con ritmo humano.
2. **La reanudación entre sesiones depende del Pasaporte de Materiales.** ARS no mantiene su propio estado de orquestador entre sesiones. Para reanudar en una nueva sesión, pega tu YAML del Pasaporte de Materiales; el orquestador lee el `historial_cumplimiento[]` y los marcadores de completado de etapa para localizar tu punto de interrupción.

### Costo del revisor del Contrato de Sprint v3.6.2

La compuerta del contrato de sprint del Esquema 13 divide la ejecución de cada agente revisor en Fase 1 (ciego al contenido, compromete plan de puntuación) + Fase 2 (revisión visible). Para los modos que usan plantillas (`completo` panel 5 + `foco-metodologia` panel 2), cada revisor cuesta aproximadamente dos turnos de LLM en lugar de uno.

| Habilidad / Modo | Efecto en tokens | Notas |
|---|---|---|
| `articulo-academico-revisor completo` | ~+30-40% entrada + pequeño aumento salida por revisor × 5 | Cada revisor lee la plantilla del contrato + metadatos en Fase 1, luego el artículo completo en Fase 2 |
| `articulo-academico-revisor foco-metodologia` | Misma forma, panel 2 | Dos revisores (EIC + metodología) ejecutan cada uno dos fases |
| Sintetizador (siempre uno) | +~2-3K entrada | Lee el contrato + salidas de los revisores para ejecutar el protocolo mecánico de tres pasos |

### Costo del agente de cumplimiento v3.4.0

Añadir al `agente_cumplimiento` a la Etapa 2.5 y Etapa 4.5 aumenta los tokens del pipeline completo en aproximadamente:

| Habilidad / Modo | Tokens Entrada | Tokens Salida | Costo Estimado |
|---|---|---|---|
| `investigacion-profunda systematic-review` (2.5 solo) | +~5–8K | +~3–5K | +~$0.15 |
| Pipeline completo SR (2.5 + 4.5) | +~10–15K | +~5–8K | +~$0.30 |
| `articulo-academico completo` (pre-finalización) | +~3–5K | +~2–3K | +~$0.08 |

### Límite de reinicio de Pasaporte v3.6.3 (opcional)

Cuando se establece `ARS_PASSPORT_RESET=1`, cada punto de control COMPLETO se convierte en un límite de reinicio de contexto. El flujo de trabajo previsto es:

1. Ejecutar una etapa hasta el punto de control COMPLETO en la sesión A.
2. Copiar la etiqueta `[REINICIO-PASAPORTE: hash=<hash>, etapa=<completada>, siguiente=<siguiente>]`.
3. Iniciar una nueva sesión de Claude Code (sesión B) y pegar `resume_desde_pasaporte=<hash>`.
4. La sesión B carga solo el libro mayor del pasaporte; no hay repetición de los turnos de la sesión A. El orquestador localiza la entrada coincidente y continúa.

**Cuándo el reinicio supera a la continuación:**
- Pipelines largos donde la sesión A ha acumulado >100K tokens de contexto que la siguiente etapa no necesita realmente.
- Ejecuciones en modo `systematic-review` donde la independencia de las etapas está claramente definida.
- Cualquier caso donde alcances el TTL de 5 minutos del caché de prompts a mitad del pipeline.

**Cuándo la continuación sigue ganando:**
- Pipelines cortos (< 30K tokens de entrada de extremo a extremo).
- Etapas con estado implícito en la sesión que el pasaporte no captura (ej. una rama de diálogo socrático que el usuario quiere mantener viva).

## Ingestión de corpus de literatura (v3.6.4+)

El campo `literature_corpus[]` del Pasaporte de Materiales es poblado por adaptadores escritos por el usuario, no por ARS mismo. Se incluyen tres adaptadores de referencia en v3.6.4 bajo `scripts/adaptadores/`.

### Postura de rendimiento
- Los adaptadores se ejecutan fuera de banda. Su tiempo de ejecución es responsabilidad del usuario.
- El tamaño de la salida del adaptador crece linealmente con el tamaño del corpus. Una biblioteca de Zotero de 500 entradas produce un pasaporte de ~300 KB. Los consumidores de ARS realizan carga diferida (lazy-load).

### Límites de la capa de ingestión
- No ingiere PDFs, no extrae texto ni ejecuta OCR.
- No llama a APIs web en vivo (Zotero, Notion, etc.).
- No descarga contenido de pago ni usa credenciales institucionales.

### Integración del lado del consumidor (v3.6.5)
A partir de v3.6.5, dos agentes de literatura leen el `literature_corpus[]` vía el flujo **primero-corpus, la búsqueda llena el vacío**. Los informes de Estrategia de Búsqueda ganan un bloque de reproducibilidad PRE-SCREENED que enumera las entradas del corpus incluidas / excluidas / omitidas.

### Costo del consumidor de corpus v3.6.5 (por presencia)
Cuando el Pasaporte de Materiales lleva un `literature_corpus[]` no vacío, la Fase 1 escala con el tamaño del corpus debido a la pre-selección (Paso 1).

| Tamaño del corpus | Pre-selección Paso 1 (por consumidor) | Notas |
|---|---|---|
| Vacío / ausente | 0 | El flujo solo-DB-externa se ejecuta sin cambios |
| ~50 entradas (subconjunto Zotero típico) | +~3-5K entrada + ~1-2K salida | Escaneo de título + resumen |
| ~200 entradas | +~10-15K entrada + ~3-5K salida | El escaneo de títulos domina |
| ~500 entradas (biblioteca grande) | +~25-40K entrada + ~8-12K salida | Considera recortar el corpus antes de emitir el pasaporte |
