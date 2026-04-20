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