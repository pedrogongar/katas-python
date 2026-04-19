import pytest
from solucion import clasificar_temperatura


def test_fuera_de_rango_negativo():
    with pytest.raises(ValueError):
        clasificar_temperatura(-214)


def test_fuera_de_rango_positivo():
    with pytest.raises(ValueError):
        clasificar_temperatura(466)


def test_input_float_no_valido():
    with pytest.raises(TypeError):
        clasificar_temperatura(34.3) # type: ignore[arg-type]


def test_input_str_no_valido():
    with pytest.raises(TypeError):
        clasificar_temperatura("cien") # type: ignore[arg-type]


def test_limite_templado():
    assert clasificar_temperatura(15) == "templado"


def test_limite_caluroso():
    assert clasificar_temperatura(25) == "caluroso"


def test_limite_extremo():
    assert clasificar_temperatura(35) == "extremo"


def test_limite_frio():
    assert clasificar_temperatura(-213) == "frío"


def test_limite_extremo_maximo():
    assert clasificar_temperatura(465) == "extremo"


def test_caso_frio_5():
    assert clasificar_temperatura(5) == "frío"


def test_caso_templado_20():
    assert clasificar_temperatura(20) == "templado"


def test_caso_caluroso_30():
    assert clasificar_temperatura(30) == "caluroso"


def test_caso_extremo_40():
    assert clasificar_temperatura(40) == "extremo"


def test_caso_frio_14():
    assert clasificar_temperatura(14) == "frío"


def test_caso_templado_24():
    assert clasificar_temperatura(24) == "templado"


def test_caso_caluroso_34():
    assert clasificar_temperatura(34) == "caluroso"