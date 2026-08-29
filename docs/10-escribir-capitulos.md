# Guía 10: Cómo Escribir los Capítulos

Esta guía explica las normas de redacción, límites de extensión institucional y la estructura que debe llevar cada capítulo dentro de la carpeta `capitulos/`.

---

## 1. Normas Generales de Redacción Institucional

- **Tiempo verbal:**
  - El **Resumen** y el **Abstract** se redactan estrictamente en **tiempo pasado** (*"Se diseñó...", "Se validó..."*).
  - El **cuerpo del documento** (Introducción hasta Conclusiones) se redacta en **tiempo presente** (*"En este capítulo se analiza...", "El sistema consta de..."*).
- **Persona gramatical:** Tercera persona impersonal (*"Se implementó un filtro"* en lugar de *"Nosotros implementamos un filtro"* o *"Implementé un filtro"*).
- **Justificación de párrafos:** Todo el documento está configurado automáticamente con texto justificado e interlineado de 1.5.

---

## 2. Guía Capítulo por Capítulo

### `01-introduccion.tex`
- Inicia la numeración formal de páginas en números arábigos (1, 2, 3...).
- Contiene una visión panorámica del contenido capítulo por capítulo.
- **Objetivo general y objetivos específicos:** Deben copiarse **exactamente como fueron aprobados en el protocolo de titulación**.

### `02-justificacion.tex`
- **Límite institucional:** Máximo **1 página**.
- Expone la relevancia técnica, económica, social o ambiental que fundamenta la realización del proyecto mecatrónico.

### `03-antecedentes.tex`
- **Límite institucional:** **1 cuartilla** (aproximadamente 1 página).
- Describe los trabajos terminales o investigaciones previas que sirven de punto de partida en la UPIIZ o en el IPN.

### `04-marco-teorico.tex`
- **Límite institucional:** Máximo **3 páginas**.
- Debe contener únicamente los principios físicos, ecuaciones dinámicas y modelos matemáticos que se usarán directamente en el desarrollo y validación.

### `05-estado-del-arte.tex`
- **Límite institucional:** Máximo **4 páginas**.
- Análisis comparativo de patentes, productos comerciales y artículos científicos recientes (últimos 5 años). Incluye una tabla comparativa de ventajas y desventajas.

### `06-planteamiento-problema.tex`
- **Sección 6.1:** Exposición clara, cuantitativa y concisa del problema u oportunidad detectada.
- **Sección 6.2:** Solución mecatrónica propuesta (integración mecánica, electrónica, control y software).

### `07-desarrollo.tex`
- **En TT I:** Orientado al **diseño detallado** (cálculos analíticos, selección de componentes, diagramas esquemáticos, planos de ensamble, algoritmos y simulaciones).
- **En TT II:** Orientado a la **implementación física** (maquinado, soldado de PCB, integración, programación de firmware y calibración).

### `08-validacion.tex`
- **Título dinámico:** La plantilla le asigna automáticamente *"Análisis y validación del diseño"* (TT I) o *"Análisis y validación de resultados"* (TT II).
- Presenta datos experimentales, tablas comparativas contra especificaciones, análisis de error y discusión de limitaciones.

### `09-conclusiones.tex`
- Conclusiones cuantitativas basadas estrictamente en la evidencia del capítulo de validación.
- Evaluación honesta del grado de cumplimiento de cada objetivo específico.

### `10-trabajo-futuro.tex`
- **Exclusivo para TT II:** Propuestas de optimización, mejoras de diseño y nuevas líneas de trabajo para futuras generaciones.

---

## 3. Próximo Paso

Continúa con la [Guía 11: Inserción de Figuras y Diagramas](11-figuras.md).
