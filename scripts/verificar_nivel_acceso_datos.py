#!/usr/bin/env python3
from __future__ import annotations
from _linter_habilidad import ejecutar_linter

NIVELES_LEGALES = frozenset({"open", "controlled", "restricted"})

if __name__ == "__main__":
    import sys
    sys.exit(ejecutar_linter(
        "data_access_level", 
        NIVELES_LEGALES, 
        "OK: todos los archivos HABILIDAD.md declaran un data_access_level válido."
    ))
