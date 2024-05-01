'''
Si deseas manejar el contenido del archivo como un conjunto de líneas, no como 
un montón de caracteres, el método readline() te ayudará con eso.

El método intenta leer una línea completa de texto del archivo, y la devuelve como 
una cadena en caso de éxito. De lo contrario, devuelve una cadena vacía.

Esto abre nuevas oportunidades: ahora también puedes contar líneas fácilmente, no solo caracteres.

Hagamos uso de ello. Observa el código en el editor.
'''
from os import strerror

try:
    character_counter = line_counter = 0
    stream = open('./Archivos/Procesando_archivos/text.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCaracteres en el archivo:", character_counter)
    print("Líneas en el archivo:     ", line_counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
    
'''
Como puedes ver, la idea general es exactamente la misma que en los dos ejemplos anteriores.
'''