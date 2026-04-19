import pytest
from solucion import calcular_coste_electricidad


def test_consumo_negativo_lanza_valueerror():
    with pytest.raises(ValueError):
        calcular_coste_electricidad(-2, 2)


def test_tarifa_negativa_lanza_valueerror():
    with pytest.raises(ValueError):
        calcular_coste_electricidad(5, -3)


def test_consumo_cero_devuelve_cero():
    assert calcular_coste_electricidad(0, 6) == 0


def test_tarifa_cero_devuelve_cero():
    assert calcular_coste_electricidad(4, 0) == 0


def test_entradas_validas():
    assert calcular_coste_electricidad(8, 10) == 0.08


def test_ambos_input_son_cero():
    assert calcular_coste_electricidad(0, 0) == 0


def test_ambos_input_son_negativos_lanza_valueerror():
    with pytest.raises(ValueError):
        calcular_coste_electricidad(-1, -3)


def test_input_decimal():
    assert calcular_coste_electricidad(100, 0.1) == pytest.approx(0.01)


def test_input_grande():
    assert calcular_coste_electricidad(8000, 0.15) == pytest.approx(1.2)
