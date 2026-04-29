# Habilidades de Investigación Académica para Claude Code

[![Versión](https://img.shields.io/badge/version-v3.6.5-blue)](https://github.com/Imbad0202/academic-research-skills/releases/tag/v3.6.5)
[![Licencia: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Patrocinio](https://img.shields.io/badge/sponsor-Buy%20Me%20a%20Coffee-orange?logo=buy-me-a-coffee)](https://buymeacoffee.com/crucify020v)

Una suite completa de habilidades de Claude Code para investigación académica, que cubre el pipeline completo desde la investigación hasta la publicación.

> **La IA es tu copiloto, no el piloto.** Esta herramienta no escribirá tu artículo por ti. Se encarga del trabajo pesado — buscar referencias, formatear citas, verificar datos, revisar la coherencia lógica — para que puedas concentrarte en las partes que realmente requieren tu cerebro: definir la pregunta, elegir el método, interpretar qué significan los datos y escribir la oración después de "Yo argumento que."
>
> A diferencia de un humanizador, esta herramienta no te ayuda a ocultar que usaste IA. Te ayuda a escribir mejor. La Calibración de Estilo aprende tu voz de trabajos anteriores. El Control de Calidad de Escritura detecta los patrones que hacen que la prosa se sienta generada por máquina. El objetivo es la calidad, no el engaño.

### ¿Por qué humano-en-el-ciclo y no automatización completa?

Lu et al. (2026, *Nature* 651:914-919) construyeron **The AI Scientist** — el primer sistema de investigación de IA totalmente autónomo en publicar un artículo mediante revisión por pares ciega en una sede de ML de primer nivel (taller ICLR 2025, puntuación 6.33/10 frente a la media del taller 4.87). Su sección de Limitaciones enumera los modos de fallo que cualquier pipeline de investigación de IA totalmente autónomo hereda: errores de implementación, resultados alucinados, dependencia de atajos, reformulación de errores como hallazgos, fabricación de metodología, bloqueo de marco y alucinaciones de citas.

ARS se construye sobre la premisa de que **un investigador humano potenciado por IA evita estos modos de fallo mejor que cualquiera de los dos por separado**. Las puertas de integridad de las Etapas 2.5 y 4.5 ejecutan una lista de verificación de bloqueo de 7 modos (ver [`pipeline-academico/referencias/modos_fallo_investigacion_ia.md`](pipeline-academico/referencias/modos_fallo_investigacion_ia.md)); el revisor ofrece un modo de calibración opcional que mide sus propios FNR/FPR frente a un conjunto de referencia proporcionado por el usuario.

La v3.3 se inspiró en [**PaperOrchestra**](https://arxiv.org/abs/2604.05018) (Song, Song, Pfister & Yoon, 2026, Google): verificación de la API de Semantic Scholar, protocolo anti-filtraciones, verificación de figuras VLM y seguimiento de la trayectoria de puntuación.

---

## Arquitectura y Pipeline

**👉 [docs/ARQUITECTURA.md](docs/ARQUITECTURA.md)** — vista completa del pipeline: diagrama de flujo, matriz etapa por etapa, flujo de acceso a datos, grafo de dependencias de habilidades, compuertas de calidad y lista de modos.

El documento de arquitectura reemplaza la extensa descripción del pipeline que solía estar aquí. Todo sobre *qué se ejecuta en qué etapa* ahora vive en un solo lugar.

## Configuración e Instalación

**👉 [docs/CONFIGURACION.md](docs/CONFIGURACION.md)** — instala Claude Code, configura claves API, Pandoc/tectonic opcional para DOCX/PDF, verificación multi-modelo (`ARS_CROSS_MODEL`) y cuatro métodos de instalación, incluyendo la importación de Proyectos de claude.ai.

## Rendimiento y Coste

**👉 [docs/RENDIMIENTO.md](docs/RENDIMIENTO.md)** — presupuestos de tokens por modo, estimación del pipeline completo (~$4–6 para un artículo de 15k palabras) y configuraciones recomendadas de Claude Code (Omitir Permisos; Equipo de Agentes opcional).

## Guías y Artículos

- [La escritura académica no debería ser un acto en solitario](https://open.substack.com/pub/edwardwu223235/p/academic-writing-shouldnt-be-a-solo?r=4dczl&utm_medium=ios) — guía completa del pipeline (Inglés)

---

## Características Principales

- **Investigación Profunda** — Equipo de investigación de 13 agentes con modo guiado socrático, revisión sistemática PRISMA, detección de intención, monitoreo de salud del diálogo, DA multi-modelo opcional y verificación de la API de Semantic Scholar.
- **Artículo Académico** — Escritura de artículos con 12 agentes, calibración de estilo, control de calidad de escritura, endurecimiento de LaTeX, visualización, coaching de revisión, conversión de citas, protocolo anti-filtraciones y verificación de figuras VLM.
- **Revisor de Artículos Académicos** — Revisión por pares multi-perspectiva con 7 agentes y rúbricas de calidad 0–100 (Editor en Jefe + 3 revisores dinámicos + Abogado del Diablo), protocolo de umbral de concesión, preservación de la intensidad del ataque, crítica/calibración DA multi-modelo opcional, matriz de trazabilidad R&R y restricción de solo lectura.
- **Pipeline Académico** — Orquestador de pipeline de 10 etapas con puntos de control adaptativos, verificación de afirmaciones, Pasaporte de Materiales, `repro_lock` opcional, verificación de integridad multi-modelo opcional, refuerzo a mitad de la conversación y seguimiento de la trayectoria de puntuación.
- **Metadatos de Nivel de Acceso a Datos** (v3.3.2+) — cada habilidad declara su `nivel_acceso_datos` (`bruto` / `redactado` / `solo_verificado`); aplicado por `scripts/verificar_nivel_acceso_datos.py`. Patrón adaptado del investigador automatizado w2s de Anthropic (2026). Ver [`shared/patron_aislamiento_verdad_absoluta.md`](shared/patron_aislamiento_verdad_absoluta.md).
- **Anotación de Tipo de Tarea** (v3.3.2+) — cada habilidad declara su `tipo_tarea` (`abierta` o `evaluable_por_resultado`). Todas las habilidades ARS actuales son `abierta`.
- **Esquema de Informe de Benchmarking** (v3.3.5+) — Esquema JSON + linter para comparaciones honestas de benchmarks. Ver [`shared/patron_informe_benchmark.md`](shared/patron_informe_benchmark.md).
- **Bloqueo de Reproducibilidad de Artefactos** (v3.3.5+) — bloque opcional `repro_lock` en el Pasaporte de Materiales. **Documentación de configuración, no garantía de repetición** — las salidas de LLM no son reproducibles bit a bit. Ver [`shared/patron_reproducibilidad_artefacto.md`](shared/patron_reproducibilidad_artefacto.md).

---

## Ejemplos: Salida Real del Pipeline

Consulta los artefactos completos de una ejecución real del pipeline de 10 etapas — informes de revisión por pares, informes de verificación de integridad y el artículo final:

**[Ver todos los artefactos del pipeline →](ejemplos/showcase/)**

| Artefacto | Descripción |
|---|---|
| [Artículo Final (EN)](ejemplos/showcase/articulo_completo_apa7.pdf) | Formateado en APA 7.0, compilado en LaTeX |
| [Informe de Integridad — Pre-Revisión](ejemplos/showcase/informe_integridad_etapa2.5.pdf) | Etapa 2.5: detectó 15 referencias fabricadas + 3 errores estadísticos |
| [Informe de Integridad — Final](ejemplos/showcase/informe_integridad_etapa4.5.pdf) | Etapa 4.5: cero regresiones confirmadas |
| [Ronda de Revisión por Pares 1](ejemplos/showcase/informe_revision_etapa3.pdf) | EIC + 3 Revisores + Abogado del Diablo |
| [Re-Revisión](ejemplos/showcase/informe_rerevision_etapa3prime.pdf) | Verificación tras las correcciones |
| [Ronda de Revisión por Pares 2](ejemplos/showcase/informe_revision_etapa3_r2.pdf) | Seguimiento de la revisión |
| [Respuesta a los Revisores](ejemplos/showcase/respuesta_a_revisores_r2.pdf) | Respuesta punto por punto del autor |
| [Informe de Auditoría Post-Publicación](ejemplos/showcase/auditoria_post_publicacion_2026-03-09.pdf) | Auditoría de referencias completa independiente: encontró 21/68 problemas omitidos por 3 rondas de comprobaciones de integridad |

---

## Complemento: Agente de Experimentos

Si tu investigación implica ejecutar experimentos (código o estudios con humanos) antes de escribir, la habilidad [Agente de Experimentos](https://github.com/Imbad0202/experiment-agent) llena el vacío entre la Etapa 1 de ARS (INVESTIGACIÓN) y la Etapa 2 (ESCRITURA).

```
ARS Etapa 1 INVESTIGACIÓN  →  Informe PI + Plan de Metodología
        ↓
  experiment-agent          →  ejecutar/gestionar experimentos → validar resultados
        ↓
ARS Etapa 2 ESCRITURA      →  escribir artículo con resultados verificados
```

**Qué hace**: ejecuta experimentos de código (Python, R, etc.) con monitoreo en tiempo real, gestiona protocolos de estudio humano con lista de ética IRB, interpreta estadísticas con detección de 11 tipos de falacias y verifica la reproducibilidad.

**Cómo usarlos juntos**: pausa el pipeline de ARS tras la Etapa 1, ejecuta experimentos en una sesión separada del agente de experimentos y luego trae los resultados (con su Pasaporte de Materiales) de vuelta a la Etapa 2 de ARS. ARS no requiere modificación. Consulta el [README del agente de experimentos](https://github.com/Imbad0202/experiment-agent) para instrucciones de configuración.

---

## Uso

### Inicio Rápido

```
# Iniciar un pipeline de investigación completo
Tú: "Quiero escribir un artículo de investigación sobre el impacto de la IA en el aseguramiento de la calidad en educación superior"

# Iniciar con guía socrática
Tú: "Guía mi investigación sobre la IA en la evaluación educativa"

# Escribir un artículo con planificación guiada
Tú: "Guíame para escribir un artículo sobre el declive demográfico"

# Revisar un artículo existente
Tú: "Revisa este artículo" (luego proporciona el artículo)

# Comprobar el estado del pipeline
Tú: "estado"
```

### Habilidades Individuales

#### Investigación Profunda (7 modos)

```
"Investiga el impacto de la IA en la educación superior" → modo completo
"Dame un resumen rápido sobre X"                        → modo rápido
"Haz una revisión sistemática sobre X con PRISMA"      → modo revision-sistematica
"Guía mi investigación sobre X"                        → modo socrático (guiado)
"Verifica estas afirmaciones"                          → modo fact-check
"Haz una revisión de literatura sobre X"               → modo lit-review
"Revisa la calidad de investigación de este artículo"  → modo revisión
```

#### Artículo Académico (10 modos)

```
"Escribe un artículo sobre X"                             → modo completo
"Guíame para escribir un artículo"                        → modo plan (guiado)
"Crea un esquema del artículo"                            → modo solo-esquema
"Tengo un borrador, aquí están los comentarios de revisión" → modo corrección
"Analiza estos comentarios de revisión en una hoja de ruta" → modo revision-coach
"Escribe un resumen para este artículo"                   → modo solo-resumen
"Convierte esto en un artículo de revisión de literatura" → modo lit-review
"Convierte a LaTeX" / "Convierte las citas a IEEE"        → modo format-convert
"Revisa las citas"                                        → modo citation-check
"Genera una declaración de uso de IA para NeurIPS"        → modo declaración
```

#### Revisor de Artículos Académicos (6 modos)

```
"Revisa este artículo"                               → modo completo (EIC + R1/R2/R3 + Abogado del Diablo)
"Evaluación rápida de este artículo"                 → modo rápido
"Guíame para mejorar este artículo"                  → modo guiado
"Revisa la metodología"                              → modo methodology-focus
"Verifica las correcciones"                          → modo re-review
"Calibra este revisor contra mi conjunto de referencia" → modo calibración
```

#### Pipeline Académico (Orquestador)

```
"Quiero escribir un artículo de investigación completo" → pipeline completo desde la Etapa 1
"Ya tengo un artículo, revísalo"                        → entrada intermedia en Etapa 2.5 (primero integridad)
"He recibido comentarios de los revisores"              → entrada intermedia en Etapa 4
```

> El pipeline termina con la **Etapa 6: Resumen del Proceso** — genera automáticamente un registro del proceso de creación del artículo con una Evaluación de Calidad de Colaboración de 6 dimensiones (puntuación 1–100).

### Idiomas Compatibles

- **Español** — idioma por defecto
- **Inglés** — compatible

> **¿Usas otro idioma?** El modo Socrático (*investigacion-profunda*) y el modo Plan (*articulo-academico*) usan **activación basada en intención** — detectan el significado de tu solicitud, no palabras clave específicas. Esto significa que funcionan en **cualquier idioma** sin modificación.

### Formatos de Cita Compatibles

- APA 7.0 (predeterminado)
- Chicago (Notas y Autor-Fecha)
- MLA
- IEEE
- Vancouver

### Estructuras de Artículo Compatibles

- IMRaD (investigación empírica)
- Revisión de Literatura Temática
- Análisis Teórico
- Estudio de Caso
- Informe de Política (Policy Brief)
- Artículo de Conferencia

---

## Detalles de las Habilidades

Las responsabilidades por agente y los artefactos por etapa están ahora en [`docs/ARQUITECTURA.md`](docs/ARQUITECTURA.md). Los números de versión están anclados aquí para que los metadatos de versiones permanezcan en un solo lugar.

### Investigación Profunda (v2.8)

Equipo de investigación de 13 agentes. Modos: completo, rápido, revisión, lit-review, fact-check, socrático, revision-sistematica. Lista completa de agentes y artefactos: ver ARQUITECTURA.md §3.

### Artículo Académico (v3.0)

Pipeline de escritura de artículos de 12 agentes. Modos: completo, plan, solo-esquema, corrección, revision-coach, solo-resumen, lit-review, format-convert, citation-check, declaración. Salida: MD + DOCX (vía Pandoc cuando esté disponible) + LaTeX (clase APA 7.0 `apa7` / IEEE / Chicago) → PDF vía tectonic. Responsabilidades por fase y lista de agentes: ver ARQUITECTURA.md §3.

### Revisor de Artículos Académicos (v1.8)

Revisión multi-perspectiva de 7 agentes con **rúbricas de calidad 0-100**. Modos: completo, re-review, rápido, methodology-focus, guiado, calibración. **Mapeo de decisiones:** ≥80 Aceptar, 65-79 Corrección Menor, 50-64 Corrección Mayor, <50 Rechazar. Límites del equipo de revisión: ver ARQUITECTURA.md §3 Etapa 3 / Etapa 3'.

### Pipeline Académico (v3.6)

Orquestador de 10 etapas con verificación de integridad, revisión en dos etapas, coaching socrático y evaluación de colaboración. Garantías del pipeline: cada etapa requiere un punto de control de confirmación del usuario; la verificación de integridad (Etapa 2.5 + 4.5) no puede omitirse; la Matriz de Trazabilidad R&R (Esquema 11) verifica independientemente las afirmaciones de corrección del autor. La v3.4 añadió el Agente de Cumplimiento (PRISMA-trAIce + RAISE) en las Etapas 2.5 / 4.5. La v3.5 añade el **Observador de Profundidad de Colaboración** (`agente_profundidad_colaboracion`, solo consultivo — nunca bloquea) en cada punto de control COMPLETO/REDUCIDO y al finalizar el pipeline. Matriz etapa por etapa con agentes, artefactos y compuertas: ver ARQUITECTURA.md §3.

---

## Optimizaciones v3.0: Lo que Descubrimos sobre los Límites Estructurales de la IA

### Qué pasó

Mientras usábamos ARS para escribir un artículo de reflexión sobre la IA en la educación superior, nos encontramos con tres problemas estructurales que ninguna cantidad de ingeniería de prompts pudo solucionar:

1. **Bloqueo de marco**: Le pedimos a la IA que realizara un debate de abogado del diablo contra su propia tesis. Lo hizo — cuatro rondas, cada una más refinada que la anterior. Pero cada ronda se quedó dentro del marco que habíamos establecido. El DA atacaba los argumentos, nunca las premisas. Nunca preguntó "¿estamos siquiera discutiendo la pregunta correcta?". Este es el mismo patrón que causó la tasa de error de citas del 31% en la prueba de estrés de la v2.7: la IA que verifica y la IA que genera comparten el mismo marco cognitivo.

2. **Sicotancia ante el rechazo**: Cada vez que desafiábamos los ataques del DA, este cedía demasiado rápido. Se retractaba de los hallazgos más rápido de lo que los lanzaba. El entrenamiento del modelo premia la armonía conversacional — así que "el usuario rechazó la idea" se trataba como evidencia de que el ataque estaba equivocado, cuando a menudo solo significaba que el usuario era persistente.

3. **Error de detección de intención**: El Mentor Socrático seguía intentando converger y producir entregables ("¿Quieres que escriba esto?") cuando aún estábamos explorando. No podía distinguir entre "el usuario quiere una discusión filosófica profunda" y "el usuario quiere un informe de PI". Ambos parecen compromiso, pero necesitan comportamientos de IA opuestos.

### Qué cambiamos (v3.0)

**Abogado del Diablo — Protocolo de Umbral de Concesión** (`investigacion-profunda` + `revisor-articulo-academico`)
- El DA debe ahora puntuar cada refutación en una escala del 1 al 5 antes de responder.
- La concesión solo se permite con una puntuación ≥4 (la refutación aborda directamente el ataque central con evidencia).
- Puntuación ≤3: mantener la posición y reafirmar el ataque original.
- Reglas anti-sicotancia: no se permiten concesiones consecutivas, seguimiento de la tasa de concesión, detección de bloqueo de marco tras cada punto de control.

**Mentor Socrático — Capa de Detección de Intención** (`investigacion-profunda`)
- Clasifica la intención del usuario como exploratoria frente a orientada a objetivos al inicio del diálogo y cada 3 turnos.
- Modo exploratorio: desactiva la autoconvergencia, eleva el máximo de rondas a 60, prohíbe avisos de "¿quieres que resuma?".
- Modo orientado a objetivos: comportamiento de convergencia estándar.
- Reglas anti-cierre-prematuro: en modo exploratorio, el usuario decide cuándo parar.

**Mentor Socrático — Indicador de Salud del Diálogo** (`investigacion-profunda`)
- Autoevaluación silenciosa cada 5 turnos en tres dimensiones: acuerdo persistente, evitación de conflictos, convergencia prematura.
- Inyecta automáticamente preguntas desafiantes cuando se detecta un patrón de acuerdo.
- Invisible para el usuario (para evitar el "juego"), pero el registro está disponible para la revisión post-sesión.

### Por qué esto importa

Estas optimizaciones no resuelven los límites estructurales de la IA — hacen que los límites sean visibles y manejables. El DA eventualmente seguirá cediendo si se le presiona lo suficiente. El Mentor Socrático seguirá teniendo cierto sesgo de convergencia. Pero ahora hay puntos de control explícitos que frenan la sicotancia, fuerzan al DA a justificar las concesiones y evitan que el Mentor cierre el tema antes de que el usuario esté listo.

La lección más profunda: la alfabetización en IA no se trata de aprender a usar la IA como herramienta, seguir reglas éticas o temer los riesgos de la IA. Se trata de interactuar con la IA con la profundidad suficiente para descubrir sus límites estructurales por ti mismo — y tus propios límites de pensamiento en el proceso.

---

## Licencia

Este trabajo está bajo la licencia [CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).

**Eres libre de:**
- Compartir — copiar y redistribuir el material.
- Adaptar — remezclar, transformar y construir sobre el material.

**Bajo los siguientes términos:**
- **Atribución** — Debes dar el crédito apropiado.
- **No Comercial** — No puedes usar el material con fines comerciales.

**Formato de atribución:**
```
Basado en Academic Research Skills por Cheng-I Wu
https://github.com/Imbad0202/academic-research-skills
```

---

## Colaboradores

**Cheng-I Wu** — Autor y mantenedor.

**[aspi6246](https://github.com/aspi6246)** — Colaborador. La optimización v3.1 se inspiró en patrones de [Claude-Code-Skills-for-Academics](https://github.com/aspi6246/Claude-Code-Skills-for-Academics).

**[mchesbro1](https://github.com/mchesbro1)** — Colaborador. Propuso y redactó originalmente el "Basket of 8" de revistas de IS.

**[cloudenochcsis](https://github.com/cloudenochcsis)** — Colaborador. Extendió la sección de IS al "Senior Scholars' Basket of 11".

---

## Registro de Cambios

### v3.6.5 (2026-04-27) — Integración del Consumidor `literature_corpus[]` en el Pasaporte de Materiales

- **Dos consumidores de literatura de la Fase 1** conectados: `investigacion-profunda/agentes/agente_bibliografia.md` y `articulo-academico/agentes/agente_estratega_literatura.md`. Ambos siguen el mismo flujo de cinco pasos **primero el corpus, la búsqueda llena el vacío** cuando el pasaporte lleva un `literature_corpus[]` no vacío y las mismas cuatro Reglas de Hierro.
- **Bloque de reproducibilidad PRE-SCREENED** en los informes de Estrategia de Búsqueda: enumera las entradas del corpus incluidas / excluidas / omitidas.
- **Referencia del protocolo del consumidor** en `pipeline-academico/referencias/consumidores_corpus_literatura.md`.
- **Lint de CI** `scripts/verificar_protocolo_consumidor_corpus.py` aplicando nueve invariantes del protocolo.

### v3.6.4 (2026-04-25) — Puerto de Entrada `literature_corpus[]` en el Pasaporte de Materiales

- **Campo `literature_corpus[]`** añadido al Esquema 9 como puerto de entrada opcional para literatura del usuario.
- **Contrato de adaptador neutral al idioma** en `pipeline-academico/referencias/adaptadores/resumen.md`.
- **Tres adaptadores de Python de referencia** bajo `scripts/adaptadores/`: `escaneo_carpetas.py`, `zotero.py`, `obsidian.py`.
- **Contrato de registro de rechazos** en `shared/contracts/passport/rejection_log.schema.json`.

### v3.6.3 (2026-04-23) — Límite de Reinicio del Pasaporte Opcional

- **Límite de reinicio del pasaporte opcional** (`ARS_PASSPORT_RESET=1`). Convierte cada punto de control COMPLETO en un límite de reinicio de contexto.
- El Esquema 9 gana un libro mayor `reset_boundary[]` de solo anexión. El hash usa JSON Canonical Form + SHA-256.
- Nuevo lint de CI `scripts/verificar_contrato_reinicio_pasaporte.py`.
- Documento del protocolo: `pipeline-academico/referencias/pasaporte_como_limite_reinicio.md`.

### v3.5.0 (2026-04-21) — Observador de Profundidad de Colaboración

- **Nuevo agente**: `agente_profundidad_colaboracion` en `pipeline-academico`. Invocado en cada punto de control COMPLETO/REDUCIDO y al finalizar el pipeline; puntúa la colaboración usuario-IA contra una rúbrica de 4 dimensiones. **Solo consultivo — nunca bloquea la progresión.**
- **Nueva rúbrica**: [`shared/rubrica_profundidad_colaboracion.md`](shared/rubrica_profundidad_colaboracion.md) v1.0. Basado en Wang & Zhang (2026).
- `pipeline-academico` versión de HABILIDAD: `3.3.0 → 3.4.0`. Versión de la suite subida a `3.5.0`.

### v3.3.2 (2026-04-15) — Niveles de Acceso a Datos + Metadatos de Tipo de Tarea

- Añadido `metadata.nivel_acceso_datos` a todos los archivos `HABILIDAD.md` con vocabulario obligatorio: `bruto`, `redactado`, `solo_verificado`.
- Añadido `metadata.tipo_tarea` a todos los archivos `HABILIDAD.md` con vocabulario obligatorio: `abierta`, `evaluable_por_resultado`.

### v3.0 (2026-04-03) — Anti-Sicotancia + Detección de Intención + Salud del Diálogo

- **Umbral de Concesión del Abogado del Diablo** (investigacion-profunda + revisor-articulo-academico): El DA debe puntuar las refutaciones 1-5 antes de responder.
- **Preservación de la Intensidad del Ataque** (revisor-articulo-academico): El DA no se ablanda ante el rechazo.
- **Capa de Detección de Intención** (investigacion-profunda socrático): Clasifica la intención del usuario como exploratoria frente a orientada a objetivos.
- **Indicador de Salud del Diálogo** (investigacion-profunda socrático): Autoverificación silenciosa cada 5 turnos.

### v2.0 (2026-02)

- **pipeline-academico v2.0**: de 5 a 9 etapas, verificación de integridad obligatoria, revisión en dos etapas, coaching de revisión socrático.
- **revisor-articulo-academico v1.1**: +Abogado del Diablo (7º agente), +modo re-review, +coaching socrático post-revisión.
- Nuevo agente: `agente_verificacion_integridad` — verificación 100% de referencias/datos con rastro de auditoría.
- Nuevo agente: `agente_revisor_abogado_diablo` — desafiador de tesis de 8 dimensiones.

### v1.0 (2026-02)

- Lanzamiento inicial.
- investigacion-profunda v2.0 (10 agentes, 6 modos incluyendo socrático).
- articulo-academico v2.0 (10 agentes, 8 modos incluyendo plan).
- revisor-articulo-academico v1.0 (6 agentes, 4 modos incluyendo guiado).
- pipeline-academico v1.0 (orquestador).
