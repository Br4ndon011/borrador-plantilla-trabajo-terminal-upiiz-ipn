# Guía 07: Cómo Obtener la Plantilla Institucional

Esta guía explica el procedimiento oficial para obtener una copia limpia e independiente de la plantilla para iniciar tu Trabajo Terminal.

---

## 🎯 Método Oficial: Usar como Plantilla (GitHub Template)

El repositorio oficial de la plantilla está configurado como **GitHub Template Repository**. Este mecanismo crea un repositorio nuevo y 100% independiente en tu cuenta de GitHub, con un historial limpio de Git desde el primer día y sin modificar la plantilla maestra.

### Pasos paso a paso:
1. Abre el enlace del repositorio maestro institucional:
   [https://github.com/rrevelesm/plantilla-trabajo-terminal-upiiz-ipn](https://github.com/rrevelesm/plantilla-trabajo-terminal-upiiz-ipn)
2. En la parte superior derecha, haz clic en el botón verde **`Use this template`** $\rightarrow$ **`Create a new repository`**.
3. Configura las opciones de tu nuevo proyecto:
   - **Owner:** Tu cuenta personal de GitHub o la organización de tu equipo.
   - **Repository name:** Nombra tu repositorio conforme a la convención sugerida (ej. `TT-2026-Control-Vehiculo-Escala`).
   - **Description:** *"Reporte de Trabajo Terminal - UPIIZ IPN - Ingeniería Mecatrónica"*.
   - **Privacy:** Selecciona **Public** o **Private** según lo acordado con tu asesor.
   - **Include all branches:** Desmarcado (solo se requiere la rama principal `main`).
4. Haz clic en **Create repository**.
5. ¡Listo! GitHub creará tu copia independiente. Ahora clona **TU PROPIO REPOSITORIO** en tu computadora:
   ```bash
   git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   ```
6. Abre la carpeta resultante en Visual Studio Code y comienza a trabajar siguiendo la [Guía 00: Inicio Rápido](00-inicio-rapido.md).

> ⚠️ **IMPORTANTE:**
> **No solicites permisos de escritura al repositorio maestro.** Todo tu trabajo, commits y pushes deben realizarse exclusivamente sobre tu propio repositorio recién creado.

---

## 📂 Convención Sugerida para Nombres de Repositorio

Para mantener orden académico y facilitar la identificación por parte de los asesores y sinodales, se sugiere nombrar los repositorios con uno de los siguientes esquemas:

- `TT-2026-TemaCorto` (ej. `TT-2026-Robot-Explorador-Irregular`)
- `TT-Apellidos-TemaCorto` (ej. `TT-Robles-Ramirez-Vehiculo-Escala`)

---

## 🧭 Próximo Paso

Continúa con la [Guía 08: Estructura del Proyecto y Carpetas](08-estructura-del-proyecto.md).
