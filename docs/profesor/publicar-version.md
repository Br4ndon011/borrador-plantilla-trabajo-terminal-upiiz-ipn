# Guía Docente: Publicación de Versiones y Gestión de Releases

Esta guía describe el procedimiento formal para etiquetar y publicar versiones oficiales de la plantilla institucional utilizando **Versionado Semántico (SemVer)** y **GitHub Releases**.

---

## 1. Esquema de Versionado Semántico (SemVer)

La plantilla utiliza el formato `MAJOR.MINOR.PATCH` (ej. `v1.0.0`):

- **MAJOR (v2.0.0):** Cambios estructurales que rompen la compatibilidad con versiones previas (ej. reestructuración total de carpetas o cambio radical de motor LaTeX).
- **MINOR (v1.1.0):** Incorporación de nuevas funciones, macros o ejemplos compatibles con versiones previas (ej. adición de nuevos entornos de código o tablas).
- **PATCH (v1.0.1):** Correcciones menores de errores tipográficos, ortográficos o ajustes finos de márgenes.

---

## 2. Procedimiento para Publicar una Nueva Versión

1. **Actualizar el Changelog:**
   Asegúrate de que `CHANGELOG.md` documente todos los cambios agregados, modificados o corregidos bajo la nueva versión.

2. **Verificar Compilación Limpia:**
   ```bash
   latexmk -C
   latexmk main.tex
   ```

3. **Crear una Etiqueta Anotada (Git Tag):**
   *(Ejecutar únicamente cuando se desee congelar una versión oficial para el semestre)*:
   ```bash
   git tag -a v1.0.0 -m "Release oficial de la Plantilla v1.0.0 para Trabajo Terminal UPIIZ"
   ```

4. **Enviar la Etiqueta a GitHub:**
   ```bash
   git push origin v1.0.0
   ```

5. **Crear el Release en GitHub:**
   - En la página del repositorio en GitHub, ve a **Releases** $\rightarrow$ **Draft a new release**.
   - Selecciona la etiqueta `v1.0.0`.
   - Asigna como título: *"Plantilla Institucional de Trabajo Terminal v1.0.0"*.
   - Pega el contenido correspondiente de `CHANGELOG.md`.
   - Haz clic en **Publish release**.
