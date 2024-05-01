'''
¿Dónde estoy ahora?
Ya sabes cómo crear directorios y cómo moverte entre ellos.

A veces, cuando tienes una estructura de directorio muy grande en la que 
navegas, es posible que no sepas en qué directorio estás trabajando actualmente.


Como probablemente habrás adivinado, el módulo os proporciona una función que 
devuelve información sobre el directorio de trabajo actual. Se llama getcwd.

Mira el código en el editor para ver cómo usarlo en la práctica.
'''
import os

print(os.getcwd())
os.chdir("./Modulo os/my_second_directory/my_third_directory")
print(os.getcwd())

'''
En el ejemplo mostramos el directorio de trabajo actual (primera línea del resultado).

A continuación, vamos al directorio my_third_directory y nuevamente mostramos el directorio 
de trabajo actual (segunda línea del resultado). Como puedes ver, la función getcwd devuelve 
la ruta absoluta a los directorios.

NOTA: En sistemas tipo Unix, el equivalente de la función getcwd es el comando pwd, que 
imprime el nombre del directorio de trabajo actual.
'''
    