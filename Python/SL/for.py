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
El código anterior define una variable count que itera sobre la cadena y calcula la cuenta de 't' letras en él. Durante cada iteración, la variable x representa la letra actual de la cadena.

La variable count se incrementa cada vez que la letra 't' es encontrada, por lo que al final del bucle representa el número de 't' letras en la cadena.
"""

"""
Estás haciendo un programa de carrito de la compra.

El carrito de la compra se declara como una lista de precios, 
y hay que añadir una funcionalidad para aplicar un descuento y mostrar el precio total.

Toma el porcentaje de descuento como entrada, calcula y genera el precio total para el carrito de la compra.

Utiliza un bucle for para iterar sobre la lista.
Utiliza la siguiente fórmula para calcular el resultado de X% descuento en $Y precio: Y - (Y*X/100) 

"""

# Carrito de compras representado como una lista de precios
carrito = [10.0, 20.0, 30.0, 40.0, 50.0]  # Puedes modificar los valores según sea necesario

# Solicitar al usuario el porcentaje de descuento
porcentaje_descuento = float(input("Introduce el porcentaje de descuento: "))

# Inicializar el total del carrito
total = 0.0

# Calcular el precio total con descuento
for precio in carrito:
    precio_con_descuento = precio - (precio * porcentaje_descuento / 100)
    total += precio_con_descuento

# Mostrar el precio total
print(f"El precio total con un {porcentaje_descuento}% de descuento es: ${total:.2f}")
