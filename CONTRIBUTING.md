# Guía de Contribución a la Plantilla Institucional

¡Gracias por tu interés en mejorar la Plantilla Institucional de Trabajo Terminal de la UPIIZ-IPN!

Este proyecto busca mantenerse como un recurso docente de alta calidad, robusto y fácil de usar para todos los estudiantes y profesores de la academia.

---

## 1. Cómo reportar errores o sugerir mejoras

Si encuentras un error tipográfico, un problema de compilación en algún sistema operativo o deseas sugerir una mejora en la estructura:

1. Revisa la pestaña de **Issues** en el repositorio para verificar si el tema ya ha sido reportado.
2. Si no existe, abre un nuevo **Issue** utilizando una de nuestras plantillas:
   - **Reporte de error (Bug Report):** Incluye tu sistema operativo, distribución LaTeX (`lualatex --version`), mensaje de error exacto y pasos para reproducirlo.
   - **Solicitud de función (Feature Request):** Describe la mejora propuesta y su justificación técnica o institucional.

---

## 2. Flujo de trabajo para contribuir código

1. **Haz un Fork** del repositorio maestro a tu cuenta de GitHub.
2. **Clona tu fork** localmente:
   ```bash
   git clone https://github.com/TU_USUARIO/Plantilla_Trabajo_Terminal.git
   ```
3. **Crea una rama de trabajo** con un nombre descriptivo:
   ```bash
   git switch -c fix-margen-portada
   ```
4. **Realiza tus modificaciones** y verifica que el documento compile limpiamente:
   ```bash
   latexmk -lualatex main.tex
   ```
5. **Haz commits claros y descriptivos** siguiendo el estándar convencional:
   - `fix: corrige espaciado en portada interna`
   - `docs: añade solución a error de fuentes en Linux`
   - `feat: agrega ejemplo de tabla con unidades en siunitx`
6. **Envía tus cambios a tu repositorio remoto**:
   ```bash
   git push origin fix-margen-portada
   ```
7. **Abre un Pull Request (PR)** hacia la rama `main` del repositorio oficial describiendo con claridad los cambios realizados.

---

## 3. Criterios de aceptación de contribuciones

- Los cambios **no deben romper la compatibilidad** con LuaLaTeX ni XeLaTeX.
- No se deben agregar paquetes obsoletos o conflictivos.
- Se debe respetar estrictamente el formato normativo de la institución (Arial, márgenes 2.5/3.0 cm, interlineado 1.5).
- Toda nueva característica debe acompañarse de su correspondiente actualización en la documentación de `docs/`.
