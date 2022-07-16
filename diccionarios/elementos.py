diccionario = {'a': 1 , 'b':2 , 'c':3 , 'd':4}

'''
valor = diccionario['d']
print(valor)
'''

# metodo GET

valor = diccionario.get('z', 'la llave no existe') # intenta obtener el valor de un Key

print(valor)

# metodo Setdefault
valor = diccionario.setdefault('e', 5) # para añadir el key con su respectivo valor
print(valor)
print(diccionario)
