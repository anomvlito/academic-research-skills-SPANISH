# Inicio Rápido

Pasa de cero a tu primera investigación asistida por IA en 3 pasos.

## Paso 1: Instalación

```bash
# Instalar Claude Code
curl -fsSL https://claude.ai/install.sh | bash

# Clonar este repo en un lugar estable
git clone https://github.com/Imbad0202/academic-research-skills.git ~/academic-research-skills

# Instalar cada una de las cuatro habilidades en el .claude/skills/ de tu proyecto
cd /ruta/a/tu/proyecto
mkdir -p .claude/skills
ln -s ~/academic-research-skills/investigacion-profunda .claude/skills/investigacion-profunda
ln -s ~/academic-research-skills/articulo-academico .claude/skills/articulo-academico
ln -s ~/academic-research-skills/articulo-academico-reviewer .claude/skills/articulo-academico-reviewer
ln -s ~/academic-research-skills/pipeline-academico .claude/skills/pipeline-academico
```

Cada habilidad debe estar en `.claude/skills/<nombre-habilidad>/HABILIDAD.md` para que Claude Code la descubra. Consulta [docs/CONFIGURACION.md](docs/CONFIGURACION.md) para alternativas basadas en copia y otros métodos.

## Paso 2: Iniciar

```bash
claude
```

## Paso 3: Empezar a investigar

Dile a Claude lo que quieres hacer. Seleccionará automáticamente la habilidad y el modo correctos.

### Ejemplo: Investigación guiada (modo Socrático)

```
Tú: "Tengo una idea vaga sobre el impacto de la IA en el aseguramiento de la calidad de la educación superior, pero no estoy seguro de cómo formular la pregunta de investigación. ¿Puedes guiarme?"
```

Claude entrará en modo Socrático — haciendo preguntas para ayudarte a aclarar tu pensamiento, no dándote respuestas directamente. Después de 5-15 rondas de diálogo, tendrás una pregunta de investigación enfocada y una dirección metodológica.

### Ejemplo: Escribir un artículo

```
Tú: "Ayúdame a escribir un artículo sobre el impacto del declive de la tasa de natalidad en las universidades privadas de Taiwán"
```

### Ejemplo: Revisar un artículo existente

```
Tú: "Revisa este artículo" (luego pega o adjunta el artículo)
```

### Ejemplo: Pipeline completo (investigación → escritura → revisión → corrección → publicación)

```
Tú: "Quiero producir un artículo de investigación completo sobre cómo la IA agéntica está remodelando la medición de los resultados de aprendizaje de los estudiantes"
```

Esto activa el pipeline completo de 10 etapas. Presupuesta ~$4-6 en costos de API y 2-4 horas de trabajo colaborativo.

## ¿Qué modo debería usar?

| Quiero... | Usa esto |
|-------------|----------|
| Explorar una idea vaga | `investigacion-profunda` modo socrático — solo describe tu interés |
| Obtener un resumen rápido de literatura | `investigacion-profunda` modo rápido |
| Hacer una revisión sistemática (PRISMA) | `investigacion-profunda` modo systematic-review |
| Escribir un artículo desde cero | `articulo-academico` modo completo |
| Planificar un artículo capítulo a capítulo | `articulo-academico` modo plan |
| Que revisen mi artículo | `articulo-academico-reviewer` modo completo |
| Hacer todo de principio a fin | `pipeline-academico` — di "Quiero un artículo de investigación completo" |

## ¿Qué sigue?

- [README Completo](README.md) — todas las características, modos, opciones de instalación e historial de cambios.
- [Showcase del Pipeline](ejemplos/showcase/) — artefactos reales de una ejecución completa del pipeline.
