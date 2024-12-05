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

#Un bucle for puede utilizarse para iterar sobre cadenas.

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

########################################################################################
cart = [15, 42, 120, 9, 5, 380]

discount = int(input())
total = 0

for price in cart:
    price_dis = price - (price * discount / 100)
    total += price_dis
    

print(total)
########################################################################################
"""
for vs while
Así que tenemos los bucles for y while, que pueden utilizarse para ejecutar un bloque de código varias veces. Entonces, ¿cuál usamos y cuándo?

Por lo general, utilizamos el bucle for cuando el número de iteraciones es fijo. Por ejemplo, iterar sobre una lista fija de artículos en una lista de la compra.

El bucle while es útil en los casos en que el número de iteraciones no se conoce y depende de algunos cálculos y condiciones en el bloque de código del bucle.

Por ejemplo, terminar el bucle cuando el usuario introduce una entrada específica en un programa de calculadora.

Mientras que ambos, el bucle for y while se puede utilizar para lograr los mismos resultados, sin embargo el bucle for tiene una sintaxis más limpia y corta, por lo que es una mejor opción en la mayoría de los casos.
"""
