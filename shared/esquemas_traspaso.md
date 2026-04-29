# Esquemas de Traspaso — Contratos de Datos entre Habilidades

## Propósito

Define la estructura exacta de datos para cada artefacto pasado entre las etapas del pipeline.
Todos los agentes que producen o consumen estos artefactos DEBEN cumplir con estos esquemas.
Los agentes consumidores deben validar la entrada y solicitar la re-generación si se encuentran violaciones del esquema.

> **Convención**: Todos los esquemas utilizan salida estructurada basada en Markdown. Los agentes DEBEN validar los campos obligatorios antes de aceptar un Traspaso. La falta de campos obligatorios activa una ruta de fallo `Traspaso_INCOMPLETE`.

---

## Esquema 1: Informe PI (investigacion-profunda -> articulo-academico)

**Productor**: `investigacion-profunda/agente_pregunta_investigacion` | `investigacion-profunda/agente_mentor_socratico`
**Consumidor**: `investigacion-profunda/agente_arquitecto_investigacion` | `articulo-academico/agente_admision`

### Campos Obligatorios

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `pregunta_investigacion` | string | La Pregunta de Investigación finalizada (una sola frase, forma interrogativa) |
| `sub_preguntas` | list[string] | 2-5 sub-preguntas descompuestas |
| `puntuaciones_finer` | object | `{factible: 1-10, interesante: 1-10, novedoso: 1-10, etico: 1-10, relevante: 1-10}` |
| `alcance` | object | `{dentro_alcance: list[string], fuera_alcance: list[string], dominio: string, marco_temporal: string, geografia: string, poblacion: string}` |
| `tipo_metodologia` | enum | `"cualitativa"` / `"cuantitativa"` / `"mixta"` |
| `marco_teorico` | string | Nombre del marco teórico seleccionado o emergente |
| `palabras_clave` | list[string] | 5-10 términos de búsqueda para literatura |

### Campos Opcionales

- `conocimientos_socraticos`: list[string] — ideas clave del diálogo socrático.
- `hipotesis`: string — hipótesis preliminar.
- `criterios_exclusion`: list[string] — lo que queda explícitamente fuera.
- `partes_interesadas`: list[string] — actores clave afectados.
- `banderas_eticas`: list[string] — consideraciones éticas preliminares.

### Ejemplo

```markdown
## Informe PI

**Pregunta de Investigación**: ¿Cómo afecta la evaluación formativa asistida por IA a los resultados de aprendizaje de grado en cursos STEM en universidades taiwanesas?

**Sub-Preguntas**:
1. ¿Qué herramientas de evaluación formativa asistida por IA se utilizan actualmente en los cursos STEM de las IES de Taiwán?
2. ¿Qué mejoras medibles en los resultados de aprendizaje se han documentado?
3. ¿Qué percepciones existen entre estudiantes y profesores respecto a la evaluación asistida por IA?

**Puntuaciones FINER**: Factible: 8, Interesante: 9, Novedoso: 7, Ético: 9, Relevante: 10

**Alcance**:
- Dentro de alcance: evaluación formativa asistida por IA, cursos STEM de grado, IES de Taiwán, 2018-2025.
- Fuera de alcance: educación K-12, solo evaluación sumativa, disciplinas no STEM.
- Dominio: Educación Superior, Tecnología Educativa.
- Marco Temporal: 2018-2025.
- Geografía: Taiwán (con comparaciones internacionales).
- Población: Estudiantes de grado STEM.

**Tipo de Metodología**: Métodos mixtos (cuasi-experimental + encuesta).

**Marco Teórico**: Modelo de Aceptación Tecnológica (TAM) + Marco de Retroalimentación de Hattie.

**Palabras Clave**: evaluación IA, evaluación formativa, educación STEM, educación superior Taiwán, resultados de aprendizaje.
```

---

## Esquema 2: Bibliografía (investigacion-profunda -> articulo-academico)

**Productor**: `investigacion-profunda/agente_bibliografia`
**Consumidor**: `investigacion-profunda/agente_sintesis` | `articulo-academico/agente_estratega_literatura`

### Campos Obligatorios

- `fuentes`: list[Fuente] — todas las fuentes identificadas.
- `estrategia_busqueda`: object — `{bases_datos: list[string], palabras_clave: list[string], criterios_inclusion: list[string], criterios_exclusion: list[string], rango_fechas: string}`.
- `evaluacion_cobertura`: string — autoevaluación de la integridad de la cobertura.
- `fuentes_minimas`: integer — 15 (modo completo), 5 (modo rápido).

