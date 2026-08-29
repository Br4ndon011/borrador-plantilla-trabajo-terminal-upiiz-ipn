# Guía 20: Cómo Resolver Conflictos en Git

Un conflicto de Git ocurre cuando dos integrantes del equipo modifican **las mismas líneas del mismo archivo** y ambos intentan subir sus cambios sin sincronizarse previamente.

---

## 1. ¿Cómo se Ve un Conflicto?

Cuando ejecutas `git pull` o `git merge` y existe un conflicto, Git no borrará nada. En su lugar, insertará **marcadores de conflicto** dentro del archivo afectado:

```latex
<<<<<<< HEAD (Tus cambios locales)
Se seleccionó un motor a pasos NEMA 17 con un par de 0.45 Nm.
=======
Se seleccionó un servomotor MG996R de alto torque para la dirección.
>>>>>>> 1a2b3c4d... (Los cambios que subió tu compañero a GitHub)
```

- **`<<<<<<< HEAD`**: Marca el inicio de lo que escribiste en tu computadora.
- **`=======`**: Línea divisoria entre ambas versiones.
- **`>>>>>>> [hash]`**: Marca el final de lo que escribió tu compañero.

---

## 2. Pasos para Resolver el Conflicto

1. **Abre el archivo en conflicto en VS Code:**
   Verás las líneas resaltadas con botones automáticos como *Accept Current Change*, *Accept Incoming Change*, *Accept Both Changes*.
2. **Lee atentamente ambas versiones:**
   Habla con tu compañero para acordar cuál es la redacción correcta o si deben combinarse ambas ideas.
3. **Edita el texto manualmente:**
   Conserva el texto correcto y **asegúrate de borrar todos los marcadores (`<<<<<<<`, `=======`, `>>>>>>>`)**.
   
   *Ejemplo resuelto:*
   ```latex
   Para el sistema de tracción se seleccionó un motor a pasos NEMA 17 (0.45 Nm), mientras que para la dirección se implementó un servomotor MG996R de alto torque.
   ```
4. **Verifica que el documento compile:**
   ```bash
   latexmk main.tex
   ```
5. **Guarda y finaliza la resolución con Git:**
   ```bash
   git add .
   git commit -m "fix: resuelve conflicto de seleccion de motores"
   git push
   ```

> ⚠️ **ADVERTENCIA:** Nunca hagas clic en *"Aceptar entrante"* o *"Aceptar actual"* a ciegas sin leer el contenido, ya que podrías borrar sin querer párrafos importantes de tu compañero.

---

## 3. Próximo Paso

Continúa con la [Guía 21: Recuperación de Cambios y Consulta de Historial](21-recuperacion-git.md).
