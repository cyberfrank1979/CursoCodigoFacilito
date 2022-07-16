diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(diccionario)
print(len(diccionario))

del diccionario['a'] # PRIMERA FORMA

print(diccionario)
print(len(diccionario))

metodo_pop = diccionario.pop('b') # SEGUNDA FORMA

print(diccionario)
print(len(diccionario))

diccionario.clear() # TERCERA FORMA
print(diccionario)
print(len(diccionario))