'''
-> El módulo time <-

Además de la clase time, la biblioteca estándar de Python ofrece un módulo 
llamado time, que proporciona una función relacionada con el tiempo. Ya se 
tuvo la oportunidad de aprender la función llamada time cuando se habló de 
la clase date. Ahora veremos otra función útil disponible en este módulo.

Debes pasar muchas horas frente a una computadora mientras realiza este curso. 
A veces puedes sentir la necesidad de tomar una siesta. ¿Por qué no? Escribamos 
un programa que simule la siesta corta de un estudiante. Echa un vistazo al 
código en el editor.
'''
import time

class Student:
    def take_nap(self, seconds):
        print("Estoy muy cansado. Tengo que tomar una siesta. Hasta luego.")
        time.sleep(seconds)
        print("¡Dormí bien! ¡Me siento genial!")

student = Student()
student.take_nap(5)

'''
Resultado:

Estoy muy cansado. Tengo que tomar una siesta. Hasta luego.
¡Dormí bien! ¡Me siento genial!

La parte más importante del código de muestra es el uso de la 
función sleep (sí, puedes recordarla de una de las prácticas 
de laboratorio anteriores en el curso), que suspende la ejecución 
del programa por el determinado número de segundos.

En nuestro ejemplo, son 5 segundos. Tienes razón, es una siesta muy corta.

Extiende el sueño del estudiante cambiando la cantidad de segundos. 
Toma en cuenta que la función sleep acepta solo un número entero o 
de punto flotante.
'''