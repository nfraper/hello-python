### Funciones de orden superior ### -> una función puede usarse dentro de otra función

from functools import reduce


def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_plus_value(first_value,second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_plus_value(5, 2, sum_one))
print(sum_two_values_plus_value(5, 2, sum_five))


#Closures

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(5))

def sum_ten2(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure2 = sum_ten2(5)
print(add_closure2(5))
print(sum_ten2(5)(5))

# Built-in Hiher Order Functions

numbers = [2, 5, 10, 21]

# Map

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter 

def filter_greater_than_ten(number):
    if(number > 10):
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce

def sum_two_values(first, second):
    return first + second

print(reduce(sum_two_values, numbers))