import pytest
from solucion import parsear_linea_http


@pytest.mark.parametrize("entrada, esperado", [
    ("GET / HTTP/1.1", ("GET", "/")),
    ("POST /crear HTTP/1.1", ("POST", "/crear")),
    ("PUT /actualizar?brillo=50 HTTP/1.1", ("PUT", "/actualizar")),
    ("delete /eliminar HTTP/1.1", ("DELETE", "/eliminar")),
    ("PATCH /ACTUALIZAR HTTP/1.1", ("PATCH", "/ACTUALIZAR")),
])
def test_casos_felices(entrada, esperado):
    assert parsear_linea_http(entrada) == esperado

@pytest.mark.parametrize("entrada", [
    ("/put crear http/1.1"),
    ("get"),
    ("/crear"),
    ("GET /actualizar HTTP/1.1 algo"),
])
def test_casos_value_error(entrada):
    with pytest.raises(ValueError):
        parsear_linea_http(entrada)

@pytest.mark.parametrize("entrada", [
    (123),
])
def test_casos_type_error(entrada):
    with pytest.raises(TypeError):
        parsear_linea_http(entrada)