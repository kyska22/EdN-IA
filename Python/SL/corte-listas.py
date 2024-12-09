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

#Al igual que con los rangos, tus cortes de lista pueden incluir un tercer número, 
#que representa el paso, para incluir sólo valores alternativos en el corte. Así:

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])


"""
Resultado:
>>>
[0, 4, 16, 36, 64]
[4, 25]
>>>
"""

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

"""
Resultado:
>>>
[1, 4, 9, 16, 25, 36, 49, 64]
>>>
"""

"""
Corte de listas
Invertir una cadena es una tarea habitual durante las entrevistas de programación.

Dada una cadena de caracteres como entrada, genera su reverso.

Ejemplo de entrada
hello world

Ejemplo de salida
dlrow olleh
"""

string = input()
reverse_string = string[::-1]

print(reverse_string)

"""
Para generar el reverso de una cadena de caracteres en Python usando listas, podemos seguir estos pasos:

Convertir la cadena en una lista de caracteres.
Invertir la lista.
Unir la lista invertida para obtener la cadena reversa.
Aquí te dejo un ejemplo de cómo hacerlo:

python
Copy code
# Función para invertir una cadena usando listas
def invertir_cadena(cadena):
    # Convertimos la cadena en una lista de caracteres
    lista_caracteres = list(cadena)
    
    # Invertimos la lista
    lista_invertida = lista_caracteres[::-1]
    
    # Unimos la lista invertida para formar la cadena de salida
    cadena_reversa = ''.join(lista_invertida)
    
    return cadena_reversa

# Ejemplo de uso
entrada = "hello world"
salida = invertir_cadena(entrada)
print(salida)
Explicación:
list(cadena) convierte la cadena en una lista de caracteres.
[::-1] es una forma en Python de invertir una lista.
''.join(lista_invertida) une los caracteres de la lista invertida en una nueva cadena.
Resultado:
Para la entrada "hello world", la salida será:

Copy code
dlrow olleh
"""
