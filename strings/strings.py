#ejercicio 1 metodo split
'''lenguaje ='Python Ruby Java Rust C++ C'
listado_lenguajes = lenguaje.split() # convierte de un string lo pasa a lista [], delimita con espacio

print(listado_lenguajes) '''

# ejercicio 2 metodo split
'''lenguaje ='Python-Ruby-Java-Rust-C++-C'
listado_lenguajes = lenguaje.split('-') # convierte de un string lo pasa a lista [], delimita con espacio

print(listado_lenguajes) '''


# ejercicio 3 metodo split
'''lenguaje ='Python//Rub//Java//Rust//C++//C'
listado_lenguajes = lenguaje.split('//') # convierte de un string lo pasa a lista [], delimita con espacio

print(listado_lenguajes)   '''

# ejercicio 4 metodo JOIN
'''
lenguaje = ['Python', 'Ruby', 'Java', 'Rust' ]
string_lenguaje = ' '.join(lenguaje)  # convierte una lista a un string
print(string_lenguaje)
print(type(string_lenguaje))  '''

# ejercicio 5 metodo JOIN

lenguaje = ['Python', 'Ruby', 'Java', 'Rust' ]
string_lenguaje = ' --- '.join(lenguaje)  # convierte una lista a un string y los puedo separa por cualquier caracter
print(string_lenguaje)
print(type(string_lenguaje))