#!/usr/bin/env python3
"""
Prueba de integridad institucional del catálogo de Líneas de Trabajo (Anexo 1).
Verifica:
1. Existencia exacta de las 6 claves: I, II, III, IV, V, VI.
2. Máximo de alumnos: Línea I = 3, Líneas II a VI = 2.
3. Línea VI sin descripción inventada (cadena vacía).
4. Ausencia total de frases no institucionales en todo el catálogo.
"""

import os
import re
import sys

def test_lineas_catalog():
    catalog_path = os.path.join(os.path.dirname(__file__), "..", "config", "lineas-trabajo.tex")
    if not os.path.exists(catalog_path):
        print(f"ERROR: No se encontro el archivo de catalogo: {catalog_path}")
        return False

    with open(catalog_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Verificar claves detectadas
    pattern = r"\\ifstrequal\{#1\}\{([A-Z]+)\}"
    keys_found = re.findall(pattern, content)
    expected_keys = ["I", "II", "III", "IV", "V", "VI"]

    print(f"Claves encontradas en el catalogo: {keys_found}")
    if keys_found != expected_keys:
        print(f"ERROR: Las claves encontradas {keys_found} no coinciden exactamente con {expected_keys}")
        return False

    # 2. Verificar que Linea VI tenga descripcion vacia
    if r"\def\DescripcionLineaTrabajo{}" not in content:
        print("ERROR: La definicion de Linea VI debe contener '\\def\\DescripcionLineaTrabajo{}' (cadena vacia).")
        return False
    
    # 3. Verificar que no exista la frase no institucional en el archivo
    if "Puesta en operación y automatización de procesos industriales" in content:
        print("ERROR: Se detecto la frase no institucional en lineas-trabajo.tex")
        return False

    # 4. Verificar maximos de alumnos
    max_alumnos = {
        "I": 3,
        "II": 2,
        "III": 2,
        "IV": 2,
        "V": 2,
        "VI": 2,
    }
    for key, expected_max in max_alumnos.items():
        pattern_max = rf"\\ifstrequal\{{#1\}}\{{{key}\}}[\s\S]+?\\def\\MaximoAlumnosLineaTrabajo\{{(\d+)\}}"
        key_match = re.search(pattern_max, content)
        if not key_match:
            print(f"ERROR: No se encontro MaximoAlumnosLineaTrabajo para la Linea {key}")
            return False
        found_max = int(key_match.group(1))
        if found_max != expected_max:
            print(f"ERROR: Para la Linea {key} se esperaba maximo {expected_max} alumnos, pero se encontro {found_max}")
            return False

    print("[OK] Prueba de integridad del catalogo de Lineas de Trabajo SUPERADA con exito.")
    return True

if __name__ == "__main__":
    success = test_lineas_catalog()
    sys.exit(0 if success else 1)
