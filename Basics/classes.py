### Classes ###

class MyEmptyPerson:
    pass #para que no de error al ejecutar si se define una clase vacía

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname): #constructor de clase
        self.name = name 
        self.__surname = surname #Propiedad privada 
        self.full_name = f"{name} {surname}"

    def walk (self):
        print(f"{self.full_name} está caminando.")
    
    def getSurname (self): #getter
        return self.__surname


my_person = Person("Nerea", "Francés")
print(f"{my_person.name} {my_person.getSurname()}")

print(my_person.full_name)

my_person.walk()