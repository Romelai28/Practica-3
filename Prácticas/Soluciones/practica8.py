# EJERCICIO 1:

# Item 1:
# Iterando por elemento en lista con for loop:
def pertenece(s: list, e) -> bool:
    for i in s:
        if i == e:
            return True
    return False


# Iterando por indice de los elementos de lista con for loop:
def pertenece2(s: list, e) -> bool:
    for i in range(len(s)):
        if s[i] == e:
            return True
    return False


# Iterando por indice de los elementos de lista con while loop:
def pertenece3(s: list, e) -> bool:
    i = 0
    while len(s) > i:
        print(i)
        if s[i] == e:
            return True
        i += 1
    return False


# Item 2:
def divide_a_todos(s: list[int], e: int) -> bool:
    # Requiere: e != 0
    for i in s:
        if i % e != 0:
            return False
    return True


# Item 3:
def suma_total(s: list[int]) -> int:
    res: int = 0
    for i in s:
        res += i
    return res


# Item 4:
def ordenados(s: list[int]) -> bool:
    for i in range(len(s)-1):
        if s[i] >= s[i+1]:  # No se cumple que s[i] < s[i+1]
            return False
    return True


# Item 5:
def es_palabra_larga(palabra: str) -> bool:
    if len(palabra) > 7:
        return True
    else:
        return False


# Item 6:
def es_palindromo(palabra: str) -> bool:
    return palabra == reverse_string(palabra)


def reverse_string(texto: str) -> str:
    res = ""
    for i in range(len(texto)):
        res += texto[len(texto) - 1 - i]
    return res


# Alternativo:
def es_palindromoBIS(palabra: str) -> bool:
    palabra_invertida = charlist_to_string(reverse_list(palabra))
    return palabra == palabra_invertida


# OBS: Si le paso un string, me devuelve una lista de characters.
def reverse_list(lista: list) -> list:
    res = []
    for i in range(len(lista)):
        res.append(lista[len(lista) - 1 - i])
    return res


def charlist_to_string(char_list: list[str]) -> str:
    res = ""
    for i in char_list:
        res += i
    return res


# Item 7:
def analisis_password(password: str) -> str:
    if len(password) > 8 and tiene_numero(password) and tiene_mayuscula(password) and tiene_minuscula(password):
        return "VERDE"
    elif len(password) < 5:
        return "AMARILLO"
    else:
        return "ROJO"
    

def tiene_numero(password: str) -> bool:
    for i in range(0, 10):
        if pertenece(password, str(i)):
            return True
    return False


def tiene_mayuscula(password: str) -> bool:
    for letra in password:
        if "A" <= letra <= "Z":
            return True
    return False


def tiene_minuscula(password: str) -> bool:
    for letra in password:
        if "a" <= letra <= "z":
            return True
    return False


# Item 8:
def banco(registro: list[tuple]) -> int:
    res: int = 0
    for tupla in registro:
        if tupla[0] == "I":
            res += tupla[1]
        else:  # tupla[0] == "R"
            res -= tupla[1]
    return res


# Item 9:
def tiene_3_vocales_distintas(palabra: str) -> bool:
    vocales: list[str] = ['a', 'e', 'i', 'o', 'u']
    vocales_distintas: int = 0
    for vocal in vocales:
        if pertenece(palabra, vocal):
            vocales_distintas += 1
            if vocales_distintas == 3:
                return True
    return False


# EJERCICIO 2:


# Item 1:
def cerosEnPosParInOut(l:list[float]):
    # l inout
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = 0

# asd = [1,2,3,4,5,6]
# print(asd)
# cerosEnPosParInOut(asd)
# print(asd)


# Item 2:
def cerosEnPosParIn(l:list[float]):
    # l in
    y: list[float] = l.copy()
    for i in range(len(y)):
        if i % 2 == 0:
            y[i] = 0
    return y

# asd = [1,2,3,4,5,6]
# print(asd)
# cerosEnPosParIn(asd)
# print(cerosEnPosParIn(asd))
# print(asd)


