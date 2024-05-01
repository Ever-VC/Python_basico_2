'''
Otro método, que maneja el archivo de texto como un conjunto de líneas, no como caracteres, es readlines().

Cuando el método readlines(), se invoca sin argumentos, intenta leer todo el contenido del archivo y 
devuelve una lista de cadenas, un elemento por línea del archivo.

Si no estás seguro de si el tamaño del archivo es lo suficientemente pequeño y no deseas probar el sistema 
operativo, puedes convencer al método readlines() de leer no más de un número especificado de bytes a la 
vez (el valor de retorno sigue siendo el mismo, es una lista de una cadena).

Siéntete libre de experimentar con el siguiente código de ejemplo para entender cómo funciona el método readlines():
'''
stream = open("./Archivos/Procesando_archivos/text.txt")
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
stream.close()

'''
El tamaño máximo del búfer de entrada aceptado se pasa al método como argumento.

Puedes esperar que readlines() procese el contenido del archivo de manera más efectiva que readline(), ya 
que puede ser invocado menos veces.

Nota: cuando no hay nada que leer del archivo, el método devuelve una lista vacía. Úsalo para detectar el final del archivo.

Puedes esperar que al aumentar el tamaño del búfer mejore el rendimiento de entrada, pero no hay una regla de 
oro para ello: intenta encontrar los valores óptimos por ti mismo.
'''