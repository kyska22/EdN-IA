# Breack detiene el bucle
i = 0
while 1==1:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break

print("Finished")

############################################################################
# Continue hace que vaya a la siguiente iteración
i = 0
while i<5:
  i += 1
  if i==3:
    print("Skipping 3")
    continue
  print(i)
##############################################################################
""""
Estás haciendo un sistema de entradas.
El precio de la entrada individual es de 100 dólares.
Pero para los niños menores de 3 años, la entrada es gratuita.

Tu programa necesita tomar las edades de 5 pasajeros como entrada y generar el precio total de tus entradas.

Ejemplo de entrada
18
24
2
5
42

Ejemplo de salida
400
""""
total = 0
i = 0

while i <= 4:
    edad = int(input())
    if edad > 3:
        total += 100
    i += 1
print(total)
