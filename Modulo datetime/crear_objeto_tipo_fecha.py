'''
Obtener la fecha local y crear objetos del tipo fecha
Una de las clases proporcionadas por el módulo datetime es una clase llamada date. 
Los objetos de esta clase representan una fecha que consta de año, mes y día. 
Mira el código en el editor para ver cómo se ve en la práctica y como obtener la 
fecha local actual usando el método today.

Ejecuta el código para ver qué sucede.
'''

from datetime import date

today = date.today()

print("Hoy:", today)
print("Año:", today.year)
print("Mes:", today.month)
print("Día:", today.day)

'''
El método today devuelve un objeto del tipo date que representa la fecha local actual. 
Toma en cuenta que el objeto date tiene tres atributos: año, mes y día.

Ten cuidado, porque estos atributos son de solo lectura. Para crear un objeto date, debes 
pasar los parámetros año, mes y día de la siguiente manera:
'''
print('-'*20)

my_date = date(2019, 11, 4)
print(my_date)

'''
Al crear un objeto date, toma en cuenta las siguientes restricciones:

┌------------------------------------------------------------------------------------------------------------------------┐
| Parámetro |                                               Restricciones                                                |
|-----------|------------------------------------------------------------------------------------------------------------|
|   year    |El parámetro year debe ser mayor o igual a 1 (constante MINYEAR) y menor o igual a 9999 (constante MAXYEAR).|
|-----------|------------------------------------------------------------------------------------------------------------|
|   month   |El parámetro month debe ser mayor o igual a 1 y menor o igual a 12.                                         |
|-----------|------------------------------------------------------------------------------------------------------------|
|   day     |El parámetro day debe ser mayor o igual a 1 y menor o igual que el último día del mes y año indicados.      |
└------------------------------------------------------------------------------------------------------------------------┘


'''