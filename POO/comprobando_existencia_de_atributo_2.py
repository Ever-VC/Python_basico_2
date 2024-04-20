'''
Python proporciona una función que puede verificar con 
seguridad si algún objeto / clase contiene una propiedad específica. 
La función se llama hasattr, y espera que le pasen dos argumentos:

La clase o el objeto que se verifica.
El nombre de la propiedad cuya existencia se debe informar 
(Nota: debe ser una cadena que contenga el nombre del atributo).

La función retorna True o False.

No olvides que la función hasattr() también puede 
operar en clases. Puedes usarla para averiguar si una 
variable de clase está disponible, como en el ejemplo en el editor.

La función devuelve True si la clase especificada contiene un 
atributo dado, y False de lo contrario.
'''

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1
 
 
example_object = ExampleClass(1)
print(example_object.a)
 
if hasattr(example_object, 'b'):
    print(example_object.b)

class ExampleClass2:
    attr = 1


print(hasattr(ExampleClass2, 'attr'))
print(hasattr(ExampleClass2, 'prop'))