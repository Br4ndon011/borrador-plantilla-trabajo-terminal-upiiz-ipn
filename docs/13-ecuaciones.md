# Guía 13: Escritura de Ecuaciones y Unidades SI

LaTeX es el estándar mundial para la escritura de expresiones matemáticas y fórmulas de ingeniería. Esta guía te enseña a escribir ecuaciones numeradas y unidades físicas según el Sistema Internacional.

---

## 1. Modo Matemático en Línea vs. Ecuación en Bloque

- **Matemáticas dentro del párrafo (Inline):** Enciérralas entre signos de dólar `$ ... $`:
  ```latex
  donde la constante de tiempo $\tau = R \cdot C$ determina la velocidad de carga.
  ```
- **Ecuación destacada y numerada en bloque:** Utiliza el entorno `equation`:
  ```latex
  \begin{equation}
      V_{\text{out}}(t) = V_{\text{in}} \left( 1 - e^{-\frac{t}{R C}} \right)
      \label{eq:carga-capacitor}
  \end{equation}
  ```

---

## 2. Sistema de Ecuaciones Alineadas (`align`)

Para varias ecuaciones alineadas con respecto al signo igual (`=`):

```latex
\begin{align}
    \dot{x}_1(t) &= x_2(t) \label{eq:estado-1} \\
    \dot{x}_2(t) &= -\frac{k}{m} x_1(t) - \frac{b}{m} x_2(t) + \frac{1}{m} u(t) \label{eq:estado-2}
\end{align}
```
*(El símbolo `&` indica el punto de alineación vertical y `\\` el salto de línea).*

---

## 3. Matrices y Vectores

```latex
\begin{equation}
    \begin{bmatrix}
        \dot{x}_1 \\
        \dot{x}_2
    \end{bmatrix}
    =
    \begin{bmatrix}
        0 & 1 \\
        -\frac{k}{m} & -\frac{b}{m}
    \end{bmatrix}
    \begin{bmatrix}
        x_1 \\
        x_2
    \end{bmatrix}
    +
    \begin{bmatrix}
        0 \\
        \frac{1}{m}
    \end{bmatrix}
    u(t)
    \label{eq:espacio-estados}
\end{equation}
```

---

## 4. Unidades Físicas Formales (`siunitx`)

En ingeniería, las unidades **nunca deben escribirse en cursiva**. El paquete `siunitx` formatea las magnitudes y unidades con espacio no rompible y tipografía recta:

| Qué deseas escribir | Comando LaTeX | Resultado generado |
|---|---|---|
| **Magnitud con unidad** | `\qty{12.5}{\volt}` | $12.5\text{ V}$ |
| **Resistencia** | `\qty{4.7}{\kilo\ohm}` | $4.7\text{ k}\Omega$ |
| **Frecuencia** | `\qty{20}{\kilo\hertz}` | $20\text{ kHz}$ |
| **Velocidad** | `\qty{1.5}{\meter\per\second}` | $1.5\text{ m/s}$ |
| **Aceleración** | `\qty{9.81}{\meter\per\second\squared}` | $9.81\text{ m/s}^2$ |
| **Ángulo** | `\ang{45}` | $45^\circ$ |
| **Temperatura** | `\qty{25.4}{\degreeCelsius}` | $25.4\ ^\circ\text{C}$ |
| **Solo la unidad** | `\unit{\newton\meter}` | $\text{N}\cdot\text{m}$ |

---

## 5. Cómo Referenciar Ecuaciones

Utiliza `\eqref{eq:mi-etiqueta}` (agrega los paréntesis automáticamente):

```latex
A partir del modelo cinemático presentado en la \eqref{eq:carga-capacitor}, se deduce...
```

---

## 6. Próximo Paso

Continúa con la [Guía 14: Manejo de Bibliografía en Formato IEEE](14-bibliografia-ieee.md).
