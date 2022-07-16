'''
def operacion(cantidad, balance, tipo= 'deposito'):
    
    def deposito(cantidad, balance):
        return cantidad + balance
    
    
    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None
        
           
    if tipo == 'deposito':
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad, balance)
    
resultado = operacion(10, 50, 'retiro')
print(resultado) '''

def operacion():
    
    def deposito(cantidad, balance):
        return cantidad + balance
    
    
    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None
    
    
    a = int(input('ingrese la cantidad: '))
    b = int(input('ingrese el balance: ')) 
    c = int(input('ingrese cantidad a retirar: '))
    d = int(input('ingresa el balance: '))
    
    print(deposito(a, b))
    print(retiro(c, d))
    
    #print(deposito(a, b))
    #print(retiro(20, 100))

operacion()
    
