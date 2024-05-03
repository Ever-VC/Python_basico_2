'''
-> El calendario para un mes específico <-

El módulo calendar tiene una función llamada month, que permite mostrar 
un calendario para un mes específico. Su uso es realmente simple, solo 
necesita especificar el año y el mes, consulta el código en el editor.
'''
import calendar
print(calendar.month(2020, 11))

'''
El ejemplo muestra el calendario de noviembre de 2020. Al igual que en la 
función calendar, puedes cambiar el formato predeterminado utilizando 
los siguientes parámetros:

    w: ancho de la columna de fecha (por defecto 2).
    l : número de líneas por semana (por defecto 1).

Nota: También puedes utilizar la función prmonth, que tiene los mismos parámetros 
que la función month, pero no requiere el uso de la función print para mostrar 
el calendario.
'''