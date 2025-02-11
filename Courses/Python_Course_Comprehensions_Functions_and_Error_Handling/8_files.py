#Aqui abrimos el archivo
#file = open("./text.txt")
#Aqui leemos el archivo
#print(file.read())
#print(file.readline())
#Aqui podemos iterar el archivo
#for line in file:
    #print(line)
#Aqui cerramos el archivo
#file.close()

#Aqui le decimos a python que cuando termine de hacer todas las instrucciones cierre el archivo
with open("./text.txt") as file:
    for line in file:
        print(line)