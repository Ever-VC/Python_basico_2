'''
La función lambda es un concepto tomado de las matemáticas, más 
específicamente, de una parte llamada el Cálculo Lambda, pero 
estos dos fenómenos no son iguales.

Los matemáticos usan el Cálculo Lambda en sistemas formales 
conectados con: la lógica, la recursividad o la demostrabilidad 
de teoremas. Los programadores usan la función lambda para 
simplificar el código, hacerlo más claro y fácil de entender.

Una función lambda es una función sin nombre (también puedes 
llamarla una función anónima). Por supuesto, tal afirmación 
plantea inmediatamente la pregunta: ¿cómo se usa algo que no 
se puede identificar?

Afortunadamente, no es un problema, ya que se puede mandar 
llamar dicha función si realmente se necesita, pero, en 
muchos casos la función lambda puede existir y funcionar 
mientras permanece completamente de incógnito.

La declaración de la función lambda no se parece a una 
declaración de función normal; compruébalo tu mismo:

```lambda parameters: expression```
 

Tal cláusula devuelve el valor de la expresión al tomar 
en cuenta el valor del argumento lambda actual.

Como de costumbre, un ejemplo será útil. Nuestro ejemplo 
usa tres funciones lambda, pero con nombres.
'''
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y
 
for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))
'''
Vamos a analizarlo:

La primer lambda es una función anónima sin parámetros que siempre 
devuelve un 2. Como se ha asignado a una variable llamada two, podemos 
decir que la función ya no es anónima, y se puede usar su nombre para invocarla.

La segunda es una función anónima de un parámetro que devuelve el 
valor de su argumento al cuadrado. Se ha nombrado sqr.

La tercer lambda toma dos parámetros y devuelve el valor del primero 
elevado al segundo. El nombre de la variable que lleva la lambda habla 
por si mismo. No se utiliza pow para evitar confusiones con la función 
incorporada del mismo nombre y el mismo propósito.

Este ejemplo es lo suficientemente claro como para mostrar como se 
declaran las funciones lambda y cómo se comportan, pero no dice nada 
acerca de por que son necesarias y para qué se usan, ya que se pueden 
reemplazar con funciones de Python de rutina.

¿Dónde está el beneficio?
'''