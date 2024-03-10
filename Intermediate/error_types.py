# Error types

# SyntaxError
#print "¡Hola comunidad!" -->
print("¡Hola comunidad!")

# NameError
#print(language) --> cuando la variable no está definida
language = "Spanish"
print(language)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
#print(my_list[5]) índice fuera de rango, no hay ningún elemento en el índice indicado del array
print(my_list[4]) 

# ModuleNotFound
#import maths -> no existe un módulo con este nombre
import math

# AttributeError
#print(math.PI) -> el módulo math no tiene un atributo llamado PI
print(math.pi)

# KeyError
my_dict = {"Nombre":"Nerea", "Apellido":"Francés", "Edad":22, 1:"Python"}
#print(my_dict["Apelido"]) -> no existe ninguna clave en el diccionario llamada 'Apelido'
print(my_dict["Apellido"])

# TypeError
#print(my_list["Nombre"]) -> para el índice de una lista se espera un tipo integer
print(my_list[0])

# ImportError
#from math import PI -> no existe este atributo en la librería math
from math import pi

# ValueError
#my_int = int("10 Años") -> invalido convertir caracteres a int
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
#print(4/0)
print(4/2)