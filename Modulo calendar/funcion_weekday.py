'''
La función weekday()

Otra función útil proporcionada por el módulo calendar es la función llamada weekday, que 
devuelve el día de la semana como un valor entero para el año, mes y día. Veámoslo en la práctica.

Ejecuta el código en el editor para verificar el día de la semana en que cae el 24 de diciembre de 2020.
'''
import calendar
print(calendar.weekday(2020, 12, 24))

'''
Resultado:

    3

La función weekday devuelve 3, lo que significa que el 24 de diciembre del 2020 es jueves.
'''