'''
¿Cómo usar lambdas y para qué?
La parte más interesante de usar lambdas aparece cuando puedes usarlas 
en su forma pura: como partes anónimas de código destinadas a evaluar 
un resultado.

Imagina que necesitamos una función (la nombraremos print_function) que 
imprime los valores de una (otra) función dada para un conjunto de 
argumentos seleccionados.

Queremos que print_function sea universal, debería aceptar un conjunto 
de argumentos incluidos en una lista y una función a ser evaluada, ambos 
como argumentos; no queremos codificar nada.
'''

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)


'''
Analicémoslo. La función print_function() toma dos parámetros:

El primero, una lista de argumentos para los que queremos imprimir los resultados.
El segundo, una función que debe invocarse tantas veces como el número de valores 
que se recopilan dentro del primer parámetro.
Nota: También hemos definido una función llamada poly(), esta es la función cuyos 
valores vamos a imprimir. El cálculo que realiza la función no es muy sofisticado: 
es el polinomio (de ahí su nombre) de la forma:

f(x) = 2x2 - 4x + 2

El nombre de la función se pasa a print_function() junto con un conjunto de cinco 
argumentos diferentes, el conjunto está construido con una cláusula de comprensión 
de la lista.

¿Podemos evitar definir la función poly(), ya que no la vamos 
a usar más de una vez? Si, podemos: este es el beneficio que 
puede aportar una función lambda.


Mira el ejemplo de abajo. ¿Puedes ver la diferencia?
```
    def print_function(args, fun):
        for x in args:
            print('f(', x,')=', fun(x), sep='')
    
    print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)
```

La función print_function() se ha mantenido exactamente igual, pero no 
hay una función poly(). Ya no la necesitamos, ya que el polinomio ahora 
está directamente dentro de la invocación de la función print_function() 
en forma de una lambda definida de la siguiente manera:

```lambda x: 2 * x**2 - 4 * x + 2```

El código se ha vuelto más corto, más claro y más legible.

Permítenos mostrarte otro lugar donde las lambdas pueden ser útiles. 
Comenzaremos con una descripción de map(), una función integrada de Python. 
Su nombre no es demasiado descriptivo, su idea es simple y la función en 
sí es muy utilizable.
'''