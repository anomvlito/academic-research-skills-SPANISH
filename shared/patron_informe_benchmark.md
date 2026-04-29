# Patrón de Informe de Benchmark (v3.3.5+)

**Estado**: v3.3.5 — documento principal para el esquema de divulgación de benchmarks.  
**Esquema**: `shared/benchmark_report.schema.json`  
**Validador**: `scripts/verificar_informe_benchmark.py`

---

## Por qué existe este documento

El artículo de Anthropic (2026) comparó:
"2 investigadores × 7 días (PGR=0.23) vs 9 agentes × 5 días (PGR=0.97)."

Dramático. Pero: n=2, realizado por los autores, sin independencia. No es una comparación científica — es un artefacto de presentación. Los autores sabían lo que el agente produciría antes de empezar la línea base humana. Una brecha así puede ser simplemente una línea base humana "preparada" para fallar.

ARS hereda este riesgo. Este patrón define un esquema obligatorio para cualquiera que publique una comparativa de benchmark de ARS. Los informes que no satisfacen el esquema no son "benchmarks de ARS" — son anécdotas.

---

## El esquema de un vistazo

Seis campos obligatorios de primer nivel en `benchmark_report.schema.json`:

- **`ars_version`** — versión exacta de semver utilizada.
- **`task_definition`** — descripción, tipo de tarea (evaluable o abierta).
- **`human_baseline`** — cinco campos de procedencia que determinan la credibilidad del lado humano.
- **`ars_run`** — costo, tiempo, habilidades usadas y nivel de acceso a datos.
- **`metrics`** — nombre de la métrica principal, valor numérico e independencia de puntuación.
- **`caveats`** — array de limitaciones conocidas (obligatorio al menos uno).

---

## Racional campo por campo

### `human_baseline` (Línea base humana)

Este bloque existe porque el lado humano es donde vive o muere la credibilidad del benchmark. Una línea base humana débil infla la ventaja aparente del agente.

- **`sample_size`** (n): El esquema rechaza cero. El silencio es peor que admitir n=1.
- **`author_independence`**: `author-conducted` (realizado por autores) es la trampa típica. `author-blinded` (autores sin ver resultados de ARS antes) es mejor. `third-party-conducted` (terceros) es ideal.
- **`hours_spent`**: Permite verificar la afirmación de tiempo. "7 días" se lee diferente para 20 artículos que para 400.

### `metrics.scoring_independence`

Cuatro valores: `authors-scored`, `third-party-scored`, `blind-scored`, `self-scored`.
`self-scored` (puntuado por la propia IA) es el peor caso de fallo de alineación. `blind-scored` (evaluadores humanos ciegos al origen) es el estándar mínimo creíble.

---

## Cómo usarlo

1. Copia la plantilla de ejemplo.
2. Rellena cada campo con valores reales.
3. Establece el tamaño de la muestra humana (el esquema rechaza 0).
4. Ejecuta: `python scripts/verificar_informe_benchmark.py tu-informe.json`.
5. Corrige todos los errores y atiende a las advertencias en el campo `caveats`.
6. Publica el JSON junto con tu artículo de benchmark.
