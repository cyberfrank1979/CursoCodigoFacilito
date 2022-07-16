from cmath import pi


e = 'e' # variable global

def funcion_primaria():
    a = 'a' # variables locales
    b = 'b'
    
    def funcion_anidada():
        c = 'c' # variables locales
        b = 'cambio de valor'
        
        print(a)
        print(b)
        print(e)
        
    funcion_anidada()
    #print(c)
    
funcion_primaria()