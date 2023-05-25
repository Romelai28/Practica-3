import sys


def quienGana(j1: str, j2: str) -> str:
    #Implementar esta funcion
    if gana(j1, j2):
        return "Jugador1"
    elif gana(j2, j1):
        return "Jugador2"
    else:
        return "Empate"


def gana(j1: str, j2: str) -> bool:
    if piedraGanaAtijera(j1, j2) or tijeraGanaAPapel(j1, j2) or papelGanaAPiedra(j1, j2):
        return True
    else:
        return False


def piedraGanaAtijera(j1: str, j2: str) -> bool:
    if j1 == "Piedra" and j2 == "Tijera":
        return True
    else:
        return False


def tijeraGanaAPapel(j1: str, j2: str) -> bool:
    if j1 == "Tijera" and j2 == "Papel":
        return True
    else:
        return False


def papelGanaAPiedra(j1: str, j2: str) -> bool:
    if j1 == "Papel" and j2 == "Piedra":
        return True
    else:
        return False


# Tests #
# print("\nj1: Piedra")
# print(quienGana("Piedra", "Piedra"))
# print(quienGana("Piedra", "Papel"))
# print(quienGana("Piedra", "Tijera"))
#
# print("\nj1: Papel")
# print(quienGana("Papel", "Piedra"))
# print(quienGana("Papel", "Papel"))
# print(quienGana("Papel", "Tijera"))
#
# print("\nj1: Tijera")
# print(quienGana("Tijera", "Piedra"))
# print(quienGana("Tijera", "Papel"))
# print(quienGana("Tijera", "Tijera"))


if __name__ == '__main__':
  x = input()
  jug = str.split(x)
  print(quienGana(jug[0], jug[1]))