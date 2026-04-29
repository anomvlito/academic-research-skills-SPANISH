# Artículo Académico — Equipo de Agentes de Escritura de Artículos Científicos

Herramienta de escritura de artículos académicos de propósito general: un pipeline de 12 agentes que cubre todas las disciplinas.

## Inicio Rápido

**Comando mínimo:**
```
Escribe un artículo sobre el impacto de la IA en el aseguramiento de la calidad.
```

## Flujo de Ejecución

1. **Entrevista de configuración:** tipo de artículo, disciplina, formato de cita.
2. **Búsqueda de literatura.**
3. **Diseño de arquitectura:** estructura del artículo y esquema.
4. **Construcción de argumentos.**
5. **Redacción del borrador completo.**
6. **Cumplimiento de citas.**
7. **Revisión por pares (simulada).**
8. **Formateo de salida:** LaTeX/DOCX/PDF.

## Equipo de Agentes (12 Agentes)

| # | Agente | Rol |
|---|-------|------|
| 1 | `agente_admision` | Entrevista de configuración y detección de traspaso. |
| 5 | `agente_redactor_borrador` | Escritura de secciones y ajuste de registro. |
| 8 | `agente_revisor_pares` | Revisión doble ciego simulada. |
| 12 | `agente_entrenador_revision` | Convierte comentarios de revisores en una hoja de ruta. |

## Modos de Operación (10 Modos)

| Modo | Función |
|------|---------|
| `full` | Artículo completo con figuras. |
| `revision` | Revisa el artículo con control de cambios. |
| `plan` | Guía paso a paso en modo socrático. |
| `disclosure` | Genera declaraciones de uso de IA para revistas. |

## Estándares de Calidad

1. **Cada afirmación debe tener una cita.**
2. **Inclusión obligatoria:** Declaración de disponibilidad de datos, Ética, Contribuciones de autor (CRediT).
3. **Control de calidad de escritura:** Eliminación de términos típicos de IA y openers de relleno.
