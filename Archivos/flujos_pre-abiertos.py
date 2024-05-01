'''
Flujos o streams pre-abiertos
Dijimos anteriormente que cualquier operación del stream debe estar precedida por la 
invocación de la función open(). Hay tres excepciones bien definidas a esta regla.

Cuando comienza nuestro programa, los tres streams ya están abiertos y no requieren 
ninguna preparación adicional. Además, tu programa puede usar estos streams explícitamente 
si tienes cuidado de importar el módulo [sys]:
'''

import sys

'''
Porque ahí es donde se coloca la declaración de estos streams.

Los nombres de los streams son: sys.stdin, sys.stdout, y sys.stderr.

Vamos a analizarlos:

* sys.stdin
    - stdin (significa entrada estándar).
    - El stream stdin normalmente se asocia con el teclado, se abre previamente para la lectura y 
    se considera como la fuente de datos principal para los programas en ejecución.
    - La función bien conocida input() lee datos de stdin por default.

* sys.stdout
    - stdout (significa salida estándar)
    - El stream stdout normalmente está asociado con la pantalla, preabierta para escritura, considerada 
    como el objetivo principal para la salida de datos por el programa en ejecución.
    - La función bien conocida print() envía los datos al stream stdout.

* sys.stderr
    - stderr (significa salida de error estándar)
    - El stream stderr normalmente está asociado con la pantalla, preabierta para escribir, considerada 
    como el lugar principal donde el programa en ejecución debe enviar información sobre los errores 
    encontrados durante su trabajo.
    - No hemos presentado ningún método para enviar datos a este stream (lo haremos pronto, lo prometemos).
    - La separación de stdout (resultados útiles producidos por el programa) de stderr (mensajes de 
    error, indudablemente útiles pero no proporcionan resultados) ofrece la posibilidad de redirigir 
    estos dos tipos de información a los diferentes objetivos. Una discusión más extensa sobre este tema 
    está más allá del alcance de nuestro curso. El manual del sistema operativo proporcionará más información 
    sobre estos temas.
'''