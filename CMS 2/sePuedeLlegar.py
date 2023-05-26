from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.


def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int:
    # definir esta función
    ciudad_actual = origen
    contador_de_viajes: int = 0
    while ciudad_actual != destino:
        contador_de_viajes_antiguo = contador_de_viajes
        for i in range(len(vuelos)):
            if ciudad_actual == vuelos[i][0] and vuelos[i][0] != vuelos[i][1]:
                ciudad_actual = vuelos[i][1]  # Hacer el viaje
                contador_de_viajes += 1
                break
        if contador_de_viajes == contador_de_viajes_antiguo:  # Significa que no pudo hacer ningún viaje, fin del camino
            return -1
    return contador_de_viajes


if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))