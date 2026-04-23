# kp04 — strings_y_metodos

Tipo: simple · Bloque: 1 (proyecto 01 LED toggle) · Dificultad: ★★

## Enunciado

Dada una línea de petición HTTP como string (por ejemplo, `"GET /on HTTP/1.1"`), extraer el método HTTP y la ruta, y devolverlos como tupla `(metodo, ruta)`. La función recibe un parámetro `linea` y devuelve una tupla de dos strings.

Este es el kata más directamente relevante del bloque para el proyecto ESP32: en MicroPython se parsea a mano la primera línea de cada petición HTTP, exactamente lo que aquí se manipula.

## Descomposición

Una petición HTTP comienza con una línea de formato `METODO RUTA VERSION`, separados por espacios. La función debe extraer el método y la ruta, ignorando la versión. Cuatro decisiones de diseño guían la implementación.

Primero, sobre permisividad: los servidores reales aceptan variaciones como espacios extra al inicio/final o métodos en minúsculas, así que la función también los acepta. El método se normaliza a mayúsculas; la ruta se devuelve tal cual (las rutas son case-sensitive en HTTP por estándar).

Segundo, sobre query strings: si la ruta incluye `?` seguido de parámetros (`/on?brillo=50`), solo se devuelve la ruta (`/on`), descartando la parte de query. Es lo que el proyecto 1 necesita.

Tercero, sobre validación: el método debe estar en una lista de métodos HTTP válidos (`GET`, `POST`, `PUT`, `DELETE`, `PATCH`), y la ruta debe empezar por `/`. Cualquier otra entrada malformada (estructura con tokens insuficientes o sobrantes, métodos no reconocidos, rutas sin barra inicial) lanza `ValueError`.

Cuarto, sobre tipos: si el argumento no es un `str`, lanza `TypeError`.

Los casos límite cubren casos felices con distintos métodos y rutas, la extracción correcta de query strings, la permisividad con minúsculas, y múltiples variantes de entradas malformadas.

## Solución

```python
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
```

El orden de operaciones es clave. Primero se valida el tipo, después se aplica la normalización mínima (`strip` para espacios extremos). La separación por `?` se hace antes del split por espacios para que la parte descartada de la query no pueda confundirse con un token adicional. El split por espacio da como resultado una lista de 2 o 3 tokens (2 si falta la versión, 3 si está completa).

La validación estructural comprueba que el número de tokens sea razonable. Después se extraen método (normalizado a mayúsculas) y ruta. Finalmente se valida semántica: método en la lista permitida, ruta empezando por `/`. Solo si todo pasa, se devuelve la tupla.

## Discusión

El kata es el primero del bloque donde la fluidez con la API estándar de Python (específicamente, los métodos de `str`) marca realmente la diferencia. `strip`, `split`, `upper`, `startswith`, `in` sobre listas: todos aparecen aquí en secuencia y cada uno hace su parte.

Una observación interesante es cómo `split("?", 1)` resuelve limpiamente un caso que parecería complicado. Si la línea tiene query string, devuelve dos elementos y nos quedamos con el primero. Si no la tiene, devuelve un solo elemento y nos quedamos con ese mismo. Indexar `[0]` funciona en ambos casos sin necesidad de un condicional. Es el patrón de "los casos especiales se resuelven solos cuando el algoritmo base es correcto", recurrente en katas anteriores.

Otra decisión defendible sería ser más estricto con la versión HTTP (validar que sea `HTTP/1.0` o `HTTP/1.1`) o más permisivo con los métodos (aceptar cualquiera sin lista blanca). La elección aquí prioriza validar lo que importa para el proyecto 1 (que el método sea conocido y la ruta parseable) sin complicar la función con validaciones que no aportan.

## Qué aprendí

- **`str.split(sep, maxsplit)`**: divide un string por un separador. El segundo argumento limita el número máximo de divisiones. `"a?b?c".split("?", 1)` devuelve `["a", "b?c"]`. Útil para separar la ruta de la query string en una sola llamada. Documentación: [str.split](https://docs.python.org/3/library/stdtypes.html#str.split).
- **`str.strip()`**: elimina espacios en blanco al inicio y al final de un string. Forma canónica de normalizar entrada permisiva. Documentación: [str.strip](https://docs.python.org/3/library/stdtypes.html#str.strip).
- **`str.startswith(prefijo)`**: devuelve `True` si el string empieza por el prefijo dado. Documentación: [str.startswith](https://docs.python.org/3/library/stdtypes.html#str.startswith).
- **Operador `in` sobre listas**: `x in lista` es la forma idiomática de comprobar pertenencia. Sustituye a `lista.__contains__(x)`, que funciona pero no se usa en Python moderno.
- **`tuple[str, str]` como type hint**: en Python 3.9+ se pueden anotar tuplas con tipos de cada elemento. `tuple[str, str]` indica una tupla de exactamente dos strings.
- **Patrón de split con `[0]` para casos con y sin separador**: cuando un split puede devolver 1 o 2 elementos, quedarse con el primero cubre ambos casos sin condicional.