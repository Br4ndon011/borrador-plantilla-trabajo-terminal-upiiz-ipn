# Registro de Cambios (Changelog)

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/), y este proyecto se adhiere a [Versionado Semántico](https://semver.org/lang/es/).

## [1.1.0] - 2026-08-29

### Agregado
- Sistema centralizado de selección de tipo de documento mediante la API `\TipoDocumento{PROTOCOLO|TTI|TTII}` en `config/datos.tex`.
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
