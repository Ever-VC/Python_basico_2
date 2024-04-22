class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Mi nombre es " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")

print(obj)

'''
En el último ejemplo, nombramos explícitamente la superclase. En este ejemplo, hacemos
uso de la función super(), que accede a la superclase sin necesidad de saber su nombre:


```super().__init__(name)```
 
La función super() crea un contexto en el que no tiene que (además, no debe) pasar el 
argumento propio al método que se invoca; es por eso que es posible activar el 
constructor de la superclase utilizando solo un argumento.

Nota: puedes usar este mecanismo no solo para invocar al constructor de la superclase, pero 
también para obtener acceso a cualquiera de los recursos disponibles dentro de la superclase.
'''