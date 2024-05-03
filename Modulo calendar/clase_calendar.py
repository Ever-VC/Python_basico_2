'''
-> Clases para la creación de calendarios <-

Las funciones que hemos mostrado hasta ahora no son todo lo que ofrece el módulo calendar. 
Además de ellos, podemos utilizar las siguientes clases:

calendar.Calendar - proporciona métodos para preparar datos de calendario y dar formato.

calendar.TextCalendar - se utiliza para crear calendarios de texto regulares.

calendar.HTMLCalendar: se utiliza para crear calendarios HTML.

calendar.LocalTextCalendar - es una subclase de la clase calendar.TextCalendar. El constructor 
de esta clase toma el parámetro locale, el cual se utiliza para devolver los nombres apropiados 
de los meses y días de la semana.

calendar.LocalHTMLCalendar - es una subclase de la clase calendar.HTMLCalendar. El constructor 
de esta clase toma el parámetro locale, que se usa para devolver los nombres apropiados de los 
meses y días de la semana.

Durante este curso, ya tuviste la oportunidad de crear calendarios de texto al discutir las funciones del módulo calendar.

Es hora de probar algo nuevo. Echemos un vistazo más de cerca a los métodos de la clase calendar.

-> Creando un objeto Calendar <-

El constructor de la clase Calendar toma un parámetro opcional llamado firstweekday, por 
defecto es igual a 0 (lunes).

El parámetro firstweekday debe ser un valor entero entre 0-6. Para este propósito, podemos 
usar las constantes ya conocidas: mira el código en el editor.
'''
import calendar  

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")
    
'''
El programa generará el siguiente resultado:

    6 0 1 2 3 4 5
    
El ejemplo de código usa el método de la clase Calendar llamado iterweekdays, que devuelve 
un iterador para los números de los días de la semana.

El primer valor devuelto siempre es igual al valor de la propiedad firstweekday. Debido a 
que en nuestro ejemplo el primer valor devuelto es 6, significa que la semana comienza un domingo.
'''