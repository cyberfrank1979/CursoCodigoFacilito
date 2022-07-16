from operator import lshift


lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
lista_cursos2 = ['C','C++', 'Docker']

print(len(lista_cursos))
lista_cursos.append('MongoDB')
lista_cursos.append('C#')
lista_cursos.append('JavaScript') # lo ingresa al final

lista_cursos.insert(1,'Rails') # ingresa en la posicion 1 de la lista
lista_cursos.insert(0,'PyGame')


lista_cursos.extend(lista_cursos2) # extender la lista de otra lista

#print(lista_cursos)
print(len(lista_cursos))
print(lista_cursos)
print(lista_cursos2)

lista_cursos.remove('MongoDB') # elimina un elemento de la lista
print(lista_cursos)
print(len(lista_cursos))

del lista_cursos[0] # Elimina con indices
print(lista_cursos)
print(len(lista_cursos))

lista_cursos.clear() # elimina todo los elemento de la lista
print(lista_cursos)
print(len(lista_cursos))