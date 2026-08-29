# Guía 09: Configuración de Datos del Trabajo Terminal

El archivo **`config/datos.tex`** es la **fuente única de verdad** de la plantilla. Al editar este archivo, todos los datos personales, académicos e institucionales se actualizarán de forma automática en la portada, portada interna, encabezados y metadatos.

---

## 1. Seleccionar el Tipo de Documento

Al inicio de `config/datos.tex`, encontrarás la instrucción principal de configuración:

```latex
% Opciones válidas: PROTOCOLO | TTI | TTII
\TipoDocumento{PROTOCOLO}
```

### Opciones disponibles:

1. **`\TipoDocumento{PROTOCOLO}` (Protocolo de Trabajo Terminal):**
   - Carga automáticamente la portada oficial reglamentaria con franja institucional.
   - Muestra el **Área de ubicación**, **Línea de Trabajo** e **Intención de titulación**.
   - **No incluye portada interna de firmas de sínodo.**
   - Oculta Agradecimientos, Dedicatorias y el Capítulo 10 (*Trabajo a futuro*).

2. **`\TipoDocumento{TTI}` (Trabajo Terminal I - Diseño Detallado):**
   - Carga automáticamente la portada de Trabajo Terminal con el rótulo:
     *"REPORTE TÉCNICO DE TRABAJO TERMINAL I"*.
   - Incluye la **Portada Interna con firmas de alumnos, asesores y jurado calificador**.
   - Asigna el título *"Análisis y validación del diseño"* al Capítulo 8.
   - Oculta Agradecimientos, Dedicatorias y el Capítulo 10 (*Trabajo a futuro*).
   - Muestra el Apéndice del *Cronograma para Trabajo Terminal II*.

3. **`\TipoDocumento{TTII}` (Trabajo Terminal II - Reporte Final):**
   - Carga automáticamente la portada de Trabajo Terminal con el rótulo:
     *"REPORTE FINAL DE TRABAJO TERMINAL"*.
   - Incluye la **Portada Interna con firmas de alumnos, asesores y jurado calificador**.
   - Muestra Agradecimientos y Dedicatorias en las páginas preliminares.
   - Asigna el título *"Análisis y validación de resultados"* al Capítulo 8.
   - Muestra el Capítulo 10 (*Trabajo a futuro*).
   - Oculta el Cronograma hacia TT II.

---

## 2. Seleccionar la Línea de Trabajo (Anexo 1 Institucional)

La denominación oficial institucional es **LÍNEA DE TRABAJO** (no usar *"Línea de investigación"*).

Para seleccionarla en `config/datos.tex`, escribe únicamente el identificador romano:

```latex
\LineaTrabajo{IV}
```

### Catálogo oficial institucional de Líneas de Trabajo:

| Clave | Línea de Trabajo | Máximo de alumnos | Entregable | Característica |
|:---:|---|:---:|---|---|
| **I** | Diseño e implementación de un sistema robótico, dispositivos o sistemas Mecatrónicos | **3** | Prototipo, Interfaz Hombre-Máquina | Las 4 áreas de la Mecatrónica se desarrollan con el mismo grado de complejidad y detalle. |
| **II** | Diseño e implementación de una máquina o mecanismo | **2** | Prototipo, Interfaz Hombre-Máquina | Énfasis en la mecánica y menor complejidad en las demás áreas. |
| **III** | Diseño e implementación de componentes o sistemas electrónicos | **2** | Prototipo, Interfaz Hombre-Máquina | Énfasis en la electrónica y menor complejidad en las demás áreas. |
| **IV** | Diseño e implementación de sistemas o técnicas de control | **2** | Prototipo, Interfaz Hombre-Máquina | Énfasis en el control y menor complejidad en las demás áreas. |
| **V** | Diseño y desarrollo de software para el control de sistemas o procesos | **2** | Software, Interfaz Hombre-Máquina y prototipo | Énfasis en la programación y menor complejidad en las demás áreas. |
| **VI** | Puesta en operación, optimización o automatización de un proceso o sistema industrial | **2** | Proceso o sistema industrial en operación | *(El Anexo 1 no establece una frase adicional de característica)* |

