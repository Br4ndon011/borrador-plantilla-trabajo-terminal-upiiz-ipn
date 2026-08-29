# Guía Docente: Actualización de la Plantilla Institucional

Esta guía explica cómo modificar los requisitos institucionales, actualizar paquetes y mantener la plantilla activa como **GitHub Template Repository**.

---

## 1. Configurar el Repositorio como GitHub Template

Para que los alumnos puedan usar el botón verde **`Use this template`**:

1. Entra a la página del repositorio maestro en GitHub con tu cuenta docente.
2. Haz clic en la pestaña superior **Settings**.
3. En la sección **General** $\rightarrow$ **Repository name**, busca la casilla:
   - [x] **Template repository** *(Set this repository as a template repository)*.
4. Marca la casilla. ¡Listo! A partir de ese momento aparecerá el botón *Use this template* para todos los estudiantes.

---

## 2. Cómo Actualizar el Formato Institucional

Si la dirección del IPN o la academia de la UPIIZ modifica los lineamientos:

- **Modificar Márgenes:** Edita los valores en `config/formato.tex`:
  ```latex
  \geometry{letterpaper, top=2.5cm, bottom=2.5cm, right=2.5cm, left=3.0cm}
  ```
- **Modificar Interlineado:** Cambia el factor en `config/formato.tex`:
  ```latex
  \setstretch{1.5}
  ```
- **Actualizar el Catálogo de Líneas de Trabajo:** Edita el catálogo oficial en `config/lineas-trabajo.tex`, los comentarios de `config/datos.tex` y la guía [09. Configurar Datos](../09-configurar-datos-del-tt.md).

---

## 3. Registro de Modificaciones

Cada vez que realices una actualización en el repositorio maestro:
1. Agrega las notas correspondientes en `CHANGELOG.md` siguiendo el estándar SemVer.
2. Incrementa el número de versión según el tipo de cambio.
