# Guía 22: Solución de Errores Comunes de LaTeX

En LaTeX es fundamental distinguir entre un **ERROR** (que detiene la generación del PDF) y una **ADVERTENCIA (Warning)** (que genera el PDF pero señala un detalle estético o de referencia pendiente).

---

## 1. Diferencia entre Error y Advertencia

- **ERROR (`!`):** El compilador no puede continuar. Debes corregirlo para obtener el archivo `main.pdf`.
- **ADVERTENCIA (`LaTeX Warning`):** El PDF sí se genera. Por lo general indica que falta compilar otra vez para resolver una cita o que un texto se desborda unos milímetros de la página.

---

## 2. Los 10 Errores y Advertencias Más Frecuentes

### 1. `! Undefined control sequence`
- **Qué significa:** Escribiste un comando que no existe o está mal escrito.
- **Causa común:** Error tipográfico (ej. `\includegrahics` en lugar de `\includegraphics` o `\centring` en lugar de `\centering`).
- **Solución:** Revisa el número de línea que indica el error y corrige la ortografía del comando.

---

### 2. `! LaTeX Error: File '...' not found`
- **Qué significa:** LaTeX no encuentra la imagen o el archivo `.tex` que intentaste incluir.
- **Causa común:** La ruta está mal escrita o la imagen tiene una extensión distinta (ej. pusiste `.png` pero el archivo era `.jpg`).
- **Solución:** Verifica que el archivo exista en `figuras/proyecto/` y que el nombre coincida exactamente respetando mayúsculas y minúsculas.

---

### 3. `! Missing $ inserted`
- **Qué significa:** Usaste un símbolo matemático (como `_`, `^`, `\alpha`, `\sum`) en texto normal sin encerrarlo entre `$ ... $`.
- **Causa común:** Escribir nombres de variables como `variable_1` en lugar de `variable\_1` o `$variable_1$`.
- **Solución:** Si es una fórmula o variable, enciérrala entre `$ ... $`. Si querías escribir un guión bajo en texto, escribe `\_`.

---

### 4. `LaTeX Warning: Citation '...' on page X undefined`
- **Qué significa:** Citaste una clave con `\cite{clave}` que no existe en `bibliografia/referencias.bib`.
- **Solución:** Verifica que la clave en tu `.tex` sea idéntica a la que definiste en el archivo `.bib` y vuelve a compilar.

---

### 5. `LaTeX Warning: Reference '...' on page X undefined`
- **Qué significa:** Usaste `\figref{fig:xyz}` o `\ref{sec:xyz}` pero no existe un `\label{fig:xyz}` correspondiente.
- **Solución:** Agrega la etiqueta `\label{...}` dentro de la figura, tabla o capítulo y compila 2 veces.

---

### 6. `! kpathsea: Running mktexmf / Font Arial not found`
- **Qué significa:** El motor no encuentra la fuente Arial en el sistema.
- **Solución:**
  - En Windows y macOS: Asegúrate de estar compilando con **XeLaTeX** o **LuaLaTeX** (los motores que leen las fuentes instaladas en el sistema operativo).
  - En Linux: Instala el paquete de fuentes de Microsoft:
    ```bash
    sudo apt install -y ttf-mscorefonts-installer && sudo fc-cache -f
    ```

---

### 7. `! LaTeX Error: File 'paquete.sty' not found`
- **Qué significa:** Falta instalar un paquete en tu distribución de LaTeX.
- **Solución:**
  - En MiKTeX: Abre *MiKTeX Console* $\rightarrow$ *Settings* $\rightarrow$ *Install missing packages on-the-fly* $\rightarrow$ selecciona **Yes**.
  - En Ubuntu/Debian: `sudo apt install -y texlive-latex-extra`.

---

### 8. `! Emergency stop`
- **Qué significa:** LaTeX se detuvo de emergencia porque encontró un error fatal previo o el archivo raíz no existe.
- **Solución:** Desplaza la terminal hacia arriba para leer el primer mensaje de error con `!` que provocó la parada.

---

### 9. `Overfull \hbox (X pt too wide)`
- **Qué es:** **ADVERTENCIA**. Una palabra, tabla o fórmula es ligeramente más ancha que los márgenes de la página y sobresale hacia la derecha.
- **Solución:** Si es una tabla, usa `tabularx` con columna `X`. Si es una ecuación larga, divídela en varias líneas con `align` o `split`.

---

### 10. `Underfull \hbox (badness X)`
- **Qué es:** **ADVERTENCIA**. LaTeX tuvo que estirar un poco el espacio entre palabras para justificar el párrafo. El PDF se genera normalmente y casi nunca requiere corrección manual.

---

## 3. Próximo Paso

Continúa con la [Guía 23: Lista de Verificación para la Entrega Final](23-entrega-final.md).
