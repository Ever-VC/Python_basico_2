'''
-> Creación de un objeto de fecha usando el formato ISO <-

El módulo datetime proporciona varios métodos para crear un objeto date. 
Uno de ellos es el método fromisoformat, que toma una fecha en el 
formato [AAAA-MM-DD] compatible con el estándar ISO 8601.

El estándar ISO 8601 define cómo se representan la fecha y la hora. 
Se usa a menudo, por lo que vale la pena tomarse un momento para 
familiarizarse con él. Echa un vistazo a la imagen que describe los 
valores requeridos por el formato:

Ahora observa el código en el editor y ejecútalo.

En nuestro ejemplo, AAAA es 2019, MM es 11 (noviembre) y DD es 18 (dieciocho de noviembre).

Cuando sustituyas la fecha, asegúrate de agregar 0 antes de un mes o 
de un día expresado por un número menor que 10.

Nota: el método fromisoformat ha estado disponible en Python desde la versión 3.7.
'''

from datetime import date

my_date = date.fromisoformat('2019-11-18')
print(my_date)