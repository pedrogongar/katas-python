# ROADMAP-KATAS-PYTHON

Plan de progresión del repositorio. Define la configuración técnica, los bloques temáticos y el detalle del bloque en curso. Los bloques posteriores al actual se concretan cuando se aproxime su proyecto ESP32 correspondiente, porque los katas de cada bloque dependen de decisiones técnicas del proyecto que aún no se han tomado.

## Configuración técnica

### Python

- Versión: 3.14 (instalada vía `uv`, cumpliendo `requires-python = ">=3.14"` en `pyproject.toml`).
- Sin tipado explícito en la mayoría de katas del bloque 1 (son fundamentos, el tipado explícito se introduce cuando aporte valor pedagógico).

### pytest

- Descubrimiento automático dentro de `bloques/`.
- Convención: archivos `test_*.py`, funciones `test_*`.
- Uso de `@pytest.mark.parametrize` cuando el kata tenga múltiples casos con el mismo flujo (equivalente a `it.each` de Vitest).

### ruff

- `line-length = 100` (coherente con Prettier de `katas-ts`).
- Reglas activas: `E`, `F`, `I`, `N`, `UP`, `B`, `SIM`.
- Formato: comillas dobles, indentación por espacios.

### basedpyright

- Modo `standard`, no `strict`.
- Se sube a `strict` si algún bloque futuro lo justifica.

### Convenciones

- Numeración de katas: `kpNN_nombre_descriptivo` dentro de cada bloque.
- Numeración de bloques: `bloque-NN-nombre-proyecto`.
- Naming en español para funciones, variables, archivos y carpetas.
- README de cada kata abre con una línea de metadatos tipo `Tipo: simple · Bloque: 1 (proyecto 01 LED toggle) · Dificultad: ★`. Sin frontmatter YAML.
- Enlaces a `docs.python.org` en la sección "qué aprendí" cada vez que aparece un concepto nuevo.

### Filosofía Exercism: qué se hereda y qué no

- Sí: README rico como enunciado profesional (descripción, ejemplos, casos límite, enlaces a docs); ciclo de iteración con feedback; discusión de soluciones tras resolver el kata.
- No: tests pre-escritos. Los tests se escriben a partir de los casos límite identificados en la fase de descomposición.

## Visión general de los diez bloques

Cada bloque es preparatorio del proyecto ESP32 del mismo número. El detalle de cada bloque se concreta cuando se aproxima su proyecto correspondiente; por ahora solo el bloque 1 está desarrollado.

| Bloque | Proyecto ESP32 | Katas estimados | Estado |
|---|---|---|---|
| 1 | 01 LED on/off desde botón web | 6 | En curso |
| 2 | 02 LED con brillo regulable (PWM) | 3-4 | Pendiente |
| 3 | 03 Potenciómetro al frontend | 4-5 | Pendiente |
| 4 | 04 Termómetro DHT11 | 3-4 | Pendiente |
| 5 | 05 Semáforo temporizado | 4-5 | Pendiente |
| 6 | 06 Cerradura con PIN | 3-4 | Pendiente |
| 7 | 07 LED RGB con color picker | 2-3 | Pendiente |
| 8 | 08 Servo con slider de ángulo | 1-2 | Pendiente |
| 9 | 09 Votación en directo | 6-8 | Pendiente |
| 10 | 10 Morse | 6-8 | Pendiente |

Total estimado: 38-49 katas. Retrospectivas: cada cinco katas, entrada en `retrospectivas/retro-NN.md`.

## Bloque 1 — Proyecto 01 LED toggle

**Objetivo**: asentar los fundamentos de Python que el proyecto 1 va a exigir: sintaxis básica, condicionales, funciones, strings, bucles, excepciones e imports. Al terminar el bloque, escribir un servidor HTTP mínimo en MicroPython que enciende y apaga un LED debe ser un ejercicio de aplicar conceptos ya interiorizados, no de aprenderlos sobre la marcha.

**Estilo**: implementación única (sin doble implementación). La doble implementación reaparece en bloques posteriores donde haya un contraste real entre imperativo e idiomático, típicamente a partir del bloque 3 con listas y comprehensiones.

**Fuente primaria de consulta**: `docs.python.org`. Regla dura: prohibido preguntarle a la IA "qué método de Python uso". Se consulta la documentación oficial.

### Lista de katas

#### kp01_variables_y_tipos

Concepto principal: calentamiento. Asentar el flujo completo del método (descomposición, casos límite, tests, código, README) aplicado a Python.

Problema: dado un consumo en Wh y una tarifa en €/kWh, calcular el coste total en euros.

Casos límite: consumo cero, consumo negativo, tarifa cero, valores muy grandes.

Conceptos nuevos: variables, tipos primitivos (`int`, `float`, `str`, `bool`), operadores aritméticos, `type()`, conversiones explícitas (`int()`, `float()`, `str()`).

Dificultad: ★

#### kp02_condicionales

Concepto principal: estructuras de decisión en Python, operadores lógicos, comparaciones encadenadas.

Problema: dada una temperatura en grados Celsius, clasificarla en una categoría ("frío", "templado", "caluroso", "extremo") según rangos definidos, con validación de entrada.

Casos límite: valores en los límites exactos entre categorías, entradas fuera de rango físico razonable, valores no numéricos (decisión de diseño del alumno).

Conceptos nuevos: `if`, `elif`, `else`, operadores `and`, `or`, `not`, comparaciones encadenadas (`0 <= x <= 100`), operador ternario (`a if cond else b`).

