# Guía 11: Inserción de Figuras y Diagramas

Esta guía explica cómo agregar imágenes, fotografías de prototipos y diagramas de ingeniería a tu reporte de Trabajo Terminal con numeración automática y referencias cruzadas.

---

## 1. Buenas Prácticas para Guardar Imágenes

1. **Ubicación:** Guarda todas las imágenes de tu proyecto dentro de la carpeta:
   ```text
   figuras/proyecto/
   ```
2. **Nombres de archivo:** Usa nombres en minúsculas, sin espacios ni caracteres especiales:
   - ✅ `diagrama_bloques.png`, `esquematico_potencia.png`, `prototipo_vista_superior.jpg`
   - ❌ `Diagrama de bloques final (1).PNG`, `foto diseño.jpg`
3. **Formatos recomendados:**
   - **PNG:** Para capturas de pantalla, diagramas de bloques y esquemáticos.
   - **JPG / JPEG:** Para fotografías reales de prototipos, maquinaria e instalaciones.
   - **PDF:** Para planos vectoriales exportados desde AutoCAD, SolidWorks o KiCAD.

---

## 2. Inserción de una Figura Individual

Para insertar una figura centrada, utiliza el entorno `figure`:

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.7\textwidth]{figuras/proyecto/mi_diagrama.png}
    \caption{Diagrama de bloques del lazo cerrado de control.}
    \label{fig:diagrama-control}
\end{figure}
```

### Explicación de los comandos:
- `[htbp]`: Indicadores de posición preferida (`h` = here, `t` = top, `b` = bottom, `p` = page of floats).
- `width=0.7\textwidth`: Escala la imagen al $70\%$ del ancho de la caja de texto.
- `\caption{...}`: Texto explicativo de la figura (Arial 10 pt automático).
- `\label{fig:...}`: Etiqueta interna única para referenciar la figura en el texto. **Debe ir SIEMPRE después del `\caption`**.

---

## 3. Inserción de Subfiguras Lado a Lado (a, b)

Para colocar dos imágenes lado a lado:

```latex
\begin{figure}[htbp]
    \centering
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{figuras/proyecto/sensor_vista1.png}
        \caption{Vista lateral del soporte.}
        \label{fig:sensor-lat}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.45\textwidth}
        \centering
        \includegraphics[width=\textwidth]{figuras/proyecto/sensor_vista2.png}
        \caption{Vista frontal del sensor.}
        \label{fig:sensor-front}
    \end{subfigure}
    \caption{Montaje mecánico del sensor de posición angular.}
    \label{fig:sensor-montaje}
\end{figure}
```

---

## 4. Cómo Referenciar Figuras en el Texto

> ⚠️ **REGLA FUNDAMENTAL:** **NUNCA escribas números a mano como *"En la Figura 3.2 se muestra..."***. Si agregas o eliminas un capítulo o figura previa, todos los números cambiarán y quedarán desfasados.

Usa siempre el comando de referencia cruzada:

```latex
Como se puede observar en la \figref{fig:diagrama-control}, la señal de realimentación...
```
O de forma equivalente:
```latex
Como se aprecia en la Figura~\ref{fig:diagrama-control}...
```

LaTeX generará automáticamente el número correlativo correspondiente (ej. *"Figura 7.1"*).

---

## 5. Próximo Paso

Continúa con la [Guía 12: Creación de Tablas Formales](12-tablas.md).
