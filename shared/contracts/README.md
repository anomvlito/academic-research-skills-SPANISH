# Contratos de Sprint de ARS

Plantillas de contratos de sprint para la orquestación de la compuerta de revisores en ARS v3.6.2+.

Esquema: `shared/sprint_contract.schema.json` (Esquema 13).
Validador: `scripts/verificar_contrato_sprint.py`.
Protocolo: `revisor-articulo-academico/referencias/protocolo_contrato_sprint.md`.

## Plantillas incluidas (v3.6.2)

- `revisor/completo.json` — panel 5, 5 dimensiones, 4 condiciones de fallo.
- `revisor/foco_metodologia.json` — panel 2, 2 dimensiones, 3 condiciones de fallo.

## Modos de revisor reservados sin plantillas incluidas

Los modos `re-review`, `calibracion` y `guiado` están en el enum del esquema pero se distribuyen sin plantillas en v3.6.2. Estos modos continúan operando en su forma existente (sin contrato, sin compuerta rígida) hasta que una actualización posterior añada sus plantillas.

## Cómo añadir una nueva plantilla

1. Añade el archivo bajo `shared/contracts/<dominio>/<modo>.json`.
2. Ejecuta `python scripts/verificar_contrato_sprint.py <ruta> --ars-version vX.Y.Z`.
3. Si las cadenas de `expresion` usan nuevas frases, actualiza el protocolo del contrato de sprint y el prompt del sintetizador.