### Objeto Fuente (Source)

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|----------|-------------|
| `id` | string | Sí | Identificador único (ej. `[S01]`) |
| `titulo` | string | Sí | Título de la fuente |
| `autores` | string | Sí | Autor(es) |
| `año` | integer | Sí | Año de publicación |
| `doi` | string | Sí* | DOI si está disponible |
| `cita` | string | Sí | Cita completa en APA 7 |
| `tipo` | enum | Sí | `journal_article` / `book` / `chapter` / etc. |
| `nivel_evidencia` | integer | Sí | 1-7 (1 = revisión sistemática, 7 = opinión experta) |
| `nivel_calidad` | enum | Sí | `tier_1` (top journal) / `tier_2` / `tier_3` / `tier_4` |
| `relevancia` | enum | Sí | `core` / `supporting` / `peripheral` |
| `puntuacion_relevancia`| integer | Sí | 1-10 relevancia respecto a la PI |
| `anotacion` | string | Sí | Resumen de 2-3 frases de hallazgos y relevancia |
| `verificado` | boolean | No | Si el DOI/existencia ha sido verificado |
| `semantic_scholar_id` | string | No | ID de Semantic Scholar (v3.3) |

---

## Esquema 3: Informe de Síntesis (investigacion-profunda -> articulo-academico)

**Productor**: `investigacion-profunda/agente_sintesis`
**Consumidor**: `articulo-academico/agente_constructor_argumentos`

### Campos Obligatorios

- `temas`: list[Tema] — 3-7 temas sintetizados.
- `brechas_investigacion`: list[string] — lo que la literatura NO aborda.
- `debates_clave`: list[Debate] — puntos de desacuerdo entre fuentes.
- `recomendaciones_metodologicas`: list[string] — enfoques recomendados según las brechas.
- `implicaciones_teoricas`: list[string] — cómo la síntesis informa la teoría.
- `areas_consenso`: list[string] — puntos de acuerdo.

---

## Esquema 4: Borrador del Artículo (articulo-academico -> integridad/revisor)

**Productor**: `articulo-academico/agente_redactor_borrador`
**Consumidor**: `pipeline-academico/agente_verificacion_integridad` | `articulo-academico-revisor/*`

### Campos Obligatorios

- `titulo`: string — título del artículo.
- `resumen`: object — `{español: string, ingles: string}`.
- `autores`: list[Autor] — información de autores con roles CRediT.
- `palabras_clave`: object — `{es: list[string], en: list[string]}`.
- `secciones`: list[Seccion] — secciones ordenadas del artículo.
- `referencias`: list[Referencia] — lista completa de referencias.
- `conteo_palabras_total`: integer.
- `formato_cita`: enum — `"APA7"` / `"Chicago"` / `"MLA"` / `"IEEE"` / `"Vancouver"`.
- `tipo_estructura`: enum — `"IMRaD"` / `"revision_literatura"` / `"teorico"` / `"estudio_caso"` / `"informe_politica"`.

---

## Esquema 5: Informe de Integridad (agente_verificacion_integridad -> pipeline)

**Productor**: `pipeline-academico/agente_verificacion_integridad`
**Consumidor**: `pipeline-academico/agente_orquestador_pipeline` | `articulo-academico/agente_redactor_borrador`

### Campos Obligatorios

- `veredicto`: enum — `"PASA"` / `"PASA_CON_CONDICIONES"` / `"FALLA"`.
- `modo`: enum — `"pre-revision"` / `"final-check"`.
- `fases`: object — estructura de fases (A_referencias, B_contexto_citas, C_datos, D_originalidad, E_afirmaciones).
- `problemas_generales`: object — `{GRAVE: integer, MEDIO: integer, MENOR: integer}`.
- `puntuacion_integridad_citas`: float (0.0-1.0).
- `puntuacion_riesgo_fabricacion`: float (0.0-1.0).
- `trayectoria_puntuacion`: object / null — seguimiento de delta de puntuación (v3.3).

---

## Esquema 6: Informe de Revisión (articulo-academico-revisor -> pipeline)

**Productor**: `articulo-academico-revisor/agente_sintetizador_editorial`

### Campos Obligatorios

- `decision_editorial`: enum — `"Aceptar"` / `"Corrección Menor"` / `"Corrección Mayor"` / `"Rechazar"`.
- `informes_revisores`: list[InformeRevisor].
- `consenso`: enum — `"CONSENSO-4"` / `"CONSENSO-3"` / `"DIVIDIDO"` / `"DA-CRITICO"`.
- `hoja_ruta_correccion`: list[ItemHojaRuta] — lista priorizada de cambios.
- `puntuacion_confianza`: integer (0-100).

---

## Esquema 7: Hoja de Ruta de Corrección (revisor -> articulo-academico)

**Productor**: `articulo-academico-revisor/agente_sintetizador_editorial`

### Campos Obligatorios

- `elementos`: list[ItemHojaRuta] — lista ordenada de elementos de corrección.
- `total_elementos`: integer.
- `cuenta_imprescindibles`: integer — número de elementos de prioridad `must_fix`.
- `decision_editorial`: enum.

