### Loops ###


# while

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 3
else:
    print("Mi condición es mayor o igual que 10") # podemos asociar un else al bucle, NO acepta elif

print("Se ha salido del bucle")

cont = 1
while my_condition < 20:
    my_condition+= 1
    if my_condition == 15:
        print("Se detiene la ejecución con valor: ", my_condition)
        break

    print("El valor es menor que 20, cont: ", cont, " , value: ", my_condition)
    cont += 1



# for

my_list = [35, 24, 62, 53, 30, 30, 17]

for element in my_list: # también funciona con tuplas y diccionarios
    print(element)