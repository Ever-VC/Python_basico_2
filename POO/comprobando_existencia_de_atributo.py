'''
La actitud de Python hacia la instanciación de objetos plantea 
una cuestión importante: en contraste con otros lenguajes de 
programación, es posible que no esperes que todos los objetos 
de la misma clase tengan los mismos conjuntos de propiedades.

Justo como en el ejemplo en el editor. Míralo cuidadosamente.
'''

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)

'''
El objeto creado por el constructor solo puede tener uno de los dos 
atributos posibles: a o b.

Como puedes ver, acceder a un atributo de objeto (clase) no existente 
genera una excepción AttributeError.

La instrucción try-except te brinda la oportunidad de 
evitar problemas con propiedades inexistentes.

```
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

try:
    print(example_object.b)
except AttributeError:
    pass
```

ta acción no es muy sofisticada. Esencialmente, acabamos de barrer el tema debajo de la alfombra.

Afortunadamente, hay una forma más de hacer frente al problema. Lo analizaremos en el archivo ``comprobando_existencia_de_atributo_2.py``.
'''




    