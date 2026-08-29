# Guía 09: Configuración de Datos del Trabajo Terminal

El archivo **`config/datos.tex`** es la **fuente única de verdad** de la plantilla. Al editar este archivo, todos los datos personales, académicos e institucionales se actualizarán de forma automática en la portada, portada interna, encabezados y metadatos.

---

## 1. Selección de Modalidad (TT I o TT II)

Al inicio de `config/datos.tex`, encontrarás las siguientes dos líneas:

```latex
\TTItrue   % Para Trabajo Terminal I (Diseño detallado)
%\TTIfalse  % Para Trabajo Terminal II / Reporte Final (Implementación y Validación)
```

- **Para Trabajo Terminal I:** Deja activa `\TTItrue` y comenta con `%` la línea `\TTIfalse`.
  - Oculta automáticamente Agradecimientos y Dedicatorias.
  - Asigna el título *"Análisis y validación del diseño"* al Capítulo 8.
  - Oculta el Capítulo 10 (*Trabajo a futuro*).
  - Muestra el Apéndice del *Cronograma para Trabajo Terminal II*.

- **Para Trabajo Terminal II / Reporte Final:** Comenta con `%` la línea `\TTItrue` y activa `\TTIfalse`.
  - Muestra Agradecimientos y Dedicatorias en las páginas preliminares.
  - Asigna el título *"Análisis y validación de resultados"* al Capítulo 8.
  - Muestra el Capítulo 10 (*Trabajo a futuro*).
  - Oculta el Cronograma hacia TT II.

---

## 2. Título y Línea de Investigación

```latex
\newcommand{\tituloProyecto}{Diseño e Integración de un Sistema Mecatrónico de Posicionamiento Angular}
\newcommand{\tituloIngles}{Design and Integration of an Angular Positioning Mechatronic System}
```

Selecciona una de las 6 líneas de investigación registradas en el programa:
```latex
\newcommand{\lineaTrabajo}{Línea de investigación: IV. Diseño e implementación de sistemas o técnicas de control.}
```

Las 6 líneas institucionales son:
1. *I. Diseño e implementación de un sistema robótico, dispositivos o sistemas mecatrónicos.*
2. *II. Diseño e implementación de una máquina o mecanismo.*
3. *III. Diseño e implementación de componentes o sistemas electrónicos.*
4. *IV. Diseño e implementación de sistemas o técnicas de control.*
5. *V. Diseño y desarrollo de software para el control de sistemas o procesos.*
6. *VI. Puesta en operación, optimización o automatización de un proceso o sistema industrial.*

---

## 3. Configuración de Alumnos (1, 2 o 3 Integrantes)

La plantilla adapta dinámicamente el diseño y las líneas de firma según la cantidad de alumnos:

### Caso A: Proyecto Individual (1 Alumno)
```latex
\newcommand{\alumnoANombre}{Mariana Robles Reynoso}
\newcommand{\alumnoABoleta}{2020670001}

\newcommand{\alumnoBNombre}{}
\newcommand{\alumnoBBoleta}{}

\newcommand{\alumnoCNombre}{}
\newcommand{\alumnoCBoleta}{}
```

### Caso B: Equipo de 2 Alumnos
```latex
\newcommand{\alumnoANombre}{Mariana Robles Reynoso}
\newcommand{\alumnoABoleta}{2020670001}

\newcommand{\alumnoBNombre}{Carlos Ramirez Lopez}
\newcommand{\alumnoBBoleta}{2020670002}

\newcommand{\alumnoCNombre}{}
\newcommand{\alumnoCBoleta}{}
```

### Caso C: Equipo de 3 Alumnos
```latex
\newcommand{\alumnoANombre}{Mariana Robles Reynoso}
\newcommand{\alumnoABoleta}{2020670001}

\newcommand{\alumnoBNombre}{Carlos Ramirez Lopez}
\newcommand{\alumnoBBoleta}{2020670002}

\newcommand{\alumnoCNombre}{Sofia Martinez Castro}
\newcommand{\alumnoCBoleta}{2020670003}
```

---

## 4. Configuración de Asesores (1 a 3 Asesores)

```latex
\newcommand{\asesorANombre}{M. en C. Rafael Reveles Martínez}
\newcommand{\asesorBNombre}{Dra. Ma. Auxiliadora Araiza Esquivel}
\newcommand{\asesorCNombre}{M. en C. Ramón Jaramillo Martínez}
```
*(Si tienes 1 o 2 asesores, deja vacíos `\asesorBNombre` o `\asesorCNombre`).*

---

## 5. Jurado Evaluador / Sínodo

Estos nombres aparecerán en la Portada Interna con sus respectivas líneas de firma:
```latex
\newcommand{\juradoPresidente}{Dr. Umanel A. Hernández González}
\newcommand{\juradoSecretario}{M. en C. Eleazar Pacheco Reyes}
\newcommand{\juradoPrimerVocal}{Dr. Primer Vocal del Sínodo}
\newcommand{\juradoSegundoVocal}{M. en C. Segundo Vocal del Sínodo}
\newcommand{\juradoTercerVocal}{}
```

---

## 6. Próximo Paso

Continúa con la [Guía 10: Cómo Escribir los Capítulos](10-escribir-capitulos.md).
