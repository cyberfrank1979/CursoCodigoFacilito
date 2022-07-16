

def pares():
    for numero in range(0, 100, 2):
        yield numero # lazy interator
        
for par in pares():
    print(par)