# Plantilla del Panel de Estado del Pipeline

Esta plantilla define el formato de salida para el Panel de Control de Progreso. Dado el estándar del repositorio, se utiliza exclusivamente la versión en español.

---

## Versión en Español

```
+=========================================+
|   Estado del Pipeline Académico         |
+=========================================+
| Tema: {tema}                            |
+-----------------------------------------+

  Etapa 1 INVESTIGACIÓN    [{icon_estado}] {texto_estado}
    {linea_modo}
    {linea_salidas}

  Etapa 2 ESCRITURA        [{icon_estado}] {texto_estado}
    {linea_modo}
    {linea_salidas}

  Etapa 3 REVISIÓN         [{icon_estado}] {texto_estado}
    {linea_modo}
    {linea_decision}

  Etapa 4 CORRECCIÓN       [{icon_estado}] {texto_estado}
    {linea_ronda_correccion}
    {linea_abordado}

  Etapa 3' RE-REVISIÓN     [{icon_estado}] {texto_estado}
    {linea_conteo_bucle}

  Etapa 5 FINALIZACIÓN     [{icon_estado}] {texto_estado}
    {linea_formato}

+-----------------------------------------+
| Materiales:                             |
|   [{icon}] Informe PI                   |
|   [{icon}] Plan de Metodología          |
|   [{icon}] Bibliografía                 |
|   [{icon}] Informe de Síntesis          |
|   [{icon}] Borrador del Artículo        |
|   [{icon}] Informes de Revisión         |
|   [{icon}] Hoja de Ruta de Corrección   |
|   [{icon}] Borrador Corregido           |
|   [{icon}] Respuesta a los Revisores    |
|   [{icon}] Artículo Final               |
+-----------------------------------------+
| Historial de Correcciones:              |
|   {historial_correcciones}              |
+-----------------------------------------+
| Siguiente Paso: {sugerencia_sig_paso}   |
+=========================================+
```

---

## Definiciones de Campos

### icon_estado

| Estado | Icono |
|--------|------|
| completado | `v` |
| en_progreso | `..` |
| pendiente | ` ` (espacio) |
| omitido | `--` |

### texto_estado

| Estado | Texto |
|--------|------|
| completado | Completado |
| en_progreso | En Progreso |
| pendiente | Pendiente |
| omitido | Omitido |

### linea_modo

Formato: `Modo: {nombre_modo}`
- Solo se muestra cuando el estado es completado o en_progreso.
- Si el modo cambió (ej. plan -> completo), mostrar la ruta completa.

### linea_salidas

Formato: `Salidas: {salida_1}, {salida_2}, ...`
- Solo se muestra cuando el estado es completado.
- Enumera todos los entregables de esa etapa.

### linea_decision

Formato: `Decisión: {Aceptar/Corrección Menor/Corrección Mayor/Rechazar}`
- Solo se muestra cuando la Etapa 3 o la Etapa 3' se han completado.

### linea_ronda_correccion

Formato: `Ronda de Corrección: {actual}/{max}`
- Solo se muestra cuando la Etapa 4 está en_progreso.

### linea_abordado

Formato: `Abordado: {cuenta}/{total} correcciones requeridas`
- Solo se muestra cuando la Etapa 4 está en_progreso.

### linea_conteo_bucle

Formato: `Bucle: {cuenta}/2`
- Solo se muestra para la Etapa 3'.

### icono de material

| Estado | Icono |
|--------|------|
| disponible | `v` |
| faltante | ` ` (espacio) |

### historial_correcciones

Una línea por ronda:
```
Ronda {n}: {decision} | {abordado}/{total} elementos abordados
  Pendiente: {resumen_elementos_pendientes}
```

Si no hay historial de correcciones, mostrar "(Aún no hay historial de correcciones)".

### sugerencia_sig_paso

Sugerencia generada automáticamente basada en el estado actual:
- Etapa 1 completada: "Se recomienda proceder a la Etapa 2 (ESCRITURA) usando el modo {modo_recomendado}"
- Etapa 3 completada (Mayor): "Es necesario entrar en la Etapa 4 (CORRECCIÓN), {N} elementos requeridos"
- Etapa 4 completada: "Se recomienda proceder a la Etapa 3' (RE-REVISIÓN) para confirmar la calidad de la corrección"
- Etapa 3' completada (Aceptar): "¡Felicidades! Procede a la Etapa 5 (FINALIZACIÓN) para producir la versión final"
- Pipeline completado: "¡Pipeline completado! El artículo final está listo."

---

## Versión Simplificada (Auto-anexada tras completar una etapa)

Barra de progreso de una línea:

```
Pipeline: [v]INVESTIGACIÓN -> [v]ESCRITURA -> [..]REVISIÓN -> [ ]CORRECCIÓN -> [ ]FINALIZACIÓN
```
