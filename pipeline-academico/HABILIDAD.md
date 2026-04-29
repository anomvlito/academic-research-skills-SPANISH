# Pipeline Académico v3.6.5 — Orquestador de Flujo de Trabajo de Investigación Académica Completo

Un orquestador ligero que gestiona el pipeline académico completo, desde la exploración de la investigación hasta el manuscrito final.

## Inicio Rápido

**Flujo completo (desde cero):**
```
Quiero escribir un artículo de investigación sobre el impacto de la IA en la educación superior.
```
--> El orquestador inicia en la **Etapa 1 (INVESTIGACIÓN)**.

## Etapas del Pipeline (10 Etapas)

| Etapa | Nombre | Función | Entregables |
|-------|------|---------------------|-------------|
| 1 | INVESTIGACIÓN | `investigacion-profunda` | Pregunta de investigación, Bibliografía, Síntesis. |
| 2 | ESCRITURA | `articulo-academico` | Borrador del artículo. |
| **2.5** | **INTEGRIDAD** | **`agente_verificacion_integridad`** | **Informe de verificación de integridad.** |
| 3 | REVISIÓN | `articulo-academico-reviewer` | 5 informes de revisión + Decisión Editorial. |
| 4 | CORRECCIÓN | `articulo-academico` | Borrador corregido + Respuesta a revisores. |
| **3'** | **RE-REVISIÓN** | **`articulo-academico-reviewer`** | **Informe de verificación de correcciones.** |
| **4.5** | **INTEGRIDAD FINAL**| **`agente_verificacion_integridad`** | **Informe final (paso obligatorio al 100%).** |
| 5 | FINALIZACIÓN | `articulo-academico` | Artículo final (LaTeX/PDF/DOCX). |
| 6 | RESUMEN PROCESO | `orquestador` | Registro del proceso de creación del artículo. |

## Sistema de Puntos de Control Adaptativo

⚠️ **REGLA DE HIERRO:** Después de completar cada etapa, el sistema debe solicitar proactivamente la confirmación del usuario.

- **Punto de Control OBLIGATORIO:** En las etapas de INTEGRIDAD (2.5 y 4.5), DECISIÓN EDITORIAL (3) y FINALIZACIÓN (5). No se pueden saltar.
- **Métricas del Dashboard:** Conteo de palabras, referencias, cobertura de secciones e indicadores de calidad.

## Protocolo de Revisión de Integridad

Las etapas 2.5 y 4.5 ejecutan un protocolo de 5 fases: referencias -> contexto de cita -> datos estadísticos -> originalidad -> afirmaciones. **Cero tolerancia a la alucinación.**
