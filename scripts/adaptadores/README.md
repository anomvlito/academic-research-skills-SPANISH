# Adaptadores de Corpus de Literatura de ARS

Adaptadores de referencia que producen entradas de `literature_corpus[]` para el Pasaporte de Materiales de ARS. Definidos por el contrato de adaptador en [`pipeline-academico/referencias/adaptadores/resumen.md`](../../pipeline-academico/referencias/adaptadores/resumen.md).

## Qué son estos archivos

Tres adaptadores de punto de partida:

- **`escaneo_carpetas.py`** — escanea un directorio de archivos y extrae metadatos de citación de los nombres de archivo.
- **`zotero.py`** — lee una exportación JSON de Better BibTeX.
- **`obsidian.py`** — lee un vault de Obsidian (Convención A de frontmatter o Convención B estilo Karpathy).

Cada uno genera dos archivos: un `pasaporte.yaml` con entradas de `literature_corpus[]`, y un `registro_rechazos.yaml` que enumera lo que el adaptador no pudo mapear.

**Estos son referencias, no productos finales.** Si tu corpus está en Zotero, Obsidian o una carpeta simple, puedes ejecutarlos directamente; si está en Notion, Readwise, Airtable, etc., copia un adaptador de referencia y adáptalo a tu fuente.

## Ejecutar un adaptador de referencia

### escaneo_carpetas

```bash
python scripts/adaptadores/escaneo_carpetas.py \
    --input /ruta/a/tu/carpeta/de/pdfs \
    --passport pasaporte.yaml \
    --rejection-log registro_rechazos.yaml
```

Los nombres de archivo se analizan con dos convenciones: `{Familia}_{Año}_{título}.{ext}` o `{Familia}{Año}{título}.{ext}`. Los archivos cuyos nombres no proporcionen familia y año son rechazados.

### zotero

Exporta tu biblioteca de Zotero como **Better BibTeX JSON**. Luego:

```bash
python scripts/adaptadores/zotero.py \
    --input ~/zotero_export.json \
    --passport pasaporte.yaml \
    --rejection-log registro_rechazos.yaml
```

Este adaptador NO llama a la API web de Zotero. Los elementos a los que les falten campos obligatorios (`title`, `authors`, `year`) son rechazados.

### obsidian

```bash
python scripts/adaptadores/obsidian.py \
    --input ~/ObsidianVault \
    --passport pasaporte.yaml \
    --rejection-log registro_rechazos.yaml
```

Se omiten los archivos bajo `_templates/` y `.obsidian/`. Los Wikilinks (`[[nota]]`) no se resuelven; aparecen como texto literal en `user_notes`.

## Validar la salida del adaptador

Antes de usar el pasaporte en cualquier flujo de ARS:

```bash
python scripts/verificar_esquema_corpus_literatura.py \
    --passport pasaporte.yaml \
    --rejection-log registro_rechazos.yaml
```

## Cómo escribir tu propio adaptador

1. Lee el contrato del adaptador en [`pipeline-academico/referencias/adaptadores/resumen.md`](../../pipeline-academico/referencias/adaptadores/resumen.md).
2. Lee los esquemas JSON en `shared/contracts/passport/`.
3. Copia uno de los adaptadores existentes como punto de partida.
4. Cambia el código de lectura de entrada y mapeo de campos.
5. Mantén la forma de la salida exactamente igual (ordenado por `citation_key`).
6. Reutiliza los ayudantes en `_common.py`.
7. Valida con `scripts/verificar_esquema_corpus_literatura.py`.

## Recordatorio de Privacidad

`abstract` y `user_notes` pueden contener material protegido por derechos de autor del editor. Antes de compartir un pasaporte públicamente, asegúrate de tener el derecho de publicar ese texto.

## Pruebas

```bash
pytest scripts/adaptadores/tests/ -v
```
