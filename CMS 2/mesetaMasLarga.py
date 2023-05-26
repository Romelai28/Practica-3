from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.


def mesetaMasLarga(l: List[int]) -> int:
    # Implementar esta funcion
    lista_cantidad_repeticiones: List[int] = []
    if len(l) < 2:
        return len(l)
    inicio: int = 0
    contador: int = 1
    while inicio < len(l) - 1:
        for i in range(inicio, len(l) - 1):
            inicio += 1
            if l[i] == l[i + 1]:
                contador += 1
            else:
                lista_cantidad_repeticiones.append(contador)
                contador = 1
        lista_cantidad_repeticiones.append(contador)
    return max(lista_cantidad_repeticiones)


if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))