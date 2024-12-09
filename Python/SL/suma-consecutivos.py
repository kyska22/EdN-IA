"""
Suma de números consecutivos
A nadie le gustan los deberes, pero tu profesor de matemáticas te ha encomendado encontrar la suma de los primeros N números.

Ahorremos tiempo creando un programa que haga el cálculo por ti.

Toma un número N como entrada y genera la suma de todos los números del 1 al N (incluyendo N).

Ejemplo de entrada
100

Ejemplo de salida
5050

Explicación: La suma de todos los números del 1 al 100 es igual a 5050.
"""
N = int(input())
Salida = 0

while N >= 0:
    Salida += N
    N -= 1

print (Salida)



