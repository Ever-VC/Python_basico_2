import time

class Vehicle:
    def change_direction(left, on):
        pass

    def turn(left):
        change_direction(left, True)
        time.sleep(0.25)
        change_direction(left, False)


class TrackedVehicle(Vehicle):
    def control_track(left, stop):
        pass

    def change_direction(left, on):
        control_track(left, on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass

    def change_direction(left, on):
        turn_front_wheels(left, on)
        
'''
Esto es lo que hemos hecho:

Definimos una superclase llamada Vehicle, la cual utiliza el método turn() 
para implementar un esquema para poder girar, mientras que el giro en si 
es realizado por change_direction(); nota: dicho método está vacío, ya 
que vamos a poner todos los detalles en la subclase (dicho método a menudo 
se denomina método abstracto, ya que solo demuestra alguna posibilidad que 
será instanciada más tarde).
Definimos una subclase llamada TrackedVehicle (nota: es derivada de la clase 
Vehicle) la cual instancia el método change_direction() utilizando el método 
denominado control_track().
Respectivamente, la subclase llamada WheeledVehicle hace lo mismo, pero usa 
el método turn_front_wheels() para obligar al vehículo a girar.
La ventaja más importante (omitiendo los problemas de legibilidad) es que esta 
forma de código te permite implementar un nuevo algoritmo de giro simplemente 
modificando el método turn(), lo cual se puede hacer en un solo lugar, ya que 
todos los vehículos lo obedecerán.

Así es como el el poliformismo ayuda al desarrollador a mantener el código limpio y consistente.

La herencia no es la única forma de construir clases adaptables. Puedes lograr 
los mismos objetivos (no siempre, pero muy a menudo) utilizando una técnica llamada composición.

La composición es el proceso de componer un objeto usando otros objetos 
diferentes. Los objetos utilizados en la composición entregan un conjunto de 
rasgos deseados (propiedades y/o métodos), podemos decir que actúan como bloques 
utilizados para construir una estructura más complicada.

Puede decirse que:

La herencia extiende las capacidades de una clase agregando nuevos componentes 
y modificando los existentes; en otras palabras, la receta completa está contenida 
dentro de la clase misma y todos sus ancestros; el objeto toma todas las 
pertenencias de la clase y las usa.
La composición proyecta una clase como contenedor capaz de almacenar y usar 
otros objetos (derivados de otras clases) donde cada uno de los objetos 
implementa una parte del comportamiento de una clase.
Permítenos ilustrar la diferencia usando los vehículos previamente definidos. 
El enfoque anterior nos condujo a una jerarquía de clases en la que la clase 
más alta conocía las reglas generales utilizadas para girar el vehículo, pero 
no sabía cómo controlar los componentes apropiados (ruedas o pistas).

Las subclases implementaron esta capacidad mediante la introducción de mecanismos 
especializados. Hagamos (casi) lo mismo, pero usando composición. La clase, como 
en el ejemplo anterior, sabe cómo girar el vehículo, pero el giro real lo realiza 
un objeto especializado almacenado en una propiedad llamada controlador. El 
controlador es capaz de controlar el vehículo manipulando las partes relevantes 
del vehículo.
'''