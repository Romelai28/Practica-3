from typing import List
from typing import Dict
import json

def unir_diccionarios(a_unir: List[Dict[str,str]]) -> Dict[str,List[str]]:
    # Implementar esta funcion
    res = {}
    for diccionario in a_unir:
        for k,v in diccionario.items():
            if k in res:
                res[k].append(v)
            else:
                res[k] = [v]
    return res


if __name__ == '__main__':
  x = json.loads(input()) # Ejemplo de input: [{"a":2},{"b":3,"a":1}]
  print(unir_diccionarios(x))