# Item 3:
def sacarVocales(textoOriginal: str) -> str:
    # textoOriginal in
    textoRes: str = ""
    vocales: list[str] = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letra in textoOriginal:
        if not (letra in vocales):
            textoRes += letra
    return textoRes


# Item 4:
def remplazaVocales(s: str) -> str:
    # s in
    vocales: list = ["a", "e", "i", "o", "u"]  # La especificación solo habla de minusculas.
    res: str = ""
    for letra in s:
        if not (letra in vocales):
            res += letra
        else:
            res += " "
    return res


# Item 5:
# OBS: Ya lo había hecho en el ejercicio 1 item 6
def daVueltaStr(s: str) -> str:
    # s in
    res = ""
    for i in range(len(s)):
        res += s[len(s) - 1 - i]
    return res


# EJERCICIO 3:


# Item 1:
def estudiantes():
    res: list[str] =  []
    condicion: bool = True
    while condicion:
        nombre: str = ""  # Limpiar
        nombre = input("'listo' para salir. Ingrese nombre del estudiante: ")
        if nombre == "listo":
            condicion = False
        else:
            res.append(nombre)
    return res


# Item 2:
def historialSube():
    res: list[(str, int)] = []
    operacion: str = ""
    while operacion != "X":
        operacion = input("Ingrese operación: ")
        if operacion == "C" or operacion == "D":
            monto: int = input("Ingrese monto de la operación: ")
            res.append((operacion, monto))
    return res


# Item 3:
import random


def juego():
    historial: list[int] = []
    seguirJugando: bool = True
    while seguirJugando:
        decision = input ("Desea otra carta? ('Si'/'No'): ")
        if decision == "Si":
            historial.append(repartir())
            if sumaMano(historial) > 7.5:
                seguirJugando = False
        else:
            seguirJugando = False
        # print(historial)
    return historial


def repartir() -> int:
    cartas: list[int] = [1,2,3,4,5,6,7,10,11,12]
    return random.choice(cartas)

def sumaMano(cartas: list[int]) -> int:
    # cartas in
    res: int = 0
    for carta in cartas:
        if carta < 8:
            res += carta
        else:
            res += 0.5
    return res


# EJERCICIO 4:


# Item 1:
def perteneceACadaUno(s:list[list[int]], e: int, res: list[bool]):
    # s in
    # e in
    # res out
    res.clear()  # Limpiar res pero no pierde referencia con la lista parametro.
    for fila in s:
        if pertenece(fila, e):
            res.append(True)
        else:
            res.append(False)


# asd = [False, False, False]
# perteneceACadaUno([[1,2,3],[2,3,4],[3,4,5]], 2, asd)
# print(asd)


# Item 2:
def esMatriz(s: list[list[int]]):
    # s in
    if len(s) == 0 or len(s[0]) == 0:
        return False
    for fila in s:
        if len(fila) != len(s[0]):
            return False
    return True


# Item 3:
def filasOrdenadas(m: list[list[int]]) -> list[bool]:
    # m in; res out
    res: list [bool] = []
    for fila in m:
        res.append(ordenados(fila))
    return res


# print(filasOrdenadas([[1,2,3],[3,2,1],[1,2,2]]))


# Item 4:
import numpy as np


def crearMatrizDeCerosCuadrada(d: int) -> list[list[int]]:
    res: list[list[int]] = []
    for i in range(d):
        res.append([])
        for j in range(d):
            res[i].append(0)
    return res


def multiplicarMatrices(d: int, p:int) -> list[list[float]]:  # La especificación decia que p sea un float pero no tiene sentido.
    matriz = np.random.random((d, d))  # OBS: Es matriz cuadrada.
    res = crearMatrizDeCerosCuadrada(d)
    for potencia in range(p):
        for fila in range(len(matriz)):
            for elemento in range(len(matriz[0])):
                for n in range(d):
                    res[fila][elemento] += matriz[fila][n] * matriz[n][elemento]
    return res
