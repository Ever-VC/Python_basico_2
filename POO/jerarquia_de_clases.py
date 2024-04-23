'''
Construir una jerarquía de clases no es solo por amor al arte.

Si divides un problema entre las clases y decides cual de ellas debe ubicarse 
en la parte superior y cual debe ubicarse en la parte inferior de la jerarquía, 
debes analizar cuidadosamente el problema, pero antes de mostrarte como hacerlo 
(y como no hacerlo), queremos resaltar un efecto interesante. No es nada 
extraordinario (es solo una consecuencia de las reglas generales presentadas 
anteriormente), pero recordarlo puede ser clave para comprender como funcionan 
algunos códigos y cómo se puede usar este efecto para construir un conjunto 
flexible de clases.
'''

class One:
    def do_it(self):
        print("do_it de One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it de Two")


one = One()
two = Two()

one.doanything()
two.doanything()

'''
Analicémoslo:

Existen dos clases llamadas One y Two, se entiende que Two es derivada 
de One. Nada especial. Sin embargo, algo es notable: el método do_it().
El método do_it() está definido dos veces: originalmente dentro de One 
posteriormente dentro de Two. La esencia del ejemplo radica en el hecho 
de que es invocado solo una vez dentro de One.
La pregunta es: ¿cuál de los dos métodos será invocado por las dos últimas 
líneas del código?


La primera invocación parece ser simple, el invocar el método doanything() 
del objeto llamado one obviamente activará el primero de los métodos.

La segunda invocación necesita algo de atención. También es simple si tienes 
en cuenta cómo Python encuentra los componentes de la clase. La segunda invocación 
ejecutará el método do_it() en la forma existente dentro de la clase Two, 
independientemente del hecho de que la invocación se lleva a cabo dentro de la clase One.

Nota: la situación en la cual la subclase puede modificar el comportamiento de 
su superclase (como en el ejemplo) se llama poliformismo. La palabra proviene 
del griego (polys: "muchos, mucho" y morphe, "formas, forma"), lo que significa 
que una misma clase puede tomar varias formas dependiendo de las redefiniciones 
realizadas por cualquiera de sus subclases.

El método, redefinido en cualquiera de las superclases, que cambia el 
comportamiento de la superclase, se llama virtual.

En otras palabras, ninguna clase se da por hecho. El comportamiento de cada 
clase puede ser modificado en cualquier momento por cualquiera de sus subclases.
'''