from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
    
    pedidios_procesados: List[Dict[str, Union[int, str, float, Dict[str, int]]]] = []
    
    while not pedidos.empty():
        # Inicialización del pedido.
        pedido_actual: Dict[str, Union[int, str, float, Dict[str, int]]] = pedidos.get()
        estado_del_pedido: str = "completo"
        precio_total: float = 0

        for producto, cantidad_comprada in pedido_actual["productos"].items():
            
            if cantidad_comprada <= stock_productos[producto]:  # Hay stock
                precio_total += cantidad_comprada * precios_productos[producto]  # Cobrar
                stock_productos[producto] -= cantidad_comprada  # Descontar del stock
                
            else:  # No hay stock
                precio_total += stock_productos[producto] * precios_productos[producto]  # Cobrar
                pedido_actual["productos"][producto] = stock_productos[producto]  # Cambiar la cantidad de productos que se lleva
                stock_productos[producto] = 0  # Descontar del stock
                estado_del_pedido = "incompleto"

        registro_pedido_actual: Dict[str, Union[int, str, float, Dict[str, int]]] = {
            "id": pedido_actual["id"],
            "cliente": pedido_actual["cliente"] ,
            "productos": pedido_actual["productos"],
            "precio_total": precio_total,
            "estado": estado_del_pedido
          }
        
        pedidios_procesados.append(registro_pedido_actual)
    return pedidios_procesados


if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))

# Ejemplo input  
# pedidos: [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
# stock_productos: {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
# precios_productos: {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}