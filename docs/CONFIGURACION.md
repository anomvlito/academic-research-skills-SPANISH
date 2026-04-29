# Configuración de ARS

Requisitos previos y configuración opcional para las Habilidades de Investigación Académica (ARS). Si solo necesitas salida en Markdown y el pipeline predeterminado de Claude Opus 4.7, puedes omitir la mayor parte de esto — consulta "Configuración mínima viable" a continuación.

---

## Configuración mínima viable

1. Instala Claude Code (ver abajo).
2. Exporta `ANTHROPIC_API_KEY`.
3. Ejecuta `claude` en este repositorio (o en cualquier proyecto que tenga ARS en `.claude/skills/`).

Esto es suficiente para obtener salida en Markdown + instrucciones de conversión a DOCX. Todo lo demás en este documento es opcional.

---

## Instalar Claude Code

**Recomendado: Instalador nativo** (no requiere Node.js, se actualiza automáticamente):

```bash
# macOS / Linux
curl -fsSL https://claude.ai/install.sh | bash

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex
```

<details>
<summary>Alternativa: instalación vía npm (obsoleto)</summary>

Requiere Node.js 18+.

```bash
npm install -g @anthropic-ai/claude-code
```

</details>

## Configurar clave API

Obtén una clave API de Anthropic en <https://console.anthropic.com/>.

```bash
# Claude Code solicitará tu clave API en la primera ejecución
claude
```

O establécela como una variable de entorno:

```bash
export ANTHROPIC_API_KEY=sk-ant-xxxxx
```

## Salida DOCX (opcional)

