'''
Trabajando con módulos estándar de Python

Función dir(): La función dir() se utiliza para devolver una lista de nombres en un módulo.
'''

import math

for name in dir(math):
    print(name, end="\t")

'''
----------------------------------
Funciones selectas del módulo math
----------------------------------

El primer grupo de funciones de módulo math están relacionadas con trigonometría:

*   sin(x) → el seno de x.
*   cos(x) → el coseno de x.
*   tan(x) → la tangente de x.

Sus versiones inversas:

*   asin(x) → el arcoseno de x.
*   acos(x) → el arcocoseno de x.
*   atan(x) → el arcotangente de x.

Para trabajar eficazmente con mediciones de ángulos, el módulo math 
proporciona las siguientes entidades:

*   pi → una constante con un valor que es una aproximación de π.
*   radians(x) → una función que convierte x de grados a radianes.
*   degrees(x) → una función que convierte x de radianes a grados.
'''

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.) # SALIDA: True
print(ar == pi / 2.) # SALIDA: True
print(sin(ar) / cos(ar) == tan(ar)) # SALIDA: True
print(asin(sin(ar)) == ar) # SALIDA: True

'''
Además de las funciones circulares (enumeradas anteriormente), el 
módulo math también contiene un conjunto de sus análogos hiperbólicos:

*   sinh(x) → el seno hiperbólico.
*   cosh(x) → el coseno hiperbólico.
*   tanh(x) → la tangente hiperbólica.
*   asinh(x) → el arcoseno hiperbólico.
*   acosh(x) → el arcocoseno hiperbólico.
*   atanh(x) → el arcotangente hiperbólico.

Existe otro grupo de las funciones math relacionadas con la exponenciación:

*   e → una constante con un valor que es una aproximación del número de Euler (e)
*   exp(x) → encontrar el valor de ex.
*   log(x) → el logaritmo natural de x.
*   log(x, b) → el logaritmo de x con base b.
*   log10(x) → el logaritmo decimal de x (más preciso que log(x, 10))
*   log2(x) → el logaritmo binario de x (más preciso que log(x, 2))

Nota: la función pow():

pow(x, y) → fencuentra el valor de xy (toma en cuenta los dominios).
Esta es una función incorporada y no se tiene que importar.
'''
from math import e, exp, log

print(pow(e, 1) == exp(log(e))) # SALIDA: True
print(pow(2, 2) == exp(2 * log(2))) # SALIDA: True
print(log(e, e) == exp(0)) # SALIDA: True

'''
El último grupo consta de algunas funciones de propósito general como:

*   ceil(x) → devuelve el entero más pequeño mayor o igual que x.
*   floor(x) → el entero más grande menor o igual que x.
*   trunc(x) → el valor de x truncado a un entero (ten cuidado, no es equivalente a ceil o floor).
*   factorial(x) → devuelve x! (x tiene que ser un valor entero y no negativo).
*   hypot(x, y) → devuelve la longitud de la hipotenusa de un triángulo rectángulo
    con las longitudes de los catetos iguales a (x) y (y) 
    (lo mismo que sqrt(pow(x, 2) + pow(y, 2)) pero más preciso).
'''
from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y)) # SALIDA: 1 2
print(floor(-x), floor(-y)) # SALIDA: -2 -3
print(ceil(x), ceil(y)) # SALIDA: 2 3
print(ceil(-x), ceil(-y)) # SALIDA: -1 -2
print(trunc(x), trunc(y)) # SALIDA: 1 2
print(trunc(-x), trunc(-y)) # SALIDA: -1 -2

'''
----------------------------------
Funciones selectas del módulo random
----------------------------------

El módulo random proporciona una serie de funciones que generan números
aleatorios. Aquí hay algunas de las más útiles:

*   seed(x) → inicializa el generador de números aleatorios.
*   random() → devuelve un número aleatorio de punto flotante en el rango [0.0, 1.0).
*   randint(a, b) → devuelve un número entero aleatorio en el rango [a, b] (incluidos).
*   choice(seq) → devuelve un elemento aleatorio de la secuencia seq.
*   shuffle(seq) → mezcla la secuencia seq.
*   sample(seq, k) → devuelve k elementos únicos de la secuencia seq.

Nota: la función randrange(): randrange(a, b) → devuelve un número entero aleatorio en el rango [a, b) (no incluido b).
Esta es una función incorporada y no se tiene que importar.
'''

from random import seed, random, randint, choice, shuffle, sample

seed(0) # Inicializa el generador de números aleatorios

