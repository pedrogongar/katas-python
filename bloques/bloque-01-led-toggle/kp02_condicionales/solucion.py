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