> **NOTA INSTITUCIONAL (ANEXO 1):**
>
> Las líneas II, III, IV y V se consideran para diseño de productos de:
> - consumo;
> - biomédicos;
> - didácticos;
> - investigación.
>
> Además:
> **Todas las líneas deben contemplar las cuatro áreas de la Mecatrónica**, independientemente de que alguna de ellas tenga menor peso.

### Macros obtenidas automáticamente:
Al configurar por ejemplo `\LineaTrabajo{IV}`, la plantilla define internamente:
- `\NumeroLineaTrabajo` $\rightarrow$ `IV`
- `\NombreLineaTrabajo` $\rightarrow$ `Diseño e implementación de sistemas o técnicas de control.`
- `\EntregableLineaTrabajo` $\rightarrow$ `Prototipo, Interfaz Hombre-Máquina.`
- `\MaximoAlumnosLineaTrabajo` $\rightarrow$ `2`
- `\DescripcionLineaTrabajo` $\rightarrow$ `Énfasis en el control y menor complejidad en las demás áreas.` (para la Línea VI, devuelve una cadena vacía `""`).

---

## 3. Título y Datos Generales del Proyecto

```latex
\newcommand{\tituloProyecto}{Título General del Trabajo Terminal de Ingeniería Mecatrónica}
\newcommand{\tituloIngles}{General Title of the Mechatronics Engineering Terminal Project}

% Campos específicos para PROTOCOLO:
\newcommand{\areaUbicacion}{Ingeniería Mecatrónica}
\newcommand{\intencionTitulacion}{Opción curricular / Trabajo Terminal}
\newcommand{\fechaDefensa}{enero de 2026}
```

---

## 4. Configuración de Alumnos (1, 2 o 3 Integrantes)

La plantilla cuenta automáticamente el número de integrantes y valida que no exceda el máximo permitido por la Línea de Trabajo seleccionada:

### Caso A: Proyecto Individual (1 Alumno)
```latex
\newcommand{\alumnoANombre}{Mariana Robles Reynoso}
\newcommand{\alumnoABoleta}{2020670001}

\newcommand{\alumnoBNombre}{}
\newcommand{\alumnoBBoleta}{}

\newcommand{\alumnoCNombre}{}
\newcommand{\alumnoCBoleta}{}
```

### Caso B: Equipo de 2 Alumnos (Válido para Líneas I a VI)
```latex
\newcommand{\alumnoANombre}{Mariana Robles Reynoso}
\newcommand{\alumnoABoleta}{2020670001}

\newcommand{\alumnoBNombre}{Carlos Ramirez Lopez}
\newcommand{\alumnoBBoleta}{2020670002}

\newcommand{\alumnoCNombre}{}
\newcommand{\alumnoCBoleta}{}
```

### Caso C: Equipo de 3 Alumnos (Exclusivo para Línea I)
```latex
\newcommand{\alumnoANombre}{Mariana Robles Reynoso}
\newcommand{\alumnoABoleta}{2020670001}

\newcommand{\alumnoBNombre}{Carlos Ramirez Lopez}
\newcommand{\alumnoBBoleta}{2020670002}

\newcommand{\alumnoCNombre}{Sofia Martinez Castro}
\newcommand{\alumnoCBoleta}{2020670003}
```

---

## 5. Configuración de Asesores (1 a 3 Asesores)

```latex
\newcommand{\asesorANombre}{M. en C. Rafael Reveles Martínez}
\newcommand{\asesorBNombre}{Mtro. José Refugio Campos Flores}
\newcommand{\asesorCNombre}{}
```

---

## 6. Jurado Evaluador / Sínodo (Para TT I y TT II)

Aparecerán en la Portada Interna con sus respectivas líneas de firma:
```latex
\newcommand{\juradoPresidente}{Dr. Umanel A. Hernández González}
\newcommand{\juradoSecretario}{M. en C. Eleazar Pacheco Reyes}
\newcommand{\juradoPrimerVocal}{Dr. Primer Vocal del Sínodo}
\newcommand{\juradoSegundoVocal}{M. en C. Segundo Vocal del Sínodo}
\newcommand{\juradoTercerVocal}{}
```

---

## 7. Próximo Paso

Continúa con la [Guía 10: Cómo Escribir los Capítulos](10-escribir-capitulos.md).
