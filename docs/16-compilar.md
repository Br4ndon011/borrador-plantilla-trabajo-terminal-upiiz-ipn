# Guía 16: Cómo Compilar y Generar el PDF

Esta guía explica cómo ejecutar la compilación del proyecto desde Visual Studio Code o desde la terminal de comandos.

---

## 1. Compilación desde Visual Studio Code (Método Gráfico)

1. Abre la carpeta del proyecto en VS Code.
2. Abre el archivo **`main.tex`** (o cualquier archivo `.tex`).
3. Presiona el atajo de teclado:
   ```text
   Ctrl + Alt + B
   ```
4. O en la barra lateral izquierda, haz clic en el ícono de la $\TeX$ $\rightarrow$ **Build LaTeX project** $\rightarrow$ **Recipe: LuaLaTeX (latexmk)**.
5. Para abrir la vista previa del PDF al lado de tu código, presiona:
   ```text
   Ctrl + Alt + V
   ```

---

## 2. Compilación desde la Terminal de Comandos

Abre la terminal en la raíz de tu proyecto y ejecuta simplemente:

```bash
latexmk main.tex
```

Gracias al archivo de configuración `latexmkrc` incluido en la plantilla, `latexmk` compila automáticamente con el motor oficial **LuaLaTeX**, detecta los cambios en bibliografía (`bibtex`) e índices (`tableofcontents`), y realiza las pasadas necesarias hasta que todas las referencias queden resueltas.

---

## 3. Limpieza de Archivos Temporales

Si alguna vez cambiaste nombres de etiquetas o reorganizaste capítulos y aparecen advertencias extrañas, limpia los archivos auxiliares:

- **Limpiar temporales (`.aux`, `.log`, `.toc`, etc.):**
  ```bash
  latexmk -c
  ```
- **Limpieza profunda (incluyendo el `.pdf` previo para compilar desde cero):**
  ```bash
  latexmk -C
  ```

---

## 4. Diagnóstico Rápido

### ✅ Si funciona:
- Verás el mensaje `Latexmk: All targets (main.pdf) are up-to-date`.
- Se generará el archivo `main.pdf` en la raíz con todas las páginas, firmas y bibliografía.
- ¡Puedes continuar redactando tus capítulos!

### ❌ Si no funciona:
1. Revisa la terminal o la pestaña **Output $\rightarrow$ LaTeX Workshop** en VS Code.
2. Busca la línea que empiece con el signo de admiración `!`.
3. Consulta la [Guía 22: Solución de Errores Comunes de LaTeX](22-errores-comunes-latex.md).

---

## 5. Próximo Paso

Continúa con la [Guía 17: Control de Versiones con Git](17-control-de-versiones.md).
