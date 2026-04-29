#!/usr/bin/env python3
from __future__ import annotations
from _linter_habilidad import ejecutar_linter

TIPOS_LEGALES = frozenset({"research", "writing", "review", "orchestration"})

if __name__ == "__main__":
    import sys
    sys.exit(ejecutar_linter(
        "task_type", 
        TIPOS_LEGALES, 
        "OK: todos los archivos HABILIDAD.md declaran un task_type válido."
    ))
