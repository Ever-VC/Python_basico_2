'''
-> Obteniendo una marca de tiempo <-

Existen muchos convertidores disponibles en Internet que pueden 
calcular una marca de tiempo en función de una fecha y hora determinadas, pero 
¿cómo podemos hacerlo en el módulo datetime?

Esto es posible gracias al método timestamp proporcionado por la clase datetime. 
Observa el código en el editor.
'''

from datetime import datetime

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())

'''
Resultado:

Timestamp: 1601823300.0

El método timestamp devuelve un valor flotante que expresa el número de 
segundos transcurridos entre la fecha y la hora indicadas por el objeto 
datetime y el 1 de enero de 1970, 00:00:00 (UTC).
'''