'''
Las funciones gmtime() y localtime()
Algunas de las funciones disponibles en el módulo time requieren conocimiento 
de la clase struct_time, pero antes de conocerlas, veamos cómo se ve la clase:

```
time.struct_time:
    tm_year   # Especifica el año.
    tm_mon    # Especifica el mes (valor de 1 a 12)
    tm_mday   # Especifica el día del mes (value from 1 to 31)
    tm_hour   # Especifica la hora (valor de 0 a 23)
    tm_min    # Especifica el minuto (valor de 0 a 59)
    tm_sec    # Especifica el segundo (valor de 0 a 61)
    tm_wday    # Especifica el día de la semana (valor de 0 a 6)
    tm_yday   # Especifica el día del año (valor de 1 a 366)
    tm_isdst  # Especifica si se aplica el horario de verano (1: sí, 0: no, -1: no se sabe)
    tm_zone   # Especifica el nombre de la zona horaria (valor en forma abreviada)
    tm_gmtoff # Especifica el desplazamiento al este del UTC (valor en segundos)
```

La clase struct_time también permite el acceso a valores usando índices. 
El índice 0 devuelve el valor en tm_year, mientras que 8 devuelve el valor en tm_isdst.

Las excepciones son tm_zone y tm_gmoff, a las que no se puede acceder mediante 
índices. Veamos cómo usar la clase struct_time en la práctica. Ejecuta el código en el editor.
'''
import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))

'''
Resultado:

```
    time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
    time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
```

El ejemplo muestra dos funciones que convierten el tiempo transcurrido desde la época Unix al objeto struct_time. 
La diferencia entre ellos es que la función [gmtime] devuelve el objeto {struct_time} en UTC, mientras que la 
función [localtime] devuelve la hora local. Para la función [gmtime], el atributo tm_isdst es siempre 0.
'''