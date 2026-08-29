# Guía 08: Estructura del Proyecto y Carpetas

Esta guía explica en detalle la organización modular de los archivos de la plantilla, indicando con claridad qué archivos debes editar y cuáles no deben modificarse.

---

## 1. Árbol General de Directorios

```text
Plantilla_Trabajo_Terminal/
├── main.tex                    <- Archivo maestro raíz
├── latexmkrc                   <- Configuración de compilación automatizada
├── README.md                   <- Documentación principal del repositorio
├── LICENSE                     <- Licencia MIT
├── CONTRIBUTING.md             <- Guía de contribución
├── CHANGELOG.md                <- Historial de versiones
├── .gitignore                  <- Filtro de archivos auxiliares
├── .gitattributes              <- Normalización de saltos de línea
│
├── .vscode/
│   └── settings.json           <- Configuración de VS Code y LaTeX Workshop
│
├── .github/
│   ├── workflows/
│   │   └── latex.yml           <- Integración continua en GitHub Actions
│   └── ISSUE_TEMPLATE/         <- Plantillas para reporte de errores y funciones
│
├── config/
│   ├── datos.tex               <- [EDITAR] Datos de alumnos, asesores, título y modalidad
│   ├── formato.tex             <- [NO EDITAR] Formato institucional y tipografía Arial
│   └── comandos.tex            <- [NO EDITAR] Macros y lógica condicional
│
├── frontmatter/
│   ├── portada.tex             <- [NO EDITAR] Portada oficial reglamentaria
│   ├── portada-interna.tex     <- [NO EDITAR] Portada interna con firmas
│   ├── agradecimientos.tex     <- [EDITAR] Agradecimientos (solo TT II)
│   ├── dedicatorias.tex        <- [EDITAR] Dedicatorias (solo TT II)
│   ├── resumen.tex             <- [EDITAR] Resumen en español y palabras clave
│   └── abstract.tex            <- [EDITAR] Abstract en inglés y keywords
│
├── capitulos/                  <- [EDITAR] Contenido principal del Trabajo Terminal
│   ├── 01-introduccion.tex
│   ├── 02-justificacion.tex
│   ├── 03-antecedentes.tex
│   ├── 04-marco-teorico.tex
│   ├── 05-estado-del-arte.tex
│   ├── 06-planteamiento-problema.tex
│   ├── 07-desarrollo.tex
│   ├── 08-validacion.tex
│   ├── 09-conclusiones.tex
│   └── 10-trabajo-futuro.tex   <- Solo visible en TT II
│
├── apendices/                  <- [EDITAR] Información técnica complementaria
│   ├── apendices.tex           <- Cálculos, planos, diagramas y hojas técnicas
│   └── cronograma-tt2.tex      <- Solo visible en TT I
│
├── bibliografia/
│   └── referencias.bib         <- [EDITAR] Base de datos BibTeX en formato IEEE
│
├── figuras/
│   ├── institucional/          <- [NO EDITAR] Logotipos oficiales IPN y UPIIZ
│   └── proyecto/               <- [EDITAR] Guarda aquí todas tus fotos y diagramas
│
├── ejemplos/                   <- [CONSULTAR] Bloques de código listos para copiar
│   ├── figuras.tex
│   ├── tablas.tex
│   ├── ecuaciones.tex
│   ├── codigo.tex
│   └── referencias.tex
│
└── docs/                       <- [CONSULTAR] Manuales y guías paso a paso
```

---

## 2. Archivos que SÍ Debe Editar el Alumno

| Archivo | Qué contiene y cómo editarlo |
|---|---|
| `config/datos.tex` | Tu nombre, número de boleta, asesores, jurado, título y modalidad (TT I o TT II). |
| `frontmatter/resumen.tex` | Resumen en español (1 párrafo, máx. 200 palabras, tiempo pasado) y palabras clave. |
| `frontmatter/abstract.tex` | Resumen en inglés y keywords equivalentes. |
| `frontmatter/agradecimientos.tex` | Agradecimientos personales e institucionales (solo TT II). |
| `frontmatter/dedicatorias.tex` | Dedicatorias (solo TT II). |
| `capitulos/*.tex` | La redacción de cada capítulo de tu Trabajo Terminal. |
| `bibliografia/referencias.bib` | Las entradas BibTeX de todos los artículos, libros y manuales que cites. |
| `apendices/*.tex` | Cálculos detallados, planos, diagramas esquemáticos y cronograma. |
| `figuras/proyecto/*` | Todas las imágenes, fotos de prototipos y diagramas que generes. |

---

## 3. Archivos que NO Debes Modificar (Salvo Indicación Docente)

- `config/formato.tex`: Contiene los márgenes de 2.5/3.0 cm, el interlineado de 1.5 y las fuentes Arial. Modificarlo alterará el cumplimiento institucional.
- `config/comandos.tex`: Contiene la lógica interna de firmas dinámicas y selección de modalidad.
- `frontmatter/portada.tex` y `frontmatter/portada-interna.tex`: Diseñadas conforme al formato oficial del IPN.
- `.vscode/settings.json` y `latexmkrc`: Configuran la compilación automática.
- `.github/workflows/latex.yml`: Automatización de pruebas en la nube.

---

## 4. Archivos Generados Automáticamente (No Versionar)

Durante la compilación, LaTeX genera archivos temporales (`.aux`, `.log`, `.toc`, `.lof`, `.lot`, `.fls`, `.fdb_latexmk`, `.synctex.gz`) y el documento final `main.pdf`. El archivo `.gitignore` se encarga de que estos archivos no ensucien tu historial de Git.

---

## 5. Próximo Paso

Continúa con la [Guía 09: Configuración de Datos del Trabajo Terminal](09-configurar-datos-del-tt.md).
