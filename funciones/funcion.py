'''
def suma():
    numero_uno = int(input('Ingresa el primer numero entero: '))
    numero_dos = int(input('Ingresa el segundo numero entero: '))
    
    resultado = numero_uno + numero_dos
    print(resultado)
    
suma()
'''

'''
def suma(numero_uno, numero_dos):
    resultado = numero_uno + numero_dos
    print(resultado)
    
suma(2,5)
'''

'''
def suma(n1, n2):
    resultado = n1 + n2
    print(resultado)
    
numero_uno = int(input('Ingresa el primer numero entero: '))
numero_dos = int(input('Ingresa el segundo numero entero: '))

suma(numero_uno, numero_dos)

'''

'''
def suma(n1, n2):
    resultado = n1 + n2
    return resultado
    
numero_uno = int(input('Ingresa el primer numero entero: '))
numero_dos = int(input('Ingresa el segundo numero entero: '))

resultado = suma(numero_uno, numero_dos)
print('El resultado es:', resultado)
'''

def suma(n1, n2):
    return n1 + n2
    
numero_uno = int(input('Ingresa el primer numero entero: '))
numero_dos = int(input('Ingresa el segundo numero entero: '))

resultado = suma(numero_uno, numero_dos)
print('El resultado es:', resultado)
