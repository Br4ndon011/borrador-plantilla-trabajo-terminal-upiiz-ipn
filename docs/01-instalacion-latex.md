# Guía 01: Instalación de LaTeX en Windows, Linux y macOS

Esta guía explica qué es LaTeX, qué distribución instalar en tu sistema operativo y cómo comprobar que tu entorno está listo para compilar la plantilla institucional con la tipografía **Arial**.

---

## 1. Conceptos Fundamentales

- **¿Qué es LaTeX?** Es un sistema de composición tipográfica de alta calidad diseñado para documentos técnicos y científicos. A diferencia de un procesador visual como Word, en LaTeX escribes texto plano estructurado con comandos y el compilador genera un documento PDF con maquetación profesional y tipografía estricta.
- **¿Qué es una distribución LaTeX?** Es el paquete completo de software que contiene el compilador, los paquetes de extensión (para tablas, figuras, matemáticas), las fuentes tipográficas y los utilitarios de automatización (como `latexmk` y `bibtex`).
- **¿Qué es un motor o compilador?** Es el programa ejecutable que lee tus archivos `.tex` y genera el `.pdf`.
  - `pdfLaTeX`: Motor clásico. No soporta fuentes TrueType/OpenType del sistema de forma directa; simula Helvetica en lugar de Arial real.
  - `XeLaTeX`: Motor moderno con soporte nativo de UTF-8 y fuentes del sistema operativo mediante `fontspec`.
  - `LuaLaTeX` *(Recomendado por la plantilla)*: Motor moderno, estándar actual de TeX Live y MiKTeX. Maneja UTF-8 nativo, fuentes TrueType/OpenType del sistema operativo (Arial oficial) y scripting embebido.

---

## 2. Instalación en Windows (Opción Recomendada: MiKTeX)

MiKTeX es la distribución más ligera y popular para Windows porque instala los paquetes faltantes de forma automática bajo demanda.

1. Entra al sitio oficial: [miktex.org/download](https://miktex.org/download).
2. Descarga el instalador para Windows (**MiKTeX Installer**).
3. Ejecuta el archivo descargado:
   - Acepta los términos de la licencia.
   - En *Install MiKTeX for:*, selecciona **"Only for: [Tu Usuario]"** (o para todos los usuarios si cuentas con permisos de administrador).
   - **MUY IMPORTANTE:** En la pantalla de opciones, en la casilla **"Install missing packages on-the-fly"**, selecciona **"Yes"** (para que MiKTeX descargue e instale automáticamente cualquier paquete que falte sin detenerte con ventanas emergentes).
4. Haz clic en **Start** y espera a que concluya la instalación (toma de 5 a 10 minutos).
5. Reinicia tu computadora para asegurar que las variables de entorno (`PATH`) se actualicen correctamente.

---

## 3. Instalación Alternativa en Windows (TeX Live)

Si prefieres una instalación completa que incluya todos los paquetes existentes sin descargas adicionales:
1. Descarga el instalador `install-tl-windows.exe` desde [tug.org/texlive](https://tug.org/texlive/acquire-netinstall.html).
2. Ejecuta el instalador y selecciona **Instalación completa (Scheme-full)**.
3. El proceso puede demorar de 30 a 60 minutos según tu velocidad de internet.

---

## 4. Instalación en Linux (Ubuntu / Debian / Fedora)

En distribuciones basadas en Debian/Ubuntu:
```bash
sudo apt update
sudo apt install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra texlive-luatex texlive-xetex latexmk ttf-mscorefonts-installer
sudo fc-cache -f -v
```

En Fedora:
```bash
sudo dnf install -y texlive-scheme-medium latexmk
```

---

## 5. Instalación en macOS

En macOS, la distribución oficial es **MacTeX**:
1. Descarga el paquete `MacTeX.pkg` desde [tug.org/mactex](https://tug.org/mactex/).
2. O instálalo mediante Homebrew:
   ```bash
   brew install --cask mactex-no-gui
   ```

---

## 6. Verificación de la Instalación

Abre una terminal (PowerShell en Windows, Terminal en Linux/macOS) y ejecuta los siguientes comandos:

```bash
lualatex --version
```
**Resultado esperado:**
```text
This is LuaHBTeX, Version 1.24.0 (MiKTeX 25.12) ...
```

Luego verifica `latexmk`:
```bash
latexmk --version
```
**Resultado esperado:**
```text
Latexmk, John Collins, Version 4.87...
```

---

## 7. ¿Qué hacer si no se reconoce el comando?

Si la terminal responde `'lualatex' is not recognized as an internal or external command`:
1. Asegúrate de haber reiniciado la terminal o la computadora tras la instalación.
2. Si persiste, verifica que la ruta `C:\Program Files\MiKTeX\miktex\bin\x64` (o la ruta correspondiente en tu usuario) esté agregada en las Variables de Entorno del Sistema (`PATH`).
