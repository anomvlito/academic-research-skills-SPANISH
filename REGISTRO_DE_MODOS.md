# Registro de Modos

Fuente única de verdad para todos los modos de la suite ARS. **25 modos** en 4 habilidades.

Última actualización: v3.6.5 (2026-04-27)

---

## investigacion-profunda (7 modos)

| Modo | Espectro | Salida | Supervisión |
|------|----------|--------|-----------|
| `full` | Equilibrado | Informe APA 7.0 | Alta |
| `quick` | Fidelidad | Resumen rápido | Media |
| `socratic` | Originalidad | Diálogo guiado (Mentor) | Muy Alta |
| `systematic-review` | Fidelidad | Informe PRISMA 2020 | Media |

## articulo-academico (10 modos)

| Modo | Espectro | Salida | Supervisión |
|------|----------|--------|-----------|
| `full` | Equilibrado | Borrador completo del artículo | Alta |
| `plan` | Originalidad | Plan de capítulos (Socrático) | Muy Alta |
| `revision` | Fidelidad | Borrador corregido + Respuesta R&R | Alta |
| `disclosure` | Fidelidad | Declaración de uso de IA para revistas | Baja |

## articulo-academico-revisor (6 modos)

| Modo | Espectro | Salida | Supervisión |
|------|----------|--------|-----------|
| `full` | Equilibrado | 5 informes + Decisión Editorial | Alta |
| `re-review` | Fidelidad | Verificación de correcciones | Media |
| `calibration` | Fidelidad | Informe de calibración (FNR/FPR) | Media |

## pipeline-academico (1 orquestador + 1 modo reanudar)

| Modo | Espectro | Función | Supervisión |
|------|----------|--------|-----------|
| (pipeline) | Equilibrado | Flujo orquestado de 10 etapas | Muy Alta |
| `resume_desde_pasaporte=<hash>` | Fidelidad | Reanuda desde un límite de reinicio | Alta |

---

### Niveles de supervisión

- **Muy Alta:** Diálogo liderado por el usuario o puntos de control obligatorios en cada etapa.
- **Alta:** El usuario confirma decisiones clave (pregunta, esquema).
- **Media:** Formato estructurado con puntos de decisión limitados.
- **Baja:** Mecánico o basado en plantillas, mínima intervención humana.
