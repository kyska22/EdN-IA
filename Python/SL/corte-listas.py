#El corte de listas más básico consiste en indexar una lista con dos enteros separados por dos puntos. Esto devolverá una nueva lista que contiene todos los valores de la antigua lista entre los índices.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

"""
OUTPUT
[4, 9, 16, 25]
[9, 16, 25, 36, 49]
[0]
"""
#Si se omite el primer número de un corte, se toma como el inicio de la lista.
#Si se omite el segundo número, se considera que es el final.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

>>>
[0, 1, 4, 9, 16, 25, 36]
[49, 64, 81]
>>>




