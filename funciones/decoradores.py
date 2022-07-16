'''
a --> La funcion principal ( Docorador)
b --> La funcion a Decorar
c --> la funcion decorada

a(b) --> c

'''
def funcion_a(funcion_b):
    
    def funcion_c():
        print('Antes de la funcion')
        funcion_b()
        print('Despues de la funcion')
    return funcion_c

@funcion_a
def saludar():
    print('Hola estoy es la funcion SALUDAR')
    
@funcion_a   
def sumar():
    print(10 + 10)
    
    
sumar()    
    