La generación directa de `.docx` usa [Pandoc](https://pandoc.org/). Si Pandoc no está disponible, el formateador generará Markdown e instrucciones de conversión a DOCX.

```bash
# macOS
brew install pandoc

# Linux (Debian/Ubuntu)
sudo apt-get install pandoc

# Windows — descargar desde https://pandoc.org/installing.html
```

## Salida LaTeX / PDF (opcional)

La salida PDF requiere [tectonic](https://tectonic-typesetting.github.io/) y fuentes específicas. **Esto es opcional** — la salida Markdown y las instrucciones de conversión a DOCX funcionan sin esto.

```bash
# macOS
brew install tectonic

# Linux (Debian/Ubuntu)
curl --proto '=https' --tlsv1.2 -fsSL https://drop-sh.fullyjustified.net | sh

# Windows — descargar desde https://tectonic-typesetting.github.io/en-US/install.html
```

**Fuentes requeridas**:
- **Times New Roman** — normalmente pre-instalada; en Linux instala `ttf-mscorefonts-installer`.
- **Courier New** — normalmente pre-instalada.

---

## Adaptadores de `literature_corpus[]` (v3.6.4+, opcional)

Si mantienes un corpus de literatura curado (Zotero, Obsidian, etc.), puedes cargarlo en un Pasaporte de Materiales para que los agentes de ARS lean tu biblioteca *antes* de buscar en bases de datos externas.

Se incluyen tres adaptadores de referencia en Python en `scripts/adaptadores/`:

```bash
# 1. Instalar dependencias (PyYAML + jsonschema)
pip install -r requirements-dev.txt

# 2. Ejecutar un adaptador de referencia.
#    Tanto --passport como --rejection-log son obligatorios.
python scripts/adaptadores/escaneo_carpetas.py --input /ruta/a/pdfs --passport pasaporte.yaml --rejection-log registro_rechazos.yaml
python scripts/adaptadores/zotero.py --input mi-exportacion.json --passport pasaporte.yaml --rejection-log registro_rechazos.yaml
python scripts/adaptadores/obsidian.py --input ~/Obsidian/Notas --passport pasaporte.yaml --rejection-log registro_rechazos.yaml

# 3. Pasa el pasaporte.yaml resultante a tu sesión de ARS
```

## Banderas de entorno opcionales (v3.5.1+)

| Bandera | Desde | Qué hace |
|---|---|---|
| `ARS_CROSS_MODEL` | v3.0 | Habilita verificación multi-modelo |
| `ARS_SOCRATIC_READING_PROBE=1` | v3.5.1 | Activa la capa de prueba de lectura en `agente_mentor_socratico`. |
| `ARS_PASSPORT_RESET=1` | v3.6.3 | Convierte cada punto de control COMPLETO en un límite de reinicio de contexto. |

---

## Verificación multi-modelo (opcional)

ARS funciona solo con Claude Opus 4.7. Para mayor confianza, puedes habilitar un segundo modelo para verificar la integridad de forma independiente.

### Configuración rápida

```bash
# Paso 1: Configura tu clave API (elige una o ambas)
export OPENAI_API_KEY="sk-tu-clave"        # Para GPT-5.4 Pro
export GOOGLE_AI_API_KEY="AIza-tu-clave"    # Para Gemini 3.1 Pro

# Paso 2: Elige tu modelo de verificación
export ARS_CROSS_MODEL="gpt-5.4-pro"
# o: export ARS_CROSS_MODEL="gemini-3.1-pro-preview"

# Paso 3: Ejecuta Claude Code normalmente
claude
```

---

## Métodos de Instalación

Claude descubre habilidades en `<raiz>/<nombre-habilidad>/HABILIDAD.md`. Este repositorio contiene cuatro habilidades separadas:

- `investigacion-profunda`
- `articulo-academico`
- `articulo-academico-revisor`
- `pipeline-academico`

### Método 1: Como habilidades del proyecto (recomendado)

Úsalo cuando quieras ARS disponible dentro de un proyecto existente de Claude Code.

Clona el repo y copia cada carpeta de habilidad en el directorio `.claude/skills/` de tu proyecto:

```bash
git clone https://github.com/Imbad0202/academic-research-skills.git ~/academic-research-skills

cd /ruta/a/tu/proyecto
mkdir -p .claude/skills
cp -R ~/academic-research-skills/investigacion-profunda .claude/skills/
cp -R ~/academic-research-skills/articulo-academico .claude/skills/
cp -R ~/academic-research-skills/articulo-academico-reviewer .claude/skills/
cp -R ~/academic-research-skills/pipeline-academico .claude/skills/
```

### Método 2: Como proyecto independiente

Úsalo cuando quieras trabajar directamente dentro del repositorio de ARS.

```bash
git clone https://github.com/Imbad0202/academic-research-skills.git
cd academic-research-skills
claude
```

### Método 3: Claude Cowork (escritorio)

Úsalo cuando quieras que las cuatro habilidades de ARS estén disponibles en [Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork).

#### Opción A: instalación vía enlace simbólico (rápido)

```bash
git clone https://github.com/Imbad0202/academic-research-skills.git ~/academic-research-skills

mkdir -p ~/.claude/skills
cd ~/.claude/skills
ln -s ~/academic-research-skills/investigacion-profunda
ln -s ~/academic-research-skills/articulo-academico
ln -s ~/academic-research-skills/articulo-academico-reviewer
ln -s ~/academic-research-skills/pipeline-academico
```

#### Opción B: instalación vía copia

```bash
mkdir -p ~/.claude/skills
cp -R ~/academic-research-skills/investigacion-profunda ~/.claude/skills/
cp -R ~/academic-research-skills/articulo-academico ~/.claude/skills/
cp -R ~/academic-research-skills/articulo-academico-reviewer ~/.claude/skills/
cp -R ~/academic-research-skills/pipeline-academico ~/.claude/skills/
```

### Método 4: Uso con claude.ai (web)

ARS es una suite nativa de Claude Code. Depende de la orquestación multi-agente y scripts locales.

- **Método 4b — Proyecto + integración con GitHub** (recomendado): trae el repositorio a un Proyecto de claude.ai como conocimiento consultable. Claude puede leer las definiciones de los agentes, referencias y ejemplos. **No es una instalación de Habilidad** (no hay ejecución autónoma), pero el contenido está disponible para lectura y citación.
- **Método 4a — Carga de Habilidad Personalizada**: no se recomienda para esta suite ya que depende de la orquestación de sub-agentes propia de Claude Code que no está presente en la web.

#### Método 4b: Proyecto + integración con GitHub (recomendado para claude.ai)

1. Inicia sesión en [claude.ai](https://claude.ai).
2. Crea un nuevo Proyecto: **Projects** → **Create Project**.
3. Importa desde GitHub: click en **Files** → **+** → **GitHub** → selecciona `Imbad0202/academic-research-skills`.
4. Selecciona las carpetas principales (`investigacion-profunda`, `articulo-academico`, `articulo-academico-reviewer`, `pipeline-academico`, `shared`, `scripts`, `REGISTRO_DE_MODOS.md`).
5. (Recomendado) Establece las **Instrucciones** del Proyecto con el contenido de `.claude/CLAUDE.md`.
6. Empieza a chatear: "Guía mi investigación sobre X" o "Ayúdame a escribir un artículo sobre Y".