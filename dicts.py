# Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Nerea", "Apellido":"Francés", "Edad":22, 1:"Python"} # key:value

my_dict = {
    "Nombre":"Brais",
    "Apellido":"Moure",
    "Edad":22,
    "Lenguajes": {"Python", "Swift", "Kotlin"}, # Set
    1:1.77
    }

print(my_dict)
print(my_other_dict)

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

my_dict["Calle"] = "Calle MoureDev" # Se crea y se añade un nuevo elemento directamente con clave "Calle" y valor "MoureDev"
print(my_dict)

del my_dict["Calle"] # Se puede eliminar un elemnto en concreto pasándole la clave como argumento 
print(my_dict) 

print("Moure" in my_dict)
print("Apellido" in my_dict) # Solo reconoce la key 

print(my_dict.items()) #devuelve todos los elementos con sus keys y values
print(my_dict.keys()) #devuelve las keys del diccionario
print(my_dict.values()) #devuelve los valores de cada key del diccionario

my_new_dict = my_dict.fromkeys(("Nombre", 1, "Piso")) #se crea un diccionario con las claves del otro diccionario o nuevas desde cero
                                                    #sin sus valores
print(my_new_dict)
      
my_list = ["Nombre", "Número", "Edad"]
my_new_dict = dict.fromkeys(my_list) #crea un diccionario con las claves indicadas en una lista y con valores None
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict) #crea un diccionario con las mismas claves que el diccionario my_dict pero con valores None
print(my_new_dict)