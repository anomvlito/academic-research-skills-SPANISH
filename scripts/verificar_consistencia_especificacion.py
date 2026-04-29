#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def leer(ruta_relativa: str) -> str:
    return (ROOT / ruta_relativa).read_text(encoding="utf-8")


def fallar(mensaje: str) -> None:
    ERRORS.append(mensaje)


def esperar_que_contenga(ruta_relativa: str, aguja: str) -> None:
    texto = leer(ruta_relativa)
    if aguja not in texto:
        fallar(f"{ruta_relativa}: falta el texto esperado: {aguja!r}")


def esperar_que_no_contenga(ruta_relativa: str, aguja: str) -> None:
    texto = leer(ruta_relativa)
    if aguja in texto:
        fallar(f"{ruta_relativa}: texto prohibido aún presente: {aguja!r}")


def extraer_seccion(texto: str, inicio: str, fin: str) -> str:
    idx_inicio = texto.find(inicio)
    if idx_inicio == -1:
        fallar(f"falta el inicio de la sección: {inicio!r}")
        return ""
    idx_fin = texto.find(fin, idx_inicio + len(inicio))
    if idx_fin == -1:
        fallar(f"falta el fin de la sección después de {inicio!r}: {fin!r}")
        return texto[idx_inicio:]
    return texto[idx_inicio:idx_fin]


def verificar_enlaces_markdown_relativos(ruta_relativa: str) -> None:
    texto = leer(ruta_relativa)
    ruta_doc = ROOT / ruta_relativa
    for destino_bruto in MARKDOWN_LINK_RE.findall(texto):
        if destino_bruto.startswith(("http://", "https://", "mailto:", "#")):
            continue
        destino = destino_bruto.split("#", 1)[0]
        if not destino:
            continue
        resuelto = (ruta_doc.parent / destino).resolve()
        if not resuelto.exists():
            fallar(f"{ruta_relativa}: enlace markdown relativo roto {destino_bruto!r}")


def verificar_registro_de_modos() -> None:
    ruta_relativa = "REGISTRO_DE_MODOS.md"
    esperar_que_contenga(ruta_relativa, "Última actualización: v3.6.5 (2026-04-27)")
    for encabezado in (
        "## investigacion-profunda (7 modos)",
        "## articulo-academico (10 modos)",
        "## revisor-articulo-academico (6 modos)",
    ):
        esperar_que_contenga(ruta_relativa, encabezado)


def verificar_claude_md() -> None:
    ruta_relativa = ".claude/CLAUDE.md"
    esperar_que_contenga(ruta_relativa, "verificación de integridad (Etapa 2.5)")
    esperar_que_contenga(ruta_relativa, "verificación de integridad final (Etapa 4.5)")
    esperar_que_contenga(ruta_relativa, "**Versión de la suite**: 3.6.5")
    for prohibido in (
        "6th independent reviewer",
        "Peer review gains 6th independent reviewer",
        "integrity check",
    ):
        esperar_que_no_contenga(ruta_relativa, prohibido)


def verificar_bloque_version_revisor() -> None:
    ruta_relativa = "revisor-articulo-academico/HABILIDAD.md"
    texto = leer(ruta_relativa)
    fm_match = re.search(
        r'metadata:\s*[\s\S]*?\n\s+version:\s"([^"]+)"\n\s+last_updated:\s"([^"]+)"',
        texto,
    )
    if not fm_match:
        fallar(f"{ruta_relativa}: no se pudo parsear versión/last_updated en el frontmatter")
        return
    version, last_updated = fm_match.groups()

    v_block_match = re.search(r"\| Versión de la Habilidad \| ([^|]+) \|", texto)
    u_block_match = re.search(r"\| Última Actualización \| ([^|]+) \|", texto)
    if not v_block_match or not u_block_match:
        fallar(f"{ruta_relativa}: faltan filas en la tabla de Información de Versión")
        return

    version_block = v_block_match.group(1).strip()
    updated_block = u_block_match.group(1).strip()

    if version != version_block:
        fallar(
            f"{ruta_relativa}: la versión del frontmatter {version!r} no coincide con el bloque {version_block!r}"
        )
    if last_updated != updated_block:
        fallar(
            f"{ruta_relativa}: la fecha del frontmatter {last_updated!r} no coincide con el bloque {updated_block!r}"
        )


def verificar_docs_pipeline() -> None:
    for ruta_relativa in (
        "pipeline-academico/HABILIDAD.md",
        "pipeline-academico/agentes/agente_orquestador_pipeline.md",
    ):
        esperar_que_no_contenga(ruta_relativa, "auto-continue in 5 seconds")
        esperar_que_contenga(
            ruta_relativa,
            "Estado en una línea + confirmación explícita de continuar/pausar",
        )

    esperar_que_contenga(
        "pipeline-academico/agentes/agente_orquestador_pipeline.md",
        "La Etapa 2.5 NUNCA puede omitirse",
    )
    esperar_que_contenga(
        "pipeline-academico/agentes/agente_orquestador_pipeline.md",
        "La Etapa 4.5 NUNCA puede omitirse",
    )


