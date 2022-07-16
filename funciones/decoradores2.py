'''
a --> La funcion principal ( Docorador)
b --> La funcion a Decorar
c --> la funcion decorada

a(b) --> c

'''
def funcion_a(funcion_b):
    
    def funcion_c(*args, **kwargs):
        print('Antes de la funcion')
        resultado = funcion_b(*args, **kwargs)
        print('Despues de la funcion')
        return resultado
    return funcion_c

@funcion_a   
def sumar(numero1, numero2):
    return numero1 + numero2
    
    
resultado = sumar(50, 60)    
print(resultado)
    