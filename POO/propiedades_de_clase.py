'''
Una variable de clase es una propiedad que 
existe en una sola copia y se almacena fuera de cualquier objeto.

Nota: no existe una variable de instancia si no hay 
ningún objeto de la clase; solo existe una variable 
de clase en una copia, incluso si no hay objetos en la clase.

Las variables de clase se crean de manera diferente. 
El ejemplo te dirá más
'''

class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1
 
 
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)
 
print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

'''
Observa:

    Hay una asignación en la primera linea de la definición de clase: 
    establece la variable denominada counter a 0; inicializando la 
    variable dentro de la clase pero fuera de cualquiera de sus 
    métodos hace que la variable sea una variable de clase.

    El acceder a dicha variable tiene el mismo aspecto que acceder 
    a cualquier atributo de instancia; está en el cuerpo del 
    constructor; como puedes ver, el constructor incrementa la 
    variable en uno; en efecto, la variable cuenta todos los objetos creados.

Dos conclusiones importantes se pueden sacar del ejemplo:

    Las variables de clase no se muestran en el diccionario 
    de un objeto __dict__ (esto es natural ya que las variables 
    de clase no son partes de un objeto), pero siempre puedes 
    intentar buscar en la variable del mismo nombre, pero a 
    nivel de clase, te mostraremos esto muy pronto.

    Una variable de clase siempre presenta el mismo valor en 
    todas las instancias de clase (objetos).
    
El cambiar el nombre de una variable de clase tiene los mismos efectos que aquellos con los que ya está familiarizado.
'''