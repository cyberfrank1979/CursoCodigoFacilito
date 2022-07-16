from turtle import title


titulo_curso = 'Curso profesional de Python'

'''
for caracter in titulo_curso:
    if caracter == 'P':
        break # nos permite finalizar de manera inmediata la ejecucion de nuestro ciclo ( for o while)
    print(caracter)
'''


for caracter in titulo_curso:
    if caracter == 'o':
        continue # pasar la siguiente interacion
    print(caracter)    