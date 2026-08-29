# Guía 06: Creación de Cuenta y Uso de GitHub

Esta guía explica la diferencia entre Git y GitHub, cómo crear tu cuenta y cómo gestionar repositorios públicos y privados con seguridad.

---

## 1. Diferencia entre Git y GitHub

Es muy común confundir ambos términos al comenzar:

| Característica | Git | GitHub |
|---|---|---|
| **¿Qué es?** | Software local de control de versiones. | Plataforma web en la nube. |
| **¿Dónde corre?** | En tu computadora (sin internet). | En los servidores de GitHub (con internet). |
| **Función principal** | Registrar el historial de cambios de tus archivos. | Alojar repositorios remotos, coordinar equipos y hacer copias de seguridad. |

> ⚠️ **REGLA DE ORO:** Un cambio guardado localmente en Git (`git commit`) **NO está respaldado en la nube** hasta que ejecutas `git push` hacia GitHub.

---

## 2. Creación de Cuenta en GitHub

1. Entra a [github.com/signup](https://github.com/signup).
2. Ingresa tu correo electrónico, crea una contraseña segura y elige un nombre de usuario profesional (ej. `nombre-apellido` o `inicialapellido`).
3. Completa la verificación y confirma tu correo electrónico.

---

## 3. Repositorio Público vs. Repositorio Privado

Cuando crees el repositorio para tu Trabajo Terminal:
- **Repositorio Privado (Recomendado durante el desarrollo):** Solo tú, tus compañeros de equipo y tus asesores pueden ver el código y los avances. Evita plagios o divulgación no autorizada antes de la defensa oral.
- **Repositorio Público:** Visible para cualquier persona en internet. Se recomienda cambiar a público una vez que hayas defendido y aprobado el Trabajo Terminal para enriquecer tu portafolio profesional.

### Cómo agregar a tus compañeros como colaboradores
1. En tu repositorio de GitHub, ve a la pestaña superior **Settings**.
2. En el menú lateral izquierdo haz clic en **Collaborators**.
3. Haz clic en el botón verde **Add people**.
4. Escribe el nombre de usuario de GitHub o correo de tu compañero de equipo y envíale la invitación.
5. Tu compañero debe aceptar la invitación desde su correo o cuenta de GitHub para poder subir cambios.

---

## 4. Autenticación Segura (Git Credential Manager)

Cuando clones o envíes cambios por primera vez mediante HTTPS:
1. Windows abrirá una ventana emergente de **Git Credential Manager**.
2. Selecciona **"Sign in with your browser"**.
3. Autoriza a Git en la ventana del navegador.
4. ¡Listo! Tus credenciales quedan guardadas de forma segura y cifrada en el Administrador de Credenciales de Windows. **Nunca debes escribir contraseñas en texto plano dentro de tus archivos.**

---

## 5. Próximo Paso

Continúa con la [Guía 07: Cómo Obtener la Plantilla](07-obtener-la-plantilla.md).
