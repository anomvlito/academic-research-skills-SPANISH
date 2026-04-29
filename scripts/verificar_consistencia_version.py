#!/usr/bin/env python3
"""Linter: las etiquetas de versión se mantienen alineadas entre .claude/CLAUDE.md, el frontmatter de HABILIDAD.md e HISTORIAL_DE_CAMBIOS.md.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _linter_habilidad import parsear_frontmatter, ErrorFrontmatter


TABLE_ROW_RE = re.compile(r"^\|\s*`([a-z0-9-]+)`\s+v(\d+\.\d+\.\d+)\s*\|", re.MULTILINE)
SUITE_VERSION_RE = re.compile(
    r"^\s*-\s*\*\*Versión de la suite\*\*:\s*(\d+\.\d+\.\d+)", re.MULTILINE
)
CHANGELOG_ENTRY_RE = re.compile(r"^##\s*\[(\d+\.\d+\.\d+)\]", re.MULTILINE)

NOMBRE_SKILL_PIPELINE = "pipeline-academico"


def _parsear_versiones_tabla(texto_claude_md: str) -> dict[str, str]:
    return dict(TABLE_ROW_RE.findall(texto_claude_md))


def _parsear_version_suite(texto_claude_md: str) -> str | None:
    m = SUITE_VERSION_RE.search(texto_claude_md)
    return m.group(1) if m else None


def _parsear_ultimo_cambio(texto_historial: str) -> str | None:
    m = CHANGELOG_ENTRY_RE.search(texto_historial)
    return m.group(1) if m else None


def verificar(raiz: Path) -> list[str]:
    errores: list[str] = []

    claude_md = raiz / ".claude" / "CLAUDE.md"
    if not claude_md.is_file():
        errores.append(f"{claude_md}: no encontrado")
        return errores
    texto_claude = claude_md.read_text(encoding="utf-8")

    versiones_tabla = _parsear_versiones_tabla(texto_claude)
    if not versiones_tabla:
        errores.append(
            f"{claude_md}: la tabla de Descripción General de Habilidades no tiene filas "
            "`<habilidad>` vX.Y.Z parseables"
        )

    version_suite = _parsear_version_suite(texto_claude)
    if version_suite is None:
        errores.append(
            f"{claude_md}: falta la línea '**Versión de la suite**: X.Y.Z'"
        )

    historial = raiz / "HISTORIAL_DE_CAMBIOS.md"
    if not historial.is_file():
        errores.append(f"{historial}: no encontrado")
    else:
        ultimo = _parsear_ultimo_cambio(historial.read_text(encoding="utf-8"))
        if ultimo is None:
            errores.append(f"{historial}: no se encontró ninguna entrada '## [X.Y.Z]'")
        elif version_suite is not None and ultimo != version_suite:
            errores.append(
                f"{claude_md}: La versión de la suite {version_suite!r} no coincide con "
                f"la última entrada del HISTORIAL_DE_CAMBIOS {ultimo!r}"
            )

    for nombre_skill, version_tabla in sorted(versiones_tabla.items()):
        habilidad_md = raiz / nombre_skill / "HABILIDAD.md"
        if not habilidad_md.is_file():
            errores.append(
                f"{claude_md}: la tabla lista {nombre_skill!r} v{version_tabla} "
                f"pero {habilidad_md} no existe"
            )
            continue
        try:
            fm = parsear_frontmatter(habilidad_md)
        except ErrorFrontmatter as exc:
            errores.append(str(exc))
            continue
        if fm is None:
            errores.append(f"{habilidad_md}: falta el frontmatter YAML")
            continue
        metadatos = fm.get("metadata") or {}
        declarada = metadatos.get("version")
        if declarada is None:
            errores.append(f"{habilidad_md}: falta metadata.version")
            continue
        declarada_str = str(declarada)
        if declarada_str != version_tabla:
            errores.append(
                f"{claude_md}: {nombre_skill!r} aparece como v{version_tabla} pero "
                f"{habilidad_md} metadata.version es {declarada_str!r}"
            )

    if version_suite is not None:
        pipeline_en_tabla = versiones_tabla.get(NOMBRE_SKILL_PIPELINE)
        if pipeline_en_tabla is not None and pipeline_en_tabla != version_suite:
            errores.append(
                f"{claude_md}: {NOMBRE_SKILL_PIPELINE} aparece como "
                f"v{pipeline_en_tabla} pero la versión de la suite es {version_suite!r} "
                "(el pipeline sigue el lanzamiento de la suite)"
            )

    return errores


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
    )
    args = parser.parse_args()

    errores = verificar(args.path)
    if errores:
        print("Fallo en la verificación de consistencia de versión:")
        for err in errores:
            print(f"- {err}")
        return 1
    print("Verificación de consistencia de versión pasada.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
