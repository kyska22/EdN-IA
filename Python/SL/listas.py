#Usando listas como una matrix

m = [
    [1,2,3],
    [4,5,6]
    ]
    
print(m[1][2]) 

#La salida de este codigo es 6

seats = [
['a', 'b', 'c'],
['d', 'e', 'f'],
['g', 'h', 'i'],
['j', 'k', 'l']
]

x = int(input())
y = int(input())

print(seats[x][y])

#Las cadenas se pueden leer como listas

str = "Hello world!"
print(str[6])

#Las listas también se pueden sumar y multiplicar del mismo modo que las cadenas.
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

"""
Salida
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 1, 2, 3, 1, 2, 3]
"""

"""
Cadenas como listas
Es necesario tomar el nombre y el apellido de una persona como entrada y generar las iniciales (primeras letras del nombre y del apellido).

Ejemplo de entrada
James
Smith

Ejemplo de salida
J.S.
"""

fname = input()
lname = input()
#your code goes here
print(fname[0]+"."+lname[0]+".")

########################################################################
# Para comprobar si un elemento está en una lista determinada, podemos utilizar el operador in.

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

"""
Salida
True
True
False
"""

#Para comprobar si un elemento no está en una lista, puede utilizar el operador not

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

"""
Operaciones de lista
Estás haciendo un sistema de reconocimiento de voz.
Los comandos admitidos se almacenan en una lista.

Completa el programa para tomar un comando como entrada, comprobar si es compatible y generar "OK", si lo es, y "Not supported", si no.

Ejemplo de entrada
Lights Off

Ejemplo de salida
OK
"""
commands = ["Lights Off", "Lock the door", "Open the door", "Make Coffee", "Shut down"]

comand = input()
if comand in commands:
    print("OK")
else:
    print("Not supported")




