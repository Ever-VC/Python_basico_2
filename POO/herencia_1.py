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
    