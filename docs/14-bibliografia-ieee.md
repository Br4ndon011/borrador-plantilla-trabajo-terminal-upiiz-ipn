# Guía 14: Manejo de Bibliografía en Formato IEEE

La carrera de Ingeniería Mecatrónica en la UPIIZ-IPN adopta el formato de citación estándar del **IEEE (Institute of Electrical and Electronics Engineers)**.

---

## 1. ¿Cómo Funciona la Bibliografía en LaTeX?

En LaTeX, las referencias se almacenan en una base de datos estructurada llamada **`bibliografia/referencias.bib`**.

Cada fuente bibliográfica tiene:
1. Un **tipo de entrada** (libro, artículo, conferencia, datasheet).
2. Una **clave de citación única** (ej. `ogata2010modern`).
3. Campos con los datos del autor, título, año, revista o editorial.

---

## 2. Tipos de Entradas BibTeX Más Comunes

### A. Libro de Texto (`@book`)
```bibtex
@book{ogata2010modern,
  author    = {Ogata, Katsuhiko},
  title     = {Modern Control Engineering},
  edition   = {5th},
  publisher = {Prentice Hall},
  address   = {Boston, MA, USA},
  year      = {2010}
}
```

### B. Artículo de Revista Científica (`@article`)
```bibtex
@article{smith2022control,
  author    = {Smith, John and Doe, Jane},
  title     = {Design and Implementation of Robust Fuzzy Controllers},
  journal   = {IEEE Transactions on Control Systems Technology},
  volume    = {30},
  number    = {4},
  pages     = {1520--1532},
  year      = {2022},
  doi       = {10.1109/TCST.2021.3123456}
}
```

### C. Artículo de Congreso / Conferencia (`@inproceedings`)
```bibtex
@inproceedings{gonzalez2021robotics,
  author    = {Gonzalez, Carlos and Ramirez, Luis},
  title     = {Real-Time State Estimation in Electric Vehicles},
  booktitle = {Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
  pages     = {4120--4126},
  year      = {2021}
}
```

### D. Hoja Técnica o Manual de Fabricante (`@manual`)
```bibtex
@manual{espressif2023esp32,
  title        = {ESP32 Series Datasheet},
  author       = {{Espressif Systems}},
  organization = {Espressif Systems Inc.},
  year         = {2023},
  url          = {https://www.espressif.com}
}
```

### E. Norma Técnica Internacional (`@standard`)
```bibtex
@standard{iso2018safety,
  title        = {ISO 13849-1: Safety of Machinery},
  organization = {International Organization for Standardization},
  institution  = {ISO},
  year         = {2018}
}
```

---

## 3. Cómo Obtener Entradas BibTeX Fácilmente

1. En **Google Scholar** ([scholar.google.com](https://scholar.google.com/)):
   - Busca el artículo o libro.
   - Haz clic en el ícono de comillas **"Citar"** debajo del resultado.
   - Haz clic en el enlace **BibTeX**.
   - Copia el texto y pégalo en tu archivo `bibliografia/referencias.bib`.
2. En **IEEE Xplore**, **ScienceDirect** o **Springer**:
   - Haz clic en *Cite this* $\rightarrow$ *Download BibTeX*.

---

## 4. Cómo Citar Dentro del Texto

Para citar una fuente, escribe `\cite{clave}`:

```latex
De acuerdo con los principios de control moderno formulados por Ogata \cite{ogata2010modern}...
```

Para citas múltiples simultáneas:
```latex
Diversos estudios han demostrado la viabilidad de este enfoque \cite{smith2022control, gonzalez2021robotics}.
```

El compilador generará automáticamente los corchetes numerados: `[1]`, `[2], [3]`.

---

## 5. Próximo Paso

Continúa con la [Guía 15: Apéndices, Planos y Datasheets](15-apendices.md).
