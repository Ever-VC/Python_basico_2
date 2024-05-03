'''
-> Métodos que devuelven la fecha y hora actual <-

La clase datetime tiene varios métodos que devuelven la fecha y hora actuales. Estos métodos son:

today(): devuelve la fecha y hora local actual con el atributo tzinfo establecido a None.

now(): devuelve la fecha y hora local actual igual que el método today, a menos que 
le pasemos el argumento opcional tz. El argumento de este método debe ser un objeto de la subclase tzinfo.

utcnow(): devuelve la fecha y hora UTC actual con el atributo tzinfo establecido a None.


Ejecuta el código en el editor para verlos todos en la práctica. ¿Qué puedes decir sobre la salida?
'''

from datetime import datetime

print("hoy:", datetime.today())
print("ahora:", datetime.now())
print("utc_ahora:", datetime.utcnow())

'''
Como puedes ver, el resultado de los tres métodos es el mismo. 
Las pequeñas diferencias se deben al tiempo transcurrido entre llamadas posteriores.

Nota: Puedes leer más sobre los objetos tzinfo en la documentación.
'''