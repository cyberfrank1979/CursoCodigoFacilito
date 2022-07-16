# son inmutables, no se pueden modificar las Tuplas
# son mas rapida para leer

tupla = ()
print(type(tupla))

curso = ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')

#*************************************************************

# *nombre --> Lista
# *_ --> Omitir valor
numeros = (1,2,3,4,5,6,7,8,9,10)
uno,dos,tres,cuatro, *_, nueve, diez = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(nueve)
print(diez)


# ZIP ****************************

lista = [1,2,3,4,5,6]

tupla = (10,20,30,40,50,60)

resultado = zip(lista, tupla) # --> ZIP
resultado =tuple(resultado)

print(resultado)
