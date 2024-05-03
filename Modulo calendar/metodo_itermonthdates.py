'''
El método itermonthdates()

La clase Calendar tiene varios métodos que devuelven un iterador. Uno de ellos es el 
método itermonthdates, que requiere especificar el año y el mes.

Como resultado, se devuelven todos los días del mes y año especificados, así como 
todos los días antes del comienzo del mes o del final del mes que son necesarios 
para obtener una semana completa.

Cada día está representado por un objeto datetime.date. Echa un vistazo al ejemplo en el editor.
'''
import calendar  

c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")
    
'''
El código muestra todos los días de noviembre de 2019. Debido a que el primer día de noviembre 
de 2019 fue viernes, los siguientes días también se devuelven para obtener la semana completa: 
10/28/2019 (lunes) 10/29/2019 (martes) 10/30/2019 (miércoles) 31/10/2019 (jueves).

El último día de noviembre de 2019 fue sábado, por lo que para mantener la semana completa, se 
devuelve un día más el 12/01/2019 (domingo).
'''