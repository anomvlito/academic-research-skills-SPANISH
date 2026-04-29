# Marco RAISE

## Descargo de responsabilidad sobre el alcance (obligatorio)

El alcance oficial de RAISE es la **síntesis de evidencia** (revisión sistemática, meta-análisis, etc.). Cuando ARS aplica los **principios** de RAISE a trabajos que no son de síntesis de evidencia — ej. `articulo-academico completo` en investigación primaria — se trata de una **extensión de principios**, no de un cumplimiento oficial de RAISE. El `agente_cumplimiento` de ARS solo reclamará cumplimiento de RAISE para resultados producidos en los modos de `revision_sistematica` u `otra_sintesis_evidencia`.

## Los Cuatro Principios

Cada principio incluye una definición, un procedimiento de verificación de ARS y criterios de pasa/advertencia/falla.

### Principio 1 — Supervisión humana

**Definición:** La IA en la síntesis de evidencia DEBE usarse con una supervisión humana significativa, no como un reemplazo autónomo.
**Verificación de ARS:** Verificar que el `plan_metodologia` especifique el número de revisores, sus calificaciones y el mecanismo de adjudicación.
**Pasa:** Número de revisores + mecanismo de adjudicación + calificaciones presentes.
**Falla:** Faltan dos o más elementos.

### Principio 2 — Transparencia

**Definición:** Cualquier uso de IA que realice o sugiera juicios DEBE ser informado de manera completa y transparente.
**Verificación de ARS:** Verificar que el manuscrito enumere cada herramienta de IA utilizada, en qué etapa, con prompts, parámetros y versiones.
**Pasa:** Todas las herramientas declaradas están informadas y viceversa.
**Falla:** Varias herramientas no declaradas o falta sistemática de prompts/parámetros.

### Principio 3 — Reproducibilidad

**Definición:** La síntesis de evidencia asistida por IA DEBE ser reproducible a un nivel declarado.
**Verificación de ARS:** Verificar la presencia de `pasaporte.repro_lock` o descripción equivalente (versión del modelo, semillas, prompt).
**Pasa:** Repro_lock presente Y estocasticidad declarada.
**Falla:** Faltan ambos.

### Principio 4 — Adecuación al propósito

**Definición:** Las herramientas de IA DEBE ser elegidas y validadas para tareas específicas, no aplicadas de forma genérica.
**Verificación de ARS:** Verificar que el manuscrito describa por qué se eligió cada herramienta para su tarea específica.
**Pasa:** Justificación por herramienta + al menos 1 referencia de validación.
**Falla:** "Usamos IA para ahorrar tiempo" genérico sin justificación por tarea.

## Matriz completa de 8 roles (Solo modo SR)

Se utiliza cuando `raise.modo == "completo"`. El agente mapea a los usuarios de ARS y a ARS mismo en los roles que ocupan.

### Atribución de roles por defecto:
- Usuario de ARS: Sintetizadores de Evidencia.
- ARS mismo: Equipos de Desarrollo de IA + Metodólogos (rol dual).

#### Rol 1 — Sintetizadores de Evidencia
1. Siguen siendo los responsables finales de la síntesis de evidencia.
2. Informan el uso de IA de forma transparente.
3. Aseguran que se cumplan los estándares éticos y legales.

#### Rol 2 — Equipos de Desarrollo de IA
1. Se adhieren a prácticas de ciencia abierta.
2. Son transparentes sobre las limitaciones e intereses.
3. Se comprometen al aprendizaje y monitoreo continuos.
