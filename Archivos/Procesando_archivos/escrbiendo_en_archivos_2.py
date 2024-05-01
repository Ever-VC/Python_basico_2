'''
Mira el ejemplo en el editor. Hemos modificado el código anterior para escribir líneas enteras en el archivo de texto.
'''
from os import strerror

try:
    file = open('./Archivos/Procesando_archivos/newtext.txt', 'wt')
    for i in range(10):
        file.write("línea #" + str(i+1) + "\n")
    file.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
    
'''
El contenido del archivo recién creado es el mismo.

Nota: puedes usar el mismo método para escribir en el stream stderr, pero no intentes abrirlo, ya que siempre está abierto implícitamente.

Por ejemplo, si deseas enviar un mensaje de tipo cadena a stderr para distinguirlo de la salida normal del programa, puede verse así:


import sys
sys.stderr.write("Mensaje de Error")
'''