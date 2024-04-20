'''
Un método es una función que está dentro de una clase.

Existe un requisito fundamental: un método está obligado 
a tener al menos un parámetro (no existen métodos sin 
parámetros; un método puede invocarse sin un argumento, pero 
no puede declararse sin parámetros).

El primer (o único) parámetro generalmente se denomina self. 
Te sugerimos que lo sigas nombrando de esta manera, darle 
otros nombres puede causar sorpresas inesperadas.

El nombre self sugiere el propósito del parámetro: identifica 
el objeto para el cual se invoca el método.

Si vas a invocar un método, no debes pasar el argumento para 
el parámetro self, Python lo configurará por ti.
'''

class Classy:
    def method(self):
        print("método")


obj = Classy()
obj.method()