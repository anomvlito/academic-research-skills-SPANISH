# Patrón de Aislamiento de la Verdad Absoluta

**Estado**: v3.3.2 — documento narrativo principal.

---

## § 1 — Por qué importa el aislamiento de la verdad absoluta

Cuando un agente puede leer las respuestas de evaluación mientras produce el resultado, aprende a optimizar directamente contra la rúbrica en lugar de contra la tarea subyacente. El resultado son puntuaciones infladas que no se transfieren a la realidad — un caso de "reward hacking".

El fallo es arquitectónico. Un agente que ve lo que cuenta como respuesta correcta tenderá a seguir las características superficiales de la corrección en lugar de la calidad real. ARS utiliza un modelo de tres capas para evitar este fallo.

## § 2 — El modelo mental de tres capas

Cada artefacto en ARS pertenece a una de estas tres capas, y el flujo es estrictamente unidireccional. Un artefacto puede ser promovido de una capa inferior a una superior al pasar una compuerta de integridad. No puede moverse en la dirección opuesta.

**Capa 1 — Entradas brutas (raw):** Consultas de usuario, fuentes primarias sin verificar. Se consideran "no confiables" por defecto. La habilidad `investigacion-profunda` opera aquí.

**Capa 2 — Artefactos verificados:** Resultados que han superado una compuerta de integridad (confirmación de API, pruebas de existencia de citas, etc.). Las habilidades posteriores pueden tratarlos como provisionalmente confiables.

**Capa 3 — Verdad absoluta y rúbricas de evaluación:** Incluye etiquetas de oro, rúbricas de puntuación y cualquier material que defina cómo debe ser un resultado correcto. Ningún agente que opere en las capas 1 o 2 debe tener material de la capa 3 en su ventana de contexto. Esta frontera es un **cortafuegos epistemológico**.

## § 3 — Reglas para añadir habilidades o agentes

1. **Declara el `nivel_acceso_datos` con honestidad.** Debe reflejar la entrada más "sucia" que la habilidad puede consumir.
2. **Separa los archivos de rúbrica de los paquetes de entrada.** Nunca incluyas etiquetas de oro en el repositorio de forma que se carguen incondicionalmente.
3. **Devuelve las puntuaciones a través de un agente revisor que mantenga la rúbrica en privado.** El agente redactor nunca debe leer la rúbrica antes de generar su borrador.

## § 4 — Implementación actual

| Mecanismo | Ubicación |
|---|---|
| Verificación de fuentes (API S2) | `investigacion-profunda/referencias/protocolo_api_semantic_scholar.md` |
| Protocolo anti-filtraciones | `articulo-academico/referencias/protocolo_anti_filtraciones.md` |
| Compuertas de integridad (Etapa 2.5/4.5) | `pipeline-academico/referencias/modos_fallo_investigacion_ia.md` |

## § 5 — Lo que este patrón NO ES

- **No es un sistema de permisos en tiempo de ejecución.** Es una convención y una anotación declarativa validada por scripts de linter.
- **No es un sustituto de la revisión humana.** Las etapas 2.5 y 4.5 son los puntos reales de cumplimiento donde el investigador humano revisa los informes.
- **No es un protocolo de benchmark.** ARS se enfoca en tareas abiertas donde la calidad depende del juicio de dominio, no en métricas escalares simples.
