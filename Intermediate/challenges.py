#Reto 0: FIZZ BUZZ
'''
Números del 1 al 100
-Múltiplos de 3 -> "fizz"
-Múltiplos de 5 -> "buzz"
-Múltiplos de 3 y 5 a la vez -> "fizzbuzz"
'''

def fizzbuzzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif(index % 3 == 0):
            print("fizz")
        elif(index % 5 == 0):
            print("buzz")
        else:
            print(index)
        
        
fizzbuzzz()

#Reto 1: ¿ES UN ANAGRAMA?
'''
Escribe una función que reciba dos palabras (string) y retorne verdadero o falso (Bool) 
según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta combrobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
'''

def is_anagram(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    if(palabra1 == palabra2):
        return False
    elif(sorted(palabra1) != sorted(palabra2)):
        return False
    else:
        return True

print(is_anagram('amor', 'roma'), is_anagram('pepito','Pitope'), is_anagram('espera','espera'))

#Reto 2: LA SUCESIÓN DE FIBONACCI
'''
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
- La serie Finonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos
anteriores.
0, 1, 1, 2, 3, 5, 8, 13, ...
'''

def fibonacci():
    prev = 0
    next = 1
    fib = 0
    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib
        
fibonacci()
        
#Reto 3: ¿ES UN NÚMERO PRIMO?
'''
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''

def is_prime(number):
    if(number < 2): return False
    for i  in range(2, 9):
        if(i != number):
            if(number % i == 0): return False
    return True


for i in range(100):
    print(i,":", is_prime(i))