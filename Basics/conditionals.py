my_condition = False

if my_condition:
    print("Ejecutando")

my_condition = 5 * 2

if my_condition == 11:
    print("El valor es 11")
elif my_condition > 11:
    print("El valor es mayor que 11")
else: 
    print("El valor es menor que 11")


# operadores lógicos
if my_condition > 5 and my_condition < 20:
    print("Se cumple con el rango")

if my_condition == 5 or my_condition == 10:
    print(my_condition)



# comprueba si la cadena de texto no es vacía

my_string = ""

if my_string:
    print("Mi cadena de texto no es vacía")


# comprueba si la cadena de texto es vacía
    
if not my_string:
    print("Mi cadena de texto es vacía")