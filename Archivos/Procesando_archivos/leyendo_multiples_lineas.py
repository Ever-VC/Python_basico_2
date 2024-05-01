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

Observa el código en el editor. Lo hemos modificado para mostrarte como usar readlines().
'''
print('-'*40)
try:
    ccnt = lcnt = 0
    s = open('./Archivos/Procesando_archivos/text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCaracteres en el archivo:", ccnt)
    print("Líneas en archivo:     ", lcnt)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
    
'''
Hemos decidido usar un búfer de 15 bytes de longitud. No pienses que es una recomendación.

Hemos utilizado ese valor para evitar la situación en la que la primera invocación de readlines() consuma todo el archivo.

Queremos que el método se vea obligado a trabajar más duro y que demuestre sus capacidades.

Existen dos bucles anidados en el código: el exterior emplea el resultado de readlines() para iterar a través 
de él, mientras que el interno imprime las líneas carácter por carácter.

El último ejemplo que queremos presentar muestra un rasgo muy interesante del objeto devuelto por la función open() en modo de texto.

Creemos que puede sorprenderte: el objeto es una instancia de la clase iterable.

¿Extraño? De ninguna manera. ¿Usable? Si, por supuesto.

El protocolo de iteración definido para el objeto del archivo es muy simple: su método __next__ solo devuelve la siguiente línea leída del archivo.

Además, puedes esperar que el objeto invoque automáticamente a close() cuando cualquiera de las lecturas del archivo lleguen al final del archivo.

Mira el editor y ve cuan simple y claro se ha vuelto el código.

'''
print('-'*40)

try:
	ccnt = lcnt = 0
	for line in open('./Archivos/Procesando_archivos/text.txt', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCaracteres en el archivo:", ccnt)
	print("Líneas en el archivo:     ", lcnt)
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))
    