'''
Si deseas que el método acepte parámetros distintos a self, debes:

    Colocarlos después de self en la definición del método.
    Pasarlos como argumentos durante la invocación sin especificar self.

El parámetro self es usado para obtener acceso a la instancia del objeto y las variables de clase.
El parámetro self también se usa para invocar otros métodos desde dentro de la clase.
Justo como aqui:
'''

class Classy1:
    varia = 2
    def other(self):
        print("otro")

    def method(self, par):
        print("método:", par)
        print(self.varia, self.var)
        self.other()
 
 
obj = Classy1()
obj.var = 3
obj.method(1)

'''
Si se nombra un método de esta manera: __init__, no 
será un método regular, será un constructor.

Si una clase tiene un constructor, este se invoca 
automática e implícitamente cuando se instancia el objeto de la clase.

El constructor:

Esta obligado a tener el parámetro self (se configura automáticamente).

Pudiera (pero no necesariamente) tener mas parámetros que solo self; si 
esto sucede, la forma en que se usa el nombre de la clase para crear 
el objeto debe tener la definición __init__.

Se puede utilizar para configurar el objeto, es decir, inicializa 
adecuadamente su estado interno, crea variables de instancia, crea 
instancias de cualquier otro objeto si es necesario, etc.

Toma en cuenta que el constructor:

No puede retornar un valor, ya que está diseñado para devolver 
un objeto recién creado y nada más.
No se puede invocar directamente desde el objeto o desde dentro 
de la clase (puedes invocar un constructor desde cualquiera de las 
superclases del objeto, pero discutiremos esto más adelante).

Como __init__ es un método, y un método es una función, puedes hacer 
los mismos trucos con constructores y métodos que con las funciones ordinarias.

El ejemplo muestra cómo definir un constructor con un 
valor de argumento predeterminado.
'''

class Persona:
    def __init__(self, nombre = None):
        self.nombre = nombre

obj_1 = Persona("Juan")
obj_2 = Persona()

print(obj_1.nombre)
print(obj_2.nombre)

'''
Todo lo que hemos dicho sobre el manejo de los nombres también 
se aplica a los nombres de métodos, un método cuyo nombre 
comienza con __ está (parcialmente) oculto.

Si deseas encontrar la clase de un objeto en particular, puedes 
usar una función llamada type(), la cual es capaz (entre otras cosas) 
de encontrar una clase que se haya utilizado para crear instancias de cualquier objeto.
'''

print(type(obj_1))
print(type(obj_2).__name__)

'''
__module__ es una cadena, también almacena el nombre del 
módulo que contiene la definición de la clase.
'''

print(Persona.__module__)
print(obj_1.__module__)

'''
___bases__ es una tupla. La tupla contiene clases (no nombres de 
clases) que son superclases directas de la clase.

El orden es el mismo que el utilizado dentro de la definición de clase.

Te mostraremos solo un ejemplo muy básico, ya que queremos resaltar 
cómo funciona la herencia.

Además, te mostraremos cómo usar este atributo cuando discutamos los 
aspectos orientados a objetos de las excepciones.

Nota: solo las clases tienen este atributo, los objetos no.

Hemos definido una función llamada printBases(), diseñada para presentar 
claramente el contenido de la tupla.

Nota: una clase sin superclases explícitas apunta a object (una clase 
de Python predefinida) como su antecesor directo.
'''

class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)

'''
Todo esto permite que el programador de Python realice dos actividades 
importantes específicas para muchos lenguajes objetivos. Las cuales son:

Introspección, que es la capacidad de un programa para examinar el tipo 
o las propiedades de un objeto en tiempo de ejecución.

Reflexión, que va un paso más allá, y es la capacidad de un programa 
para manipular los valores, propiedades y/o funciones de un objeto 
en tiempo de ejecución.

En otras palabras, no tienes que conocer la definición completa de 
clase/objeto para manipular el objeto, ya que el objeto y/o su clase 
contienen los metadatos que te permiten reconocer sus características 
durante la ejecución del programa.
'''