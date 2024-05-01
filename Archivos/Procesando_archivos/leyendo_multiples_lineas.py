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