'''
Para eliminar un directorio y sus subdirectorios, puedes utilizar la 
función removedirs, que requiere que se especifique una ruta que 
contenga todos los directorios que deben eliminarse:
'''

import os
 
os.makedirs("./Modulo os/sample_1/sample_2")
os.chdir("./Modulo os")
os.removedirs("sample_1/sample_2")
print(os.listdir())

'''
Al igual que con la función rmdir, si uno de los directorios no existe 
o no está vacío, se generará una excepción.

NOTA: Tanto en Windows como en Unix, hay un comando llamado rmdir, que, al 
igual que la función rmdir, elimina directorios. Además, ambos sistemas 
tienen comandos para eliminar un directorio y su contenido. En Unix, este 
es el comando rm con el indicador -r.
'''