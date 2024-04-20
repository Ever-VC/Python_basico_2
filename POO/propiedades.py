'''
En general, una clase puede equiparse con dos tipos diferentes 
de datos para formar las propiedades de una clase.

Este tipo de propiedad existe solo cuando se crea explícitamente 
y se agrega a un objeto. Esto se puede hacer durante la 
inicialización del objeto, realizada por el constructor.

Además, se puede hacer en cualquier momento de la vida del objeto. 
Es importante mencionar también que cualquier propiedad 
existente se puede eliminar en cualquier momento.

Tal enfoque tiene algunas consecuencias importantes:

    Diferentes objetos de la misma clase pueden poseer 
    diferentes conjuntos de propiedades.

    Debe haber una manera de verificar con seguridad si un 
    objeto específico posee la propiedad que deseas utilizar 
    (a menos que quieras generar una excepción, siempre vale la pena considerarlo).

    Cada objeto lleva su propio conjunto de propiedades, no 
    interfieren entre sí de ninguna manera.

Tales variables (propiedades) se llaman variables de instancia.

La palabra instancia sugiere que están estrechamente conectadas a los 
objetos (que son instancias de clase), no a las clases mismas. 
Echemos un vistazo más de cerca.
'''

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val
 
    def set_second(self, val):
        self.second = val
 
 
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
 
example_object_2.set_second(3)
 
example_object_3 = ExampleClass(4)
example_object_3.third = 5
 
print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

'''
Los objetos de Python, cuando se crean, están dotados de un pequeño 
conjunto de propiedades y métodos predefinidos. Cada objeto los 
tiene, los quieras o no. Uno de ellos es una variable llamada __dict__ (es un diccionario).

La variable contiene los nombres y valores de todas las propiedades (variables) que 
el objeto contiene actualmente. Vamos a usarla para presentar de forma 
segura el contenido de un objeto.

Vamos a sumergirnos en el código ahora:

La clase llamada ExampleClass tiene un constructor, el cual crea 
incondicionalmente una variable de instancia llamada first, y le 
asigna el valor pasado a través del primer argumento (desde la perspectiva 
del usuario de la clase) o el segundo argumento (desde la perspectiva 
del constructor); ten en cuenta el valor predeterminado del parámetro: 
cualquier cosa que puedas hacer con un parámetro de función regular 
también se puede aplicar a los métodos.

La clase también tiene un método que crea otra variable de instancia, llamada second.

Hemos creado tres objetos de la clase ExampleClass, pero todas estas instancias difieren:

example_object_1 solo tiene una propiedad llamada first.

example_object_2 tiene dos propiedades: first y second.

example_object_3 ha sido enriquecido sobre la marcha con una propiedad 
llamada third fuera del código de la clase: esto es posible y totalmente permisible.
'''