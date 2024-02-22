my_string = "Este es el primer string"
my_other_string = "Este es mi segundo string"

print("\n1. " + my_string + " " + my_other_string)
print("2." ,len(my_string))

print("3. " + my_string + "\nEsto es un salto de línea")
print("4. " + my_string + "\n\tEsto es un tab")
print("5. \\t Imprimimos todo \\n")

# Formateo

print("\n\n#Formateo \n")

name, surname, age = "Nerea", "Francés", 22

print("- Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("- Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"- Mi nombre es {name} {surname} y mi edad es {age}")


# Desempaquetado de caracteres

print("\n\n#Desempaquetado de caracteres \n")

language = "python"
a, b, c, d, e, f = language

print(a)
print(b)


# División

print("\n\n#División \n")

language_slice = language[1:3]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

print("\n\n#Reverse \n")

reversed_language = language[::-1]
print(reversed_language)


# Funciones

print("\n\n#Funciones \n")

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("p"))