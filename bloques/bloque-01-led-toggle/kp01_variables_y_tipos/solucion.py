def calcular_coste_electricidad(
    consumo_wh: int | float, tarifa_eur_kwh: int | float
) -> int | float:
    if consumo_wh < 0 or tarifa_eur_kwh < 0:
        raise ValueError("El input debe ser >= 0")

    consumo_kwh = consumo_wh / 1000
    return tarifa_eur_kwh * consumo_kwh
