# Protocolo PRISMA-trAIce

Instantánea de la lista de verificación de 17 ítems de PRISMA-trAIce para el reporte transparente de IA en revisiones sistemáticas de literatura.

## Leyenda de niveles

| Nivel | Comportamiento en FALLO |
|---|---|
| Obligatorio (M) | **Bloqueo**: el pipeline se detiene; el usuario debe rellenar datos o usar la escalera de anulación. |
| Altamente Recomendado (HR) | **Advertencia**: se muestra en el punto de control; el usuario puede omitirlo. |
| Recomendado (R) | **Información**: se registra en el informe de cumplimiento. |
| Opcional (O) | **Información**: igual que R. |

## Ítems (Resumen)

### T1 — Título
**Nivel:** Opcional
Indicar el uso de IA en el título o subtítulo si jugó un papel sustancial.

### A1 — Resumen (Abstract)
**Nivel:** Opcional
Resumir brevemente las herramientas de IA y las etapas de la revisión donde se aplicaron.

### I1 — Introducción
**Nivel:** Recomendado
Declarar brevemente la razón de usar IA para tareas específicas.

### M1 — Registro del protocolo
**Nivel:** Obligatorio
Declarar si el uso de IA fue pre-especificado en un protocolo y documentar desviaciones.

### M2 — Identificación de la herramienta y acceso
**Nivel:** Obligatorio
Especificar nombre, versión y proveedor de cada herramienta.

### M3 — Propósito y etapa
**Nivel:** Obligatorio
Describir la etapa específica de la SLR y la tarea precisa que realizó la IA.

### M4 — Datos de entrada
**Nivel:** Obligatorio
Describir los datos proporcionados a la IA (ej. datos de entrenamiento).

### M5 — Datos de salida
**Nivel:** Obligatorio
Describir el formato de salida (ej. JSON, puntuaciones) y post-procesamiento.

### M6 — Ingeniería de prompts
**Nivel:** Obligatorio
Informar el proceso de ingeniería de prompts, los prompts completos y parámetros clave.

### M8 — Interacción humano-IA
**Nivel:** Obligatorio
Describir la interacción humana (número de revisores, proceso de verificación).

### M9 — Métodos de evaluación del desempeño
**Nivel:** Obligatorio
Describir los métodos usados para evaluar el desempeño de la IA (métricas, estándares).

### R1 — Selección de estudios (asistida por IA)
**Nivel:** Obligatorio
En el diagrama de flujo PRISMA, distinguir entre registros manejados por IA vs humanos.

### R2 — Métricas de desempeño de IA (resultados)
**Nivel:** Obligatorio
Informar los resultados de las evaluaciones de desempeño (ej. tasas de acuerdo).

### D1 — Limitaciones del uso de IA
**Nivel:** Recomendado
Discutir limitaciones (sesgos, alucinaciones) y su impacto.
