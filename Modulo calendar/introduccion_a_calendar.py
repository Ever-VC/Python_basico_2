'''
-> Introducción al módulo calendar <-

Además de los módulos datetime y time, la biblioteca estándar de Python 
proporciona un módulo llamado calendar que, como su nombre indica, ofrece 
funciones relacionadas con el calendario.

Uno de ellos es, por supuesto, mostrar el calendario. Es importante que los 
días de la semana se muestren de lunes a domingo, y cada día de la semana 
tiene su representación en forma de número entero:

┌-------------------------------------------------------┐
| Día de la semana  | Valor entero |      Constante     |
|-------------------|--------------|--------------------|
|       Lunes       |       0      |  calendar.MONDAY   |
|-------------------|--------------|--------------------|
|       Martes      |       1      |  calendar.TUESDAY  |
|-------------------|--------------|--------------------|
|     Miercoles     |       2      | calendar.WEDNESDAY |
|-------------------|--------------|--------------------|
|       Jueves      |       3      |  calendar.THURSDAY |
|-------------------|--------------|--------------------|
|      Viernes      |       4      |  calendar.FRIDAY   |
|-------------------|--------------|--------------------|
|       Sábado      |       5      | calendar.SATURDAY  |
|-------------------|--------------|--------------------|
|      Domingo      |       6      |  calendar.SUNDAY   |
└-------------------------------------------------------┘

La tabla de arriba muestra la representación de los días de la semana en el módulo calendar. 
El primer día de la semana (lunes) está representado por el valor 0 y la constante 
calendar.MONDAY, mientras que el último día de la semana (domingo) está representado 
por el valor 6 y la constante calendar.SUNDAY.
'''