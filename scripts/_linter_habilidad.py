"""Ayudantes compartidos para el linter de HABILIDAD.md.

Utilizado por verificar_nivel_acceso_datos.py y verificar_tipo_tarea.py para validar
que cada HABILIDAD.md de nivel superior declare un campo de metadatos requerido con
un valor extraído de un vocabulario cerrado.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

DIR_OMITIDOS = frozenset(
    {"shared", "scripts", "docs", ".git", ".github", "examples", ".local-plans", ".claude"}
)


class ErrorFrontmatter(Exception):
    """Se lanza cuando el frontmatter de HABILIDAD.md no se puede parsear."""


def iterar_archivos_habilidad(raiz: Path) -> list[Path]:
    """Solo archivos HABILIDAD.md de nivel superior. Omite DIR_OMITIDOS."""
    resultados: list[Path] = []
    for hijo in sorted(raiz.iterdir()):
        if not hijo.is_dir() or hijo.name in DIR_OMITIDOS:
            continue
        habilidad_md = hijo / "HABILIDAD.md"
        if habilidad_md.is_file():
            resultados.append(habilidad_md)
    return resultados


def parsear_frontmatter(ruta: Path) -> dict | None:
    """Parsea el frontmatter YAML de un HABILIDAD.md."""
    texto = ruta.read_text(encoding="utf-8")
    if not texto.startswith("---"):
        return None
    match = re.match(r"\A---\r?\n(?P<fm>.*?)(?:\r?\n)---(?:\r?\n|$)", texto, re.DOTALL)
    if not match:
        raise ErrorFrontmatter(f"{ruta}: falta el cierre de la valla YAML del frontmatter")
    fm = match.group("fm")
    try:
        datos = yaml.safe_load(fm) or {}
    except yaml.YAMLError as exc:
        raise ErrorFrontmatter(f"{ruta}: frontmatter YAML malformado: {exc}") from exc
    if not isinstance(datos, dict):
        raise ErrorFrontmatter(
            f"{ruta}: el frontmatter YAML debe ser un mapeo/objeto, se obtuvo {type(datos).__name__}"
        )
    return datos


def dividir_frontmatter(texto: str) -> tuple[dict | None, str]:
    """Divide el frontmatter YAML del cuerpo."""
    if not texto.startswith("---"):
        return None, texto
    match = re.match(r"\A---\r?\n(?P<fm>.*?)(?:\r?\n)---(?:\r?\n|$)", texto, re.DOTALL)
    if not match:
        return None, texto
    try:
        datos = yaml.safe_load(match.group("fm")) or {}
    except yaml.YAMLError:
        return None, texto
    if not isinstance(datos, dict):
        return None, texto
    return datos, texto[match.end():]


def verificar_campo_metadatos(
    raiz: Path,
    campo: str,
    valores_legales: set[str] | frozenset[str],
) -> list[str]:
    """Devuelve una lista de mensajes de violación, vacía si todos pasan."""
    violaciones: list[str] = []
    habilidades = iterar_archivos_habilidad(raiz)
    if not habilidades:
        violaciones.append(f"no se encontraron archivos HABILIDAD.md bajo {raiz}")
        return violaciones
    for ruta in habilidades:
        try:
            fm = parsear_frontmatter(ruta)
        except ErrorFrontmatter as exc:
            violaciones.append(str(exc))
            continue
        if fm is None:
            violaciones.append(f"{ruta}: falta el frontmatter YAML")
            continue
        metadatos = fm.get("metadata") or {}
        if campo not in metadatos:
            violaciones.append(f"{ruta}: falta metadata.{campo}")
            continue
        valor = metadatos[campo]
        if valor not in valores_legales:
            violaciones.append(
                f"{ruta}: metadata.{campo} = {valor!r}, "
                f"debe ser uno de {sorted(valores_legales)}"
            )
    return violaciones


def ejecutar_linter(campo: str, valores_legales: set[str] | frozenset[str], mensaje_ok: str) -> int:
    """Wrapper para argparse + check + print + exit-code."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
    )
    args = parser.parse_args()

    violaciones = verificar_campo_metadatos(args.path, campo, valores_legales)
    if violaciones:
        for v in violaciones:
            print(f"ERROR: {v}")
        print(f"\n{len(violaciones)} violación(es) encontrada(s).", file=sys.stderr)
        return 1
    print(mensaje_ok)
    return 0
