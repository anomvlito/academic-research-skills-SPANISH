# Revisor de Artículos Académicos v1.9.0 — Equipo de Agentes de Revisión Multi-Perspectiva

Simula un proceso completo de revisión por pares de una revista internacional: identifica el campo del artículo y configura dinámicamente a 5 revisores (Editor en Jefe + 3 revisores pares + Abogado del Diablo).

## Inicio Rápido

**Comando más simple:**
```
Revisa este artículo: [pegar texto o archivo]
```

## Equipo de Agentes (7 Agentes)

| # | Agente | Rol |
|---|-------|------|
| 1 | `agente_analista_campo` | Analiza el campo y configura los 5 perfiles de revisores. |
| 2 | `agente_editor_jefe` | Originalidad, ajuste a la revista y calidad general. |
| 3 | `agente_revisor_metodologia` | Diseño de investigación y validez estadística. |
| 6 | `agente_revisor_abogado_diablo` | Desafía argumentos centrales y detecta falacias. |
| 7 | `agente_sintetizador_editorial` | Sintetiza las revisiones y toma la decisión editorial. |

## Flujo de Trabajo (3 Fases)

1. **FASE 0: Análisis de Campo y Configuración de Personas** -> Perfiles de revisores.
2. **FASE 1: Revisión Multi-Perspectiva en Paralelo** -> 5 informes independientes.
3. **FASE 2: Síntesis Editorial y Decisión** -> Carta de decisión + Hoja de ruta de revisión.

## Modos de Operación (6 Modos)

- **`full`**: Revisión completa (5 informes).
- **`re-review`**: Verificación de si las revisiones abordaron los comentarios previos.
- **`methodology-focus`**: Enfocado solo en métodos y estadísticas.
- **`calibration`**: Mide la precisión del revisor (FNR/FPR).

## Estándares de Calidad

1. **Diferenciación de perspectivas:** cada revisor debe tener un ángulo distinto.
2. **Basado en evidencia:** la decisión editorial no puede inventar críticas.
3. **REGLA DE HIERRO:** el Revisor NO MODIFICA el manuscrito (solo lectura).
4. **REGLA DE HIERRO:** si el Abogado del Diablo encuentra fallos CRÍTICOS, la decisión no puede ser "Aceptado".
