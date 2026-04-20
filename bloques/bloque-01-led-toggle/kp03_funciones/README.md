# kp03 — funciones

Tipo: simple · Bloque: 1 (proyecto 01 LED toggle) · Dificultad: ★

## Enunciado

Calcular el área de una figura geométrica. La función recibe `tipo` (string con el nombre de la figura) y los parámetros necesarios según el tipo. Tipos soportados: `"circulo"` (recibe `radio`), `"rectangulo"` y `"triangulo"` (reciben `base` y `altura`). Debe devolver el área como número.

## Descomposición

Una única función que atiende tres figuras distintas requiere una firma flexible. De entre las opciones disponibles (parámetros opcionales con `None` por defecto, `*args`/`**kwargs`, o funciones separadas con dispatcher), se eligen parámetros opcionales con `None` por defecto. Es la opción más legible y la que mejor documenta en la propia firma qué parámetros acepta la función.

Se siguen las mismas decisiones sobre excepciones que en los katas anteriores: `TypeError` cuando el tipo del argumento no es el esperado, `ValueError` cuando el tipo es correcto pero el valor no. La función valida que `tipo` sea un `str` (TypeError si no), que su valor esté en la lista de figuras soportadas (ValueError si no), que los parámetros requeridos para cada figura no sean `None` y sean ≥ 0 (ValueError si no), y que no se pasen parámetros sobrantes para la figura indicada (ValueError si se pasan).

El resultado se devuelve exacto, sin redondear ni truncar, siguiendo la misma decisión del kp01.

## Solución

```python
import math


def calcular_area(
    tipo: str,
    radio: int | float | None = None,
    base: int | float | None = None,
    altura: int | float | None = None,
) -> int | float:
    if not isinstance(tipo, str):
        raise TypeError("Tipo debe ser circulo, rectangulo o triangulo")
    if tipo not in ("circulo", "rectangulo", "triangulo"):
        raise ValueError("Tipo debe ser circulo, rectangulo o triangulo")

    if tipo == "circulo":
        if base is not None or altura is not None:
            raise ValueError("Para círculo, base y altura deben ser None")
        if radio is None or radio < 0:
            raise ValueError("Radio debe ser un número mayor o igual que 0")
        return math.pi * radio**2

    if tipo == "rectangulo":
        if radio is not None:
            raise ValueError("Para rectángulo, radio debe ser None")
        if base is None or altura is None or base < 0 or altura < 0:
            raise ValueError("Base y altura deben ser números mayores o iguales que 0")
        return base * altura

    if radio is not None:
        raise ValueError("Para triángulo, radio debe ser None")
    if base is None or altura is None or base < 0 or altura < 0:
        raise ValueError("Base y altura deben ser números mayores o iguales que 0")
    return base * altura / 2
```

Firma con cuatro parámetros, tres de ellos opcionales con `None` por defecto. La validación del tipo y del valor de `tipo` se hace al inicio porque es transversal a todas las figuras. Después, cada rama (círculo, rectángulo, triángulo) se aísla y valida solo los parámetros que le conciernen: los que necesita (no pueden ser `None` y deben ser ≥ 0) y los que no (deben ser `None`).

La rama del triángulo no necesita un `if tipo == "triangulo"` explícito: si la ejecución llega hasta allí, ya se ha pasado la validación inicial del valor de `tipo` y no es ni círculo ni rectángulo, por tanto solo puede ser triángulo. Es el mismo patrón del `else` en kp02, extendido a una cadena de `if` con `return` temprano.

## Discusión

El problema es trivial en matemática (tres fórmulas de área) pero se complica rápido cuando se introducen validaciones estrictas. La versión inicial de las decisiones de diseño pedía validar cualquier parámetro "sobrante" para la figura correspondiente (por ejemplo, rechazar `calcular_area("rectangulo", radio=4, base=6, altura=2)` porque `radio` sobra para el rectángulo). Esta decisión infla la función con seis validaciones adicionales y añade complejidad estructural que no aporta valor pedagógico al kata. En una sesión real de diseño, la decisión correcta habría sido ignorar los parámetros sobrantes silenciosamente (comportamiento permisivo), lo cual reduce la función a un tercio de su tamaño.

Otra discusión interesante es cómo interactúan los type hints con la validación runtime. La firma declara `tipo: str`, pero la función valida con `isinstance(tipo, str)` para capturar el caso en que alguien ignore el contrato. Basedpyright marca esa validación como "código inalcanzable" desde su análisis estático, porque confía en la anotación. Esto fuerza a usar `# pyright: ignore[reportUnreachable]` o, como en este kata, a reorganizar el código para que basedpyright pueda convivir con la validación runtime. Es una tensión recurrente en Python moderno entre documentación de tipos y defensa en tiempo de ejecución.

## Qué aprendí

- **`@pytest.mark.parametrize` para agrupar tests**: el equivalente en pytest de `it.each` de Vitest. Permite escribir una función de test con múltiples casos pasados como lista de tuplas. Útil cuando varios casos comparten la misma estructura de aserción, como los casos de cálculo correcto o los casos que lanzan una excepción determinada. Documentación: [pytest.mark.parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html).
- **Agrupación de tests por tipo de aserción**: con parametrize, conviene separar los tests en grupos según qué tipo de comprobación hacen: cálculos correctos por un lado, excepciones por otro, y dentro de las excepciones, un grupo por cada tipo de error. Reduce la cantidad de funciones de test sin perder claridad.
- **Valores por defecto en la firma de funciones**: `def f(x: int | None = None)` declara que `x` acepta un `int` o `None`, y que si no se pasa el argumento al llamar, vale `None`. Combinado con type hints `int | None`, permite firmas flexibles donde algunos parámetros son opcionales según el caso de uso. Documentación: [Default argument values](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values).
- **`isinstance(x, T)` sobre `type(x) is T`**: más idiomático en Python. En este kata ambos funcionan igual porque `str` no tiene subclases relevantes, pero `isinstance` es la opción convencional y preferible por defecto.
- **Import ordering con ruff**: ruff verifica que los imports sigan el orden estándar PEP 8 (stdlib, externos, locales). Se corrige automáticamente con `ruff check --fix`.