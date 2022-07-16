from urllib import response


def saludar(username):
    mensaje = f'Hola como estas {username}' # variable local
    
    def mostrar_mensaje():
        print(mensaje)
        
    return mostrar_mensaje


username = 'Cody'
respuesta = saludar(username)

respuesta()



