"""
Cuando sales a comer fuera, siempre dejas el 20% del importe de la cuenta. 
Pero, ¿quién tiene tiempo para calcular la cantidad correcta de propina cada vez? 
Seguro que tú no. Haz un programa para calcular las propinas y ahorrar algo de tiempo.

Tu programa tiene que tomar el importe de la factura como entrada y emitir la propina como float.

Ejemplo de entrada
50

Ejemplo de salida
10.0
"""
bill = int(input())
tips=bill*20/100

print (tips)
