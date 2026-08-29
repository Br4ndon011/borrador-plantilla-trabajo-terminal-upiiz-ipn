# Plantilla Institucional de Trabajo Terminal (UPIIZ - IPN)
### Programa Académico de Ingeniería Mecatrónica

[![Validar Compilación LaTeX](https://github.com/REPOSITORIO_OFICIAL/Plantilla_Trabajo_Terminal/actions/workflows/latex.yml/badge.svg)](https://github.com/REPOSITORIO_OFICIAL/Plantilla_Trabajo_Terminal/actions/workflows/latex.yml)
[![Versión](https://img.shields.io/badge/versión-1.1.1-blue.svg)](CHANGELOG.md)
[![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-green.svg)](LICENSE)
[![Motor: LuaLaTeX](https://img.shields.io/badge/Motor-LuaLaTeX-orange.svg)](https://lualatex.org/)

Bienvenido al repositorio oficial de la **Plantilla Institucional de Trabajo Terminal** para la carrera de **Ingeniería Mecatrónica** de la **Unidad Profesional Interdisciplinaria de Ingeniería Campus Zacatecas (UPIIZ)** del **Instituto Politécnico Nacional (IPN)**.

Esta plantilla ha sido diseñada para ser **modular, robusta, fácil de usar y 100% conforme a los lineamientos normativos institucionales**.

---

> ### 🚀 ¿Primera vez con LaTeX o Git?
> **Si nunca has usado LaTeX, Git, GitHub o Visual Studio Code, no te preocupes:**
> 👉 **[Comienza aquí con la Guía de Inicio Rápido](docs/00-inicio-rapido.md)** 👈
>
> Esta guía te llevará paso a paso desde cero, sin asumir ningún conocimiento previo.

---

## 🎯 Propósito y Documentos Soportados

La plantilla cubre todo el ciclo formal de titulación curricular de Trabajo Terminal en la UPIIZ:
- **1. Protocolo de Trabajo Terminal (`PROTOCOLO`):** Registro formal del proyecto con área de ubicación, línea de trabajo e intención de titulación.
- **2. Trabajo Terminal I (`TTI`):** Reporte de diseño mecatrónico detallado (cálculos, selección de componentes, planos mecánicos, esquemáticos electrónicos, algoritmos, simulaciones y cronograma hacia TT II).
- **3. Trabajo Terminal II (`TTII`):** Reporte final con manufactura, integración física, programación de firmware, validación experimental, resultados, conclusiones y trabajo a futuro.

La selección se realiza configurando una sola línea en `config/datos.tex`:
```latex
\TipoDocumento{PROTOCOLO} % o TTI o TTII
```
La plantilla adapta automáticamente la portada correspondiente, la inclusión de portada interna de firmas, agradecimientos, dedicatorias, títulos de validación y apéndices.

---

## 📋 Requisitos del Sistema

Para compilar la plantilla en tu computadora necesitas:
1. **Distribución LaTeX:** [MiKTeX](https://miktex.org/) o [TeX Live](https://tug.org/texlive/) (incluye **LuaLaTeX** y `latexmk`).
2. **Editor recomendado:** [Visual Studio Code](https://code.visualstudio.com/) con la extensión **LaTeX Workshop**.
3. **Control de versiones:** [Git](https://git-scm.com/) y una cuenta en [GitHub](https://github.com/).
4. **Tipografía:** Fuente **Arial** (instalada por defecto en Windows y macOS; disponible en Linux mediante `ttf-mscorefonts-installer` o Liberation Sans como respaldo automático).

---

## ⚡ Inicio Rápido en 4 Pasos

1. **Obtener tu propia copia:**
   Haz clic en el botón verde **`Use this template`** $\rightarrow$ **`Create a new repository`** en GitHub.
2. **Clonar tu repositorio:**
   ```bash
   git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   ```
3. **Configurar tus datos:**
   Abre la carpeta en VS Code y edita el archivo `config/datos.tex` con tus datos personales, los de tus compañeros, asesores y título del proyecto.
4. **Compilar:**
   - Desde VS Code: Presiona `Ctrl + Alt + B` (o guarda `main.tex`).
   - Desde la terminal:
     ```bash
     latexmk -lualatex main.tex
     ```
   El archivo generado será **`main.pdf`**.

---

## 📂 Estructura del Proyecto

```text
Plantilla_Trabajo_Terminal/
├── main.tex                 <- Archivo raíz maestro (incluye los módulos)
├── latexmkrc                <- Configuración de compilación con LuaLaTeX
├── config/
│   ├── datos.tex            <- EDITA AQUÍ: Modalidad (TT1/TT2), autores, asesores, jurado
│   ├── formato.tex          <- Parámetros institucionales (Arial, 1.5, márgenes)
│   └── comandos.tex         <- Macros y comandos mecatrónicos auxiliares
├── frontmatter/             <- Portada, portada interna, resumen, abstract
├── capitulos/               <- Capítulos 01 al 10 (un archivo .tex por sección)
├── apendices/               <- Cálculos, planos, esquemáticos y cronograma
├── bibliografia/            <- Base de datos bibliográfica IEEE (referencias.bib)
├── figuras/                 <- Logotipos institucionales e imágenes del proyecto
├── ejemplos/                <- Bloques de ejemplo listos para copiar (tablas, figuras, código)
└── docs/                    <- Colección de 25 guías paso a paso para principiantes
```

---

## 📚 Índice de Documentación Completa

Hemos preparado manuales detallados paso a paso clasificados por tema:

### Preparación del Entorno
- [00. Inicio Rápido](docs/00-inicio-rapido.md)
- [01. Instalación de LaTeX en Windows, Linux y macOS](docs/01-instalacion-latex.md)
- [02. Instalación de Visual Studio Code](docs/02-instalacion-vscode.md)
- [03. Configuración de LaTeX Workshop](docs/03-configuracion-latex-workshop.md)
- [04. Instalación de Git](docs/04-instalacion-git.md)
- [05. Configuración Inicial de Git](docs/05-configuracion-git.md)
- [06. Cuenta y Uso de GitHub](docs/06-github.md)
- [07. Cómo Obtener la Plantilla (GitHub Template vs Clone)](docs/07-obtener-la-plantilla.md)

### Redacción del Trabajo Terminal
- [08. Estructura del Proyecto y Carpetas](docs/08-estructura-del-proyecto.md)
- [09. Configurar Datos del Trabajo Terminal](docs/09-configurar-datos-del-tt.md)
- [10. Cómo Escribir los Capítulos](docs/10-escribir-capitulos.md)
- [11. Inserción de Figuras y Diagramas](docs/11-figuras.md)
- [12. Creación de Tablas Formales](docs/12-tablas.md)
- [13. Escritura de Ecuaciones y Unidades SI](docs/13-ecuaciones.md)
- [14. Manejo de Bibliografía en Formato IEEE](docs/14-bibliografia-ieee.md)
- [15. Apéndices, Planos y Datasheets](docs/15-apendices.md)
- [16. Cómo Compilar y Generar el PDF](docs/16-compilar.md)

### Control de Versiones y Trabajo en Equipo
- [17. Fundamentos de Control de Versiones con Git](docs/17-control-de-versiones.md)
- [18. Flujo de Trabajo Diario con Git](docs/18-flujo-de-trabajo-git.md)
- [19. Trabajo en Equipo para 2 o 3 Integrantes](docs/19-trabajo-en-equipo.md)
- [20. Cómo Resolver Conflictos en Git](docs/20-resolver-conflictos.md)
- [21. Recuperación de Cambios y Consulta de Historial](docs/21-recuperacion-git.md)
- [22. Guía de Solución de Errores Comunes de LaTeX](docs/22-errores-comunes-latex.md)
- [23. Lista de Verificación para la Entrega Final](docs/23-entrega-final.md)
- [24. Preguntas Frecuentes (FAQ)](docs/24-preguntas-frecuentes.md)

### Para Profesores y Administradores de la Plantilla
- [Mantenimiento de la Plantilla](docs/profesor/mantenimiento.md)
- [Actualización de Estilos y Requisitos](docs/profesor/actualizar-plantilla.md)
- [Publicación de Nuevas Versiones y Tags](docs/profesor/publicar-version.md)

---

## 🏛️ Formato Normativo Institucional Implementado

| Parámetro | Requisito Institucional UPIIZ-IPN | Implementación en la Plantilla |
|---|---|---|
| **Tipografía de Títulos** | Arial 16 pt, Negrita | `\titleformat{\chapter}` |
| **Tipografía de Subtítulos** | Arial 14 pt, Negrita | `\titleformat{\section}` |
| **Tipografía de Cuerpo** | Arial 12 pt | `\fontsize{12}{15}\selectfont` |
| **Tipografía de Tablas/Figuras** | Arial 10 pt | `\captionsetup{font={small}}` |
| **Interlineado** | 1.5 | `\setstretch{1.5}` (`setspace`) |
| **Márgenes** | Sup: 2.5cm, Inf: 2.5cm, Der: 2.5cm, Izq: 3.0cm | `geometry` |
| **Alineación** | Justificado | Por defecto |
| **Citas y Referencias** | Formato IEEE | `IEEEtran.bst` |

---

## 📄 Licencia

Este proyecto está bajo la Licencia **MIT** para fines académicos y educativos. Consulta el archivo [LICENSE](LICENSE) para más información.
