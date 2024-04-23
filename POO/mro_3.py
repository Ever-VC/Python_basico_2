'''
Modifiquemos el código una vez más; ahora intercambiaremos 
ambos nombres de superclase en la definición de clase 
Bottom. Así es como se ve el fragmento de código ahora:
'''
class Top:
    def m_top(self):
        print("superior")


class Middle(Top):
    def m_middle(self):
        print("medio")


class Bottom(Top, Middle):
    def m_bottom(self):
        print("abajo")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
'''
Para anticiparnos a tu pregunta, diremos que esta enmienda 
ha estropeado el código y ya no se ejecutará. Qué pena. El 
orden que intentamos forzar (Top, Middle) es incompatible con 
la ruta de herencia que se deriva de la estructura del código. 
A Python no le gustará. Esto es lo que veremos:

```TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Middle```

Creemos que el mensaje habla por sí solo. El MRO de Python 
no se puede doblar ni violar, no solo porque esa es la forma 
en que funciona Python, sino también porque es una regla que debes obedecer.
'''