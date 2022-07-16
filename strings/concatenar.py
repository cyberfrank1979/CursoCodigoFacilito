# los string son inmutable, asi se quedaran para siempre
nombre = 'Francisco Javier'
apellido = 'Galan'
segundo = 'Freile'
edad = 42

#primera forma
# nombre_completo = 'Mr.' + ' ' + nombre + ' ' + apellido + '.'

#segunda forma
# nombre_completo = 'Mr. %s %s %s= %s.' %(nombre,apellido,segundo, 'Si sabe')

#tercera forma
#nombre_completo = 'Mr. {} {} {}.' .format(nombre,apellido,segundo)

#cuarta forma
#
#nombre_completo = 'Mr. {primer_apellido} {segundo_apellido} {nombre}  ' .format(
#nombre=nombre,
#primer_apellido=apellido,
#segundo_apellido=segundo)

#quinta y la mas recomendada FString
nombre_completo = f'Mr. {nombre} {apellido} {segundo} {"Es_el_mejor"} {edad} {10 * 2}' 

print(nombre_completo) 
