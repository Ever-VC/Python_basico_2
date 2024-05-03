'''
-> Operaciones con la fecha y hora <-

Tarde o temprano tendrás que realizar algunos cálculos sobre la fecha y 
la hora. Afortunadamente, existe una clase llamada timedelta en el módulo 
datetime que se creó con tal propósito.

Para crear un objeto timedelta, simplemente realiza una resta en los objetos 
date o datetime, tal como hicimos en el ejemplo en el editor. Ejecútalo.
'''
from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)

'''
Resultado:

    366 days, 0:00:00
    365 days, 9:07:00

El ejemplo muestra la resta para los objetos date y datetime. En el primer 
caso, recibimos la diferencia en días, que es de 366 días. Toma en cuenta 
que también se muestra la diferencia en horas, minutos y segundos. En el 
segundo caso, recibimos un resultado diferente, porque especificamos el 
tiempo que se incluyó en los cálculos. Como resultado, recibimos 365 
días, 9 horas y 7 minutos.

En un momento aprenderás más sobre la creación de los objetos timedelta 
y sobre las operaciones que puedes realizar con ellos.
'''