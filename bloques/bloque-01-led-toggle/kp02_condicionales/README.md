# kp02 — condicionales

Tipo: simple · Bloque: 1 (proyecto 01 LED toggle) · Dificultad: ★

## Enunciado

Dada una temperatura en grados Celsius, clasificarla en una de cuatro categorías: `frío` (menor que 15), `templado` (de 15 inclusive hasta 25 exclusive), `caluroso` (de 25 inclusive hasta 35 exclusive), o `extremo` (mayor o igual a 35). La función recibe `temperatura_celsius` y devuelve un string con la categoría.

## Descomposición

La clasificación por rangos es el caso de uso paradigmático de `if/elif/else`. La lógica del problema es trivial; el valor pedagógico está en los detalles: razonar sobre los límites exactos entre categorías, validar el tipo y el rango de entrada, y escribir la cascada de condicionales sin comparaciones redundantes.

Dos decisiones de diseño relevantes. La primera, sobre el tipo de entrada: solo se acepta `int`. Esta decisión es voluntaria y restrictiva; podría haberse aceptado `float` también, pero en el contexto pedagógico del kata la restricción es deliberada porque fuerza validar `TypeError` explícitamente. Se distingue `TypeError` (cuando el tipo no es `int`) de `ValueError` (cuando el tipo es correcto pero el valor está fuera del rango físico válido), siguiendo la convención idiomática de Python. La segunda, sobre el rango físico: la función acepta temperaturas entre -213 °C (aproximación al cero absoluto) y 465 °C (máxima superficial del Sistema Solar en Venus). Por fuera, se lanza `ValueError`.

Los casos límite cubren tres grupos: entradas inválidas (tipo incorrecto o rango imposible), valores justo en los límites exactos entre categorías (15, 25, 35, y los extremos -213 y 465), y valores típicos intermedios (5, 14, 20, 24, 30, 34, 40) para verificar que cada categoría se comporta bien en su rango completo y no solo en los límites.

## Solución

```python
def clasificar_temperatura(temperatura_celsius: int) -> str:
    if type(temperatura_celsius) is not int:
        raise TypeError("El input debe ser de tipo int")
    if temperatura_celsius > 465 or temperatura_celsius < -213:
        raise ValueError("El rango se encuentra entre -213 y 465")
    if temperatura_celsius < 15:
        return "frío"
    elif temperatura_celsius < 25:
        return "templado"
    elif temperatura_celsius < 35:
        return "caluroso"
    else:
        return "extremo"
```

Validación en dos pasos al inicio (*fail fast*): primero el tipo, después el rango. Cada validación es un `if` independiente porque son comprobaciones atómicas, no ramas de una misma decisión.

La cascada de clasificación aprovecha el orden de evaluación de `elif`: cuando la ejecución llega a un `elif`, Python ya garantiza que las condiciones anteriores fallaron, por lo que no hace falta repetirlas. Así, `elif temperatura_celsius < 25` implica implícitamente `>= 15` (porque si no, habría entrado en la rama anterior). Este patrón elimina todas las comparaciones redundantes y reduce el número total de operaciones a cuatro, una por rama. El `else` final actúa como *catch-all* para el caso `>= 35`, lo que también garantiza que la función siempre devuelva un `str` (no hay camino implícito que retorne `None`).

El uso de `type(x) is not int` en lugar de `isinstance(x, int)` merece comentario. En Python, `bool` es un subtipo de `int`, por lo que `isinstance(True, int)` devuelve `True`. Para este kata, donde queremos rechazar booleanos como entrada, `type() is` es más estricto y resuelve el problema accidentalmente en una sola comparación. `isinstance` seguido de un `not isinstance(x, bool)` sería la alternativa más verbosa y más explícita; ambas son defendibles y la elección aquí prioriza la concisión.

## Discusión

El problema es trivial en su lógica, pero el kata expone dos aspectos del tipado en Python que no son evidentes para quien viene de TypeScript.

El primero es la distinción semántica entre `TypeError` y `ValueError`. Python tiene una jerarquía de excepciones donde cada tipo comunica una intención distinta al consumidor de la función. `TypeError` significa "el tipo del argumento no es el esperado"; `ValueError`, "el tipo es correcto pero el valor no es válido". Distinguirlas es idiomático y permite al consumidor capturar específicamente lo que le interese.

El segundo es la interacción entre los type hints y la validación en tiempo de ejecución. Los type hints en Python **no se ejecutan**: son metadatos que leen herramientas como `basedpyright`, pero no impiden que alguien llame a la función con un tipo incorrecto en runtime. Por eso, una función que declara `temperatura_celsius: int` aún necesita validar el tipo con `isinstance` o `type()` si quiere seguridad real. Declarar el tipo es documentación; la validación runtime es defensa. Son dos mecanismos complementarios.

Esto genera una tensión al escribir tests. Los tests `test_input_float_no_valido` y `test_input_str_no_valido` llaman a la función con argumentos que rompen su contrato de tipo a propósito para verificar la defensa runtime. Basedpyright los marca como errores, con razón desde su punto de vista. La solución idiomática es añadir `# type: ignore[arg-type]` en las líneas donde se rompe el contrato voluntariamente. El comentario documenta la intención al lector futuro y silencia el falso positivo en la línea específica sin debilitar la firma de la función.

## Qué aprendí

- **Distinción entre `TypeError` y `ValueError`**: Python distingue tipos de excepción por convención. `TypeError` cuando el tipo es inadecuado; `ValueError` cuando el tipo es correcto pero el valor no. Usar la adecuada ayuda a que el código comunique su intención correctamente. Documentación: [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html).
- **`type(x) is T` vs `isinstance(x, T)`**: la primera comprueba el tipo exacto; la segunda admite subtipos. En Python, `bool` es subtipo de `int`, lo que hace relevante la distinción cuando se quiere rechazar booleanos. Documentación: [type()](https://docs.python.org/3/library/functions.html#type) y [isinstance()](https://docs.python.org/3/library/functions.html#isinstance).
- **Cascada de `if/elif` con orden descendente**: reordenar las ramas elimina comparaciones redundantes. Cada `elif` solo necesita comprobar un límite, porque el otro lo garantiza el flujo de control.
- **`else` final vs `elif` final**: usar `else` en la última rama garantiza que la función cubra todos los casos y siempre devuelva un valor, evitando retornos implícitos de `None`.
- **Type hints en Python no se ejecutan**: son metadatos para herramientas de análisis estático, no restricciones en runtime. La validación real requiere `isinstance` o equivalente dentro de la función.
- **`# type: ignore[arg-type]` para silenciar tests que rompen contratos a propósito**: permite mantener la firma correcta y silenciar falsos positivos en los tests que verifican defensas. Documentación: [typing — type-ignore comments](https://typing.python.org/en/latest/spec/directives.html#type-ignore-comments).