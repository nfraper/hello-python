### Functions ###

def my_function ():
    print("Esto es una función")

def sum_two_values (first_num, sec_num):
    print(first_num + sec_num)

my_function()
sum_two_values(5, 7)
sum_two_values(10, 15)
sum_two_values("2", "6")

# returns

def sum_values (first_num, sec_num):
    total = first_num + sec_num
    return total

res = sum_values(10.4, 5.3)

print(res)


def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Nerea", "Francés")
print_name(surname="Francés", name="Nerea")


def print_name_with_default(name, surname, alias = "No alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Nerea", "Francés", "nfraper")
print_name_with_default("Brais", "Moure")

# numero indefinido de parámetros con *
def print_texts(*text):
    print(text)

print_texts("Hola")
print_texts("Hola", "Pepe", "Como", "estás", "?")


def print_texts2(*texts):
    for text in texts:
        print(text)

print_texts2("Hola")
print_texts2("Hola", "Pepe", "Como", "estás", "?")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola")
print_upper_texts("Hola", "Pepe", "Como", "estás", "?")