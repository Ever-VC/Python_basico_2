'''
Otros métodos que retornan o devuelven iteradores

Otro método útil en la clase Calendar es el método llamado itermonthdates, que 
toma año y mes como parámetros, y luego devuelve el iterador a los días de la semana 
representados por números.

Mira el ejemplo en el editor.
'''
import calendar  

c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")
    
'''
Sin duda habrás notado la gran cantidad de ceros devueltos como resultado del código de ejemplo. 
Estos son días fuera del intervalo de meses especificado que se agregan para mantener la semana completa.

Los primeros cuatro ceros representan el 28/10/2019 (lunes) el 29/10/2019 (martes) el 
30/10/2019 (miércoles) el 31/10/2019 (jueves). Los números restantes son días del mes, excepto 
el último valor de 0, que reemplaza la fecha 12/01/2019 (domingo).

Hay otros cuatro métodos similares en la clase Calendar que difieren en los datos devueltos:

itermonthdates2 - devuelve días en forma de tuplas que consisten en un número de día del mes y un número de día de la semana.

itermonthdates3 - devuelve días en forma de tuplas que constan de un año, un mes y un día de los números del mes. 
Este método ha estado disponible desde la versión 3.7 de Python.

itermonthdates4 - devuelve días en forma de tuplas que constan de números de año, mes, día del mes y día de la semana. 
Este método ha estado disponible desde la versión 3.7 de Python.

Con fines de prueba, utiliza el ejemplo anterior y ve cómo se ven en la práctica los valores de retorno de los métodos descritos.
'''