# katas-python

Katas de Python organizados por bloques, cada bloque preparatorio de un proyecto del carril de electrónica con ESP32. El objetivo del repositorio es construir fluidez con los fundamentos de Python y entrenar las habilidades de descomposición, consulta a documentación oficial y debugging por hipótesis, antes de aplicar cada conjunto de conceptos en hardware real.

## Contexto

Este repositorio forma parte de un plan de aprendizaje más amplio que se divide en tres carriles paralelos (ver `CLAUDE.md` del plan general):

- **Carril 1** — Python + ESP32: diez proyectos de electrónica, cada uno precedido de un bloque de katas Python preparatorios.
- **Carril 2** — Fundamentos TypeScript: repositorio `katas-ts`.
- **Carril 3** — Mini-apps Vue.

`katas-python` es el complemento preparatorio del carril 1. Cada bloque agrupa los katas necesarios para afrontar un proyecto ESP32 con los fundamentos Python ya interiorizados.

## Filosofía

- Descomposición previa al código. Cada kata se piensa antes de escribirse. La descomposición ocurre fuera del repositorio, en notas privadas; el repositorio contiene el resultado pulido.
- Tests propios. No hay tests pre-escritos. Los tests se derivan de los casos límite identificados en la fase de descomposición.
- Documentación oficial como fuente primaria. Cada README de kata enlaza a la entrada de `docs.python.org` correspondiente para los conceptos nuevos utilizados.
- Conventional Commits en todo el historial.

## Estructura

```
katas-python/
├── bloques/
│   ├── bloque-01-led-toggle/
│   │   ├── kp01_variables_y_tipos/
│   │   │   ├── README.md
│   │   │   ├── solucion.py
│   │   │   └── test_solucion.py
│   │   └── ...
│   ├── bloque-02-led-pwm/
│   └── ...
├── retrospectivas/
│   └── retro-NN.md      ← cada 5 katas
├── ROADMAP-KATAS-PYTHON.md
├── pyproject.toml
├── uv.lock
└── README.md
```

## Convenciones

- Nomenclatura de katas: `kpNN_nombre_descriptivo` (kata preparatoria), padding de dos cifras, empezando en `kp01` dentro de cada bloque.
- Nomenclatura de bloques: `bloque-NN-nombre-proyecto`, vinculando cada bloque al proyecto ESP32 que prepara.
- Nombres de funciones, variables, archivos y carpetas en español.
- README de cada kata: abre con una línea tipo `Tipo: simple · Bloque: 1 (proyecto 01 LED toggle) · Dificultad: ★`. Sin frontmatter YAML.
- Enlaces a `docs.python.org` en la sección "qué aprendí" del README cada vez que aparece un concepto nuevo.

## Setup local

Requisitos: `uv` (gestor de entornos y dependencias de Astral).

```fish
uv sync              # instala dependencias desde uv.lock
uv run pytest        # ejecuta pytest una vez
uv run pytest -v     # pytest con output verboso
uv run ruff check    # linting sobre todo el repo
uv run ruff format   # formato sobre todo el repo
uv run basedpyright  # type checking
```

`uv run X` ejecuta `X` dentro del entorno virtual sin necesidad de activarlo manualmente.

## Roadmap

Ver `ROADMAP-KATAS-PYTHON.md` para la planificación de bloques y la lista detallada del bloque en curso.

## Índice de katas

| Kata | Bloque | Proyecto ESP32 | Dificultad | Estado |
|---|---|---|---|---|
| kp01 — variables_y_tipos | 1 | 01 LED toggle | ★ | Completado |
| kp02 — condicionales | 1 | 01 LED toggle | ★ | Pendiente |
| kp03 — funciones | 1 | 01 LED toggle | ★ | Pendiente |
| kp04 — strings_y_metodos | 1 | 01 LED toggle | ★★ | Pendiente |
| kp05 — bucles | 1 | 01 LED toggle | ★ | Pendiente |
| kp06 — excepciones_e_imports | 1 | 01 LED toggle | ★★ | Pendiente |