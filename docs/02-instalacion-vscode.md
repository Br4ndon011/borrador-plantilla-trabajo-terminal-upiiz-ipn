# Guía 02: Instalación de Visual Studio Code

Visual Studio Code (VS Code) es el entorno de desarrollo y edición recomendado para trabajar con la plantilla LaTeX del Trabajo Terminal.

---

## 1. ¿Qué es Visual Studio Code?

VS Code es un editor de código fuente moderno, ligero, gratuito y extensible desarrollado por Microsoft. A diferencia de editores tradicionales de LaTeX (como TeXmaker o TeXstudio), VS Code ofrece:
- Excelente integración con **Git y GitHub** para control de versiones en equipo.
- Visualización de PDF en tiempo real con sincronización bidireccional (SyncTeX: clic en el PDF te lleva a la línea de código y viceversa).
- Autocompletado inteligente de comandos LaTeX, citas bibliográficas y referencias cruzadas.
- Terminal integrada para ejecutar comandos sin salir del editor.

---

## 2. Descarga e Instalación en Windows

1. Accede al sitio oficial: [code.visualstudio.com](https://code.visualstudio.com/).
2. Haz clic en el botón azul **"Download for Windows"** (User Installer x64).
3. Ejecuta el archivo instalador descargado (`VSCodeUserSetup-x64-...exe`).
4. En el asistente de instalación:
   - Acepta el acuerdo de licencia.
   - Selecciona la ubicación de instalación por defecto.
   - **PASO CLAVE:** En la ventana *Seleccionar tareas adicionales*, marca las siguientes casillas:
     - [x] **Agregar la acción "Abrir con Code" al menú contextual de archivos de Windows Explorer**.
     - [x] **Agregar la acción "Abrir con Code" al menú contextual de directorios de Windows Explorer**.
     - [x] **Registrar Code como editor para tipos de archivo admitidos**.
     - [x] **Agregar a PATH (disponible después de reiniciar)**.
5. Haz clic en **Instalar** y al finalizar marca **"Ejecutar Visual Studio Code"**.

---

## 3. Instalación en Linux y macOS

- **Ubuntu / Debian:**
  Descarga el paquete `.deb` desde el sitio oficial o ejecuta:
  ```bash
  sudo snap install --classic code
  ```
- **macOS:**
  Descarga el archivo `.zip` para Mac, descomprímelo y arrastra `Visual Studio Code.app` a tu carpeta de **Aplicaciones**.

---

## 4. Primeros Pasos y Conceptos Básicos en VS Code

### A. Abrir una Carpeta de Proyecto
En VS Code se trabaja siempre abriendo la **carpeta completa** del repositorio, no archivos sueltos:
1. Menú superior: **Archivo (File)** $\rightarrow$ **Abrir carpeta... (Open Folder...)**.
2. Selecciona la carpeta `Plantilla_Trabajo_Terminal`.
3. Si aparece el mensaje *"Do you trust the authors of the files in this folder?"*, haz clic en **"Yes, I trust the authors"**.

### B. Usar la Terminal Integrada
VS Code incluye una terminal para que ejecutes comandos de Git y LaTeX:
- Presiona `Ctrl + \`` (Ctrl + comilla invertida) o ve al menú **Terminal** $\rightarrow$ **Nueva terminal (New Terminal)**.
- En Windows se abrirá PowerShell por defecto en la raíz de tu proyecto.

---

## 5. Próximo Paso

Ahora que tienes VS Code instalado, continúa con la [Guía 03: Configuración de LaTeX Workshop](03-configuracion-latex-workshop.md).
