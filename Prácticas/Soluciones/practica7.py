import math

# EJERCICIO 1:

def raizDe2() -> float:
    return round(math.sqrt(2), 4)

def imprimir_hola():
    print("hola")

def imprimir_un_verso():
    print("A lake with no fish\nIs the heart of a horse\nNamed Cold Air")

def factorial_de_dos() -> int:
    return math.factorial(2)

def factorial_3() -> int:
    return math.factorial(3)

def factorial_4() -> int:
    return math.factorial(4)

def factorial_5() -> int:
    return math.factorial(5)

# EJERCICIO 2:

def  imprimir_saludo(nombre: str):
    print("Hola " + nombre)

def raiz_cuadrada_de(numero: int) -> float:
    return math.sqrt(numero)

def imprimir_dos_veces(estribillo: str):
    print((estribillo + " " )* 2)

def es_multiplo_de(n: int, m: int) -> bool:
    return ((n % m) == 0)

def es_par(n: int) -> bool:
    return es_multiplo_de(n, 2)

def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    # Me devuelve pizzas
    porciones: int = comensales * min_cant_de_porciones
    return math.ceil(porciones / 8)

# EJERCICIO 3:

def alguno_es_0(n1: float, n2: float) -> bool:
    return n1 == 0 or n2 == 0

def ambos_son_0(n1: float, n2: float) -> bool:
    return n1 == 0 and n2 == 0

def problema_es_nombre_largo(nombre: str) -> bool:
    return 3 <= len(nombre) <= 8

def es_bisiesto(year: int) -> bool:
    return ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))

print(es_bisiesto(2500))