'''
Las funciones asctime() y mktime()
El módulo time tiene funciones que esperan un objeto struct_time o una 
tupla que almacena valores de acuerdo con los índices presentados cuando 
se habla de la clase struct_time. Ejecuta el ejemplo en el editor.
'''
import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))

'''
Resultado:

Mon Nov 4 14:53:00 2019
1572879180.0

La primera de las funciones, llamada asctime, convierte un objeto struct_time 
o una tupla en una cadena. Toma en cuenta que la conocida función gmtime se 
usa para obtener el objeto struct_time. Si no se proporciona un argumento a 
la función asctime, se utilizará el tiempo devuelto por la función localtime.

La segunda función llamada mktime convierte un objeto struct_time o una tupla 
que expresa la hora local al número de segundos desde la época de Unix. En 
nuestro ejemplo, le pasamos una tupla, que consta de los siguientes valores:

2019 => tm_year
11 => tm_mon
4 => tm_mday
14 => tm_hour
53 => tm_min
0 => tm_sec
0 => tm_wday
308 => tm_yday
0 => tm_isdst
'''