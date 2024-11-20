"""
¡Estás haciendo un juego! El jugador intenta disparar a un objeto y puede hacer hit o miss.

El jugador comienza con 100 puntos, un acierto añade 10 puntos a la puntuación del jugador, y un fallo le resta 20 puntos.

Tu programa necesita tomar 4 resultados de acción como entrada ("hit" or "miss"), calcular y genera a los puntos restantes del jugador.

Ejemplo de entrada
hit
hit
miss
hit

Ejemplo de salida
110

Explicación: 3 hits(hit) añaden 30 puntos, un miss(miss) descuenta 20, lo que hace que el total de puntos sea igual a 110.
"""

puntuacion = 100
i = 0
gol = "hit"

while i<=3:
    marca = input()
    if marca == gol:
        puntuacion += 10
    else:
        puntuacion -= 20

    i +=1

print (puntuacion)
