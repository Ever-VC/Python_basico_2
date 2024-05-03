'''
La función setfirstweekday()

Como ya sabes, por defecto en el módulo calendar, el primer día de la 
semana es el lunes. Sin embargo, puedes cambiar este comportamiento 
usando una función llamada setfirstweekday.

¿Recuerdas la tabla que muestra los días de la semana y su representación 
en forma de valores enteros? Es hora de usarla, porque el método setfirstweekday 
requiere un parámetro que exprese el día de la semana en forma de valor entero. 
Echa un vistazo al ejemplo en el editor.
'''
import calendar

calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12)

'''
El ejemplo usa la constante calendar.SUNDAY, que contiene un valor de 6. 
Por supuesto, puedes pasar este valor directamente a la función setfirstweekday, pero 
la versión con una constante es más elegante.

Como resultado, obtenemos un calendario que muestra el mes de diciembre de 2020, en 
el que el primer día de todas las semanas es el domingo.
'''