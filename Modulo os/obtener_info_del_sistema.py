'''
-> Obteniendo información sobre el sistema operativo <-


Antes de crear tu primera estructura de directorios, verás cómo puedes obtener información 
sobre el sistema operativo actual. Esto es realmente fácil porque el módulo os proporciona 
una función llamada uname, que devuelve un objeto que contiene los siguientes atributos:

systemname - almacena el nombre del sistema operativo.
nodename - almacena el nombre de la máquina en la red.
release - almacena el release o actualización del sistema operativo.
version - almacena la versión del sistema operativo.
machine - almacena el identificador de hardware, por ejemplo, x86_64.
Veamos cómo es en la práctica:
'''

import os
print(os.uname())

'''
Resultado:

```
posix.uname_result(sysname='Linux', nodename='debian', release='6.1.0-20-amd64', version='#1 SMP PREEMPT_DYNAMIC Debian 6.1.85-1 (2024-04-11)', machine='x86_64')
```

Como puedes ver, la función uname devuelve un objeto que contiene información sobre el sistema operativo. 
El código anterior se ejecutó en Debian 12, así que no te sorprendas si obtienes un resultado 
diferente, porque depende de tu sistema operativo.

Desafortunadamente, la función uname solo funciona en algunos sistemas Unix. Si usas Windows, puede usar 
la función uname en el módulo plataform, que devuelve un resultado similar.

El módulo os te permite distinguir rápidamente el sistema operativo mediante el atributo name, que 
soporta uno de los siguientes nombres:

posix - obtendrás este nombre si usas Unix.
nt - obtendrás este nombre si usas Windows.
java - obtendrás este nombre si tu código está escrito en Jython.

Para Debian 12, el atributo name devuelve el nombre posix:
'''

print(os.name)

'''
NOTA: En los sistemas Unix, hay un comando llamado uname que devuelve la misma información (si lo ejecutas con la opción -a) que la función uname.
'''