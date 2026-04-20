import math

import pytest
from solucion import calcular_area


@pytest.mark.parametrize("tipo, radio, base, altura, esperado", [
    ("rectangulo", None, 5, 0, 0),
    ("rectangulo", None, 5, 2, 10),
    ("triangulo", None, 6, 3, 9),
])
def test_calculo_correcto(tipo, radio, base, altura, esperado):
    assert calcular_area(tipo, radio, base, altura) == esperado

@pytest.mark.parametrize("tipo, radio, base, altura, esperado", [
    ("circulo", 4, None, None, math.pi * 16),
])
def test_calculo_circulo(tipo, radio, base, altura, esperado):
    assert calcular_area(tipo, radio, base, altura) == pytest.approx(esperado)

@pytest.mark.parametrize("tipo, radio, base, altura", [
    ("circulo", -2, None, None),
    ("cuadrado", None, 1, 6),
    ("triangulo", None, None, None),
    ("rectangulo",4, 6, 2),
    ("5", None, None, None),
])
def test_value_error(tipo, radio, base, altura):
    with pytest.raises(ValueError):
        calcular_area(tipo, radio, base, altura)

@pytest.mark.parametrize("tipo, radio, base, altura", [
    (None, 4, 8, None)
])
def test_type_error(tipo, radio, base, altura):
    with pytest.raises(TypeError):
        calcular_area(tipo, radio, base, altura)