"""
Obtener el nivel de pureza correspondiente en quilates.

Esta es la tabla de pureza que utilizaremos:
24K – 99.9%
22K – 91.7%
20K – 83.3%
18K – 75.0%

Si el porcentaje está entre 75 y 83,3, se considera que el oro es de 18K.
Si está entre 83,3 y 91,7 - entonces es 20K, y así sucesivamente.

Dado el porcentaje como entrada, genera el valor de quilates correspondiente, incluyendo la letra K.

Ejemplo de entrada:
92.4

Ejemplo de salida:
22K
"""
purity = float(input())

if 75.0 <= purity < 83.3:
    print("18K")
elif 83.3 <= purity < 91.7:
    print("20K")
elif 91.7 <= purity < 99.9:
    print("22K")
elif purity >= 99.9:
    print("24K")
else:
  print("Fuera del rango clasificable")
