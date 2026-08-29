# Guía 24: Preguntas Frecuentes (FAQ)

Respuestas directas a las dudas más comunes sobre la plantilla y el flujo de trabajo.

---

### ¿Puedo usar esta plantilla en Overleaf?
**Sí.** Para usarla en Overleaf:
1. Comprime los archivos de la plantilla en un archivo `.zip`.
2. En Overleaf, crea un nuevo proyecto seleccionando **Upload Project**.
3. En el menú superior izquierdo de Overleaf (icono de engranaje **Menu**):
   - En **Compiler**, selecciona **XeLaTeX** o **LuaLaTeX**.
   - En **Main document**, asegúrate de que esté seleccionado `main.tex`.
4. Haz clic en **Recompile**.

---

### ¿Cómo cambio la cantidad de alumnos o asesores?
En `config/datos.tex`, simplemente escribe los nombres que correspondan y **deja completamente vacíos** los campos que no utilices. La plantilla adaptará automáticamente el espaciado y las líneas de firma en la portada y portada interna:
```latex
\newcommand{\alumnoANombre}{Mariana Robles Reynoso}
\newcommand{\alumnoABoleta}{2020670001}

\newcommand{\alumnoBNombre}{}  % Vacío para proyecto individual
\newcommand{\alumnoBBoleta}{}

\newcommand{\alumnoCNombre}{}  % Vacío
\newcommand{\alumnoCBoleta}{}
```

---

### ¿Por qué la plantilla utiliza Arial en lugar de la fuente clásica de LaTeX?
Porque **Arial es el estándar tipográfico normativo oficial** establecido por el Instituto Politécnico Nacional y la academia de Mecatrónica de la UPIIZ para los reportes de titulación. La plantilla utiliza motores modernos (`XeLaTeX` / `LuaLaTeX`) para garantizar el cumplimiento tipográfico institucional exacto.

---

### ¿Cómo subdivido el Capítulo 7 (Desarrollo) si mi proyecto es muy extenso?
Puedes crear archivos adicionales dentro de la carpeta `capitulos/` (por ejemplo: `07a-mecanica.tex`, `07b-electronica.tex`, `07c-control.tex`) e incluirlos en `capitulos/07-desarrollo.tex` mediante:
```latex
\input{capitulos/07a-mecanica.tex}
\input{capitulos/07b-electronica.tex}
\input{capitulos/07c-control.tex}
```

---

### ¿Cómo le envío el avance a mi asesor?
1. Compila tu proyecto para generar `main.pdf`.
2. Envía únicamente el archivo `main.pdf` generado por correo electrónico o comparte el enlace de tu repositorio de GitHub si tu asesor tiene cuenta en la plataforma.
3. Recuerda que no debes subir `main.pdf` a Git (el `.gitignore` lo ignora automáticamente para evitar inflar el historial).

---

### ¿Es obligatorio usar Mendeley?
**No.** Mendeley Reference Manager es un gestor bibliográfico recomendado que facilita organizar lecturas, guardar PDFs y exportar entradas en formato BibTeX, pero su uso es **completamente opcional**.

El único requisito técnico indispensable para compilar la bibliografía en la plantilla es disponer de entradas válidas en el archivo **`bibliografia/referencias.bib`**. Puedes editar este archivo a mano o utilizar cualquier otro gestor compatible con BibTeX (como Zotero o JabRef). Para más información, consulta la [Guía 14a: Uso de Mendeley](14a-mendeley.md).
