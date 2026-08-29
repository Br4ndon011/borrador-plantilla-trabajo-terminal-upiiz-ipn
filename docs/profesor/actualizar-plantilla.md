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

---

## 3. Mantenimiento del Catálogo de Líneas de Trabajo (Anexo 1)

> ⚠️ **ADVERTENCIA PARA EL MANTENEDOR:**
>
> El archivo **`config/lineas-trabajo.tex`** representa un **catálogo institucional inmutable** derivado del Anexo 1 del Reglamento Interno de Trabajo Terminal.
>
> **No debe modificarse por preferencia editorial ni agregarse frases inventadas.**

Si en el futuro la academia de la UPIIZ o el Consejo Técnico modifica el Reglamento Interno y el Anexo 1, el procedimiento obligatorio de actualización es:

1. **Consultar el nuevo Anexo 1 oficial aprobado.**
2. **Actualizar las definiciones** en `config/lineas-trabajo.tex` respetando la literalidad del texto normativo.
3. **Actualizar los entregables principales** por cada línea.
4. **Actualizar el número máximo de alumnos** admitido por línea.
5. **Actualizar la documentación y tablas** en `docs/09-configurar-datos-del-tt.md` y `config/datos.tex`.
6. **Ejecutar las pruebas automáticas de integridad y compilación.**
7. **Incrementar el número de versión** siguiendo versionado semántico (SemVer).
8. **Registrar detalladamente el cambio** en `CHANGELOG.md`.

---

## 4. Registro de Modificaciones

Cada vez que realices una actualización en el repositorio maestro:
1. Agrega las notas correspondientes en `CHANGELOG.md` siguiendo el estándar SemVer.
2. Incrementa el número de versión según el tipo de cambio.
