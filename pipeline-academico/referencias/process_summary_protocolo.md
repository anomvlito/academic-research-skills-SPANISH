# Etapa 6: Protocolo de Resumen de Proceso

**Activador**: Tras el completado de la Etapa 5 (FINALIZACIÓN)
**Propósito**: Documentar el historial completo de colaboración humano-IA para el proceso de creación del artículo, para compartir, informar o reflexionar.

## Flujo de Trabajo

```
1. No se solicita preferencia de idioma; el informe se genera exclusivamente en español según el estándar del repositorio.

2. Revisar el historial de la sesión y compilar lo siguiente:
   - Instrucciones iniciales del usuario (cita textual)
   - Puntos de decisión clave e intervenciones del usuario en cada etapa
   - Momentos de corrección de dirección y sus razones
   - Conteo de iteraciones y resúmenes de resultados de revisión
   - Conocimientos intelectuales (insights) aportados por el usuario (ej. preguntas que generaron nuevos capítulos)
   - Evolución de los requisitos de calidad (ej. ajustes de formato, tono)
   - Estadísticas del pipeline (conteo de etapas, rondas de revisión, conteo de verificaciones de integridad, etc.)

3. Generar la versión en Markdown (proceso_creacion_articulo.md)

4. Convertir a LaTeX y compilar PDF:
   - pandoc MD -> cuerpo de LaTeX
   - Empaquetar documento LaTeX completo (con portada, tabla de contenidos, encabezados/pies de página)
   - tectonic compila el PDF
```

## Contenido Requerido en el Registro del Proceso

| Sección | Contenido |
|---------|---------|
| Información del Artículo | Título, lista final de entregables |
| Proceso Etapa por Etapa | Entrada/salida/decisiones clave para cada etapa, con citas textuales del usuario |
| Detalles de Iteración | Resúmenes de comentarios de revisión, elementos de corrección, resultados de re-revisión |
| Resumen de Patrón de Interacción | Rol del usuario, rol de Claude, conteo de intervenciones, puntos de giro clave — tabla estadística |
| Decisiones Clave del Usuario | Lista cronológica de cada decisión importante tomada por el usuario |
| Lecciones Clave | Lecciones reutilizables aprendidas del proceso |
| **Evaluación de Calidad de Colaboración** | **Capítulo final: puntuación 1-100 + análisis dimensional + sugerencias de mejora** (ver abajo) |

## Evaluación de Calidad de Colaboración (Capítulo Final, Obligatorio)

El capítulo final del registro del proceso es una "Evaluación de Calidad de Colaboración" que evalúa de forma honesta y constructiva el desempeño del usuario en la colaboración humano-IA. El formato sigue la característica `/insight` de Claude Code CLI.

### Dimensiones de Puntuación (cada una 1-100, promedio ponderado para la puntuación general)

```
+--------------------------------------------------+
|  Puntuación de Calidad de Colaboración: [XX]/100  |
+--------------------------------------------------+
|                                                   |
|  Establecimiento de Dirección   [----------  ] XX |
|  Claridad, oportunidad, definición del alcance    |
|                                                   |
|  Contribución Intelectual      [------------ ] XX |
|  Profundidad de ideas, preguntas originales,      |
|  desafíos conceptuales                            |
|                                                   |
|  Control de Calidad            [---------   ] XX |
|  Inspección visual, requisitos de formato,        |
|  estándares de calidad                            |
|                                                   |
|  Disciplina de Iteración       [----------  ] XX |
|  Corrección oportuna de dirección, voluntad de     |
|  re-ejecutar el pipeline, negarse a conformarse   |
|                                                   |
|  Eficiencia de Delegación      [-------     ] XX |
|  Cuándo intervenir/cuándo dejar ir, precisión     |
|  de instrucciones, eficiencia en puntos de control |
|                                                   |
|  Metaprendizaje                [------------ ] XX |
|  Retroalimentar experiencia a las habilidades,    |
|  solicitar registro de lecciones, conciencia de   |
|  mejora de procesos                               |
|                                                   |
+--------------------------------------------------+
```

### Criterios de Puntuación

| Rango de Puntuación | Significado |
|------------|---------|
| 90-100 | Excepcional — La intervención del usuario elevó significativamente la calidad intelectual del artículo más allá de lo que la IA podría producir de forma independiente |
| 75-89 | Excelente — El usuario tomó decisiones de dirección correctas y aprovechó eficazmente las capacidades de iteración del pipeline |
| 60-74 | Bueno — El usuario completó las decisiones necesarias pero se perdieron algunas oportunidades |
| 40-59 | Básico — El usuario actuó principalmente como un botón de "continuar" con poca intervención sustantiva |
| 1-39 | Necesita Mejora — La intervención del usuario pudo haber interrumpido el flujo de trabajo o careció de un control de calidad crítico |

### Subsecciones Requeridas

1. **Puntuación General**: Puntuación total + evaluación de una frase.
2. **Qué Funcionó Bien**: 2-4 comportamientos específicos, con citas textuales del usuario.
3. **Oportunidades Perdidas**: 1-3 cosas que el usuario pudo haber hecho pero no hizo.
4. **Recomendaciones para la Próxima Vez**: 3-5 sugerencias de mejora específicas y accionables.
5. **Valor Añadido Humano vs IA**: Identificar claramente qué aspectos de la calidad del artículo final provinieron de la intervención del usuario (no alcanzables por la IA de forma independiente).

