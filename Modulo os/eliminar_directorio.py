'''
-> Eliminando directorios en Python <-

El módulo os también te permite eliminar directorios. Te da la opción de borrar 
un solo directorio o un directorio con sus subdirectorios. Para eliminar un solo 
directorio, puedes usar una función llamada rmdir, que toma la ruta como argumento. 
Mira el código en el editor.
'''

import os

os.mkdir("./Modulo os/sampledir")
os.chdir("./Modulo os")
print(os.listdir())
os.rmdir("sampledir")
print(os.listdir())

'''
El ejemplo anterior es realmente simple. Primero, se crea el directorio sampledir y 
luego se elimina usando la función rmdir. La función listdir se utiliza como prueba 
de que el directorio se ha eliminado correctamente. En este caso, devuelve una lista 
vacía. Al eliminar un directorio, asegúrate de que exista y esté vacío; de lo 
contrario, se generará una excepción.
'''