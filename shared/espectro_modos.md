# Espectro de Modos: Fidelidad vs Originalidad

**Estado**: v3.2
**Fuente**: Lu et al. (2026, Nature 651:914-919) Figura 1c — el modo basado en plantillas produce artículos de mayor calidad y menor varianza; el modo sin plantillas produce resultados más diversos pero de menor calidad media y mayor varianza. ARS mapea este hallazgo en su propia taxonomía de modos.

---

## Por qué existe este espectro

No todos los modos deben tratar las plantillas y los ejemplos de la misma manera. Una `revision-sistematica` necesita una estructura rígida (lista de verificación PRISMA, secciones predefinidas) — las plantillas son fundamentales. Un diálogo `socratico` necesita espacio para deambular — las plantillas pesadas matan la exploración.

Lu et al. comparan los modos basados en plantillas frente a los libres dándonos un lenguaje para este equilibrio: **fidelidad** (reproducible, cargado de plantillas, menor varianza) vs **originalidad** (exploratorio, ligero de plantillas, mayor varianza, mayor techo de novedad).

Los modos de ARS caen en un espectro entre estos polos. Esta tabla es la referencia para decidir:
- Cuánta plantilla/ejemplo cargar al inicio del modo.
- Si sugerir el modo cuando el objetivo del usuario es un "resultado predecible" vs "exploración creativa".

---

## Tabla del espectro de modos

| Habilidad | Modo | Posición en el espectro | Carga de plantilla | Racional |
|---|---|---|---|---|
| investigacion-profunda | `revision-sistematica` | Fidelidad | Pesada | Protocolo PRISMA, pasos reproducibles |
| investigacion-profunda | `revision-literatura` | Fidelidad | Pesada | Bibliografía anotada estructurada |
| investigacion-profunda | `fact-check` | Fidelidad | Pesada | Pipeline afirmación → evidencia → veredicto |
| investigacion-profunda | `rapido` | Fidelidad | Pesada | Formato fijo de 3 secciones |
| investigacion-profunda | `completo` | Equilibrado | Media | Salida estructurada, selección de metodología exploratoria |
| investigacion-profunda | `socratico` | Originalidad | Ligera | Diálogo guiado por el usuario |
| articulo-academico | `completo` | Equilibrado | Media | Plantillas de sección, pero la escritura se adapta |
| articulo-academico | `revision` | Fidelidad | Pesada | Plantilla de seguimiento R&R |
| articulo-academico | `solo-resumen` | Fidelidad | Pesada | Estructura fija de resumen |
| articulo-academico | `plan` | Originality | Ligera | Diálogo de planificación socrática |
| articulo-academico | `declaracion` | Fidelidad | Pesada | Base de datos de políticas de sedes |
| articulo-academico-revisor | `completo` | Equilibrado | Media | Rúbrica cargada, pero perspectivas dinámicas |
| articulo-academico-revisor | `re-review` | Fidelidad | Pesada | Matriz de trazabilidad R&R |
| articulo-academico-revisor | `guiado` | Originalidad | Ligera | Diálogo socrático adaptativo |

---

## Recomendación de modo

- El usuario quiere "predecible" / "consistente" → sugerir modos de **Fidelidad**.
- El usuario quiere "explorar" / "reflexionar" → sugerir modos de **Originalidad**.
- No está claro → sugerir modos **Equilibrados** por defecto.
