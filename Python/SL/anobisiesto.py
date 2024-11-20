"""
Necesitas hacer un programa que tome un año como entrada y genere "Leap year"si es un año bisiesto, y "Not a leap year", si no es así.

Para saber si un año es bisiesto o no, hay que comprobar lo siguiente:
1) Si el año es divisible en partes iguales por 4, ve al paso 2. En caso contrario, el año NO es bisiesto.
2) Si el año es divisible por 100, ve al paso 3. En caso contrario, el año es bisiesto.
3) Si el año es divisible por 400, el año es bisiesto. En caso contrario, no es bisiesto.

Ejemplo de entrada
2000

Ejemplo de salida
Leap year

Usa el operador % modulo para comprobar si el año es divisible en partes iguales por un número.
"""

year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")  # Ano bissexto
        else:
            print("Not a leap year")  # Não é um ano bissexto
    else:
        print("Leap year")  # Ano bissexto
else:
    print("Not a leap year")  # Não é um ano bissexto
