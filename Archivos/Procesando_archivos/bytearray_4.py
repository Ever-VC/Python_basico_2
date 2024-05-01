'''
Ahora vas a juntar todo este nuevo conocimiento, agregarle algunos elementos nuevos 
y usarlo para escribir un código real que pueda copiar el contenido de un archivo.

Por supuesto, el propósito no es crear un reemplazo para los comandos como copy 
de (MS Windows) o cp de (Unix/Linux) pero para ver una forma posible de crear una 
herramienta de trabajo, incluso si nadie quiere usarla.

Observa el código en el editor.
'''
from os import strerror

srcname = input("Ingresa el nombre del archivo fuente: ")
try:
    src = open('./Archivos/Procesando_archivos/' + srcname, 'rb')
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)	

dstname = input("Ingresa el nombre del archivo destino: ")
try:
    dst = open('./Archivos/Procesando_archivos/' + dstname, 'wb')
except Exception as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) escritos con éxito')
src.close()
dst.close()

'''
Analicémoslo:

Las líneas 13 a la 18: solicitan al usuario el nombre del archivo a copiar e intentan abrirlo para leerlo; se 
termina la ejecución del programa si falla la apertura; nota: emplea la función exit() para detener la 
ejecución del programa y pasar el código de finalización al sistema operativo; cualquier código de finalización 
que no sea 0 significa que el programa ha encontrado algunos problemas; se debe utilizar el valor errno para 
especificar la naturaleza del problema.

Las líneas 20 a la 26: repiten casi la misma acción, pero esta vez para el archivo de salida.

La línea 28: prepara una parte de memoria para transferir datos del archivo fuente al destino; tal 
área de transferencia a menudo se llama un búfer, de ahí el nombre de la variable; el tamaño del búfer 
es arbitrario; en este caso, decidimos usar 64 kilobytes; técnicamente, un búfer más grande es más rápido 
al copiar elementos, ya que un búfer más grande significa menos operaciones de E/S; en realidad, siempre 
hay un límite, cuyo cruce no genera más ventajas; pruébalo tú mismo si quieres.

Línea 29: cuenta los bytes copiados: este es el contador y su valor inicial.

Línea 31: intenta llenar el búfer por primera vez.

Línea 32: mientras se obtenga un número de bytes distinto a cero, repite las mismas acciones.

Línea 33: escribe el contenido del búfer en el archivo de salida (nota: hemos usado un segmento para 
limitar la cantidad de bytes que se escriben, ya que write() siempre prefiere escribir todo el búfer).

Línea 34: actualiza el contador.

Línea 35: lee el siguiente fragmento de archivo.

Las líneas 40 a la 42: limpieza final, el trabajo está hecho.
'''