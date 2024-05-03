'''
¿Cómo comprobamos si un año es bisiesto?

El módulo calendar proporciona dos funciones útiles para comprobar si los años son bisiestos.

La primera, llamada isleap, devuelve True si el año pasado es bisiesto, o False d
e lo contrario. El segundo, llamado leapdays, devuelve el número de años bisiestos en el rango de años dado.

Ejecuta el código en el editor.
'''
import calendar

print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2021))  # Hasta 2021, pero sin incluirlo.

'''
Resultado:

    True
    3

En el ejemplo, obtenemos el resultado 3, porque en el período de 2010 a 2020 solo hay 
tres años bisiestos (nota: 2021 no está incluido). Son los años 2012, 2016 y 2020.
'''