'''
La herencia es una práctica común (en la programación de objetos) de 
pasar atributos y métodos de la superclase (definida y existente) 
a una clase recién creada, llamada subclase.

En otras palabras, la herencia es una forma de construir una nueva 
clase, no desde cero, sino utilizando un repertorio de rasgos ya 
definido. La nueva clase hereda (y esta es la clave) todo el 
equipamiento ya existente, pero puedes agregar algo nuevo si es necesario.

Gracias a eso, es posible construir clases más especializadas 
(más concretas) utilizando algunos conjuntos de reglas y 
comportamientos generales predefinidos.

El factor más importante del proceso es la relación 
entre la superclase y todas sus subclases (nota: si B 
es una subclase de A y C es una subclase de B, esto 
también significa que C es una subclase de A, ya que 
la relación es totalmente transitiva).

Aquí se presenta un ejemplo muy simple de herencia de dos niveles:
'''

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass

'''
Todas las clases presentadas están vacías por ahora, ya que te 
mostraremos cómo funcionan las relaciones mutuas entre las superclases 
y las subclases. Las llenaremos con contenido pronto.

Podemos decir que:

La clase Vehicle es la superclase para clases LandVehicle y TrackedVehicle.
La clase LandVehicle es una subclase de Vehicle y la superclase de TrackedVehicle al mismo tiempo.
La clase TrackedVehicle es una subclase tanto de Vehicle y LandVehicle.
El conocimiento anterior proviene de la lectura del código (en otras palabras, lo sabemos porque podemos verlo).

¿Python sabe lo mismo? ¿Es posible preguntarle a Python al respecto? Sí lo es.

Python ofrece una función que es capaz de identificar una relación entre 
dos clases, y aunque su diagnóstico no es complejo, puede verificar si 
una clase particular es una subclase de cualquier otra clase.

Así es como se ve:


```issubclass(ClassOne, ClassTwo)```

La función devuelve True si ClassOne es una subclase de ClassTwo, y False de lo contrario.

Hay dos bucles anidados. Su propósito es verificar todos los pares de clases ordenadas posibles y que 
imprima los resultados de la verificación para determinar si el par coincide con la relación subclase-superclase.
'''
for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()

'''
Como ya sabes, un objeto es la encarnación de una clase. 
Esto significa que el objeto es como un pastel horneado 
usando una receta que se incluye dentro de la clase.

Esto puede generar algunos problemas.

Supongamos que tienes un pastel (por ejemplo, resultado de un 
argumento pasado a tu función). Deseas saber que receta se ha 
utilizado para prepararlo. ¿Por qué? Porque deseas saber que 
esperar de él, por ejemplo, si contiene nueces o no, lo cual 
es información crucial para ciertas personas.

Del mismo modo, puede ser crucial si el objeto tiene (o no tiene) 
ciertas características. En otras palabras, si es un objeto de 
cierta clase o no.

Tal hecho podría ser detectado por la función llamada isinstance():

```isinstance(objectName, ClassName)```

La función devuelve True si el objeto es una instancia de la clase, o 
False de lo contrario.

Ser una instancia de una clase significa que el objeto (el pastel) se 
ha preparado utilizando una receta contenida en la clase o en una de 
sus superclases.

No lo olvides: si una subclase contiene al menos las mismas 
características que cualquiera de sus superclases, significa que 
los objetos de la subclase pueden hacer lo mismo que los objetos 
derivados de la superclase, por lo tanto, es una instancia de su 
clase de inicio y cualquiera de sus superclases.
'''

print("---------------------")
my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()
for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()

'''
Hemos creado tres objetos, uno para cada una de las clases. 
Luego, usando dos bucles anidados, verificamos todos los 
pares posibles de clase de objeto para averiguar si los 
objetos son instancias de las clases.
'''