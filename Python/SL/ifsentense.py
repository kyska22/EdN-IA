# Declaraciones if pueden estar anidadas, una dentro de otra

num = 12
if num > 5:
    print("Bigger than 5")
    if num <=47:
        print("Between 5 and 47")
#################################################################
# Para anidar varias sentencias if, podemos usar elif

num = 3
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3: 
    print("Three")
else: 
    print("Something else")
