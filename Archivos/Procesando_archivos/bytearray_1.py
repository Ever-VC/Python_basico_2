'''
¿Qué es un bytearray?
Antes de comenzar a hablar sobre archivos binarios, tenemos que informarte sobre una de las 
clases especializadas que Python usa para almacenar datos amorfos.

Los datos amorfos son datos que no tienen forma específica, son solo una serie de bytes.

Esto no significa que estos bytes no puedan tener su propio significado o que no puedan 
representar ningún objeto útil, por ejemplo, gráficos de mapa de bits.

Lo más importante de esto es que en el lugar donde tenemos contacto con los datos, no 
podemos, o simplemente no queremos, saber nada al respecto.

Los datos amorfos no pueden almacenarse utilizando ninguno de los medios presentados 
anteriormente: no son cadenas ni listas.

Debe haber un contenedor especial capaz de manejar dichos datos.

Python tiene más de un contenedor, uno de ellos es una clase especializada llamada 
bytearray, como su nombre indica, es un arreglo que contiene bytes (amorfos).

Si deseas tener dicho contenedor, por ejemplo, para leer una imagen de mapa de bits y 
procesarla de alguna manera, debes crearlo explícitamente, utilizando uno de los constructores disponibles.

Observa:


data = bytearray(10)
 

Tal invocación crea un objeto bytearray capaz de almacenar diez bytes.

Nota: dicho constructor llena todo el arreglo con ceros.

Bytearrays se asemejan a listas en muchos aspectos. Por ejemplo, son mutables, son susceptibles a la 
función len(), y puedes acceder a cualquiera de sus elementos usando indexación convencional.

Existe una limitación importante: no debes establecer ningún elemento del arreglo de bytes con un valor 
que no sea un entero (violar esta regla causará una excepción TypeError) y tampoco está permitido 
asignar un valor fuera del rango de 0 a 255 (a menos que quieras provocar una excepción ValueError).

Puedes tratar cualquier elemento del arreglo de bytes como un valor entero, al igual que en el ejemplo en el editor.
'''

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))
    
'''
Nota: hemos utilizado dos métodos para iterar el arreglo de bytes, y hemos utilizado la función hex() 
para ver los elementos impresos como valores hexadecimales.

Ahora te vamos a mostrar como escribir un arreglo de bytes en un archivo binario, como no queremos 
guardar su representación legible, queremos escribir una copia uno a uno del contenido de la memoria física, byte a byte.
'''