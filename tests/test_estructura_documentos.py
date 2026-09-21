#!/usr/bin/env python3
"""
Prueba automatizada de estructura documental (TOC) para PROTOCOLO, TTI y TTII.
Verifica:
1. PROTOCOLO:
   - Contiene: Objetivos del proyecto, Justificación, Antecedentes,
               Marco Teórico / teórico, Estado del Arte / arte,
               Descripción del trabajo propuesto, Metodología de trabajo,
               Productos o resultados esperados, Viabilidad del proyecto,
               Bibliografía, Firmas.
   - NO contiene: Introducción, Planteamiento del Problema,
                  Desarrollo del Sistema Mecatrónico, Análisis y validación de resultados,
                  Conclusiones, Trabajo a Futuro.
2. TTI:
   - Contiene: Introducción, Análisis y validación del diseño, Cronograma de TT II.
   - NO contiene: Trabajo a Futuro, capítulos exclusivos de protocolo.
3. TTII:
   - Contiene: Introducción, Análisis y validación de resultados, Trabajo a Futuro.
   - NO contiene: Cronograma de TT II como apéndice, capítulos exclusivos de protocolo.
4. Restaura config/datos.tex y regenera el estado compilado de PROTOCOLO al finalizar.
"""

import os
import re
import subprocess
import sys

def get_repo_paths():
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    datos_path = os.path.join(repo_dir, "config", "datos.tex")
    toc_path = os.path.join(repo_dir, "main.toc")
    return repo_dir, datos_path, toc_path

def compile_document(repo_dir, tipo_doc, datos_path, original_content):
    test_content = re.sub(
        r"\\TipoDocumento\{[A-Za-z0-9]+\}",
        lambda m: f"\\TipoDocumento{{{tipo_doc}}}",
        original_content,
        count=1
    )
    with open(datos_path, "w", encoding="utf-8") as f:
        f.write(test_content)

    subprocess.run(["latexmk", "-C"], cwd=repo_dir, capture_output=True, text=True)
    cmd = ["latexmk", "-silent", "main.tex"]
    res = subprocess.run(cmd, cwd=repo_dir, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Fallo la compilacion para {tipo_doc}:\n{res.stderr[:600]}")

def check_toc_protocolo(toc_content):
    print("Verificando estructura de PROTOCOLO...")
    required_patterns = [
        r"Objetivos del proyecto",
        r"Justificación",
        r"Antecedentes",
        r"Marco [Tt]eórico",
        r"Estado del [Aa]rte",
        r"Descripción del trabajo propuesto",
        r"Metodología de trabajo",
        r"Productos o resultados esperados",
        r"Viabilidad del proyecto",
        r"Bibliografía",
        r"Firmas",
    ]
    forbidden_patterns = [
        r"Introducción",
        r"Planteamiento del Problema",
        r"Desarrollo del Sistema Mecatrónico",
        r"Análisis y validación de resultados",
        r"Conclusiones",
        r"Trabajo a Futuro",
    ]

    for req in required_patterns:
        if not re.search(req, toc_content):
            print(f"ERROR: PROTOCOLO debe contener '{req}' en main.toc")
            return False

    for forb in forbidden_patterns:
        if re.search(forb, toc_content):
            print(f"ERROR: PROTOCOLO NO debe contener '{forb}' en main.toc")
            return False

    print("[OK] Estructura de PROTOCOLO validada correctamente.")
    return True

def check_toc_tti(toc_content):
    print("Verificando estructura de TTI...")
    required_patterns = [
        r"Introducción",
        r"Análisis y validación del diseño",
        r"Cronograma.*(?:TT\s*II|Trabajo Terminal II)",
    ]
    forbidden_patterns = [
        r"Trabajo\s+(?:a\s+)?Futuro",
        r"Objetivos del proyecto",
        r"Descripción del trabajo propuesto",
        r"Metodología de trabajo",
        r"Productos o resultados esperados",
        r"Viabilidad del proyecto",
    ]

    for req in required_patterns:
        if not re.search(req, toc_content, re.IGNORECASE):
            print(f"ERROR: TTI debe contener patrón '{req}' en main.toc")
            return False

    for forb in forbidden_patterns:
        if re.search(forb, toc_content, re.IGNORECASE):
            print(f"ERROR: TTI NO debe contener patrón '{forb}' en main.toc")
            return False

    if re.search(r"\{chapter\}\{Firmas\}", toc_content):
        print("ERROR: TTI NO debe contener el capitulo 'Firmas' de protocolo en main.toc")
        return False

    print("[OK] Estructura de TTI validada correctamente.")
    return True

def check_toc_ttii(toc_content):
    print("Verificando estructura de TTII...")
    required_patterns = [
        r"Introducción",
        r"Análisis y validación de resultados",
        r"Trabajo\s+(?:a\s+)?Futuro",
    ]
    forbidden_patterns = [
        r"Cronograma.*(?:TT\s*II|Trabajo Terminal II)",
        r"Objetivos del proyecto",
        r"Descripción del trabajo propuesto",
        r"Metodología de trabajo",
        r"Productos o resultados esperados",
        r"Viabilidad del proyecto",
    ]

    for req in required_patterns:
        if not re.search(req, toc_content, re.IGNORECASE):
            print(f"ERROR: TTII debe contener patrón '{req}' en main.toc")
            return False

    for forb in forbidden_patterns:
        if re.search(forb, toc_content, re.IGNORECASE):
            print(f"ERROR: TTII NO debe contener patrón '{forb}' en main.toc")
            return False

    if re.search(r"\{chapter\}\{Firmas\}", toc_content):
        print("ERROR: TTII NO debe contener el capitulo 'Firmas' de protocolo en main.toc")
        return False

    print("[OK] Estructura de TTII validada correctamente.")
    return True

def run_tests():
    repo_dir, datos_path, toc_path = get_repo_paths()
    with open(datos_path, "r", encoding="utf-8") as f:
        original_content = f.read()

    success = True
    try:
        # 1. Probar PROTOCOLO
        compile_document(repo_dir, "PROTOCOLO", datos_path, original_content)
        with open(toc_path, "r", encoding="utf-8") as f:
            proto_toc = f.read()
        if not check_toc_protocolo(proto_toc):
            success = False

        # 2. Probar TTI
        compile_document(repo_dir, "TTI", datos_path, original_content)
        with open(toc_path, "r", encoding="utf-8") as f:
            tti_toc = f.read()
        if not check_toc_tti(tti_toc):
            success = False

        # 3. Probar TTII
        compile_document(repo_dir, "TTII", datos_path, original_content)
        with open(toc_path, "r", encoding="utf-8") as f:
            ttii_toc = f.read()
        if not check_toc_ttii(ttii_toc):
            success = False

    except Exception as e:
        print(f"Excepcion durante pruebas de estructura: {e}")
        success = False
    finally:
        print("Restaurando estado original en config/datos.tex y recompilando PROTOCOLO...")
        with open(datos_path, "w", encoding="utf-8") as f:
            f.write(original_content)
        subprocess.run(["latexmk", "-C"], cwd=repo_dir, capture_output=True, text=True)
        subprocess.run(["latexmk", "-silent", "main.tex"], cwd=repo_dir, capture_output=True, text=True)

    if success:
        print("\n[OK] Todas las pruebas de estructura documental SUPERADAS con exito.")
    else:
        print("\n[ERROR] Fallaron una o mas pruebas de estructura documental.")

    return success

if __name__ == "__main__":
    ok = run_tests()
    sys.exit(0 if ok else 1)
