
'''
def pares():
    for numero in range(0, 100, 2):
        yield numero # lazy interator --  la funcion suspende por un momento
        

generador = pares()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print('Hola continua')
print(next(generador))

'''
def pares():
    for numero in range(0, 50, 2):
        yield numero
        
        
generador = pares()

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El genrador termino')
        break