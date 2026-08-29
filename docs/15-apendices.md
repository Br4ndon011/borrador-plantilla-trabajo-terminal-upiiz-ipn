# Guía 15: Apéndices, Planos y Datasheets

Los apéndices permiten documentar información técnica complementaria que es vital para la reproducibilidad del Trabajo Terminal pero cuya extensión saturaría la lectura de los capítulos principales.

---

## 1. ¿Qué Información Debe Incluirse en los Apéndices?

1. **Cálculos extensos:** Desarrollos analíticos completos de cinemática inversa, balances térmicos, dimensionamiento de engranes o análisis de esfuerzos detallados.
2. **Planos mecánicos:** Planos normalizados de despiece, ensambles y vistas en explosión (con cotas y tolerancias).
3. **Diagramas electrónicos:** Esquemáticos de circuitos impresos (PCB), diagramas de cableado y mapas de puertos de microcontrolador.
4. **Hojas de especificaciones (Datasheets):** Tablas de pines y curvas características de sensores y actuadores clave.
5. **Código fuente completo:** Firmware de microcontroladores y scripts de procesamiento en Python/MATLAB.
6. **Cronograma de Trabajo Terminal II:** Planeación temporal de TT II (exclusivo para el reporte de TT I).

---

## 2. Estructura y Numeración Automática

En LaTeX, el comando `\appendix` transforma automáticamente la numeración de los capítulos en letras: **Apéndice A, Apéndice B, Apéndice C...**

Para agregar un nuevo apéndice en `apendices/apendices.tex`:

```latex
\chapter{Título de tu Nuevo Apéndice}
\label{ap:mi-nuevo-apendice}

Contenido técnico del apéndice...
```

---

## 3. Cómo Insertar Planos Mecánicos en PDF Completo

Si exportaste planos normalizados en formato PDF desde SolidWorks, AutoCAD o KiCAD, puedes insertarlos a página completa empleando `pdfpages`:

```latex
\chapter{Planos de manufactura estructural}
\label{ap:planos-completos}

\includepdf[pages=-, landscape=true]{figuras/proyecto/planos_ensamble.pdf}
```

---

## 4. Próximo Paso

Continúa con la [Guía 16: Cómo Compilar y Generar el PDF](16-compilar.md).
