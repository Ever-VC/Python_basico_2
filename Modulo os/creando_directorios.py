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

'''
La función mkdir crea un directorio en la ruta especificada. Ten en cuenta que ejecutar el programa dos 
veces generará un FileExistsError.

Esto significa que no podemos crear un directorio si ya existe. Además del argumento de la ruta, la función 
mkdir puede tomar opcionalmente el argumento mode, que especifica los permisos del directorio. Sin embargo, en 
algunos sistemas, el argumento mode se ignora.

Para cambiar los permisos del directorio, recomendamos la función chmod, que funciona de manera similar 
al comando chmod en sistemas Unix. Puedes encontrar más información al respecto en la documentación.

En el ejemplo anterior, se usa otra función proporcionada por el módulo os llamada listdir. La función 
listdir devuelve una lista que contiene los nombres de los archivos y directorios que se encuentran en la 
ruta pasada como argumento.

Si no se le pasa ningún argumento, se utilizará el directorio de trabajo actual (como en el ejemplo anterior). 
Es importante que el resultado de la función listdir omita las entradas '.' y '..', que se muestran, por 
ejemplo, cuando se usa el comando ls -a en sistemas Unix.

NOTA: Tanto en Windows como en Unix, hay un comando llamado mkdir, que requiere una ruta de directorio. 
El equivalente del código anterior que crea el directorio my_first_directory es el comando mkdir my_first_directory.
'''