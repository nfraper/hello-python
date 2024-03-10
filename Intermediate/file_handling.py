### File Handling ###

# .txt file
import os

txt_file = open("Intermediate/my_file.txt", "r+") # abrir desde el directorio raíz || "r" -> read, "w" -> write, "r+" -> read&write
#print(txt_file.read())
#print(txt_file.read(10)) # únicamente lee los primeros 10 caracteres del fichero
#print(txt_file.readline())
#print(txt_file.readline())
#print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)

#txt_file.write("\nAunque tambien me gusta Kotlin")
#os.remove("Intermediate/my_file.txt")
txt_file.close()

#with open("Intermediate/my_file.txt", "a") as my_other_file:
    #my_other_file.write("\nY Swift")



# .json file
import json

json_file = open("Intermediate/my_file.json", "w+") 
json_test = {
    "name":"Nerea",
    "surname":"Francés",
    "age":22,
    "language":["Python","Kotlin","Java"]
}

json.dump(json_test, json_file, indent=2) #el atributo 'indent' se puede pasar como parámetro para añadir 
                                #espacios antes de cada línea en el fichero json 
json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json")) #transforma el json en un dict
print(json_dict)



#.csv file
import csv

csv_file = open("Intermediate/my_file.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["nombre", "appellido", "age", "language"]) # El primero escribe los headers de cada columna
csv_writer.writerow(["Nerea", "Francés", 22, "Python"]) # Segunda fila
csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
#import xlrd # Debe instalarse el módulo



# .xml file
import xml