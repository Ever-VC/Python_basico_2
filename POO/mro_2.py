#Sin sorpresas hasta ahora. Hagamos un pequeño cambio en este código. Echa un vistazo:

class Top:
    def m_top(self):
        print("superior")


class Middle(Top):
    def m_middle(self):
        print("medio")


class Bottom(Middle, Top):
    def m_bottom(self):
        print("abajo")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

'''
¿Puedes ver la diferencia? Está escondida en esta línea:


```class Bottom(Middle, Top):```
 
De esta manera exótica, hemos convertido un código muy simple con 
una clara ruta de herencia única en un misterioso acertijo de 
herencia múltiple. "¿Es válido?" Te puedes preguntar. Sí lo es. 
"¿Cómo es eso posible?" te preguntas, esperamos que realmente 
sientas la necesidad de hacer esta pregunta.

Como puedes ver, el orden en el que se enumeran las dos superclases 
entre paréntesis cumple con la estructura del código: la clase Middle 
precede a la clase Top, justo como en la ruta de herencia real.

A pesar de su rareza, la muestra es correcta y funciona como se 
esperaba, pero debe indicarse que esta notación no aporta ninguna 
funcionalidad nueva ni significado adicional.
'''