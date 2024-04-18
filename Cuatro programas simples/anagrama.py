'''
Un anagrama es una nueva palabra formada al reorganizar las letras de una 
palabra, usando todas las letras originales exactamente una vez. Por ejemplo, las 
frases "rail safety" y "fairy tales" son anagramas, mientras que "I am" y "You are" no lo son.

Tu tarea es escribir un programa que:

Le pida al usuario dos textos por separado.
Compruebe si los textos ingresados son anagramas e imprima el resultado.
Nota:

Supongamos que dos cadenas vacías no son anagramas.
Tratar a las letras mayúsculas y minúsculas como iguales.
Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.
'''

str_1 = input("Ingresa la primera cadena: ")
str_2 = input("Ingresa la segunda cadena: ")

strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
if len(strx_1) > 0 and strx_1 == strx_2:
	print("Anagramas")
else:
	print("No son anagramas")