for i in range(5):
    print(random())# Imprime 5 números aleatorios

for i in range(5):
    print(randint(1, 10)) # Imprime 5 números aleatorios en el rango [1, 10]

lst = [1, 2, 3, 4, 5]
print(choice(lst)) # Imprime un elemento aleatorio de la lista

shuffle(lst)
print(lst) # Imprime la lista mezclada

print(sample(lst, 3)) # Imprime 3 elementos únicos de la lista


'''
----------------------------------
Funciones randrange y randint
----------------------------------

Si deseas valores aleatorios enteros, una de las siguientes funciones encajaría mejor:

*   randrange(fin)
*   randrange(inicio, fin)
*   randrange(inicio, fin, incremento)
*   randint(izquiera, derecha)

Las primeras tres invocaciones generarán un valor entero tomado (pseudoaleatoriamente) del rango:

*   range(fin)
*   range(inicio, fin)
*   range(inicio, fin, incremento)

Toma en cuenta la exclusión implícita del lado derecho.

La última función es equivalente a randrange(izquierda, derecha+1) - genera el valor 
entero i, el cual cae en el rango [izquierda, derecha] (sin exclusión en el lado derecho).
'''
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

'''
Las funciones anteriores tienen una desventaja importante - pueden producir valores 
repetidos incluso si el número de invocaciones posteriores no es mayor que el rango especificado.
'''
from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

'''
Las funciones choice y sample
Como puedes ver, esta no es una buena herramienta para generar números para la lotería. 
Afortunadamente, existe una mejor solución que escribir tu propio código para verificar la 
singularidad de los números "sorteados".

Es una función con el nombre de choice:

*   choice(secuencia)
*   sample(secuencia, elementos_a_elegir=1)
La primera variante elige un elemento "aleatorio" de la secuencia de entrada y lo devuelve.

El segundo crea una lista (una muestra) que consta del elemento 
elementos_a_elegir (que por defecto es 1) «sorteado» de la secuencia de entrada.

En otras palabras, la función elige algunos de los elementos de entrada, devolviendo 
una lista con la elección. Los elementos de la muestra se colocan en orden aleatorio. 
Nota que elementos_a_elegir no debe ser mayor que la longitud de la secuencia de entrada.
'''
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

'''
----------------------------------
Funciones selectas del módulo platform
----------------------------------

Existe también una función que puede mostrar todas las capas subyacentes en un 
solo vistazo, llamada platform. Simplemente devuelve una cadena que describe 
el entorno; por lo tanto, su salida está más dirigida a los humanos que al 
procesamiento automatizado.

Así es como se puede invocar:

platform(aliased = False, terse = False)

La función platform() devuelve una cadena que describe el entorno en el que se está ejecutando el script.

Y ahora:

*   aliased → cuando se establece a True (o cualquier valor distinto a cero) 
    puede hacer que la función presente los nombres de capa subyacentes 
    alternativos en lugar de los comunes.
*   terse → cuando se establece a True (o cualquier valor distinto a cero) puede convencer 
    a la función de presentar una forma más breve del resultado (si lo fuera posible).
'''
from platform import platform
 
print(platform())
print(platform(1))
print(platform(0, 1))

'''
La función machine() devuelve el nombre de la máquina en la que se está ejecutando el script.
'''
from platform import machine
 
print(machine())

'''
La función processor() devuelve el nombre del procesador de la máquina en la que se está ejecutando el script.
'''

from platform import processor

print(processor())

'''
La función system() devuelve el nombre del sistema operativo en el que se está ejecutando el script.
'''
from platform import system

print(system())

'''
La función version() devuelve una cadena que describe la versión del sistema operativo en el que se está ejecutando el script.
'''
from platform import version

print(version())

'''
Las funciones python_build() y python_compiler() devuelven información sobre la versión de Python que se está ejecutando.
'''
from platform import python_build, python_compiler

print(python_build())
print(python_compiler())

'''
La función python_version() devuelve la versión de Python que se está ejecutando.
'''
from platform import python_version

print(python_version())

'''
La función python_implementation() devuelve el nombre de la implementación de Python que se está ejecutando.
'''
from platform import python_implementation

print(python_implementation())

'''
La función python_version_tuple() devuelve una tupla que contiene la revisión de Python que se está ejecutando.

La tupla contiene tres elementos:

*   La parte mayor de la versión de Python
*   El número de revisión menor
*   el número de revisión micro (número del nivel de parche )(si está disponible)
'''
from platform import python_version_tuple

print(python_version_tuple())