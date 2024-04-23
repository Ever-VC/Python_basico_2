'''
Te mostraremos como usar el poliformismo para extender la flexibilidad de la clase.
'''


class TrackedVehicle:
    def control_track(left, stop):
        pass

    def turn(left):
        control_track(left, True)
        time.sleep(0.25)
        control_track(left, False)


class WheeledVehicle:
    def turn_front_wheels(left, on):
        pass

    def turn(left):
        turn_front_wheels(left, True)
        time.sleep(0.25)
        turn_front_wheels(left, False)

'''
¿Se parece a algo? Sí, por supuesto que lo hace. Se refiere al ejemplo que se
muestra al comienzo del módulo cuando hablamos de los conceptos generales 
de la programación orientada a objetos.

Puede parecer extraño, pero no utilizamos herencia en este ejemplo, solo 
queríamos mostrarte que no nos limita.

Definimos dos clases separadas capaces de producir dos tipos diferentes de 
vehículos terrestres. La principal diferencia entre ellos está en cómo giran. 
Un vehículo con ruedas solo gira las ruedas delanteras (generalmente). 
Un vehículo con pistas tiene que detener una de las pistas.

¿Puedes seguir el código?

Un vehículo con pistas realiza un giro deteniéndose y moviéndose en una de sus 
pistas (esto lo hace el método control_track() el cual se implementará más tarde).
Un vehículo con ruedas gira cuando sus ruedas delanteras giran (esto lo hace 
el método turn_front_wheels()).
El método turn() utiliza el método adecuado para cada vehículo en particular.
¿Puedes detectar el error del código?

Los métodos turn() son muy similares como para dejarlos en esta forma.

Vamos a reconstruir el código: vamos a presentar una superclase para 
reunir todos los aspectos similares de los vehículos, trasladando todos 
los detalles a las subclases.

Archivo ``polimorfismo_2.py``:
'''