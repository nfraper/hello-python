### Python Package Manager ###

import numpy


print(numpy.version.version)

my_array = numpy.array([35, 24, 22, 54, 67, 88])

print(type(my_array))

print(my_array * 2)


import pandas

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
#print(response.json()) #muestra los 151 pokemon

pokemon_data = response.json()
for pokemon in pokemon_data['results']:
    print(pokemon['name']) #imprime solo los nombres de los pokemon del json

# local Arithmetics Package
from package import arithmetics 

print(arithmetics.sum(1, 4))