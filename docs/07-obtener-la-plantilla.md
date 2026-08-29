# Guía 07: Cómo Obtener la Plantilla Institucional

Esta guía explica las dos formas de obtener una copia limpia de la plantilla para iniciar tu Trabajo Terminal.

---

## Opción 1: GitHub Template Repository (MÉTODO RECOMENDADO)

El repositorio oficial de la plantilla está configurado como **GitHub Template**. Este mecanismo crea un repositorio nuevo en tu cuenta con un historial limpio de Git desde el primer día, sin vincularte a los commits de desarrollo del profesor.

### Pasos para el alumno:
1. Abre el enlace del repositorio oficial de la plantilla en GitHub.
2. En la parte superior derecha, haz clic en el botón verde **`Use this template`** y selecciona **`Create a new repository`**.
3. Configura las opciones del nuevo repositorio:
   - **Repository name:** Usa la convención sugerida: `TT_Apellido1_Apellido2_TemaCorto` (ej. `TT_Martinez_Rios_BrazoRobotico`).
   - **Description:** *"Reporte de Trabajo Terminal - UPIIZ IPN - Ingeniería Mecatrónica"*.
   - **Privacy:** Selecciona **Private** (puedes cambiarlo a público tras la titulación).
   - **Include all branches:** Desmarcado (solo necesitas la rama `main`).
4. Haz clic en **Create repository**.
5. Ahora tienes tu propio repositorio independiente. Cópialo a tu computadora con:
   ```bash
   git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   ```

---

## Opción 2: Clonado Directo con Git (MÉTODO ALTERNATIVO)

Si deseas clonar el repositorio y desvincular el origen para apuntar a un nuevo repositorio propio:

1. Clona el repositorio maestro:
   ```bash
   git clone https://github.com/REPOSITORIO_OFICIAL/Plantilla_Trabajo_Terminal.git Mi_Trabajo_Terminal
   ```
2. Entra a la carpeta:
   ```bash
   cd Mi_Trabajo_Terminal
   ```
3. Cambia la URL remota para apuntar a tu propio repositorio de GitHub:
   ```bash
   git remote set-url origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   git push -u origin main
   ```

---

## 3. Convención Sugerida para Nombres de Repositorio

Para mantener orden institucional y facilitar la identificación por parte de los asesores, se sugiere nombrar los repositorios con uno de los siguientes formatos:

- `TT_Apellido1_Apellido2_Tema` (ej. `TT_Gomez_Hernandez_SistemaVision`)
- `TrabajoTerminal_NombreCorto` (ej. `TrabajoTerminal_VehiculoAutonomo`)

---

## 4. Próximo Paso

Continúa con la [Guía 08: Estructura del Proyecto y Carpetas](08-estructura-del-proyecto.md).
