'''

-> Creando objetos datetime <-

En el módulo datetime, la fecha y la hora se pueden representar como objetos 
separados o como un solo objeto. La clase que combina fecha y hora se llama datetime.

datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)

Su constructor acepta los siguientes parámetros:

┌------------------------------------------------------------------------------------------------------------------------┐
| Parámetro |                                               Restricciones                                                |
|-----------|------------------------------------------------------------------------------------------------------------|
|   year    |El parámetro year debe ser mayor o igual a 1 (constante MINYEAR) y menor o igual a 9999 (constante MAXYEAR).|
|-----------|------------------------------------------------------------------------------------------------------------|
|   month   |El parámetro month debe ser mayor o igual a 1 y menor o igual a 12.                                         |
|-----------|------------------------------------------------------------------------------------------------------------|
|   day     |El parámetro day debe ser mayor o igual a 1 y menor o igual que el último día del mes y año indicados.      |
|-----------|------------------------------------------------------------------------------------------------------------|
|   hour    |El parámetro hour debe ser mayor o igual que 0 y menor que 23.                                              |
|-----------|------------------------------------------------------------------------------------------------------------|
|   minute  |	El parámetro minute debe ser mayor o igual que 0 y menor que 59.                                         |
|-----------|------------------------------------------------------------------------------------------------------------|
|   second  |El parámetro second debe ser mayor o igual que 0 y menor que 59.                                            |
|-----------|------------------------------------------------------------------------------------------------------------|
|microsecond|El parámetro microsecond debe ser mayor o igual que 0 y menor que 1000000.                                  |
|-----------|------------------------------------------------------------------------------------------------------------|
|   tzinfo  |El parámetro tzinfo debe ser una subclase del objeto tzinfo o None (de manera predeterminada).              |
|-----------|------------------------------------------------------------------------------------------------------------|
|   fold    |El parámetro fold debe ser 0 o 1 (predeterminadamente 0).                                                   |
└------------------------------------------------------------------------------------------------------------------------┘

Ahora echemos un vistazo al código en el editor para ver cómo creamos un objeto del tipo datetime.

    Fecha y Hora: 2019-11-04 14:53:00
    Fecha: 2019-11-04
    Hora: 14:53:00

El ejemplo crea un objeto datetime que representa el 4 de noviembre de 2019 a las 14:53:00. 
Todos los parámetros pasados al constructor van a atributos de clase de solo lectura. Son year, 
month, day, hour, minute, second, microsecond, tzinfo, y fold.

El ejemplo muestra dos métodos que devuelven dos objetos diferentes. El método llamado date devuelve 
el objeto date con el año, mes y día dados, mientras que el método llamado time devuelve el objeto 
time con la hora y minuto dados.
'''

from datetime import datetime

dt = datetime(2019, 11, 4, 14, 53, 0)

print(f'Fecha y Hora: {dt}')