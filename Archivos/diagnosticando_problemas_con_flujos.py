'''
El objeto IOError está equipado con una propiedad llamada errno (el nombre viene de 
la frase error number, número de error) y puedes accederla de la siguiente manera:
'''

try:
    # Algunas operaciones con streams.
    pass
except IOError as exc:
    print(exc.errno)
    
'''
El valor del atributo errno se puede comparar con una de las constantes simbólicas predefinidas en módulo errno.

Echemos un vistazo a algunas constantes seleccionadas útiles para detectar errores en los streams:

errno.EACCES → Permiso denegado

El error se produce cuando intentas, por ejemplo, abrir un archivo con atributos de solo lectura para escritura.

errno.EBADF → Número de archivo incorrecto

El error se produce cuando intentas, por ejemplo, operar un stream sin abrirlo.

errno.EEXIST → Archivo existente

El error se produce cuando intentas, por ejemplo, cambiar el nombre de un archivo con su nombre anterior.

errno.EFBIG → Archivo demasiado grande

El error ocurre cuando intentas crear un archivo que es más grande que el máximo permitido por el sistema operativo.

errno.EISDIR → Es un directorio

El error se produce cuando intentas tratar un nombre de directorio como el nombre de un archivo ordinario.

errno.EMFILE → Demasiados archivos abiertos

El error se produce cuando intentas abrir simultáneamente más streams de los aceptables para el sistema operativo.

errno.ENOENT → El archivo o directorio no existe

El error se produce cuando intentas acceder a un archivo o directorio inexistente.

errno.ENOSPC → No queda espacio en el dispositivo

El error ocurre cuando no hay espacio libre en el dispositivo.
La lista completa es mucho más larga (incluye también algunos códigos de error no relacionados con el procesamiento del los streams).

Si eres un programador muy cuidadoso, puedes sentir la necesidad de usar una secuencia de sentencias similar a las que se te presentan en el editor.
'''

import errno

try:
    s = open("archivo_inexistente.txt", "rt")
    # El procesamiento va aquí.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("El archivo no existe.")
    elif exc.errno == errno.EMFILE:
        print("Demasiados archivos abiertos.")
    else:
        print("El numero del error es:", exc.errno)
        
'''
Afortunadamente, existe una función que puede simplificar el código de manejo de errores.

Su nombre es strerror(), y proviene del módulo os y espera solo un argumento: un número de error.

Su función es simple: proporciona un número de error y una cadena que describe el significado del error.

Nota: si pasas un código de error inexistente (un número que no está vinculado a ningún error real), la función generará una excepción ValueError.

Ahora podemos simplificar nuestro código de la siguiente manera:
'''
from os import strerror

try:
    s = open("archivo_inexistente.txt", "rt")
    # El procesamiento va aquí.
    s.close()
except Exception as exc:
    print("El archivo no pudo ser abierto:", strerror(exc.errno))