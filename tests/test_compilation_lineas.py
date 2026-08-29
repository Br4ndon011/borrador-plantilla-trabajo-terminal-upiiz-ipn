#!/usr/bin/env python3
"""
Pruebas exhaustivas de compilacion para las 6 Lineas de Trabajo y los 3 Tipos de Documento.
"""

import os
import re
import subprocess
import sys

def test_line(line_code, tipo_doc="PROTOCOLO"):
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    datos_path = os.path.join(repo_dir, "config", "datos.tex")

    with open(datos_path, "r", encoding="utf-8") as f:
        original_content = f.read()

    try:
        # Modificar datos.tex temporalmente para la prueba
        test_content = re.sub(r"\\TipoDocumento\{[A-Za-z0-9]+\}", lambda m: f"\\TipoDocumento{{{tipo_doc}}}", original_content, count=1)
        test_content = re.sub(r"\\LineaTrabajo\{[A-Za-z0-9]+\}", lambda m: f"\\LineaTrabajo{{{line_code}}}", test_content, count=1)
        
        with open(datos_path, "w", encoding="utf-8") as f:
            f.write(test_content)

        print(f"Probando TipoDocumento={tipo_doc}, LineaTrabajo={line_code}...")
        cmd = ["latexmk", "-silent", "main.tex"]
        res = subprocess.run(cmd, cwd=repo_dir, capture_output=True, text=True)

        if res.returncode != 0:
            print(f"ERROR al compilar con LineaTrabajo={line_code}, TipoDocumento={tipo_doc}")
            print(res.stderr[:500])
            return False
        else:
            print(f"[OK] Compilacion exitosa: TipoDocumento={tipo_doc}, LineaTrabajo={line_code}")
            return True

    finally:
        # Restaurar datos.tex original
        with open(datos_path, "w", encoding="utf-8") as f:
            f.write(original_content)

def run_all_tests():
    lines = ["I", "II", "III", "IV", "V", "VI"]
    for l in lines:
        if not test_line(l, "PROTOCOLO"):
            return False

    # Probar TT I y TT II
    if not test_line("IV", "TTI"):
        return False
    if not test_line("VI", "TTII"):
        return False

    print("\n[OK] Todas las pruebas de compilacion de Lineas de Trabajo concluyeron exitosamente.")
    return True

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