def verificar_secciones_readme() -> None:
    ruta_relativa = "README.md"
    texto = leer(ruta_relativa)

    esperar_que_contenga(ruta_relativa, "version-v3.6.5-blue")
    esperar_que_contenga(ruta_relativa, "releases/tag/v3.6.5")
    esperar_que_contenga(ruta_relativa, "### v3.6.5 (2026-04-27)")
    
    ENCABEZADOS = [
        "#### Investigación Profunda (7 modos)",
        "#### Artículo Académico (10 modos)",
        "#### Revisor de Artículo Académico (6 modos)",
        "### Investigación Profunda (v2.8)",
        "### Artículo Académico (v3.0)",
        "### Revisor de Artículo Académico (v1.8)",
        "### Pipeline Académico (v3.6)",
    ]
    for h in ENCABEZADOS:
        esperar_que_contenga(ruta_relativa, h)

    paper_start = "#### Artículo Académico (10 modos)"
    paper_end = "#### Revisor de Artículo Académico (6 modos)"
    deep_start = "#### Investigación Profunda (7 modos)"
    deep_end = "#### Artículo Académico (10 modos)"
    reviewer_start = "#### Revisor de Artículo Académico (6 modos)"
    reviewer_end = "#### Pipeline Académico (Orquestador)"

    uso_paper = extraer_seccion(texto, paper_start, paper_end)
    for esperado in [
        "modo solo-esquema",
        "modo solo-resumen",
        "modo declaración",
    ]:
        if esperado not in uso_paper:
            fallar(f"{ruta_relativa}: sección de uso de Artículo Académico falta {esperado!r}")

    uso_deep = extraer_seccion(texto, deep_start, deep_end)
    if "modo revisión" not in uso_deep:
        fallar(f"{ruta_relativa}: sección de uso de Investigación Profunda falta 'modo revisión'")

    uso_revisor = extraer_seccion(texto, reviewer_start, reviewer_end)
    if "modo calibración" not in uso_revisor:
        fallar(f"{ruta_relativa}: sección de uso de revisor falta 'modo calibración'")

    esperar_que_contenga(ruta_relativa, "DOCX (vía Pandoc cuando esté disponible)")
    verificar_enlaces_markdown_relativos(ruta_relativa)


def verificar_docs_setup() -> None:
    esperar_que_contenga(
        "docs/SETUP.md",
        "La generación directa de `.docx` usa [Pandoc]",
    )
    esperar_que_contenga(
        "docs/SETUP.md",
        "La generación directa de `.docx` requiere Pandoc, y la generación de PDF requiere `tectonic`",
    )
    verificar_enlaces_markdown_relativos("docs/SETUP.md")


def verificar_contrato_docx() -> None:
    esperar_que_contenga(
        "articulo-academico/HABILIDAD.md",
        "salida LaTeX/DOCX-vía-Pandoc/PDF",
    )
    esperar_que_contenga(
        "articulo-academico/agentes/agente_formateador.md",
        "Si Pandoc está disponible, genera el archivo `.docx` directamente",
    )
    esperar_que_contenga(
        "articulo-academico/agentes/agente_formateador.md",
        "Si Pandoc no está disponible, proporciona instrucciones completas de conversión a DOCX",
    )
    esperar_que_contenga(
        "pipeline-academico/HABILIDAD.md",
        "DOCX vía Pandoc cuando esté disponible, de lo contrario instrucciones de conversión",
    )
    esperar_que_contenga(
        "pipeline-academico/agentes/agente_orquestador_pipeline.md",
        "DOCX vía Pandoc cuando esté disponible (de lo contrario instrucciones)",
    )


def verificar_documentos_referencia() -> None:
    ruta_passport = "pipeline-academico/referencias/pasaporte_como_limite_reinicio.md"
    esperar_que_contenga(ruta_passport, "# Pasaporte como Límite de Reinicio (v3.6.3)")
    esperar_que_contenga(ruta_passport, "## Contrato del modo `resume_from_pasaporte`")
    esperar_que_contenga(ruta_passport, "## Reglas de Hierro")
    
    formato_tag = "[REINICIO-PASAPORTE: hash=<hash>, etapa=<completada>, siguiente=<siguiente>]"
    esperar_que_contenga(ruta_passport, formato_tag)
    esperar_que_contenga(
        "pipeline-academico/agentes/agente_orquestador_pipeline.md",
        formato_tag,
    )


def main() -> int:
    verificar_registro_de_modos()
    verificar_claude_md()
    verificar_bloque_version_revisor()
    verificar_docs_pipeline()
    verificar_secciones_readme()
    verificar_docs_setup()
    verificar_contrato_docx()
    verificar_documentos_referencia()

    if ERRORS:
        print("Fallo en la verificación de consistencia de la especificación:")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print("Verificación de consistencia de la especificación pasada.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
