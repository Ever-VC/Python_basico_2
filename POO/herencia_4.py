# Probando propiedades: variables de instancia.
class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)
'''
Como puedes observar, la clase Super define una variable de clase llamada supVar, y 
la clase Sub define una variable llamada subVar.

El constructor de la clase Sub crea una variable de instancia llamada subVar, mientras 
que el constructor de Super hace lo mismo con una variable de nombre supVar. Al igual 
que el ejemplo anterior, ambas variables son accesibles desde el objeto de clase Sub.

Nota: La existencia de la variable supVar obviamente está condicionada por la 
invocación del constructor de la clase Super. Omitirlo daría como resultado la 
ausencia de la variable en el objeto creado (pruébalo tu mismo).


Ahora es posible formular una declaración general que describa el comportamiento de Python.

Cuando intentes acceder a una entidad de cualquier objeto, Python intentará (en este orden):

    Encontrarla dentro del objeto mismo.
    Encontrarla en todas las clases involucradas en la línea de herencia del objeto de abajo hacia arriba.
    Si ambos intentos fallan, una excepción (AttributeError) será generada.


La primera condición puede necesitar atención adicional. Como sabes, todos los objetos 
derivados de una clase en particular pueden tener diferentes conjuntos de atributos, y 
algunos de los atributos pueden agregarse al objeto mucho tiempo después de la creación del objeto.
'''