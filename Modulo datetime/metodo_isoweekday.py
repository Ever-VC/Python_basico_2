'''
La clase date tiene un método similar a weekday, llamado isoweekday, que también 
devuelve el día de la semana como un número entero, pero 1 es lunes y 7 es domingo:
'''
from datetime import date
 
d = date(2019, 11, 4)
print(d.isoweekday())# Salida: 1

'''
Como puedes ver, para la misma fecha usada con el método weekday obtenemos un número 
entero diferente, pero expresando el mismo día de la semana. El entero devuelto 
por el método isodayweek sigue la especificación ISO 85601
'''