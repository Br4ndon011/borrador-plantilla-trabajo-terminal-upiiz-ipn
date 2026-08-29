# Guía 04: Instalación de Git en Windows

Git es el sistema de control de versiones distribuido estándar en la industria del software y la ingeniería moderna.

---

## 1. ¿Por qué usar Git para tu Trabajo Terminal?

- **Evita la pesadilla de archivos duplicados:** Adiós a archivos como `Reporte_Final.docx`, `Reporte_Final_v2_este_si.docx`, `Reporte_Final_bueno_corregido_ahorasi.docx`.
- **Historial completo y recuperable:** Cada cambio queda registrado con fecha, autor y explicación. Si borras algo por accidente, puedes recuperarlo en segundos.
- **Trabajo en equipo sin sobrescribirse:** Permite que 2 o 3 estudiantes escriban diferentes capítulos simultáneamente y fusionen su trabajo de forma limpia y ordenada.
- **Respaldo en la nube:** Sincronización segura con GitHub para evitar pérdidas por fallos en el disco duro o extravío de memorias USB.

---

## 2. Descarga e Instalación en Windows

1. Entra a la página oficial: [git-scm.com/download/win](https://git-scm.com/download/win).
2. Descarga el instalador de 64 bits para Windows (**64-bit Git for Windows Setup**).
3. Ejecuta el archivo `.exe` descargado y avanza en el asistente con las opciones recomendadas:
   - **Editor por defecto:** Elige *Use Visual Studio Code as Git's default editor*.
   - **Nombre de la rama inicial:** Elige *Override the default branch name for new repositories* y escribe **`main`**.
   - **Ajuste del PATH:** Selecciona *Git from the command line and also from 3rd-party software* (recomendado).
   - **Finales de línea:** Selecciona *Checkout Windows-style, commit Unix-style line endings* (la plantilla además cuenta con `.gitattributes`).
   - **Gestor de credenciales:** Selecciona *Git Credential Manager* (facilita el inicio de sesión con GitHub sin escribir contraseñas).
4. Haz clic en **Install** y espera a que concluya el proceso.

---

## 3. Instalación en Linux y macOS

- **Ubuntu / Debian:**
  ```bash
  sudo apt update && sudo apt install -y git
  ```
- **Fedora:**
  ```bash
  sudo dnf install -y git
  ```
- **macOS:**
  ```bash
  git --version
  ```
  *(Si no está instalado, macOS te solicitará instalar las herramientas de línea de comandos de Xcode automáticamente).*

---

## 4. Verificación de la Instalación

Abre una terminal (PowerShell o Git Bash) y escribe:

```bash
git --version
```

**Resultado esperado:**
```text
git version 2.52.0.windows.1 (o superior)
```

---

## 5. Próximo Paso

Continúa con la [Guía 05: Configuración Inicial de Git](05-configuracion-git.md) para registrar tu identidad de autor.
