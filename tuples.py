my_tuple = ()
my_other_tuple = tuple()

my_tuple = (22, 1.59, 'Nerea', 'Francés', 'Francés')

print(my_tuple.index('Nerea'))
print(my_tuple.index('Francés'))

my_other_tuple = (30, 40, 50)

# Diferencia entre tuplas y listas: las tuplas tienen valores constantes, es decir, no se puede reasignar su valor

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple[3:6])