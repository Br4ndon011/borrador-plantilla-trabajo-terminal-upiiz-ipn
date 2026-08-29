# Registro de Cambios (Changelog)

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/), y este proyecto se adhiere a [Versionado Semántico](https://semver.org/lang/es/).

## [1.1.2] - 2026-08-29

### Agregado
- Archivo `CITATION.cff` para citación formal del repositorio en GitHub con identificadores ORCID verificados.
- Sección de autoría y mantenimiento institucional en `README.md`, `LICENSE`, `main.tex` y `docs/profesor/mantenimiento.md`.
- Guía 14a (`docs/14a-mendeley.md`) para instalación, captura de metadatos y exportación BibTeX con Mendeley Reference Manager.

### Corregido
- Se unifica LuaLaTeX como motor principal de compilación oficial.
- Se alinea la configuración de `latexmkrc` ($pdf_mode = 4), VS Code (`.vscode/settings.json`) y GitHub Actions.
- Se actualiza la documentación del tipo de documento y Línea de Trabajo en el `README.md`.
- Se simplifica la compilación para estudiantes mediante la instrucción estándar `latexmk main.tex`.

## [1.1.1] - 2026-08-29

### Corregido
- Se elimina una descripción no establecida institucionalmente para la Línea de Trabajo VI, retornando una cadena vacía conforme a la literalidad del Anexo 1 del Reglamento Interno.
- Se fortalece la validación del catálogo oficial I–VI y la correspondencia entre la línea seleccionada y el número máximo de integrantes permitido (3 para Línea I, 2 para Líneas II a VI).
- Se incorporan scripts de pruebas automáticas de integridad y compilación para todas las Líneas de Trabajo en `tests/`.
- Se actualiza la documentación institucional y las advertencias docentes en `docs/09-configurar-datos-del-tt.md` y `docs/profesor/actualizar-plantilla.md`.

## [1.1.0] - 2026-08-29

### Agregado
- Sistema centralizado de selección de tipo de documento mediante la API `\TipoDocumento{PROTOCOLO|TTI|TTII}` en `config/datos.tex`.
- Catálogo institucional modular de Líneas de Trabajo en `config/lineas-trabajo.tex` con la API `\LineaTrabajo{...}`.
- Despachador modular de portadas en `frontmatter/portada.tex`.
- Portada institucional exclusiva para Protocolo de Trabajo Terminal (`frontmatter/portada-protocolo.tex`) con área de ubicación, línea de trabajo e intención de titulación.
- Portada institucional unificada para reportes de Trabajo Terminal I y II (`frontmatter/portada-tt.tex`).
- Inclusión condicional de portada interna de firmas (exclusiva para TT I y TT II).
- Advertencias de validación de campos obligatorios mediante `\validarDatosDocumento`.

## [1.0.0] - 2026-08-29

### Agregado
- Plantilla inicial modular para Reportes de Trabajo Terminal de la UPIIZ-IPN (Ingeniería Mecatrónica).
- Soporte condicional para Trabajo Terminal I (Diseño detallado) y Trabajo Terminal II (Implementación y Validación).
- Centralización de metadatos del proyecto y autores en `config/datos.tex`.
- Configuración tipográfica institucional estricta (Arial 16pt, 14pt, 12pt, 10pt, márgenes e interlineado 1.5).
- Portada oficial institucional con franja reglamentaria y portada interna con registro de firmas de jurado.
- Sistema de bibliografía en formato IEEE con base de datos en `bibliografia/referencias.bib`.
- Colección de ejemplos prácticos para figuras, tablas, ecuaciones, código fuente y referencias.
- Configuración de entorno para Visual Studio Code con LaTeX Workshop (`.vscode/settings.json`).
- Automatización de compilación multiplataforma con `latexmk` (`latexmkrc`).
- Integración continua en GitHub Actions (`.github/workflows/latex.yml`).
- Guías paso a paso completas en `docs/` para principiantes y docentes (`docs/profesor/`).
