'''
def promedio(listado): # con un solo paremetro
    return sum(listado) / len(listado)

resultado = promedio([10,10,5,7,10]) # se mete en una lista
print(resultado)
'''




def promedio(*args): # con el * puedo recibir una N cantidad de elementos y por convencion se coloca *ARGS
    return sum(args) / len(args)

resultado = promedio(10,10,5,7,10,10,10)
print(resultado)
