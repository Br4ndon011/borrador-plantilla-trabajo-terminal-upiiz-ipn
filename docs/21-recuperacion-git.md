# Guía 21: Recuperación de Cambios y Consulta de Historial

Git registra cada paso que das en tu proyecto. Esta guía te enseña a consultar tu historial y recuperar archivos o párrafos borrados por accidente de forma segura.

---

## 1. Ver qué Cambió Antes de Guardar (`git diff`)

Si quieres ver exactamente qué líneas modificaste respecto al último guardado:

```bash
git diff
```
*(Las líneas con un signo `+` verde son texto agregado; las líneas con `-` rojo son texto eliminado).*

Para ver los cambios de un solo archivo:
```bash
git diff capitulos/02-justificacion.tex
```

---

## 2. Consultar el Historial de Commits (`git log`)

Para ver la lista cronológica de todos los avances guardados:

```bash
git log --oneline -10
```

**Ejemplo de salida:**
```text
f3a8b1c (HEAD -> main, origin/main) report: incorpora tabla de resultados
e4d2a9f figures: agrega plano de ensamble en apendice B
b7c1d5e fix: corrige ortografia en marco teorico
a8e0f21 feat: crea plantilla inicial institucional
```

---

## 3. Descartar Modificaciones No Deseadas en un Archivo

Si estuviste editando un archivo pero decidiste que quieres descartar los cambios y volver exactamente a como estaba en el último commit:

```bash
git restore capitulos/02-justificacion.tex
```

---

## 4. Recuperar un Archivo Borrado Accidentalmente

Si borraste por error una imagen o un archivo `.tex` desde el explorador de archivos:

```bash
git restore figuras/proyecto/esquematico.png
```
*(El archivo reaparecerá al instante en su carpeta).*

---

## 5. ⚠️ ADVERTENCIA CRÍTICA: Comandos Destructivos

> 🛑 **NUNCA ejecutes comandos como:**
> ```bash
> git reset --hard
> git clean -fd
> git push --force
> ```
> Estos comandos **destruyen permanentemente el trabajo no guardado** y pueden borrar commits del repositorio remoto sin posibilidad de recuperación. Consulta siempre con tu asesor o docente antes de intentar forzar un reseteo de Git.

---

## 6. Próximo Paso

Continúa con la [Guía 22: Solución de Errores Comunes de LaTeX](22-errores-comunes-latex.md).
