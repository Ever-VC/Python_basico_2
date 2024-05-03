'''
-> Dando formato a la fecha y hora <-

Todas las clases del módulo datetime presentadas hasta ahora tienen un método 
llamado strftime. Este es un método muy importante, porque nos permite devolver 
la fecha y la hora en el formato que especificamos.

El método strftime toma solo un argumento en forma de cadena que especifica un 
formato que puede constar de directivas.

Una directiva es una cadena que consta del carácter % (porcentaje) y una letra 
minúscula o mayúscula. Por ejemplo, la directiva %Y significa el año con el siglo 
como número decimal. Veámoslo en un ejemplo. Ejecuta el código en el editor.
'''
from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

'''
Resultado:

    2020/01/04

En el ejemplo, hemos pasado un formato que consta de tres directivas separadas 
por / (diagonal) al método strftime. Por supuesto, el carácter separador se puede 
reemplazar por otro carácter, o incluso por una cadena.

Puedes poner cualquier carácter en el formato, pero solo las directivas reconocibles se 
reemplazarán con los valores apropiados. En nuestro formato, hemos utilizado las siguientes directivas:

%Y: devuelve el año con el siglo como número decimal. En nuestro ejemplo, esto es 2020.
%m: devuelve el mes como un número decimal con relleno de ceros. En nuestro ejemplo, es 01.
%d: devuelve el día como un número decimal con relleno de ceros. En nuestro ejemplo, es 04.

Nota: Puedes encontrar todas las directivas disponibles: aquí.

El formato de hora funciona de la misma forma que el formato de fecha, pero requiere el uso de 
directivas adecuadas. Echemos un vistazo más de cerca a algunos de ellos en el editor.
'''
from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

'''
Resultado:

    14:53:00
    20/November/04 14:53:00

El primero de los formatos utilizados se refiere únicamente al tiempo. Como puede 
adivinar, %H devuelve la hora como un número decimal con ceros, %M devuelve los minutos 
como un número decimal con ceros, mientras que % S devuelve el segundo como un número 
decimal con ceros. En nuestro ejemplo, %H se reemplaza por 14, %M por 53 y %S por 00.

El segundo formato utilizado combina directivas de fecha y hora. Hay dos directivas 
nuevas, %Y y %B. La directiva %Y devuelve el año sin un siglo como un número decimal 
con ceros (en nuestro ejemplo es 20). La directiva %B devuelve el mes como el nombre 
completo de la configuración regional (en nuestro ejemplo, es noviembre).

En general, tienes mucha libertad para crear formatos, pero debes recordar usar las directivas 
correctamente. Como Pregunta , puedes comprobar qué sucede si, por ejemplo, intentas utilizar 
la directiva %Y en el formato pasado al método strftime del objeto time. Intenta averiguar 
por qué se obtuvo este resultado. ¡Buena suerte!
'''