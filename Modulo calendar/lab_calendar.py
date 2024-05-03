'''
El módulo calendar

Durante este curso, echamos un breve vistazo a la clase Calendar. Tu tarea ahora es ampliar 
su funcionalidad con un nuevo método llamado count_weekday_in_year, que toma un año y un día 
de la semana como parámetros, y luego devuelve el número de ocurrencias de un día de la semana específico en el año.

Utiliza los siguientes consejos:

Crea una clase llamada MyCalendar que se extiende de la clase Calendar.

Crea el método count_weekday_in_year con los parámetros de year y weekday. El parámetro weekday 
debe tener un valor entre 0 y 6, donde 0 es el lunes y 6 es el domingo. El método debe devolver 
el número de días como un número entero.

En tu implementación, usa el método monthdays2calendar de la clase Calendar.

Los siguientes son resultados esperados de ejemplo:

Argumentos de muestra

    year=2019, weekday=0

Salida esperada

    52

Argumentos de muestra

    year=2000, weekday=6

Salida esperada

    53
'''
import calendar


class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        current_month = 1
        number_of_days = 0
        while (current_month <= 12):
            for data in self.monthdays2calendar(year, current_month):
                if data[weekday][0] != 0:
                    number_of_days = number_of_days + 1

            current_month = current_month + 1
        return number_of_days

my_calendar = MyCalendar()
number_of_days = my_calendar.count_weekday_in_year(2019, calendar.MONDAY)

print(number_of_days)
