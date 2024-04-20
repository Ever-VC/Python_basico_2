'''
Por supuesto, la idea principal sigue siendo la misma. 
Usaremos una lista como almacenamiento de la pila. 
Solo tenemos que saber como poner la lista en la clase.

Esperamos dos cosas de la clase:

    Queremos que la clase tenga una propiedad como el 
    almacenamiento de la pila, tenemos que "instalar" una 
    lista dentro de cada objeto de la clase (nota: cada 
    objeto debe tener su propia lista; la lista no debe 
    compartirse entre diferentes pilas).

    Despues, queremos que la lista esté oculta de la vista 
    de los usuarios de la clase. de la vista de los usuarios' de la clase.

Agreguemos solo una propiedad al nuevo objeto, una lista para la pila. La nombraremos stack_list
emos agregado dos guiones bajos antes del nombre stack_list. 
Esto es una convención que indica que la propiedad es privada y no debe ser accesible desde fuera de la clase.

Ahora es momento de implementar las operaciones push y pop, tales 
componentes serán de tipo público, por ello no puede comenzar su 
nombre con dos (o más) guiones bajos. Hay un requisito más el 
nombre no debe tener más de un guión bajo. Dado que ningún 
guion bajo final cumple completamente con el requisito, puedes 
suponer que el nombre es aceptable.
'''

class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())