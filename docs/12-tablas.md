# Guía 12: Creación de Tablas Formales

Esta guía explica cómo diseñar tablas técnicas, estructuradas y formalmente maquetadas para tu reporte de Trabajo Terminal.

---

## 1. Reglas de Estilo para Tablas de Ingeniería

1. **Sin líneas verticales excesivas:** Las tablas formales de ingeniería evitan las cuadrículas completas de Excel. Se emplean líneas horizontales limpias con el paquete `booktabs` (`\toprule`, `\midrule`, `\bottomrule`).
2. **El título (`\caption`) va ARRIBA de la tabla:** A diferencia de las figuras (cuyo título va abajo), en las tablas el `\caption` y el `\label` se colocan en la parte superior.
3. **Alineación:**
   - Textos descriptivos: alineados a la izquierda (`l` o `X`).
   - Números y cantidades: alineados a la derecha (`r`) o centrados (`c`).
   - Siempre incluye las unidades físicas en los encabezados de columna.

---

## 2. Ejemplo 1: Tabla Compacta Estándar (`tabular` + `booktabs`)

```latex
\begin{table}[htbp]
    \centering
    \caption{Consumo eléctrico y especificaciones de componentes.}
    \label{tab:componentes-consumo}
    \begin{tabular}{llr}
        \toprule
        \textbf{Componente} & \textbf{Modelo} & \textbf{Potencia (\unit{\watt})} \\
        \midrule
        Microcontrolador & ESP32-WROOM-32 & 0.8 \\
        Controlador Puente H & L298N Dual & 25.0 \\
        Sensor IMU & MPU-6050 & 0.02 \\
        Servomotor & MG996R & 4.5 \\
        \bottomrule
    \end{tabular}
\end{table}
```

---

## 3. Ejemplo 2: Tabla Ancha con Ajuste Automático (`tabularx`)

Si la tabla contiene descripciones largas y debe ocupar exactamente el $100\%$ del ancho de página, utiliza `tabularx` con una o más columnas de tipo `X`:

```latex
\begin{table}[htbp]
    \centering
    \caption{Matriz de requerimientos y criterios de selección.}
    \label{tab:requerimientos-seleccion}
    \begin{tabularx}{\textwidth}{l c X}
        \toprule
        \textbf{Subsistema} & \textbf{Voltaje (\unit{\volt})} & \textbf{Criterio de Selección y Justificación Técnica} \\
        \midrule
        Alimentación & 12.0 & Batería recargable de polímero de litio seleccionada por densidad energética. \\
        Regulación & 5.0 & Regulador conmutado reductor DC-DC de alta eficiencia ($>90\,\%$). \\
        Sensado & 3.3 & Sensores digitales I2C con baja sensibilidad a ruido electromagnético. \\
        \bottomrule
    \end{tabularx}
\end{table}
```

---

## 4. Cómo Referenciar Tablas en el Texto

Usa siempre el comando `\tabref{tab:mi-etiqueta}`:

```latex
Los resultados del balance de potencia se resumen en la \tabref{tab:componentes-consumo}.
```

---

## 5. Próximo Paso

Continúa con la [Guía 13: Escritura de Ecuaciones y Unidades SI](13-ecuaciones.md).
