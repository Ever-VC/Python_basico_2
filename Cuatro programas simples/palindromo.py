'''
¿Sabes qué es un palíndromo?

Es una palabra que se ve igual cuando se lee hacia adelante y hacia atrás. 
Por ejemplo, "kayak" es un palíndromo, mientras que "leal" no lo es.

Tu tarea es escribir un programa que:

Le pida al usuario algún texto.
Compruebe si el texto introducido es un palíndromo e imprima el resultado.
Nota:

Supón que una cadena vacía no es un palíndromo.
Trata a las letras mayúsculas y minúsculas como iguales.
Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.
Existe más de una solución correcta: intenta encontrar más de una.
'''

text = input("Ingresa un texto: ")

# Quitar todos los espacios...
text = text.replace(' ','')

# ... y revisar si la palabra es igual en ambos sentidos
if len(text) > 1 and text.upper() == text[::-1].upper():
	print("Es un palíndromo")
else:
	print("No es un palíndromo")