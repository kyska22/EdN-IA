"""
Motor de búsqueda
Estás trabajando en un motor de búsqueda. ¡Vigila tu espalda Google!
El código dado toma un text y un word como entrada y los pasa a una función llamada search().

La función search() debe devolver "Word found" si la palabra está presente en el texto, o "Word not found", si no es así.

Ejemplo de entrada
"This is awesome"
"awesome"

Ejemplo de salida
Word found
"""
text = input()
word = input()

def search (text, word):

    if word in text:
        print("Word found")
    else:
        print("Word not found")

search(text, word)
