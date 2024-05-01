'''
Escribir archivos de texto parece ser más simple, ya que hay un método que puede usarse para realizar dicha tarea.

El método se llama write() y espera solo un argumento: una cadena que se transferirá a un archivo 
abierto (no lo olvides), el modo de apertura debe reflejar la forma en que se transfieren los 
datos, escribir en un archivo abierto en modo de lectura no tendrá éxito).

No se agrega carácter de nueva línea al argumento de write(), por lo que debes agregarlo tu mismo si 
deseas que el archivo se complete con varias líneas.

El ejemplo en el editor muestra un código muy simple que crea un archivo llamado newtext.txt 
(nota: el modo de apertura w asegura que el archivo se creará desde cero, incluso si existe y contiene datos) 
y luego coloca diez líneas en él.
'''
from os import strerror

try:
	file = open('./Archivos/Procesando_archivos/newtext.txt', 'wt') # Un nuevo archivo (newtext.txt) es creado.
	for i in range(10):
		s = "línea #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))

'''
La cadena que se grabará consta de la palabra línea, seguida del número de línea. 
Hemos decidido escribir el contenido de la cadena carácter por carácter (esto lo hace 
el bucle interno for) pero no estás obligado a hacerlo de esta manera.

Solo queríamos mostrarte que write() puede operar con caracteres individuales.

El código crea un archivo con el siguiente texto:

línea #1
línea #2
línea #3
línea #4
línea #5
línea #6
línea #7
línea #8
línea #9
línea #10

¿Puedes imprimir el contenido del archivo en la consola?

Te alentamos a que pruebes el comportamiento del método write() localmente en tu máquina.

'''
    