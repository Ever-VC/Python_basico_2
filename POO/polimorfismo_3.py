import time

class Tracks:
    def change_direction(self, left, on):
        print("pistas: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("ruedas: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)

'''
Existen dos clases llamadas Tracks y Wheels, ellas saben como controlar 
la dirección del vehículo. También hay una clase llamada Vehicle que puede 
usar cualquiera de los controladores disponibles (los dos ya definidos o 
cualquier otro definido en el futuro): el controlador se pasa a la clase 
durante la inicialización.

De esta manera, la capacidad de giro del vehículo se compone de un objeto 
externo, no implementado dentro de la clase Vehicle.

En otras palabras, tenemos un vehículo universal y podemos instalar pistas o ruedas en él.
'''