class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Mi nombre es " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)


obj = Sub("Andy")

print(obj)
'''
Vamos a analizarlo:

    Existe una clase llamada Super, que define su propio constructor utilizado para 
    asignar la propiedad del objeto, llamada name.
    
    La clase también define el método __str__(), lo que permite que la clase pueda 
    presentar su identidad en forma de texto.
    
    La clase se usa luego como base para crear una subclase llamadaSub. La clase Sub 
    define su propio constructor, que invoca el de la superclase. Toma nota de como lo 
    hemos hecho: Super.__init__(self, name).
    
    Hemos nombrado explícitamente la superclase y hemos apuntado al método para invocar 
    a __init__(), proporcionando todos los argumentos necesarios.
    
    Hemos instanciado un objeto de la clase Sub y lo hemos impreso.
    
    Nota: Como no existe el método __str__() dentro de la clase Sub, la cadena a imprimir 
    se producirá dentro de la clase Super. Esto significa que el método __str__() ha 
    sido heredado por la clase Sub.
'''