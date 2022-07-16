# Docstring
# __doc__ (Modulos, Clases, Metodos y Funciones)

def suma(numero1, numero2):
    
    '''
    La funcion suma 2 numeros enteros
    Argumento:
    numero1 (int)
    numero2 (int)
    
    Se retona la suma de los parametros
    en consola escribir : python -m doctest testearfunciones.py
    
    >>> suma(50,20)
    70
    >>> suma(80,20)
    100
    
    '''
    return numero1 + numero2

#print(suma.__doc__)
#print(help(suma))