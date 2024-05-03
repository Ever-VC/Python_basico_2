'''
-> Tu primer calendario <-

Comenzarás tu aventura con el módulo calendar con una función simple llamada 
calendar, que te permite mostrar el calendario para todo el año. Veamos cómo 
usarlo para mostrar el calendario de 2020. Ejecuta el código en el editor y 
ve qué sucede.
'''
import calendar
print(calendar.calendar(2020))

'''
El resultado mostrado es similar al resultado del comando cal disponible en Unix. 
Si deseas cambiar el formato de calendario predeterminado, puedes utilizar los siguientes parámetros:

    w: ancho de la columna de fecha (por defecto 2).
    l: número de líneas por semana (por defecto 1).
    c: número de espacios entre las columnas del mes (por defecto 6).
    m: número de columnas (por defecto 3).
    
La función de calendario requiere que se especifique el año, mientras que los 
otros parámetros responsables del formato son opcionales. Te recomendamos 
que pruebes estos parámetros tu mismo.

Una buena alternativa a la función anterior es la función llamada prcal, que 
también toma los mismos parámetros que la función calendar, pero no requiere 
el uso de la función print para mostrar el calendario. Su uso se ve así:


    import calendar
    calendar.prcal(2020)
'''