# EJERCICIO 1:

# Item 1:
# Iterando por elemento en lista con for loop:
def pertenece1(s: list[int], e: int) -> bool:
    for i in s:
        if i == e:
            return True
    return False

# Iterando por indice de los elementos de lista con for loop:
def pertenece2(s: list[int], e: int) -> bool:
    for i in range(len(s)):
        if s[i] == e:
            return True
    return False


# Iterando por indice de los elementos de lista con while loop:
def pertenece3(s: list[int], e: int) -> bool:
    i = 0
    while len(s) >  i:
        print(i)
        if s[i] == e:
            return True
        i += 1
    return False


# Item 2:
def divideATodos(s: list[int], e: int) -> bool:
    # Requiere: e != 0
    for i in s:
        if i % e != 0:
            return False
    return True


# Item 3:
def sumaTotal(s: list[int]) -> int:
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
    return palabra == reverseString(palabra)


def reverseString(l: list) -> str:
    res = ""
    for i in range(len(l)):
        res += l[len(l) - 1 - i]
    return res


# Alternativo:
def es_palindromoBIS(palabra: str) -> bool:
    palabra_invertida = charlist_to_string(reverseList(palabra))
    return palabra == palabra_invertida


# OBS: Si le paso un string, me devuelve una lista de characteres.
def reverseList(l: list) -> list:
    res = []
    for i in range(len(l)):
        res.append(l[len(l) - 1 - i])
    return res


def charlist_to_string(charList: list[str]) -> str:
    res = ""
    for i in charList:
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
        if pertenece1(password, str(i)):
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
        if pertenece1 (palabra, vocal):
            vocales_distintas += 1
            if vocales_distintas == 3:
                return True
    return False


# EJERCICIO 2: