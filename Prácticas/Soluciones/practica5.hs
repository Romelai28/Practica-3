{- Notas varias: (Después borrar)

lista ++ lista concatenar.
elemento : lista agregar.

ultimo x | (longitud x) == 1 = head x -- primera alternativa para hablar de una lista con un solo elemento. Sin patter matching
que la lista sólo tiene un solo elemento se puede escribir con patter matching con:
ultimo [x] = ...

patter matching (x:y:xs) x primer elemento, y segundo elemento, xs la lista del resto de elementos. -}



-- EJERCICIO 1 --

    -- ITEM 1 --

longitud :: [t] -> Integer
-- Requiere: True
longitud [] = 0
longitud (x:xs) = (longitud xs) + 1


    -- ITEM 2 --

ultimo :: [t] -> t
-- Requiere: Lista no vacía.
ultimo [a] = a
ultimo (x:xs) = ultimo xs


    -- ITEM 3 --

principio :: [t] -> [t]
-- Requiere: Lista no vacía.
-- Devuelve una lista con todos los elementos menos el último.
principio [a] = []
principio (x:xs) = x : (principio xs)


    -- ITEM 4--

reverso :: [t] -> [t]
-- Requiere: True
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]


-- EJERCICIO 2 --

    -- ITEM 1 --

pertenece :: (Eq t) => t -> [t] -> Bool
-- Requiere: True
pertenece _ [] = False
pertenece e (x:xs) = if e == x then True else pertenece e xs
-- Alternativa: pertenece e (x:xs) = e == x || pertenece e xs


    -- ITEM 2 --

todosIguales :: (Eq t) => [t] -> Bool
-- Requiere: True
todosIguales [] = True
todosIguales (x:xs) = (x == ultimo (x:xs)) && (todosIguales xs)


    -- ITEM 3 --

todosDistintos :: (Eq t) => [t] -> Bool
-- Requiere: True
todosDistintos [] = True
todosDistintos (x:xs) = (not (pertenece x xs)) && (todosDistintos xs)


    -- ITEM 4 --

hayRepetidos :: (Eq t) => [t] -> Bool
-- Requiere: True
hayRepetidos [] = False
hayRepetidos (x:xs) = (pertenece x xs) || (hayRepetidos xs)


    -- ITEM 5 --

quitar :: (Eq t) => t -> [t] -> [t]
-- Requiere: True
-- Elimina, de existir, la primera (solamente) aparición del elemento e.
quitar _ [] = []
quitar e (x:xs) = if e == x then xs else (x) : (quitar e xs)


    -- ITEM 6 --

quitarTodos :: (Eq t) => t -> [t] -> [t]
-- Requiere: True
quitarTodos _ [] = []
quitarTodos e (x:xs) = if e == x then (quitarTodos e xs) else (x) : (quitarTodos e xs)
-- Alternativa usando "quitar": quitarTodos e (x:xs) = if pertenece e (x:xs) then (quitarTodos (e) (quitar (e) (x:xs))) else (x:xs)


    -- ITEM 7 --

eliminarRepetidos :: (Eq t) => [t] -> [t]
-- Requiere: True
eliminarRepetidos s | todosDistintos s = s  
eliminarRepetidos (x:xs) = (x) : (if pertenece x xs then (eliminarRepetidos (quitarTodos x xs)) else (eliminarRepetidos xs))


    -- ITEM 8 --

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
-- Requiere: True
mismosElementos s r = (esContenido s r) && (esContenido r s)

{- Otra opción, desconozco cual es mejor.
mismosElementos s r = (esContenido a b) && (esContenido b a)
    where a = eliminarRepetidos s
          b = eliminarRepetidos r -}


esContenido :: (Eq t) => [t] -> [t] -> Bool
-- Requiere: True
-- Quiero ver que a contenido en b. o sea cada elemento de a esta también en b.
esContenido [] b = True
esContenido (x:xs) b = if pertenece x b then esContenido xs b else False


    -- ITEM 9 --

capicua :: (Eq t) => [t] -> Bool
capicua s = s == reverso s


-- EJERCICIO 3 --

    -- ITEM 1 --

sumatoria :: [Integer] -> Integer
-- Requiere: True
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs


    -- ITEM 2 --

productoria :: [Integer] -> Integer
-- Requiere: True
productoria [] = 1
productoria (x:xs) = x * productoria xs


    -- ITEM 3 --

-- maximo :: [Integer] -> Integer