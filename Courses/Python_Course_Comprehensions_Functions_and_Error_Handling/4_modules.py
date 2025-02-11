#Este funcionara para obtener informacion del sistema
import sys

#print(sys.path)

#Este funcionara para poder obtener patrones dentro de un string 
import re
text = "Mi numero de telefono es 300 445 7558 3, el codigo de mi pais de 353, mi numero favortio es el 19"
result = re.findall(pattern="[0-9]+", string=text)
#print(result)

#Este funcionara para poder obtener la hora
import time

timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
#print(result)

#Este funciona para poder obtener la cantidad de veces que algo se repite
import collections
numbers = [1,2,3,4,1,1,2,1,3,4,5,6,6,21]
counter = collections.Counter(numbers)
print(counter)