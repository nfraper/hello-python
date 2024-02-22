my_set = set()
my_other_set = {} # Inicialmente es un diccionario
print(type(my_set))
print(type(my_other_set))

my_other_set = {"Nerea", "Francés", 22} # Pasa a ser un set
print(type(my_other_set))

my_other_set.add("nfraper")
print(my_other_set) # Un set no es una estructura ordenada 

my_other_set.add("nfraper")
print(my_other_set) # Un set no admite elementos repetidos

# Los set son modificables

print("Nerea" in my_other_set)

my_other_set.clear() # Eliminamos los elementos del set
print(len(my_other_set)) 

del my_other_set # Eliminamos la variable
# print(my_other_set) 