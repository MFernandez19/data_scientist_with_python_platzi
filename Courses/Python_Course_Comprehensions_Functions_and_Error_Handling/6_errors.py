#print(0/0)
#print(result)

suma = lambda x,y: x + y
assert suma(2,2) == 4

print("Hola")

age = 10
if age < 18:
    raise Exception("No se permiten menores de edad")