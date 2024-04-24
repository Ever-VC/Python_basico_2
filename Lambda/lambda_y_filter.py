'''
Otra función de Python que se puede embellecer significativamente 
mediante la aplicación de una lambda es filter().

Espera el mismo tipo de argumentos que map(), pero hace algo diferente: 
filtra su segundo argumento mientras es guiado por direcciones que fluyen 
desde la función especificada en el primer argumento (la función se 
invoca para cada elemento de la lista, al igual que en map()).

Los elementos que devuelven True de la función pasan el filtro, los 
otros son rechazados.

El ejemplo en el editor muestra la función filter() en acción.
'''

from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

'''
Nota: hemos hecho uso del módulo random para inicializar el 
generador de números aleatorios con la función 
seed(), para producir cinco valores enteros aleatorios de -10 a 10 
usando la función randint().

Luego se filtra la lista y solo se aceptan los números que son pares y mayores que cero.

Por supuesto, no es probable que recibas los mismos resultados
'''