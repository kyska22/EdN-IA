def print_with_exclamation(word):
   print(word + "!")
    
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

"""
OUTPUT
spam!
eggs!
python!
"""

def print_sum_twice(x, y):
   print(x + y)
   print(x + y)

print_sum_twice(5, 8)

"""
Convertidor de pies a pulgadas
Necesitas hacer una función que convierta un valor de pies a pulgadas.

1 pie tiene 12 pulgadas.

Define una función convert() que tome el valor de los pies como argumento y produzca el valor de las pulgadas.
"""

feet = int(input())

def convert(feet):
    pulgadas = 12 * feet
    print (pulgadas)

convert(feet)

#Retorno de las funciones

def max(x, y):
    if x >=y:
        return x
    else:
        return y
        
print(max(4, 7))
z = max(8, 5)
print(z)

"""
OUTPUT
7
8
"""

"""
Recuento de letras
Escribe una función que tome una cadena y una letra como argumentos y devuelva la cuenta de la letra en la cadena.

Ejemplo de entrada
hello, how are you?
o

Ejemplo de salida
3

Explicación: La letra o aparece 3 veces en el texto dado.
"""

def letter_count(text, letter):
    #tu código va aquí
    exit = text.count(letter)
    return exit


text = input()
letter = input()

print(letter_count(text, letter))
