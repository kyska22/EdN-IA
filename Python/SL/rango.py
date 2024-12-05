#Por defecto, comienza en 0, se incrementa en 1 y se detiene antes del número especificado.

numbers = list(range(10))
print(numbers)

"""
Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

#Si se llama con dos argumentos, producirá valores del primero al segundo.

numbers = list(range(3, 8))
print(numbers)

"""
OUTPUT
[3, 4, 5, 6, 7]
"""
# También hay un tercer argumento que se puede utilizar con range(), y es realmente útil. Se llama Step(step) y determina el intervalo de la secuencia producida

numbers = list(range(5, 20, 2))
print(numbers)

"""
OUTPUT
[5, 7, 9, 11, 13, 15, 17, 19]
"""

for i in range(5):
    print("hello!")

"""
OUTPUT
hello!
hello!
hello!
hello!
hello!
"""
##############################################################################################################################################################
"""
Un grupo de edificios tiene baños en cada 5º piso.
Por ejemplo, un edificio de 12 plantas tiene baños en las plantas 5ª y 10ª.

Crea un programa que tome el número total de pisos como entrada y dé como resultado los pisos que tienen baños.

Ejemplo de entrada
23

Ejemplo de salida
5
10
15
20
"""
n = int(input())

for i in range(5,n,5):
    print(i)




