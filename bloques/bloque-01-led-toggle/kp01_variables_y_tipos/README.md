# kp01 — variables_y_tipos

Tipo: simple · Bloque: 1 (proyecto 01 LED toggle) · Dificultad: ★

## Enunciado

Dada una tarifa eléctrica en euros por kilovatio-hora (€/kWh) y un consumo en vatios-hora (Wh), calcular el coste total en euros.

## Descomposición

Dos datos llegan con unidades distintas: el consumo en Wh y la tarifa en €/kWh. Antes de multiplicar hay que alinear unidades. La conversión es directa: 1 kWh = 1000 Wh, así que el consumo en kWh sale de dividir el consumo en Wh entre 1000. Una vez alineadas las unidades, el coste es consumo por tarifa.

Dos decisiones de diseño relevantes. La primera es qué hacer con inputs inválidos: consumo y tarifa negativos no tienen sentido físico, así que la función lanza `ValueError` en esos casos. El cero sí es válido (consumo cero cuesta cero, tarifa cero también cuesta cero) y no necesita tratamiento especial: la multiplicación por cero ya devuelve cero. La segunda decisión es sobre precisión: la función devuelve el valor exacto del cálculo sin redondear, porque redondear mezclaría responsabilidades de cálculo y presentación. El formateo visual, si hiciera falta, es trabajo de quien consume la función.

Casos límite:

- Consumo negativo → lanza `ValueError`.
- Tarifa negativa → lanza `ValueError`.
- Ambos negativos → lanza `ValueError`.
- Consumo cero → devuelve 0.
- Tarifa cero → devuelve 0.
- Ambos cero → devuelve 0.
- Input válido (8 Wh, 10 €/kWh) → 0.08 €.
- Input decimal (100 Wh, 0.1 €/kWh) → 0.01 €.
- Input grande (8000 Wh, 0.15 €/kWh) → 1.20 €.

## Solución

```python
def calcular_coste_electricidad(consumo_wh: int | float, tarifa_eur_kwh: int | float) -> int | float:
    if consumo_wh < 0 or tarifa_eur_kwh < 0:
        raise ValueError("El input debe ser >= 0")
    consumo_kwh = consumo_wh / 1000
    return tarifa_eur_kwh * consumo_kwh
```

Validación al inicio siguiendo el patrón *fail fast*: si los inputs son inválidos, la función falla antes de entrar en la lógica de cálculo. La conversión de Wh a kWh se aísla en una variable con nombre descriptivo (`consumo_kwh`) para que la línea del `return` lea como lo que es: una multiplicación de consumo por tarifa. La anotación de tipos con `int | float` deja explícito que la función acepta tanto enteros como decimales en cualquiera de los dos parámetros, y devuelve el mismo tipo de unión.

El caso de inputs cero no necesita un *guard* propio: la multiplicación `consumo_kwh * tarifa_eur_kwh` devuelve cero de forma natural cuando cualquiera de los dos operandos es cero. Añadir un `elif` para ese caso sería código redundante.

## Discusión

El problema es trivial en su lógica (tres operaciones aritméticas y una guarda), pero el valor pedagógico de este kata como primer contacto con Python está en otro sitio: asentar el flujo completo (descomposición → tests → implementación → README) con herramientas nuevas.

El único tropiezo real durante la implementación apareció en el test `test_input_decimal`. El caso `100 Wh × 0.1 €/kWh` debería dar exactamente `0.01`, pero Python devolvió `0.010000000000000002`. La comparación con `==` falló y obligó a cambiar el test a `pytest.approx(0.01)`. El bug no estaba en la función: estaba en la comparación. Los `float` de Python siguen el estándar IEEE 754 y no pueden representar `0.1` con exactitud en binario; cualquier operación que involucre `0.1` arrastra un error mínimo pero suficiente para romper una comparación estricta. La regla práctica es no comparar floats con `==` cuando el valor sale de una operación, siempre con tolerancia.

## Qué aprendí

- **`ValueError` como excepción idiomática para input inválido**: Python distingue tipos de excepción (`ValueError`, `TypeError`, `KeyError`, etc.) y cada tipo tiene un significado convencional. `ValueError` es la adecuada cuando el valor es sintácticamente válido pero semánticamente inválido (un número negativo cuando el dominio exige no negativo). Documentación: [Built-in Exceptions — ValueError](https://docs.python.org/3/library/exceptions.html#ValueError).
- **`pytest.approx` para comparar floats con tolerancia**: la función `pytest.approx(valor)` genera un objeto que, al compararse con `==`, admite una pequeña tolerancia por defecto. Imprescindible para tests que involucren operaciones aritméticas con decimales. Documentación: [pytest.approx](https://docs.pytest.org/en/stable/reference/reference.html#pytest-approx).
- **`pytest.raises` como context manager**: la forma idiomática de testear excepciones en pytest es `with pytest.raises(TipoDeError): codigo_que_debe_lanzarla()`. El test pasa si la excepción se lanza; falla si no se lanza o si se lanza una distinta. Documentación: [Assertions about expected exceptions](https://docs.pytest.org/en/stable/how-to/assert.html#assertions-about-expected-exceptions).
- **Union types con `|` en anotaciones (Python 3.10+)**: `int | float` es el idiomático moderno para declarar que un parámetro acepta varios tipos. Sustituye a la sintaxis anterior `Union[int, float]` del módulo `typing`. Documentación: [Typing — Unions](https://docs.python.org/3/library/typing.html#typing.Union).
- **Imprecisión flotante IEEE 754**: los `float` en Python (y en casi todos los lenguajes) no pueden representar todos los decimales con exactitud. `0.1` se almacena como una aproximación y cualquier operación que lo use arrastra un pequeño error. No es un bug, es una limitación del estándar. Documentación: [Floating Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html).
- **Los casos especiales se resuelven solos cuando la lógica base es correcta**: patrón ya identificado en `ej05 — factorial` de `katas-ts`. Aquí aplica igual: el caso de input cero no necesita un `elif` porque la multiplicación por cero ya devuelve cero. Añadir guards para casos que el algoritmo base cubre es ruido que se paga en legibilidad y mantenimiento.