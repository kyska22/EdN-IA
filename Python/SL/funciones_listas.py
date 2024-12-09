"""
Funciones de lista
Estás analizando un conjunto de datos y necesita eliminar los valores atípicos (los más pequeños y los más grandes. Los datos están almacenados en una lista.

Completa el código para eliminar los elementos más pequeños y más grandes de la lista y obtener la suma de los números restantes.
"""

data = [7, 5, 6.9, 1, 8, 42, 33, 128, 2, 8, 11, 0.4, 1024, 66, 809, 11, 8.9, 1.1, 3.42, 9, 100, 444, 78]

aqui = list(data)
exit = 0

valor_max = max(aqui)
valor_min = min(aqui)

aqui.remove(valor_max)
aqui.remove(valor_min)

i = len(aqui)

for i in aqui:
    exit += i

print(exit)
