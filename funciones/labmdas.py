'''def centigrados_a_farhenheit(grados):
    return (grados * 1.8) + 32
  
#print(centigrados_a_farhenheit(10))
#print(centigrados_a_farhenheit(30))
#print(centigrados_a_farhenheit(8))

mi_funcion = centigrados_a_farhenheit
print(mi_funcion(10))
'''
# Funcion LAMBDA  
# lambda <parametro> : <cuerpo de la funcion>

funcion_grado = lambda grados : grados * 1.8 + 32

print(funcion_grado(10))

'''
sin_parametro = lambda : True
parametro_default = lambda p1=10, p2=20, p3=30 : p1 + p2 +p3
asterisco = lambda *args, **kwargs : len(args) + len(kwargs)
'''
  


