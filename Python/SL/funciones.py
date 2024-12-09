"""
Las funciones ayudan a dividir nuestro programa en trozos más pequeños y modulares. 
A medida que nuestro programa se hace más grande y más complejo, las funciones ayudan a hacerlo más organizado y manejable.
"""

#Len, permite obtener el número de elementos de una lista.Así:
#También puedes utilizar len sobre las cadenas para devolver su longitud (número de caracteres).

nums = [1, 3, 5, 2, 4]
print(len(nums))

# Output 5

#append() - añade un elemento al final de una lista existente:
nums = [1, 2, 3]
nums.append(4)
print(nums)

#OUTPUT [1, 2, 3, 4]

#insert() - inserta un nuevo elemento en cualquier posición de la lista:

words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words) 

#

#index() - encuentra la primera aparición de un elemento de la lista y devuelve su índice.
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('q')) 

#

#max(list): Devuelve el valor máximo.

#min(list): Devuelve el valor mínimo.

#list.count(item): Devuelve un recuento de cuántas veces aparece un elemento en una lista.

#list.remove(item): Elimina un elemento de una lista.

#list.reverse(): Invierte los elementos de una lista.
