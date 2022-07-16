'''
rango = range(11) # 0 - 10
for valor in rango:
    print(valor)
''' 

'''
for valor1 in range(10,20): # puedes colar donde quiere iniciar
    print(valor1)
    
'''
'''
  # start = 0 --> end, skips
for valor1 in range(10,21,2): # puedes colar los saltos ( esta va de 2 en 2)
    print(valor1)    
'''

numero = [10,20,30,40,50]
for indice, numero in enumerate(numero):
    print(indice, numero)