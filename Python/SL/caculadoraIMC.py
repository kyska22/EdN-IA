"""
Calculadora de IMC
El seguimiento del IMC es una forma útil de comprobar si se mantiene un peso saludable. Se calcula a partir del peso y la altura de una persona, utilizando esta fórmula: peso / altura²

El número resultante indica una de las siguientes categorías:
Underweight = menos de 18.5
Normal = mayor o igual a 18.5 y menor a 25
Overweight = mayor  o igual a 25 y menor a 30
Obesity = 30 o más

Hagamos que averiguar tu IMC sea más rápido y fácil, creando un programa que tome el peso y la altura de una persona como entrada y genere la categoría de IMC correspondiente.

Ejemplo de entrada
85
1.9

Ejemplo de salida
Normal
"""
peso = float(input())
altura = float(input())

IMC = peso / altura ** 2

if IMC < 18.5:
    print("Underweight")
elif 18.5 <= IMC < 25:
    print("Normal")
elif 25 <= IMC < 30:
    print("Overweight")
else:
    print("Obesity")
