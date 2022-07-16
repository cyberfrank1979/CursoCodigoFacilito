'''
def pares():
    for numero in range(0, 100, 2):
        print(numero)
         
pares()

'''
'''
def pares():
    for numero in range(0, 100, 2):
        return numero # con este solo se va el 0 por que encuentra en el primer recorrido un valor se detiene

print(pares())
'''

def pares():
    for numero in range(0, 100, 2):
        yield numero # este si es un generador ----  con el YIELD
        print('se reanuda la ejecucion')

for par in pares():
    print(par)
