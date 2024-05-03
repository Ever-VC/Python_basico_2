'''
El método strptime()

Saber cómo crear un formato puede ser útil cuando se usa un método 
llamado strptime en la clase datetime. A diferencia del método strftime, crea 
un objeto datetime a partir de una cadena que representa una fecha y una hora.

El método strptime requiere que especifiques el formato en el que guardaste la 
fecha y la hora. Veámoslo en un ejemplo. Echa un vistazo al código en el editor.
'''
from datetime import datetime
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

'''
Resultado:

    2019-11-04 14:53:00

En el ejemplo, hemos especificado dos argumentos obligatorios. El primero es una 
fecha y hora como una cadena: "2019/11/04 14:53:00", mientras que el segundo es un 
formato que facilita el análisis a un objeto datetime. Ten cuidado, porque si el formato 
que se especifica no coincide con la fecha y la hora en la cadena, generará un excepción ValueError.

Nota: En el módulo time, puedes encontrar una función llamada strptime, que analiza 
una cadena que representa un tiempo en un objeto struct_time. Su uso es análogo al 
método strptime en la clase datetime:


import time
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
 

Su resultado será el siguiente:

time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=-1)
'''