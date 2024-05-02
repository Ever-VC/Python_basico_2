'''
La función ctime()

El módulo time proporciona una función llamada ctime, que convierte 
el tiempo en segundos desde el 1 de enero de 1970 (época Unix) en una cadena.

¿Recuerdas el resultado de la función time? Eso es lo que necesitas 
pasar a ctime. Echa un vistazo al ejemplo en el editor.
'''
import time

timestamp = 1572879180
print(time.ctime(timestamp))

'''
Resultado:

Mon Nov 4 14:53:00 2019

La función ctime devuelve una cadena para la marca de tiempo pasada. En nuestro 
ejemplo, la marca de tiempo expresa el 4 de noviembre de 2019 a las 08:53:00.

También es posible llamar a la función ctime sin especificar el tiempo en segundos. En este 
caso, se devolverá la hora actual:
'''

print(time.ctime())