Dificultad: ★

#### kp03_funciones

Concepto principal: definición de funciones, parámetros, valores de retorno, ámbito, docstrings.

Problema: función que calcula el área de figuras geométricas según un parámetro `tipo` (`"circulo"`, `"rectangulo"`, `"triangulo"`), recibiendo las dimensiones necesarias.

Casos límite: tipo desconocido, dimensiones negativas o cero, parámetros faltantes.

Conceptos nuevos: `def`, parámetros posicionales, valores por defecto, `return`, ámbito local vs global, docstrings como convención.

Discusión post-kata: ventajas de una función por forma vs una función con `if/elif`, y cómo se relacionará esto con las decisiones de diseño de los endpoints del servidor HTTP del proyecto 1.

Dificultad: ★

#### kp04_strings_y_metodos

Concepto principal: manipulación de strings. Kata crítico para el proyecto 1, donde se parseará peticiones HTTP a mano en MicroPython.

Problema: dada una línea inicial de petición HTTP como string (por ejemplo `"GET /on HTTP/1.1"`), extraer el método HTTP y la ruta como una tupla `(metodo, ruta)`. Debe manejar entradas malformadas lanzando error.

Casos límite: string vacío, línea sin espacios suficientes, método en minúsculas, ruta con query string (`/on?brillo=50`), espacios múltiples.

Conceptos nuevos: indexación, slicing, métodos de string clave (`strip`, `split`, `startswith`, `endswith`, `replace`, `lower`, `upper`), f-strings, concatenación.

Dificultad: ★★

#### kp05_bucles

Concepto principal: estructuras iterativas, bucles controlados, `break` y `continue`.

Problema: simular un bucle de lectura de sensor. Recibe una función generadora de lecturas, un umbral y un máximo de iteraciones; devuelve la lectura que supera el umbral y el número de iteraciones necesarias. Si se alcanza el máximo sin superar el umbral, devuelve `None`.

Casos límite: umbral nunca alcanzado, umbral alcanzado en la primera iteración, iteraciones máximas a cero.

Conceptos nuevos: `while` (incluido `while True` con `break`), `for` con `range`, `for` sobre iterables, `continue`, `break`, `else` en bucles (opcional, mencionarlo pero no exigirlo).

Dificultad: ★

#### kp06_excepciones_e_imports

Concepto principal: manejo robusto de errores, estructura de imports. Cierre del bloque con el concepto que permite al proyecto 1 capturar fallos de WiFi o socket de forma limpia.

Problema: función que recibe un string con un número, lo convierte a entero y lo devuelve. Debe capturar todos los casos de error posibles (string vacío, no numérico, con espacios, con signo) y lanzar una excepción propia con un mensaje informativo.

Casos límite: string vacío, números válidos, decimales (rechazar), signos, espacios alrededor.

Conceptos nuevos: `try`, `except`, `except ExcepcionEspecifica`, `except (A, B)`, `finally`, `raise`, excepciones personalizadas (básico, una clase heredando de `Exception`), estructura de imports (`import x`, `from x import y`, `from x import y as z`).

Dificultad: ★★

### Cierre del bloque 1

Tras `kp06`, primera retrospectiva: `retrospectivas/retro-01.md`. Tras la retrospectiva, el repositorio está listo para que arranque el proyecto 01 LED toggle en su repo propio (`esp32-01-led-toggle`).

## Bloques 2-10

Los bloques siguientes se concretan cuando se aproxime su proyecto ESP32 correspondiente. A continuación, el esqueleto temático de cada uno según el `ROADMAP-ESP32.md`.

### Bloque 2 — Proyecto 02 LED PWM

Conceptos: conversión de tipos (string ↔ int), aritmética de mapeo de rangos, manejo de query strings, validación de entrada.

### Bloque 3 — Proyecto 03 Potenciómetro

Conceptos: listas (creación, indexación, slicing), bucles con acumuladores, funciones de agregación, concepto básico de async/await.

Nota: posible reintroducción de doble implementación (imperativo vs comprehensiones) cuando entren las listas.

### Bloque 4 — Proyecto 04 Termómetro DHT11

Conceptos: manejo avanzado de excepciones, diccionarios, serialización a JSON con `json`, tipos en JSON.

### Bloque 5 — Proyecto 05 Semáforo

Conceptos: bucles infinitos controlados, estructuras de datos para máquinas de estados, `time.sleep` y sus implicaciones, introducción a `uasyncio`.

### Bloque 6 — Proyecto 06 Cerradura PIN

Conceptos: strings (comparación, métodos), `hashlib`, variables de estado entre peticiones, manejo de tiempo con `time.time()`.

### Bloque 7 — Proyecto 07 LED RGB

Conceptos: conversión entre bases (hex a decimal), slicing avanzado de strings, tuplas y desempaquetado.

### Bloque 8 — Proyecto 08 Servo

Conceptos: funciones con cálculos matemáticos, validación de rangos.

### Bloque 9 — Proyecto 09 Votación

Conceptos: `time.ticks_ms()` y `time.ticks_diff()`, estructuras de control con timestamps, concurrencia con `uasyncio` (corutinas, `await`, `asyncio.gather`), manejo de listas de conexiones.

### Bloque 10 — Proyecto 10 Morse

Conceptos: diccionarios complejos como tablas de lookup, iteración anidada, manejo preciso de tiempo en MicroPython, funciones generadoras (`yield`) opcional, estado compartido y cancelación cooperativa.