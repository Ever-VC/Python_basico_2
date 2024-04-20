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

También existe un operador de Python que vale la pena mencionar, ya 
que se refiere directamente a los objetos - aquí está:

```object_one is object_two```

El operador is verifica si dos variables, en este caso 
(object_one y object_two) se refieren al mismo objeto.

No olvides que las variables no almacenan los objetos en sí, sino 
solo los identificadores que apuntan a la memoria interna de Python.

Asignar un valor de una variable de objeto a otra variable no copia 
el objeto, sino solo su identificador. Es por ello que un operador 
como is puede ser muy útil en ciertas circunstancias.
'''

class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print("---------------------")
print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)
string_1 = "Mary tenía un "
string_2 = "Mary tenía un corderito"
string_1 += "corderito"

print(string_1 == string_2, string_1 is string_2)

'''
Analicémoslo:

Existe una clase muy simple equipada con un constructor simple, que 
crea una sola propiedad. La clase se usa para instanciar dos objetos. 
El primero se asigna a otra variable, y su propiedad val se incrementa en uno.

Luego, el operador is se aplica tres veces para verificar todos los 
pares de objetos posibles, y todos los valores de la propiedad val 
son mostrados en pantalla.

La última parte del código lleva a cabo otro experimento. 
Después de tres tareas, ambas cadenas contienen los mismos textos, pero 
estos textos se almacenan en diferentes objetos.
'''