---

## Esquema 8: Respuesta a los Revisores (articulo-academico -> re-revisión)

**Productor**: `articulo-academico/agente_redactor_borrador` (modo revision)

### Campos Obligatorios

- `ronda_correccion`: integer (1, 2, ...).
- `elementos`: list[ItemRespuesta] — respuesta a cada elemento de la hoja de ruta.
- `resumen`: object — `{resueltos: int, limitaciones: int, irresolubles: int, en_desacuerdo: int}`.
- `delta_conteo_palabras`: integer.
- `nuevas_referencias`: integer.
- `resumen_de_cambios`: string.

---

## Esquema 9: Pasaporte de Materiales (metadatos entre etapas)

**Propósito**: Acompaña a cada artefacto proporcionando procedencia y seguimiento de verificación.

### Campos Obligatorios

- `habilidad_origen`: string — ej. `investigacion-profunda`.
- `modo_origen`: string — ej. `completo`, `socratico`.
- `fecha_origen`: string — ISO 8601.
- `estado_verificacion`: enum — `"VERIFIED"` / `"UNVERIFIED"` / `"STALE"`.
- `etiqueta_version`: string — ej. `v1.0`, `borrador_v2`.

### Campos Opcionales

- `fecha_paso_integridad`: string.
- `hash_contenido`: string — SHA-256.
- `dependencias_aguas_arriba`: list[string].
- `repro_lock`: object | null — archivo de bloqueo de configuración.
- `historial_cumplimiento`: list[object] — rastro de auditoría de informes de cumplimiento (v3.4.0+).
- `limite_reinicio`: list[object] — libro mayor de reinicios de pasaporte (v3.6.3+).
- `literature_corpus`: list[object] — corpus de literatura opcional del usuario (v3.6.4+).

---

## Esquema 10: Perfil de Estilo (admisión -> redactor/compilador)

**Productor**: `articulo-academico/agentes/agente_admision`

### Campos Obligatorios

- `fuente_calibracion`: list[string] — nombres de las muestras analizadas.
- `conteo_muestras`: integer (mínimo 1, recomendado 3+).
- `longitud_sentencia`: object — `{media: float, desviacion: float, patron_ritmo: string}`.
- `longitud_parrafo`: object — `{media_sentencias: float, variacion: string}`.
- `preferencias_vocabulario`: object — `{atenuacion: list, transicion: list, verbos: list, formalidad: string}`.
- `estilo_cita`: object — `{ratio_narrativo: float, ratio_parentetico: float, densidad: float, colocacion: string}`.

---

## Reglas de Validación

1. **Comprobación de campos obligatorios**: Todos los campos marcados como obligatorios son REQUERIDOS. Los agentes consumidores DEBEN verificar esto antes de proceder.
2. **Comprobación de tipos**: Los campos deben coincidir con los tipos declarados (ej. valores de `enum` permitidos).
3. **Referencias cruzadas**: Los IDs de fuentes referenciados en Síntesis deben existir en la Bibliografía.
4. **Seguimiento de versiones**: Cada artefacto DEBEN llevar un Pasaporte de Materiales (Esquema 9) con una etiqueta de versión creciente.
5. **Fallo ante falta de datos**: Si falta un campo obligatorio, devolver `Traspaso_INCOMPLETE` con la lista de campos faltantes; NO proceder con datos parciales.
6. **Validación del productor**: El agente productor debe validar la salida contra su esquema ANTES del Traspaso.
7. **Validación del consumidor**: El agente consumidor debe validar la entrada al recibirla.
8. **Compuerta de integridad**: Los artefactos verificados deben actualizar su Pasaporte de Materiales a `estado_verificacion: "VERIFIED"`.
9. **Detección de obsolescencia (Staleness)**: Si un artefacto aguas arriba es modificado, los artefactos dependientes deben marcarse como `"STALE"`.
10. **Frescura del Pasaporte**: Los resultados de integridad se consideran CADUCADOS si tienen más de 24 horas.

## `nivel_acceso_datos` (v3.3.2+)

Cada `HABILIDAD.md` declara `metadata.nivel_acceso_datos` con uno de tres valores:

- `bruto` — consume fuentes no verificadas; asume entrada adversarial/alucinada.
- `redactado` — opera sobre material sanitizado; sin nueva ingestión bruta.
- `solo_verificado` — se ejecuta solo después de las compuertas de integridad.

## `tipo_tarea` (v3.3.2+)

Cada `HABILIDAD.md` declara `metadata.tipo_tarea` con uno de dos valores:

- `evaluable_por_resultado` — la tarea tiene una métrica escalar objetiva (ej. benchmark).
- `abierta` — la calidad depende del juicio de dominio, trabajo interpretativo o contexto.

Todas las habilidades actuales de ARS son `abierta`.
