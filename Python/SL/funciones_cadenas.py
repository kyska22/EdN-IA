#format()  permite incrustar valores en la cadena, utilizando marcadores de posición.

nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

#OUTPUT => Numbers: 4 5 6

print("{0}{1}{0}".format("abra", "cad"))

#OUTPUT => abracadabra

a = "{x}, {y}".format(x=5, y=12)
print(a)

#OUTPUT => 5, 12

"""
Funciones de cadenas

join - une una lista de cadenas con otra cadena como separador.

replace - sustituye una subcadena de una cadena por otra.

startswith y endswith - determinan si hay una subcadena al principio y al final de una cadena, respectivamente.
lower y upper – cambia el caso de una cadena

split – lo contrario de join, convierte una cadena con un determinado separador en una lista.
"""
print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

"""
Tu amigo te está enviando un mensaje de texto, pero su bloqueo de mayúsculas está roto y todo el mensaje está en mayúsculas.
A nadie le gusta que le griten, y además el texto en mayúsculas es difícil de leer, así que decides escribir un programa que convierta el texto en minúsculas y lo genere.

Toma una cadena como entrada y genérala en minúsculas.
"""

text = input()

exit = text.lower()
print (exit)

