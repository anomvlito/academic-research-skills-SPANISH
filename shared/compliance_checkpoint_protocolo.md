# Protocolo de Punto de Control de Cumplimiento

Define cómo el `agente_cumplimiento` participa en las Compuertas de Integridad de las Etapas 2.5 y 4.5, cómo su decisión interactúa con el bucle de FALLO existente y cómo se procesan las anulaciones de usuario.

## Resumen de doble compuerta

| Aspecto | Etapa 2.5 | Etapa 4.5 |
|---|---|---|
| Alcance PRISMA-trAIce | M1 a M10 | T1, A1, I1, R1, R2, D1, D2 |
| Enfoque principios RAISE | supervisión_humana, adecuación | transparencia, reproducibilidad |
| Condición de Bloqueo | Modo SR Y cualquier ítem Obligatorio = FALLO | Igual |
| Condición de Advertencia | Ítem Altamente Recomendado = FALLO | Igual |

## Precedencia de decisiones

Dentro de un punto de control, las decisiones se agregan como:
`decision_general = max_severidad(bloqueo_prisma, bloqueo_raise, verificacion_integridad_legacy)`

Orden de severidad: pasa < advertir < bloquear.

## UX de acción del usuario

### En bloqueo
El orquestador presenta:
```
[BLOQUEO DE CUMPLIMIENTO] Etapa <N>
Falla obligatoria PRISMA-trAIce: M4 (Datos de entrada)
Falla de principios RAISE: reproducibilidad

Elegir:
  (a) rellenar — volver a la Etapa 2 y añadir material faltante.
  (b) manejo manual — editar el manuscrito directamente.
  (c) reconocer limitación — invocar anulación de usuario.
```

## Escalera de Anulación (Fricción de 3 rondas)

Se activa cuando el usuario elige "reconocer limitación" en un bloqueo.

| Ronda | Comportamiento |
|---|---|
| 1ª anulación | Advertir al usuario. Racional opcional. Permitido. |
| 2ª anulación | Requiere cadena de racional (cualquier longitud). |
| 3ª anulación | Requiere racional ≥ 100 caracteres. |

Tras una anulación exitosa, el agente genera una `adenda_divulgación` que se auto-inyecta en la sección de divulgación de IA del manuscrito. Esta adenda no es eliminable.

## Historial de solo adición

`pasaporte_materiales.historial_cumplimiento[]` nunca se sobrescribe. Cada intento se preserva con su marca de tiempo. El Informe de Auto-Reflexión de IA en la Etapa 6 cita el historial completo para demostrar cómo se realizó la corrección — esto es transparencia RAISE aplicada a ARS mismo.
