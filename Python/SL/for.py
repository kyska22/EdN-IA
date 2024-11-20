#El bucle for se utiliza para iterar sobre una secuencia dada, como listas o cadenas.

words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

""""
hello!
world!
spam!
eggs!
"""
str = "testing for loops"
count = 0

for x in str:
   if(x == 't'):
    count += 1

print(count)

"""
Estás haciendo un programa de carrito de la compra.

El carrito de la compra se declara como una lista de precios, 
y hay que añadir una funcionalidad para aplicar un descuento y mostrar el precio total.

Toma el porcentaje de descuento como entrada, calcula y genera el precio total para el carrito de la compra.

Utiliza un bucle for para iterar sobre la lista.
Utiliza la siguiente fórmula para calcular el resultado de X% descuento en $Y precio: Y - (Y*X/100) 

"""
