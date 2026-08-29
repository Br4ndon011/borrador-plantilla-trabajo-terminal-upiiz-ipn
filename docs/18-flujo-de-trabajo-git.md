# Guía 18: Flujo de Trabajo Diario con Git

Esta guía detalla los 4 comandos esenciales que utilizarás todos los días para guardar y respaldar tu trabajo.

---

## 1. El Ciclo Diario de 4 Comandos

Cada vez que completes una unidad lógica de redacción (un párrafo, una sección, una tabla o una figura):

```bash
# 1. Ver qué archivos has modificado
git status

# 2. Agregar todos los cambios al área de preparación
git add .

# 3. Guardar los cambios con un mensaje claro
git commit -m "report: redacta marco teorico y agrega funciones de transferencia"

# 4. Enviar los avances a GitHub en la nube
git push
```

---

## 2. Mensajes de Commit: Buenos vs. Malos

El mensaje del commit explica el **por qué** y el **qué** del cambio. Ayuda a tu equipo y asesores a entender el avance.

### ❌ Ejemplos de Malos Mensajes (EVÍTARLOS):
- `git commit -m "cambios"` *(¿Qué cambió? No da información).*
- `git commit -m "subiendo avance"`
- `git commit -m "final"`
- `git commit -m "final final"`
- `git commit -m "ya quedo ahora si"`
- `git commit -m "asdfg"`

### ✅ Ejemplos de Buenos Mensajes (RECOMENDADOS):
Usa prefijos cortos y descriptivos:
- `git commit -m "report: agrega justificacion tecnica y social"`
- `git commit -m "report: actualiza objetivos especificos aprobados"`
- `git commit -m "figures: agrega diagrama esquematico de la etapa de potencia"`
- `git commit -m "tables: incorpora matriz de requerimientos y metricas"`
- `git commit -m "math: formula ecuaciones dinamicas de Euler-Lagrange"`
- `git commit -m "references: añade citas bibtex para control difuso"`
- `git commit -m "fix: corrige error tipografico en capitulo de validacion"`

---

## 3. Frecuencia de Guardado

- **Haz commits frecuentes y pequeños:** Es mejor hacer 5 commits descriptivos al día que 1 commit gigante de 500 líneas al final del mes.
- **Ventaja:** Si cometes un error, es mucho más fácil identificar y deshacer un cambio pequeño que uno masivo.

---

## 4. Próximo Paso

Continúa con la [Guía 19: Trabajo en Equipo para 2 o 3 Integrantes](19-trabajo-en-equipo.md).
