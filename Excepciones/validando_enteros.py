'''
La tarea es escribir una función capaz de ingresar valores enteros y verificar si están dentro de un rango especificado.

La función deberá:

Aceptar tres argumentos: una entrada, un límite inferior aceptable y un límite superior aceptable.
Si el usuario ingresa una cadena que no es un valor entero, la función debe emitir el mensaje Error: entrada incorrecta, y solicitará al usuario que ingrese el valor nuevamente.
Si el usuario ingresa un número que está fuera del rango especificado, la función debe emitir el mensaje Error: el valor no está dentro del rango permitido (min..max) y solicitará al usuario que ingrese el valor nuevamente.
Si el valor de entrada es válido, será regresado como resultado.
'''

def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print("Error: entrada incorrecta")
        if ok:
            ok = value >= min and value <= max
        if not ok:
            print("Error: el valor no está dentro del rango permitido (" + str(min) + ".." + str(max) + ")")
    return value


v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)