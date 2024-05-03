'''
La función weekheader()

Probablemente hayas notado que el calendario contiene encabezados semanales 
en forma abreviada. Si es necesario, puedes obtener nombres cortos de días de 
la semana utilizando el método weekheader.

El método weekheader requiere que se especifique el ancho en caracteres para 
un día de la semana. Si el ancho que se proporciona es mayor que 3, aún obtendrás 
los nombres abreviados de los días de la semana que constan de tres caracteres.

Entonces, veamos cómo obtener un encabezado más pequeño. Ejecuta el código en el editor.
'''
import calendar
print(calendar.weekheader(2))

'''
Resultado:

Mo Tu We Th Fr Sa Su

Nota: Si cambias el primer día de la semana, por ejemplo, usando la función 
setfirstweekday, afectará el resultado de la función weekheader.
'''