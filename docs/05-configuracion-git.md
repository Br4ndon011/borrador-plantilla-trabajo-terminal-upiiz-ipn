# Guía 05: Configuración Inicial de Git

Antes de realizar tu primer cambio o guardar avances, debes indicarle a Git quién eres. Esta configuración se realiza **una sola vez** en tu computadora.

---

## 1. Configurar tu Nombre y Correo Institucional

Abre una terminal (PowerShell o Git Bash) y ejecuta los siguientes dos comandos sustituyendo tus datos reales:

```bash
git config --global user.name "Nombre Apellido"
git config --global user.email "tu_correo@alumno.ipn.mx"
```

### ¿Qué hace cada comando?
- `user.name`: Asocia tu nombre real a cada versión o cambio que guardes (*commit*), permitiendo que tus compañeros y profesores identifiquen quién escribió cada sección.
- `user.email`: Vincula tu correo electrónico a tu cuenta de GitHub. Es recomendable usar tu correo institucional del IPN o el correo principal con el que te registrarás en GitHub.
- `--global`: Aplica esta configuración a todos los repositorios que manejes en tu equipo.

---

## 2. Configurar la Rama Principal por Defecto

Para alinearse con el estándar internacional y la plantilla:

```bash
git config --global init.defaultBranch main
```

---

## 3. Verificar tu Configuración

Para comprobar que los datos se guardaron correctamente, ejecuta:

```bash
git config --global --list
```

**Resultado esperado:**
```text
user.name=Juan Perez Gonzalez
user.email=jperezg@alumno.ipn.mx
init.defaultbranch=main
```

---

## 4. Próximo Paso

Continúa con la [Guía 06: Creación de Cuenta y Uso de GitHub](06-github.md).
