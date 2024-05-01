'''
-> Creando directorios en Python <-

El módulo os proporciona una función llamada mkdir, la cual, como el comando mkdir en 
Unix y Windows, te permite crear un directorio. La función mkdir requiere una ruta que 
puede ser relativa o absoluta. Recordemos cómo se ven ambas rutas en la práctica:

my_first_directory - esta es una ruta relativa que creará el directorio my_first_directory en 
el directorio de trabajo actual.

./my_first_directory - esta es una ruta relativa que apunta explícitamente al directorio de trabajo 
actual. Tiene el mismo efecto que la ruta anterior.

../my_first_directory - esta es una ruta relativa que creará el directorio my_first_directory en el 
directorio superior del directorio de trabajo actual.

/python/my_first_directory - esta es una ruta absoluta que creará el directorio my_first_directory, que 
a su vez está en el directorio raíz de python.

Observa el código en el editor. Muestra un ejemplo de cómo crear el directorio my_first_directory usando una 
ruta relativa. Esta es la variante más simple de la ruta relativa, que consiste en pasar solo el nombre 
del directorio.

Si pruebas tu código aquí, generará el directorio recién creado ['my_first_directory'](y todo el contenido del catálogo de trabajo actual).
'''

import os

os.mkdir("./modulo os/my_first_directory")
print(os.listdir())