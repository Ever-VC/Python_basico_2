'''
Creación de un objeto de fecha a partir de una marca de tiempo
La clase date nos da la capacidad de crear un objeto del tipo fecha a 
partir de una marca de tiempo.

En Unix, la marca de tiempo expresa el número de segundos desde el 
1 de Enero de 1970 a las 00:00:00 (UTC). Esta fecha se llama la época 
Unix, porque es cuando comenzó el conteo del tiempo en los sistemas Unix.

La marca de tiempo es en realidad la diferencia entre una fecha en 
particular (incluida la hora) y el 1 de enero de 1970, 00:00:00 (UTC), expresada en segundos.

Para crear un objeto de fecha a partir de una marca de tiempo, debemos 
pasar una marca de tiempo Unix al método fromtimestamp.

Para este propósito, podemos usar el módulo time, que proporciona funciones 
relacionadas con el tiempo. Uno de ellos es una función llamada time(), 
que devuelve el número de segundos desde el 1 de enero de 1970 hasta el 
momento actual en forma de número flotante. Echa un vistazo al ejemplo en el editor.
'''

from datetime import date
import time

timestamp = time.time()
print("Marca de tiempo:", timestamp)

d = date.fromtimestamp(timestamp)
print("Fecha:", d)

'''
Ejecuta el código para ver el resultado.

Si ejecutas el código de muestra varias veces, podrás ver cómo se 
incrementa la marca de tiempo. Vale la pena agregar que el resultado 
de la función time depende de la plataforma, porque en los sistemas Unix y Windows, los 
segundos intercalares no se cuentan.

Nota: en esta parte del curso también hablaremos sobre el módulo time.
'''