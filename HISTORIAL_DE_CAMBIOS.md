# Historial de Cambios

Todos los cambios notables en este proyecto serán documentados en este archivo.

## [Sin versión]

## [3.6.5.2] - 2026-04-27

### Cambiado

- **Revisión de la recomendación del Método 4 (claude.ai) en `docs/CONFIGURACION.md`**. El Método 4b (Integración Proyecto + GitHub) se presenta ahora como la ruta recomendada para claude.ai, ya que trae el repositorio al conocimiento del Proyecto para lectura y citación sin perder fidelidad. El Método 4a (Carga de Habilidad Personalizada) se marca ahora explícitamente como **no recomendado para esta suite**, con una justificación que cubre dos razones principales:
  - ARS depende de características de orquestación exclusivas de Claude Code. Cada habilidad dirige 12-13 agentes especializados a través de las herramientas de Tarea / subagente de Claude Code y los Traspasos de archivos del Pasaporte de Materiales que se reanudan entre sesiones.
  - El recorte de los cuatro campos de `description` por debajo del límite de 200 caracteres de claude.ai debilitaría el enrutamiento de Claude Code y Cowork en las plataformas para las que la suite fue construida originalmente.

### Notas

- Parche solo de documentación. Sin cambios en `HABILIDAD.md`, archivos de agentes, esquemas, scripts o pruebas. Los cuatro campos de `description` actuales se mantienen en sus longitudes nativas de Claude Code (440-842 caracteres) para que el enrutamiento en Claude Code y Cowork permanezca intacto.

## [3.6.5.1] - 2026-04-27

### Corregido

- **Rutas de instalación del Método 3 en `docs/CONFIGURACION.md`** — Las opciones A (enlace simbólico) y B (copia) ahora instalan cada una de las cuatro carpetas de habilidades por separado en `~/.claude/skills/<nombre-habilidad>/`, coincidiendo con la convención de descubrimiento de habilidades.
- **Restructuración del Método 4 (claude.ai)** — dividido en Método 4a (Carga de Habilidad Personalizada) y Método 4b (Integración Proyecto + GitHub, modo de conocimiento de respaldo).
- **Terminología de la UI de Cowork** — se reemplazó "pestaña Cowork" / "directorio de trabajo" con las etiquetas actuales de la UI de Cowork.

## [3.6.5] - 2026-04-27

### Añadido

- Integración del consumidor `literature_corpus[]` del Pasaporte de Materiales en la Fase 1 (`investigacion-profunda/agente_bibliografia` + `articulo-academico/agente_estratega_literatura`).
- `pipeline-academico/referencias/consumidores_corpus_literatura.md` — protocolo del consumidor con las cuatro Reglas de Hierro.

### Cambiado

- `shared/esquemas_traspaso.md` Esquema 9 — se eliminó la advertencia de v3.6.4 sobre la integración diferida; reemplazada con una referencia al protocolo del consumidor.

## [3.5.0] - 2026-04-21

### Añadido
- `shared/rubrica_profundidad_colaboracion.md` v1.0 — rúbrica canónica de 4 dimensiones basada en Wang & Zhang (2026).
- `pipeline-academico/agentes/agente_profundidad_colaboracion.md` — agente observador (el equipo de agentes crece de 3 a 4). **Solo consultivo — nunca bloquea la progresión.**

## [3.4.0] - 2026-04-20

### Añadido

- `shared/agentes/agente_cumplimiento.md` — agente único consciente del modo para el cumplimiento de PRISMA-trAIce + RAISE.
- `shared/prisma_trAIce_protocolo.md` — instantánea de 17 ítems de `cqh4046/PRISMA-trAIce` (2025-12-10).

## [3.3] - 2026-04-09

### Añadido — Mejoras inspiradas en PaperOrchestra
- **Verificación de la API de Semantic Scholar** (investigacion-profunda, pipeline-academico): Verificación programática de referencias de Nivel 0 vía API S2.
- **Protocolo Anti-Filtraciones** (articulo-academico, investigacion-profunda): La Directiva de Aislamiento de Conocimiento prioriza los materiales de la sesión sobre la memoria paramétrica del LLM.
- **Verificación de Figuras VLM** (articulo-academico): Verificación opcional de bucle cerrado de figuras renderizadas usando un LLM con capacidad de visión.

## [2.7] - 2026-03-09

### Añadido
- Verificación de Integridad v2.0: Revisión completa anti-alucinaciones.
- Suite completa de habilidades de investigación académica (4 habilidades, 116 archivos).
- Investigación Profunda v2.3 — equipo de investigación de 13 agentes con 7 modos.
- Artículo Académico v2.4 — escritura de artículos con 12 agentes y endurecimiento de LaTeX.
- Revisor de Artículos Académicos v1.4 — revisión por pares multi-perspectiva con rúbricas de calidad.
- Pipeline Académico v2.6 — orquestador de 10 etapas con verificación de integridad.
