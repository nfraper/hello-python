### Expresiones Regulares ###

# Sirven para comprobar si una cadena de texto tiene lo que estamos buscando

import re

my_string = "Esta es la lección número 7:\nLección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de Ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match) # comprueba si nuestro texto contiene el 
            # texto que le pasamos como parámetro
#re.I aplica una serie de reglas a tener en cuenta como ignorar las mayúsculas, espacios en blanco y comentarios, etc

print(match.span()) #muestra el rango en el que se encuentra el matching, p.e. entre los índices 0 y 18

start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string, re.I)
if not(match == None):
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])
else:
    print(match)


print(re.match("Expresiones Regulares", my_string)) # devuelve None porque empieza a buscar desde la posicón 0 


# search

search = re.search("lección", my_string, re.I) # te busca el elemento en cualquier posición del texto
print(search)
start, end = search.span()
print(my_string[start:end])


# findall
findall = re.findall("lección", my_string, re.I) # listado con las veces que ha encontrado el elemento en el texto
print(findall) # no distingue entre mayúsculas y minúsculas


# split
print(re.split(":", my_string)) #divide el texto a partir de l matching con el valor del parámetro


# sub
print(re.sub("[l|L]ección", "LECCIÓN", my_string)) #sustituye el primer elemento de la cadena que haga matching 
                                                #con el primer parámetro por el segundo parámetro


# patterns
# para aprender y valdar expresiones regulares: https://regex101.com

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_string))

pattern = r"[\d]" 
print(re.findall(pattern, my_string)) #busca los dígitos

pattern = r"[\D]" 
print(re.findall(pattern, my_string)) #busca los caracteres

pattern = r"[l].*" 
print(re.findall(pattern, my_string))
