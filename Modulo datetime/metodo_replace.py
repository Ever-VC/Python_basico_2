'''
-> El método replace() <-

A veces, es posible que debas reemplazar el año, el mes o el día con 
un valor diferente. No puedes hacer esto con los atributos de año, mes 
y día porque son de solo lectura. En este caso, puedes utilizar el 
método llamado replace.

Ejecuta el código en el editor.
'''

from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

'''
Los parámetros year, month y day son opcionales. Puedes pasar solo un parámetro 
al método replace, por ejemplo, año, o los tres como en el ejemplo.

El método replace devuelve un objeto date modificado, por lo que debes recordar asignarlo a alguna variable
'''