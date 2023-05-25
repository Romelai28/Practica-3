import math

# EJERCICIO 1:


def raiz_de_2() -> float:
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


def imprimir_saludo(nombre: str):
    print("Hola " + nombre)


def raiz_cuadrada_de(numero: int) -> float:
    return math.sqrt(numero)


def imprimir_dos_veces(estribillo: str):
    print((estribillo + " ") * 2)


def es_multiplo_de(n: int, m: int) -> bool:
    return (n % m) == 0


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
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


# EJERCICIO 4:

def peso_pino(altura: int) -> int:
    # Altura dada en metros. Peso dado en kg.
    altura = altura * 100  # metros -> centimetros
    peso: int = min(altura, 300) * 3 + max(0, altura - 300) * 2
    return peso


def es_peso_util(peso: int) -> bool:
    return 400 <= peso <= 1000


def sirve_pino(altura: int) -> bool:
    # Altura dada en metros. Peso dado en kg.
    return es_peso_util(peso_pino(altura))

# EJERCICIO 5:


def devolver_el_doble_si_es_par(n: int) -> int:
    if es_par(n):
        return n * 2


def devolver_valor_si_es_par_sino_el_que_sigue(n: int) -> int:
    if es_par(n):
        return n
    else:
        return n + 1


def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n: int) -> int:
    if es_multiplo_de(n, 9):
        return n * 3
    elif es_multiplo_de(n, 3):
        return n * 2
    else:
        return n


def es_nombre_largo(nombre: str) -> str:
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"


def agarra_la_pala(sexo: str, edad: int) -> str:
    if (sexo == "F" and edad >= 60) or (sexo == "M" and edad >= 65) or (edad < 18):
        return "Andá de vacaciones"
    else:
        return "Te toca trabajar"

# EJERCICIO 6:


def ej6_contar_hasta_10():
    contador: int = 1
    while contador <= 10:
        print(contador)
        contador += 1


def ej6_contar_pares_de_10_hasta_40():
    contador: int = 10
    while contador <= 40:
        print(contador)
        contador += 2


def ej6_eco():
    contador: int = 0
    while contador < 10:
        contador += 1
        print("eco")


def ej6_cuenta_regresiva(n: int):
    while n >= 1:
        print(n)
        n = n-1
    print("Despegue")


def ej6_viaje_tiempo(year_partida: int, year_llegada: int):
    # Requiere (year_llegada < year_partida)
    year_actual = year_partida
    while year_llegada < year_actual:
        year_actual -= 1
        print(f"“Viajó un año al pasado, estamos en el año: {year_actual}")


def ej6_viaje_tiempo_aristoteles(year_partida: int):
    # Requiere (year_llegada < year_partida)
    # OBS: Año más cercano que sea más lejano a -384 es +-10
    year_actual = year_partida
    while -384 + 10 < year_actual:
        year_actual -= 20
        print(f"“Viajó un año al pasado, estamos en el año: {year_actual}")


# Alternativa:
def ej6_viaje_tiempo_aristoteles_BIS(year_partida: int):
    # Requiere (year_llegada < year_partida)
    # OBS: Año más cercano que sea más lejano a -384 es +-10
    year_actual = year_partida
    while abs(-384 - year_actual) >= 10:
        year_actual -= 20
        print(f"“Viajó un año al pasado, estamos en el año: {year_actual}")


# EJERCICIO 7:

def contar_hasta_10():
    for i in range(1, 11):
        print(i)


def contar_pares_de_10_hasta_40():
    for i in range(10, 41, 2):
        print(i)


def eco():
    for i in range(0, 10):
        print("eco")


def cuenta_regresiva(n: int):
    for i in range(n, 0, -1):
        print(i)
    print("Despegue")


def viaje_tiempo(year_partida: int, year_llegada: int):
    # Requiere (year_llegada < year_partida)
    for i in range(year_partida, year_llegada, -1):
        print(f"“Viajó un año al pasado, estamos en el año: {i - 1}")


def viaje_tiempo_aristoteles(year_partida: int):
    # Requiere (year_llegada < year_partida)
    # OBS: Año más cercano que sea más lejano a -384 es +-10
    for i in range(year_partida, -384 + 10, -20):
        print(f"“Viajó un año al pasado, estamos en el año: {i - 20}")
