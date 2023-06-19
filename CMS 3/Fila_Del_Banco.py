from queue import Queue

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
def avanzarFila(fila: Queue, min: int):
    #implementar función
    n: int = longitud_cola(fila)
    minuto_de_entrada: int = -10 # Valor absurdo de inicialización

    for minuto in range(min + 1):
        
        # Caja 1:
        if not fila.empty():
            if minuto % 10 == 1:
                fila.get()

        # Caja 2:
        if not fila.empty():
            if minuto % 4 == 3:
                fila.get()

        # Caja 3:
        if not fila.empty():
            if minuto % 4 == 2:
                minuto_de_entrada = minuto
                persona_a_volver: int = fila.get()
          
        # Regreso de la persona de caja 3:
        if minuto == minuto_de_entrada + 3:
            fila.put(persona_a_volver)
    
        # Nueva persona:
        if minuto % 4 == 0:
            n += 1
            fila.put(n)

    return fila


def cola_a_lista(cola):
    lista_elem: list = []
    while not cola.empty():
        elem = cola.get()
        lista_elem.append(elem)
    for e in lista_elem:
        cola.put(e)
    return lista_elem


def lista_a_cola(lista):
    cola: Queue = Queue()
    for e in lista:
        cola.put(e)
    return cola


def longitud_cola(cola: Queue):
    lista: list = cola_a_lista(cola)
    res: int = len(lista)
    cola = lista_a_cola(lista)
    return res


# Testing
#print(cola_a_lista(avanzarFila(lista_a_cola([1,2,3]), 100)))


if __name__ == '__main__':
  fila: Queue = Queue()
  fila_inicial: int = int(input())
  for numero in range(1, fila_inicial+1):
    fila.put(numero)
  min: int = int(input())
  avanzarFila(fila, min)
  res = []
  for i in range(0, fila.qsize()):
    res.append(fila.get())
  print(res)


# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)

