# Habilidades de Investigación Académica (ARS)

Una suite de habilidades de Claude Code para investigación académica rigurosa, escritura de artículos, revisión por pares y orquestación de pipelines.

## Descripción de Habilidades

| Habilidad | Propósito | Modos Clave |
|-------|---------|-----------|
| `investigacion-profunda` v2.9.2 | Equipo de investigación de 13 agentes | completo, rapido, socrático, revision, revision-literatura, fact-check, revision-sistematica |
| `articulo-academico` v3.1.1 | Escritura de artículos con 12 agentes | completo, plan, solo-esquema, revision, coaching-revision, solo-resumen, revision-literatura, convertir-formato, check-citas, declaracion |
| `articulo-academico-revisor` v1.9.0 | Revisión multi-perspectiva (5 revisores + crítica DA multi-modelo opcional) | completo, re-review, rapido, foco-metodologia, guiado, calibracion |
| `pipeline-academico` v3.6.5 | Orquestador de pipeline completo | (coordina todas las anteriores) |

## Novedades clave de v3.6.5

- **Integración del consumidor `literature_corpus[]` en Fase 1**: `agente_bibliografia` y `agente_estratega_literatura` ahora leen el corpus del usuario vía el flujo **primero-corpus, la búsqueda llena el vacío**. Siguen las cuatro Reglas de Hierro (Mismos criterios / Sin omisión silenciosa / Sin mutación / Retroceso elegante).
- **Bloque de reproducibilidad PRE-SCREENED**: Los informes de Estrategia de Búsqueda ganan un bloque que enumera las entradas del corpus incluidas / excluidas / omitidas, con informe de procedencia F4.
- **Protocolo de consumidor**: Referencia canónica en `pipeline-academico/referencias/consumidores_corpus_literatura.md`.
- **Linter de CI**: `scripts/verificar_protocolo_consumidor_corpus.py` aplicando nueve invariantes del protocolo.
- **Sin cambios de esquema**: Los adaptadores de usuario existentes funcionan sin modificación.

## Novedades clave de v3.6.4

- **Puerto de entrada `literature_corpus[]` en Pasaporte**: El Esquema 9 gana un campo opcional para literatura curada por el usuario.
- **Contrato de adaptador neutral al idioma**: Especificado en `pipeline-academico/referencias/adaptadores/resumen.md`.
- **Tres adaptadores de referencia en Python**: `scripts/adaptadores/{escaneo_carpetas,zotero,obsidian}.py`.
- **Contrato de registro de rechazos**: `shared/contracts/passport/registro_rechazos.schema.json`.

## Novedades clave de v3.6.3

- **Límite de reinicio de pasaporte opcional**: Bandera `ARS_PASSPORT_RESET=1` para habilitar límites de reinicio de contexto en puntos de control COMPLETOS. Permite reanudar con `resume_desde_pasaporte=<hash>`.
- **Libro mayor `reset_boundary[]` en Esquema 9**: Entradas de tipo `boundary` y `resume` con hash SHA-256.

## Novedades clave de v3.6.2

- **Contrato de Sprint para revisores**: Esquema 13 + protocolo de dos fases (Fase 1 ciego al artículo / Fase 2 visible). Protocolo mecánico de tres pasos para el sintetizador editorial.

## Novedades clave de v3.5.1

- **Prueba de lectura socrática opcional**: Activada por `ARS_SOCRATIC_READING_PROBE=1` en el Mentor Socrático. Verifica la lectura de artículos citados por el usuario.

## Novedades clave de v3.5

- **Observador de Profundidad de Colaboración**: Nuevo `agente_profundidad_colaboracion` que puntúa la colaboración humano-IA en 4 dimensiones. Solo consultivo — nunca bloquea.

## Novedades clave de v3.4

- **Agente de Cumplimiento (compartido)**: Ejecuta PRISMA-trAIce y RAISE en las Etapas 2.5 / 4.5.
- **Informe de cumplimiento Esquema 12**: Historial de auditoría en el Pasaporte de Materiales.
- **Escalera de anulación de 3 rondas**: Las anulaciones de usuario generan una adenda de declaración automática.

## Reglas de Enrutamiento

1. **pipeline-academico vs habilidades individuales**: pipeline-academico = orquestador completo. Si el usuario solo necesita una función específica, activar la habilidad correspondiente directamente.
2. **investigacion-profunda vs articulo-academico**: Complementarios. El flujo recomendado es investigacion-profunda (investigación) → articulo-academico (escritura).
3. **Modos socrático/plan**: Cuando la pregunta de investigación o la estructura del artículo no están claras, sugerir los modos `socratico` o `plan` para una guía paso a paso.

## Reglas Clave

- Todas las afirmaciones deben tener citas.
- Respeto a la jerarquía de evidencia (meta-análisis > ECA > cohorte > opinión experta).
- Divulgación de contradicciones con comparación de calidad de evidencia.
- Declaración de uso de IA en todos los informes.
- El idioma de salida por defecto coincide con la entrada del usuario (Español o Inglés).

## Pipeline Académico Completo

```
investigacion-profunda (socratico/completo)
  → articulo-academico (plan/completo)
    → Verificación de Integridad (Etapa 2.5)
      → articulo-academico-revisor (completo/guiado)
        → articulo-academico (revision)
          → articulo-academico-revisor (re-revisión, max 2 bucles)
            → Verificación de Integridad Final (Etapa 4.5)
              → articulo-academico (convertir-formato → salida final)
                → Resumen de Proceso + Informe de Auto-Reflexión de la IA
```

## Protocolo de Traspaso

### investigacion-profunda → articulo-academico
Materiales: Informe PI, Plan de Metodología, Bibliografía Anotada, Informe de Síntesis, Colección de INSIGHTS.

### articulo-academico → articulo-academico-revisor
Materiales: Texto completo del artículo. `agente_analista_campo` detecta el dominio automáticamente.

### articulo-academico-revisor → articulo-academico (revision)
Materiales: Carta de Decisión Editorial, Hoja de Ruta de Corrección, comentarios detallados.

## Información de Versión
- **Versión de la suite**: 3.6.5 (según HISTORIAL_DE_CAMBIOS.md)
- **Última actualización**: 2026-04-29 (Traducción Radical al Español)
- **Licencia**: CC-BY-NC 4.0
