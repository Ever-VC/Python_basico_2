'''
Una pila es una estructura desarrollada para almacenar datos de 
una manera muy específica. Imagina una pila de monedas. No puedes 
poner una moneda en ningún otro lugar sino en la parte superior de la pila.

Del mismo modo, no puedes sacar una moneda de la pila desde ningún 
lugar que no sea la parte superior de la pila. Si deseas obtener 
la moneda que se encuentra en la parte inferior, debes eliminar 
todas las monedas de los niveles superiores.

El nombre alternativo para una pila (pero solo en la terminología 
de TI) es UEPS (LIFO son sus siglas en inglés).

Es una abreviatura para una descripción muy clara del comportamiento 
de la pila: Último en Entrar - Primero en Salir (Last In - First Out). 
La moneda que quedó en último lugar en la pila saldrá primero.. La moneda 
que llegó en último lugar a la pila se irá primero.

Una pila es un objeto con dos operaciones elementales, denominadas 
convencionalmente push (cuando un nuevo elemento se coloca en la 
parte superior) y pop (cuando un elemento existente se retira de la parte superior).

Las pilas se usan muy a menudo en muchos algoritmos clásicos, y es 
difícil imaginar la implementación de muchas herramientas ampliamente 
utilizadas sin el uso de pilas.

Implementemos una pila en Python. Esta será una pila muy simple, y te 
mostraremos como hacerlo en dos enfoques independientes: de manera 
procedimental y de orientado a objetos.

Comencemos con el primero.
'''

# Implementando una pila de manera procedimental

'''
Primero, debes decidir como almacenar los valores que 
llegarán a la pila. Sugerimos utilizar el método más simple, y 
emplear una lista para esta tarea. Supongamos que el tamaño de la 
pila no está limitado de ninguna manera. Supongamos también que 
el último elemento de la lista almacena el elemento superior.

La pila en sí ya está creada:
'''

stack = []

'''
Estamos listos para definir una función que coloca un valor en la pila. 
Aquí están las presuposiciones para ello:

El nombre para la función es push.
La función obtiene un parámetro (este es el valor que se debe colocar en la pila).
La función no retorna nada.
La función agrega el valor del parámetro al final de la pila.
'''

def push(val):
    stack.append(val)

'''
Ahora es tiempo de que una función quite un valor de la pila. Así es como puedes hacerlo:

El nombre de la función es pop.
La función no obtiene ningún parámetro.
La función devuelve el valor tomado de la pila.
La función lee el valor de la parte superior de la pila y lo elimina.
'''
# NOTA: La función pop() no verifica si la pila está vacía.
def pop():
    val = stack[-1]
    del stack[-1]
    return val

# Ahora, es tiempo de probar la pila. Vamos a llenarla con algunos valores y luego los sacaremos.
push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())