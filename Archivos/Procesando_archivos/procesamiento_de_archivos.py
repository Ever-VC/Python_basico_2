'''
Comenzaremos con la variante más simple y usaremos un archivo llamado text.txt. El archivo contiene lo siguiente:

Lo hermoso es mejor que lo feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
'''
from os import strerror

try:
    counter = 0
    stream = open('./Archivos/Procesando_archivos/text.txt', "rt", encoding='utf-8')
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
    
'''
La rutina es bastante simple:

    - Se usa el mecanismo try-except y se abre el archivo con el nombre (text.txt en este caso).
    - Intenta leer el primer carácter del archivo (char = stream.read(1)).
    - Si tienes éxito (esto se demuestra por el resultado positivo de la condición while), se muestra 
    el carácter (nota el argumento end=, ¡es importante! ¡No querrás saltar a una nueva línea después 
    de cada carácter!).
    - Tambien, se actualiza el contador (counter).
    - Intenta leer el siguiente carácter y el proceso se repite.
    
Si estás absolutamente seguro de que la longitud del archivo es segura y puedes leer todo el archivo 
en la memoria de una vez, puedes hacerlo: la función read(), invocada sin ningún argumento o con un 
argumento que se evalúa a None, hará el trabajo por ti.

Recuerda: el leer un archivo muy grande (en terabytes) usando este método puede dañar tu sistema operativo.

No esperes milagros: la memoria de la computadora no se puede extender.

Observa el código en el editor. ¿Qué piensas de el?
'''
print("\n\n")
try:
    counter = 0
    stream = open('./Archivos/Procesando_archivos/text.txt', "rt")
    content = stream.read()
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S: ", strerr(e.errno))
    
'''
Vamos a analizarlo:

    - Abre el archivo, como anteriormente se hizo.
    - Lee el contenido mediante una invocación de la función read().
    - Después, se procesa el texto, iterando con un bucle for su contenido, y se actualiza el valor del contador en cada vuelta del bucle.
El resultado será exactamente el mismo que en el ejemplo anterior.
'''