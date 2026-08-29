# Guía 03: Configuración de LaTeX Workshop en VS Code

Esta guía explica cómo instalar y utilizar la extensión **LaTeX Workshop** para compilar y visualizar tu Trabajo Terminal con total comodidad dentro de Visual Studio Code.

---

## 1. Instalación de la Extensión

1. Abre Visual Studio Code.
2. Abre la vista de extensiones presionando `Ctrl + Shift + X` (o haciendo clic en el ícono de bloques en la barra lateral izquierda).
3. En la barra de búsqueda superior escribe: `LaTeX Workshop`.
4. Selecciona la extensión desarrollada por **James Yu**.
5. Haz clic en el botón azul **Install**.

---

## 2. Configuración Automática del Proyecto

**No necesitas configurar nada manualmente.** La plantilla ya incluye el archivo `.vscode/settings.json` preconfigurado con las siguientes opciones profesionales:

- **Motor principal:** `latexmk` ejecutando `lualatex` con soporte completo de fuentes del sistema y caracteres en español.
- **Detección de raíz:** Define automáticamente `main.tex` como el archivo maestro del proyecto, permitiéndote compilar desde cualquier archivo abierto en `capitulos/` o `config/`.
- **Visor integrado:** Abre el PDF resultante directamente en una pestaña lateral de VS Code (`tab`).
- **Limpieza de auxiliares:** Configurado para limpiar archivos temporales (`.aux`, `.log`, `.toc`, `.fls`, `.fdb_latexmk`) sin borrar tu código fuente.

---

## 3. Atajos de Teclado Imprescindibles

| Acción | Atajo de Teclado (Windows/Linux) | Atajo (macOS) |
|---|---|---|
| **Compilar el proyecto** | `Ctrl + Alt + B` | `Cmd + Option + B` |
| **Abrir visor de PDF al lado** | `Ctrl + Alt + V` | `Cmd + Option + V` |
| **Sincronización Código $\rightarrow$ PDF (Forward Synctex)** | `Ctrl + Alt + J` | `Cmd + Option + J` |
| **Sincronización PDF $\rightarrow$ Código (Reverse Synctex)** | `Ctrl + Clic` en el PDF | `Cmd + Clic` en el PDF |

---

## 4. Uso de la Barra Lateral de LaTeX Workshop

Cuando abres un archivo `.tex` en VS Code, aparece un ícono con la letra $\TeX$ en la barra lateral izquierda:

1. **Commands $\rightarrow$ Build LaTeX project:**
   Permite compilar manualmente tu documento. Haz clic en **Recipe: LuaLaTeX (latexmk)**.
2. **Commands $\rightarrow$ View LaTeX PDF $\rightarrow$ View in VSCode tab:**
   Abre el documento compilado en una pestaña dividida a la derecha de tu código.
3. **Commands $\rightarrow$ Clean up auxiliary files:**
   Elimina todos los archivos temporales generados durante la compilación en caso de que ocurra algún error de sincronización de índices o referencias.

---

## 5. Próximo Paso

Continúa con la [Guía 04: Instalación de Git](04-instalacion-git.md) para preparar el sistema de control de versiones.
