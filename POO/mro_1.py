'''
MRO (Orden de Resolución de Métodos), en general, es una forma (puedes llamarlo una estrategia) en 
la que un lenguaje de programación en particular escanea la parte 
superior de la jerarquía de una clase para encontrar el método que 
necesita actualmente. Vale la pena enfatizar que los diferentes 
lenguajes usan MROs levemente (o incluso completamente) diferentes. 
Python es único en este aspecto y sus costumbres son un poco específicas.

Te mostraremos cómo funciona el MRO de Python en dos casos 
peculiares que son ejemplos claros de problemas que pueden 
ocurrir cuando intentas usar la herencia múltiple de manera 
demasiado imprudente. Comencemos con un fragmento que 
inicialmente puede parecer simple.
'''
class Top:
    def m_top(self):
        print("superior")


class Middle(Top):
    def m_middle(self):
        print("Medio")


class Bottom(Middle):
    def m_bottom(self):
        print("abajo")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

'''
Estamos seguros de que si analizas el fragmento tu mismo, no 
verás ninguna anomalía en él. Sí, tienes toda la razón: parece 
claro y simple, y no genera preocupaciones.
'''