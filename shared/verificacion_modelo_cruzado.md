# Protocolo de Verificación Multi-Modelo (v3.0)

## Descripción General

Este protocolo habilita la verificación multi-modelo opcional para juicios de IA de alto riesgo. Cuando se activa, un segundo modelo de IA revisa de forma independiente los resultados del modelo principal, reduciendo los puntos ciegos de sesgo compartido.

**Esto es totalmente opcional.** Todas las habilidades de ARS funcionan solo con Claude Opus 4.7. La verificación multi-modelo es una capa adicional para usuarios que desean mayor confianza en los controles de integridad, los desafíos del Abogado del Diablo y los juicios de revisión.

## Por qué la verificación multi-modelo

Una prueba de estrés de 68 citas generadas por IA encontró que el 31% tenía problemas — y todas pasaron tres rondas de controles de integridad del mismo modelo. La causa raíz: la IA verificadora y la IA generadora comparten la misma distribución de datos de entrenamiento, por lo que comparten los mismos puntos ciegos. Un modelo diferente (entrenado con datos superpuestos pero no idénticos) puede detectar errores que el modelo principal omite sistemáticamente.

**Qué mejora:** Reducción de la tasa de error (estimada 31% → ~5-10%).

## Modelos Soportados

| Modelo | ID de API | Proveedor | Ideal para |
|-------|--------|----------|----------|
| Claude Opus 4.7 | `claude-opus-4-7` | Anthropic | Modelo principal (por defecto) |
| GPT-5.4 Pro | `gpt-5.4-pro` | OpenAI | Verificación — razonamiento más fuerte |
| Gemini 3.1 Pro | `gemini-3.1-pro-preview` | Google | Verificación — fuerte en hechos |

## Guía de Configuración

### Paso 1: Obtener claves API

- **OpenAI (GPT-5.4):** [platform.openai.com](https://platform.openai.com/api-keys)
- **Google (Gemini 3.1 Pro):** [aistudio.google.com](https://aistudio.google.com/apikey)

### Paso 2: Establecer variables de entorno

Añade a tu perfil de shell (`~/.zshrc` o `~/.bashrc`):

```bash
export OPENAI_API_KEY="sk-tu-clave"
export GOOGLE_AI_API_KEY="AIza-tu-clave"

# Elige tu modelo de verificación preferido
export ARS_CROSS_MODEL="gpt-5.4-pro"
```

## Cómo funciona en cada habilidad

### Verificación de Integridad (Etapa 2.5 / 4.5)

**Cuando `ARS_CROSS_MODEL` está activado:**
- El modelo principal (Claude) ejecuta la verificación normal.
- Se envía una muestra aleatoria del 30% de las referencias al segundo modelo.
- Los desacuerdos se marcan como `[DESACUERDO-MULTI-MODELO]` y se priorizan para revisión humana.

### Abogado del Diablo (investigacion-profunda + revisor-articulo-academico)

**Cuando `ARS_CROSS_MODEL` está activado:**
- Después de que el DA completa su revisión estándar, el segundo modelo genera una crítica independiente.
- Cualquier problema CRÍTICO o MAYOR encontrado por el segundo modelo pero no por el DA se añade como `[HALLAZGO-MULTI-MODELO]`.

## Consideraciones de Costo

La verificación multi-modelo añade costos de API del segundo proveedor:

| Escenario | Llamadas Adicionales | Costo Adicional Estimado |
|----------|-----------------|--------------------------|
| Verificación de integridad (30%) | ~4 llamadas | ~$0.30-0.60 |
| Contraste del Abogado del Diablo | 3 llamadas | ~$0.30-0.50 |
| **Pipeline completo** | **~7 llamadas** | **~$0.60-1.10** |

## Limitaciones

1. **No resuelve totalmente el sesgo compartido.** Todos los LLMs comparten gran parte de los datos de entrenamiento.
2. **Latencia de API.** Las llamadas adicionales añaden 2-5 segundos por vez.
3. **Diferencias de formato.** El agente debe procesar formatos variados del segundo modelo.
