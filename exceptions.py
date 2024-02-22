### Exception Handling ###

num1 = 1
num2 = '1'

try:
    print(num1 + num2)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else: #se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally: #se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipo
    
try:
    print(num1 + num2)
    print("No se ha producido error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")


# Captura la información de la excepción
    
try:
    print(num1 + num2)
    print("No se ha producido error")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)