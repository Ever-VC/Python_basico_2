'''
-> Los módulos datetime y time <-

Durante este curso, has aprendido sobre el método strftime, que requiere 
conocimiento de las directivas para crear un formato. Ahora es el momento 
de poner en práctica estas directivas.

Por cierto, tendrás la oportunidad de practicar el trabajo con documentación, porque 
tendrás que encontrar directivas que aún no conoces.

Aquí está tu tarea:
Escribe un programa que cree un objeto datetime para el 4 de noviembre de 2020, 14:53:00. 
El objeto creado debe llamar al método strftime con el formato apropiado para mostrar el siguiente resultado:

    2020/11/04 14:53:00
    20/November/04 14:53:00 PM
    Wed, 2020 Nov 04
    Wednesday, 2020 November 04
    Día de la semana: 3
    Día del año: 309
    Número de semana en el año: 44

Nota: Cada línea de resultado debe crearse llamando al método strftime con al menos una directiva en el argumento de formato.
'''
from datetime import datetime

my_date = datetime(2020, 11, 4, 14, 53)

print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
print(my_date.strftime("%a, %Y %b %d"))
print(my_date.strftime("%A, %Y %B %d"))
print(my_date.strftime("Día de la semana: %w"))
print(my_date.strftime("Día del año: %j"))
print(my_date.strftime("Número de semana en el año: %W"))