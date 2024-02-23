# Listas de forma comprimida

#creamos listas en base a listas que ya tenemos

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]

my_list = [i for i in my_original_list]
print(my_list)

my_list2 = [i for i in range(8)]
print(my_list2)

my_range = range(8)
print(list(my_range))

my_list3 = [i * 2 for i in my_range] #creamos una lista modificándola en el momento de su creación
print(my_list3)