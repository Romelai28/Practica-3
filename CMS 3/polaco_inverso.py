from queue import LifoQueue


# para el tipo pila de enteros, usar: "pila: LifoQueue". La notación "pila: LifoQueue[float]" no funciona.
def calcular_expresion(expr: str) -> float:
    # implementar función con el TAD Pila
    pila = LifoQueue()

    operadores = ["*", "+", "/", "-"]

    expresion_split = expr.split()
    for i in expresion_split:
       
       if i not in operadores:
        pila.put(i)

       else:
          a = pila.get()
          b = pila.get()

          if i == "*":
             pila.put(float(b) * float(a))
          elif i == "+":
             pila.put(float(b) + float(a))
          elif i == "/":
             pila.put(float(b) / float(a))
          else:
             pila.put(float(b) - float(a))

    return pila.get()

    
if __name__ == '__main__':
  x = input() # Por ejemplo: 2 5 * 7 +
  print(round(calcular_expresion(x), 5))