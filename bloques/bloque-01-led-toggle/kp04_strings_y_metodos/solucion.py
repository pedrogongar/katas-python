def parsear_linea_http(linea: str) -> tuple[str, str]:
    if type(linea) is not str:
        raise TypeError("La entrada debe ser un string")

    metodos = ["GET", "POST", "PUT", "DELETE", "PATCH"]

    sin_query_string = linea.strip().split("?", 1)
    linea_formateada = sin_query_string[0].split(" ")

    if len(linea_formateada) < 2 or len(linea_formateada) > 3:
        raise ValueError("La entrada debe estar formada por MÉTODO RUTA VERSIÓN")

    metodo = linea_formateada[0].upper()
    ruta = linea_formateada[1]

    if metodo not in metodos or not ruta.startswith("/"):
        raise ValueError("La entrada está mal formada")

    return metodo, ruta




    