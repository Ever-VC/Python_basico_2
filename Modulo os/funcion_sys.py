'''
Todas las funciones presentadas en esta parte del curso pueden ser reemplazadas por una 
función llamada system, que ejecuta un comando que se le pasa como una cadena.

La función system está disponible tanto en Windows como en Unix. Dependiendo del 
sistema, devuelve un resultado diferente.

En Windows, devuelve el valor devuelto por el shell después de ejecutar el 
comando dado, mientras que en Unix, devuelve el estado de salida del proceso.

Veamos el código en el editor y veamos cómo es en la práctica.
'''

import os

returned_value = os.system("mkdir my_directory")
print(returned_value)

'''
El ejemplo anterior funcionará tanto en Windows como en Unix. En nuestro caso, recibimos 
el estado de salida 0, que indica éxito en los sistemas Unix.

Esto significa que se ha creado el directorio my_first_directory. Como parte del 
Pregunta , intenta enumerar el contenido del directorio donde se creó el directorio my_directory.
'''