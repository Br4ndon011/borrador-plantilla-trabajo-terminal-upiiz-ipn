# Guía 14a: Uso de Mendeley como Gestor Bibliográfico

Esta guía explica paso a paso cómo instalar y utilizar **Mendeley Reference Manager** para recopilar artículos, libros y manuales técnicos, revisar sus metadatos y exportarlos al archivo `bibliografia/referencias.bib` de la plantilla de Trabajo Terminal.

---

## 1. ¿Qué es Mendeley y cuál es su función en el proyecto?

**Mendeley** es un gestor bibliográfico académico gratuito desarrollado por Elsevier que permite:
- Organizar artículos científicos, libros, conferencias y hojas de datos (*datasheets*).
- Guardar y anotar documentos PDF en una biblioteca personal.
- Editar y estandarizar metadatos bibliográficos (autores, títulos, revistas, DOIs).
- Exportar referencias en formato estándar **BibTeX (`.bib`)**.

> ⚠️ **ACLARACIÓN IMPORTANTE:**
> - **Mendeley NO sustituye a LaTeX:** Es una herramienta externa de apoyo para gestionar tu biblioteca personal.
> - **Mendeley es 100% opcional:** La plantilla de Trabajo Terminal lee directamente el archivo `bibliografia/referencias.bib`. Puedes editar dicho archivo con Mendeley, con otro gestor (como Zotero o JabRef) o manualmente.
> - **La plantilla aplica automáticamente el formato IEEE:** No necesitas dar formato visual IEEE a mano; LaTeX se encarga del formato a través del motor bibliográfico oficial.

---

## 2. Instalación y Configuración Inicial

