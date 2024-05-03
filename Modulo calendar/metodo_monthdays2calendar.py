'''
El método monthdays2calendar()
La clase Calendar tiene varios otros métodos útiles sobre los que puedes obtener 
más información en la documentación (https://docs.python.org/3/library/calendar.html).

Uno de ellos es el método monthdays2calendar, que toma el año y el mes, y luego devuelve 
una lista de semanas en un mes específico. Cada semana es una tupla que consta de números 
de días y números de días de la semana. Mira el código en el editor.
'''
import calendar  

c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12):
    print(data)
    
'''
Toma en cuenta que los números de los días fuera del mes están representados por 0, mientras 
que los números de los días de la semana son un número del 0 al 6, donde 0 es el lunes y 6 es el domingo.
'''