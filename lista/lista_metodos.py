from cgi import print_arguments
from operator import lshift


lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

lista.sort() # ordena la lista de menor a mayor
print(lista)

lista.sort(reverse=True) # ordena la lista de mayo a menor
print(lista)

#lista.sort()
#print(lista[0]) # menor
#lista.sort(reverse=True)
#print(lista[0]) # mayor

lista.sort()
print(lista[0]) # Menor
print(lista[-1]) # mayor
#**************************************************

# funcion MIN y MAX

print(min(lista)) # MIN
print(max(lista))  # MAX

# *************************************************
# para saber si el numero esta dentro de la lista

valor_lista = 5 in lista
print(valor_lista)

valor_lista2 = 11 not in lista
print(valor_lista2)

# para saber su INDIXE

index = lista.index(90)
print(index)

