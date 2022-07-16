from operator import contains

'''
# mientras que contador sea menor o igual a 10
contador = 1
while contador <= 10:   hasta que se cumpla
    print(contador)
    contador = contador + 1
'''
# Miestras que numero sea mayor o igual a uno
numero = 1234
contador_digitos = 0 # 0 + 1= 1 --> 1 + 1 = 2 --> 2 + 1= 3 --> 3 + 1= 4
while numero >= 1: # hasta que se cumpla
    #contador_digitos = contador_digitos + 1
    contador_digitos += 1
    numero = numero / 10
print(contador_digitos)
        
    
    
    
   