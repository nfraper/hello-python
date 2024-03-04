#función anónima (sin nombre)

sum_two_values = lambda first_value, second_value: print(first_value + second_value)
sum_two_values(2, 4)

multiply_values = lambda first_value, second_value: print(first_value * second_value - 3)
multiply_values(2, 4)

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

my_sum = sum_three_values(5)(2, 4)
print(my_sum)