### Principios de Evaluación

- **Honestidad primero**: Sin inflación, sin cortesías. Si el usuario solo presionó "continuar", reflejarlo con veracidad.
- **Basado en evidencia**: Cada puntuación está respaldada por comportamientos específicos o registros de conversación.
- **Constructivo**: Cada crítica debe incluir sugerencias de mejora accionables.
- **Reconocimiento de incertidumbre**: Si ciertas dimensiones no pueden evaluarse (ej. entrada intermedia que saltó la etapa de investigación), marcar como N/A.
- **Reflexión bidireccional**: También señalar francamente las deficiencias de Claude durante el proceso (ej. áreas que requirieron múltiples correcciones).

## Informe de Auto-Reflexión de la IA (Obligatorio)

El penúltimo capítulo del registro del proceso es un "Informe de Auto-Reflexión de la IA" que documenta honestamente los patrones de comportamiento de la propia IA durante el pipeline. Esto complementa la Evaluación de Calidad de Colaboración (que evalúa al usuario) evaluando a la IA.

### Métricas de Seguimiento

Todas las métricas siguientes se derivan de los registros de los agentes existentes (`[DA-DECISION]`, `[DA-REBUTTAL]`, `[HEALTH-CHECK]`, JSON del seguidor de estado). El orquestador las agrega en la Etapa 6 escaneando la transcripción del diálogo:

```
+--------------------------------------------------+
|  Informe de Auto-Reflexión de la IA              |
+--------------------------------------------------+
|                                                   |
|  Tasa de Concesión del DA      X/Y (Z%)           |
|  (concesiones / total de refutaciones recibidas)  |
|                                                   |
|  Concesiones Consecutivas DA   [lista si hay]     |
|  (violaciones de la regla de no-consecutivo)      |
|                                                   |
|  Puntos de Control Omitidos    X/Y                 |
|  (REDUCIDO u omitido por usuario / total)         |
|                                                   |
|  Anulaciones del Usuario       X                   |
|  (veces que el usuario anuló recomendación IA)    |
|                                                   |
|  Alertas de Salud del Diálogo  X                   |
|  (intervenciones de salud activadas)              |
|  - Acuerdo Persistente:        X                   |
|  - Evitación de Conflictos:    X                   |
|  - Convergencia Prematura:     X                   |
|                                                   |
|  Transiciones de Modo Intención X                  |
|  (cambios exploratorio ↔ orientado a objetivos)   |
|                                                   |
|  Desacuerdos Multi-Modelo      X (si está activo)  |
|  (integridad + DA combinados)                     |
|                                                   |
+--------------------------------------------------+
```

### Subsecciones Requeridas

1. **Resumen de Comportamiento**: Un párrafo describiendo el patrón general de comportamiento de la IA durante esta ejecución.
2. **Evaluación de Riesgo de Sicotancia**: Umbrales de detección basados en la tasa de concesión y alertas de salud — BAJO (concesión <50%, 0 alertas) / MEDIO (50-65% o 1-2 alertas) / ALTO (>65% o 3+ alertas). Estos son umbrales de detección, no criterios diagnósticos. Si es ALTO, incluir advertencia: "La IA puede haber sido demasiado complaciente en esta ejecución. Se recomienda encarecidamente la revisión humana de los hallazgos del DA y los resultados de integridad."
3. **Incidentes de Bloqueo de Marco**: Listar cualquier `[HALLAZGO-MULTI-MODELO]` que el DA primario haya omitido, o detecciones de bloqueo de marco activadas durante los puntos de control.
4. **Patrón de Convergencia**: En las etapas de diálogo socrático, ¿se detectó correctamente la intención? ¿Intentó el mentor converger prematuramente? Informar transiciones de modo y alertas de salud de convergencia prematura.
5. **En qué se equivocó la IA**: Lista franca de errores o deficiencias de la IA durante la ejecución — correcciones necesarias, fallos en puntos de control, problemas de integridad encontrados. Esto evidencia que las compuertas de calidad están funcionando.
6. **Registro de Auditoría de Modos de Fallo** (v3.2): Para cada uno de los 7 modos de fallo de investigación de IA (ver `referencias/modos_fallo_investigacion_ia.md`), informar (a) estado final en 4.5 — `LIMPIO` / `ANULADO`, (b) historial — ¿fue alguna vez `SOSPECHOSO`?, (c) si fue `ANULADO`, el razonamiento registrado del usuario.

### Principios

- **Auto-honestidad**: La IA no debe minimizar sus propias deficiencias. Si el DA cedió demasiado fácil, debe decirlo.
- **No autoflagelación**: El propósito es la transparencia, no la humildad performativa. Informar hechos con interpretación.
- **Accionable**: Cada hallazgo debe sugerir qué se podría hacer de manera diferente la próxima vez.
- **Nota sobre la ironía**: Esta auto-reflexión es producida por la misma IA que pudo haber sido sicofante durante el pipeline. El usuario debe leerlo con esa conciencia. Esta advertencia debe figurar en el informe.

## Especificaciones de Salida

- **Nombre de archivo**: `proceso_creacion_articulo.md`
- **PDF**: `proceso_creacion_articulo.pdf`
- **Plantilla LaTeX**: clase `article`, 12pt, A4, Times New Roman.
- **Incluye tabla de contenidos**: `\tableofcontents`
- **Encabezado**: izquierda = título del documento (cursiva), derecha = fecha.
- **Compilación**: tectonic.