### Paso 1: Descargar Mendeley Reference Manager
1. Ingresa al sitio oficial: [https://www.mendeley.com/download-reference-manager/](https://www.mendeley.com/download-reference-manager/)
2. Descarga el instalador correspondiente a tu sistema operativo (**Windows**, **macOS** o **Linux**).
3. Ejecuta el instalador y sigue las instrucciones en pantalla.

### Paso 2: Crear o Iniciar Sesión en tu Cuenta
1. Abre **Mendeley Reference Manager**.
2. Inicia sesión con tu cuenta de Elsevier o crea una cuenta gratuita con tu correo institucional (`@ipn.mx` o `@alumno.ipn.mx`) o personal.
3. Verifica que la ventana principal de la biblioteca cargue correctamente.

### Paso 3: (Opcional recomendado) Instalar Mendeley Web Importer
Para guardar artículos directamente desde tu navegador (Google Chrome, Firefox o Edge):
1. Instala la extensión **Mendeley Web Importer** desde la tienda de complementos de tu navegador o desde [mendeley.com/reference-management/web-importer](https://www.mendeley.com/reference-management/web-importer).
2. Te permitirá capturar referencias con un solo clic desde Google Scholar, IEEE Xplore, ScienceDirect y SpringerLink.

---

## 3. Cómo Agregar Referencias a tu Biblioteca

Mendeley ofrece varios métodos para incorporar fuentes a tu trabajo:

### Método A: Arrastrar archivos PDF
Arrastra uno o varios archivos PDF descargados directamente sobre la ventana de Mendeley Reference Manager. El programa extraerá automáticamente los metadatos disponibles.

### Método B: Búsqueda por identificador (DOI, arXiv ID o PubMed ID)
1. En Mendeley, haz clic en el botón superior **`+ Add new`** $\rightarrow$ **`Add entry manually`**.
2. En el campo **Identifiers** (DOI), pega el identificador del artículo (por ejemplo: `10.1109/TCST.2023.1234567`).
3. Haz clic en el ícono de **Lupa** (*Look up*). Mendeley completará automáticamente los campos oficiales.
4. Haz clic en **Add entry**.

### Método C: Desde el navegador con Web Importer
Al navegar en bases de datos científicas (IEEE Xplore, Scopus, ScienceDirect):
1. Haz clic en el ícono de **Mendeley Web Importer** en la barra de extensiones.
2. Selecciona los artículos deseados y la colección de destino.
3. Haz clic en **Add**.

---

## 4. Calidad y Revisión Obligatoria de Metadatos

> 🚨 **ADVERTENCIA FUNDAMENTAL DE RIGOR ACADÉMICO:**
> **NUNCA asumas que Mendeley genera metadatos 100% perfectos de forma automática.**
>
> La extracción automática de PDFs a menudo confunde iniciales con apellidos, omite números de página o importa títulos en mayúsculas sostenidas. **La responsabilidad académica y formal de la bibliografía es siempre del estudiante.**

Antes de exportar cualquier referencia a tu Trabajo Terminal, haz clic sobre ella en Mendeley y revisa en el panel lateral derecho:

| Campo | Qué debes verificar | Ejemplo correcto |
|---|---|---|
| **Authors** | Formato `Apellido, Nombre` por cada autor, separados adecuadamente. | `Aström, Karl J. and Murray, Richard M.` |
| **Title** | Ortografía correcta, acentos y mayúsculas solo al inicio o en nombres propios. | `Feedback Systems: An Introduction for Scientists and Engineers` |
| **Publication / Journal** | Nombre completo o abreviatura formal de la revista o congreso. | `IEEE Transactions on Control Systems Technology` |
| **Year** | Año de publicación de 4 dígitos. | `2024` |
| **Volume / Issue** | Volumen y número de la edición. | Vol: `32`, Issue: `4` |
| **Pages** | Rango de páginas con guion doble en BibTeX (`--`). | `1120--1135` |
| **DOI** | Enlace persistente estándar sin prefijos duplicados. | `10.1109/TCST.2024.012345` |

---

## 5. Documentos Especiales: Datasheets, Manuales y Normas

En proyectos de Ingeniería Mecatrónica es común consultar manuales de componentes y normas técnicas. Dado que estos no siempre tienen DOI, regístralos manualmente en Mendeley o en BibTeX con especial atención:

### A. Hoja de Datos / Manual de Fabricante (*Datasheet*)
- **Tipo en Mendeley:** *Generic* o *Report*.
- **Author:** Nombre de la empresa o fabricante (ej. `Texas Instruments`, `STMicroelectronics`).
- **Title:** Nombre del componente y descripción (ej. `STM32F401xD/xE ARM Cortex-M4 Microcontroller Datasheet`).
- **Year:** Año de la revisión del documento.
- **URL:** Enlace oficial del fabricante.

### B. Normas Técnicas (ISO, IEC, IEEE, NOM)
- **Author:** Organismo normalizador (ej. `International Organization for Standardization`).
- **Title:** Clave y título de la norma (ej. `ISO 12100:2010 - Safety of machinery`).
- **Year:** Año de emisión.

---

## 6. Exportar Referencias a Formato BibTeX (`.bib`)

Una vez verificados los metadatos en Mendeley:

### Paso 1: Exportar desde Mendeley Desktop / Reference Manager
1. Selecciona la(s) referencia(s) que deseas incluir en tu reporte.
2. Ve al menú superior: **File** $\rightarrow$ **Export...** (o selecciona las referencias $\rightarrow$ clic derecho $\rightarrow$ **Export**).
3. Selecciona el formato **BibTeX (.bib)**.
4. Guarda el archivo temporal en tu equipo (por ejemplo, `referencias_exportadas.bib`).

### Paso 2: Integrar en la Plantilla de Trabajo Terminal

#### ✅ OPCIÓN RECOMENDADA (Copiar y Pegar Selectivo):
1. Abre el archivo exportado `referencias_exportadas.bib` en Visual Studio Code.
2. Abre también el archivo oficial de tu proyecto: **`bibliografia/referencias.bib`**.
3. Copia el bloque de la referencia verificada y pégalo al final de `bibliografia/referencias.bib`.
4. Ajusta la **clave de cita** a una denominación clara y estándar.
5. Guarda el archivo (`Ctrl + S`).

> ⛔ **PRECAUCIÓN:** No reemplaces ni sobrescribas directamente todo el archivo `bibliografia/referencias.bib` con una exportación masiva, ya que podrías borrar referencias agregadas previamente por tus compañeros de equipo.

---

## 7. Estructura de una Entrada BibTeX y Claves de Cita

Cada referencia en el archivo `.bib` tiene la siguiente estructura:

```bibtex
@article{ejemplo2026,
  author  = {Robles, Mariana and Ramirez, Carlos},
  title   = {Modelado dinámico y control en espacio de estados de un robot móvil},
  journal = {Revista de Mecatrónica Aplicada},
  year    = {2026},
  volume  = {12},
  number  = {3},
  pages   = {45--58},
  doi     = {10.1234/rma.2026.03.45}
}
```

### ¿Qué es la clave de cita?
En el ejemplo anterior, **`ejemplo2026`** es la clave única que usarás en tu texto para citar.

### Buenas prácticas para nombrar claves de cita:
Se recomienda seguir una convención homogénea basada en el primer autor y año:
- ✅ `smith2024control`
- ✅ `garcia2025robot`
- ✅ `ogata2010modern`
- ✅ `ieee2023standard`
- ❌ `ref1`, `paper2`, `articulo_final` *(evitar: son ambiguas y propensas a colisiones)*.

---

## 8. Cómo Citar en LaTeX

Para citar una referencia en cualquier capítulo (`capitulos/01-introduccion.tex`, `capitulos/04-marco-teorico.tex`, etc.), utiliza el comando **`\cite{clave}`**:

### Cita individual:
```latex
De acuerdo con el modelo no lineal propuesto por \cite{smith2024control}, la velocidad...
```

### Citas múltiples:
```latex
Diversos estudios en vehículos terrestres \cite{smith2024control, garcia2025robot, ogata2010modern} demuestran...
```

### 🚫 Reglas indispensables:
1. **NUNCA escribas números entre corchetes manualmente** (como `[1]` o `[2]`).
2. Usa siempre `\cite{...}`. LaTeX y BibTeX asignarán la numeración correcta automáticamente conforme al orden de aparición, siguiendo el estándar oficial **IEEE**.

---

## 9. Mendeley, Git y Trabajo en Equipo

Al trabajar con Git y compañeros de equipo en Trabajo Terminal:

1. **Lo que se versiona en Git:**
   - Únicamente el archivo de texto: **`bibliografia/referencias.bib`**.
2. **Lo que NO debe subirse a Git:**
   - Archivos PDF de artículos completos descargados en tu disco local.
   - Bases de datos internas o archivos de caché de Mendeley.
   - Contraseñas o credenciales de Elsevier.
3. **Buenas prácticas para equipos de 2 o 3 integrantes:**
   - Antes de agregar nuevas citas, ejecuta `git pull` para obtener las referencias agregadas por tus compañeros.
   - Agrega tu bloque al final de `bibliografia/referencias.bib` con una clave clara.
   - Haz commit con un mensaje descriptivo:
     ```bash
     git add bibliografia/referencias.bib
     git commit -m "references: agrega articulos sobre observador de Luenberger"
     git push
     ```
   - Si ocurre un conflicto en `referencias.bib`, abre el archivo en VS Code y conserva ambas referencias unificándolas sin duplicar claves.

---

## 10. Errores Comunes y Soluciones Rápidas

| Error frecuente | Causa | Solución |
|---|---|---|
| **Aparece un signo de interrogación `[?]` en el PDF** | LaTeX no encuentra la clave de cita en `referencias.bib` o falta compilar. | Revisa que la clave en `\cite{clave}` coincida exactamente (distingue mayúsculas) y compila con `latexmk main.tex`. |
| **Autores mal formateados en el PDF** | En el `.bib` se usaron comas en vez de la palabra `and`. | En BibTeX los autores **siempre** se separan con la palabra `and`: `author = {Perez, Juan and Gomez, Luisa}`. |
| **Caracteres especiales rotos** | Caracteres no UTF-8 o símbolos de porcentaje `%` o `&` sin escapar en el título. | Escribe `\%` o `\&` en títulos para evitar que LaTeX los interprete como comentarios o alineadores. |
| **Claves de cita duplicadas** | Dos entradas en `referencias.bib` tienen la misma clave. | Asigna una clave única a cada entrada (por ejemplo, `smith2024a` y `smith2024b`). |
| **Título pierde mayúsculas en el PDF** | El estilo IEEE convierte títulos a minúsculas excepto la primera letra. | Encierra entre llaves las siglas o nombres que deben conservar mayúsculas: `title = {Diseño de un controlador {PID} para un vehículo {RC}}`. |

---

## 11. Resumen del Flujo de Trabajo Recomendado

```text
┌────────────────────────┐
│  1. Buscar artículo    │  Google Scholar / IEEE Xplore / ScienceDirect
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│  2. Importar a Mendeley│  Arrastrar PDF o usar Mendeley Web Importer
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│  3. Revisar metadatos  │  Verificar autores, año, revista, páginas, DOI
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│  4. Exportar a BibTeX  │  File -> Export -> BibTeX (.bib)
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│  5. Copiar al proyecto │  Pegar en bibliografia/referencias.bib
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│  6. Citar en LaTeX     │  Escribir \cite{clave} en el capítulo deseado
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│  7. Compilar           │  Ejecutar: latexmk main.tex
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│  8. Verificar PDF      │  Confirmar número de cita y lista bibliográfica IEEE
└────────────────────────┘
```

---

## 12. Próximos Pasos

- Consulta la [Guía 14: Manejo de Bibliografía en Formato IEEE](14-bibliografia-ieee.md) para conocer los tipos de entradas `@article`, `@book`, `@inproceedings` y `@manual`.
- Consulta la [Guía 16: Cómo Compilar y Generar el PDF](16-compilar.md).
