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