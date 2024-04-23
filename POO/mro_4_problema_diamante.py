'''
El problema del diamante
El segundo ejemplo del espectro de problemas que 
posiblemente pueden surgir de la herencia múltiple 
está ilustrado por un problema clásico llamado problema 
del diamante. El nombre refleja la forma del diagrama 
de herencia; observa la imagen:

Existe la superclase superior llamada A.

Existen dos subclases derivadas de A: B y C.

También está la subclase inferior llamada D, derivada de B y C 
(o C y B, ya que estas dos variantes significan cosas diferentes en Python).

¿Puedes ver el diamante ahí?

        A
    B       C
        D

```
    class A:
        pass


    class B(A):
        pass


    class C(A):
        pass


    class D(B, C):
        pass


    d = D()
```

Algunos lenguajes de programación no permiten la herencia múltiple 
en absoluto y, como consecuencia, no te permitirán construir un 
diamante; este es el camino que Java y C# han elegido seguir desde sus orígenes.

Python, sin embargo, ha elegido una ruta diferente: permite la 
herencia múltiple y no le importa si escribe y ejecuta código 
como el del editor. Pero no te olvides del MRO: siempre está a cargo.


Reconstruyamos nuestro ejemplo de la página anterior para hacerlo 
más parecido a un diamante, como se muestra a continuación:

Nota: ambas clases Middle definen un método con el mismo nombre: m_middle().
'''

class Top:
    def m_top(self):
        print("top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
	def m_bottom(self):
		print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

'''
Introduce una pequeña incertidumbre en nuestra muestra, aunque 
estamos absolutamente seguros de que puedes responder la siguiente 
pregunta clave: ¿cuál de los dos métodos m_middle() se invocará 
realmente cuando la siguiente línea se ejecute?

```Object.m_middle()```

En otras palabras, qué verás en la pantalla: middle_left o middle_right?

No es necesario que te apresures, ¡piénselo dos veces y toma en cuenta el MRO de Python!

¿Estás listo?

Sí, tienes razón. La invocación activará el método m_middle(), que proviene de 
la clase Middle_Left. La explicación es simple: la clase aparece antes de Middle_Right 
en la lista de herencia de la clase Bottom. Si deseas asegurarte de que no haya dudas 
al respecto, intenta intercambiar estas dos clases en la lista y verifica los resultados.

Si deseas experimentar algunas impresiones más profundas sobre la herencia múltiple 
y las piedras preciosas, intenta modificar nuestro fragmento y equipar la clase 
Upper con otro espécimen del método m_middle() e investigua su comportamiento detenidamente.

Como puedes ver, los diamantes pueden traer algunos problemas a tu vida, tanto 
los reales como los que ofrece Python.
'''
