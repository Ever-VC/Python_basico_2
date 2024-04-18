'''
Vamos a jugar un juego. Te daremos dos cadenas: una es una palabra (por ejemplo, "dog") 
y la segunda es una combinación de un grupo de caracteres.

La tarea es escribir un programa que responda la siguiente pregunta: ¿Los caracteres 
que comprenden la primera cadena están ocultos dentro de la segunda cadena?

Por ejemplo:

Si la segunda cadena es "vcxzxduybfdsobywuefgas", la respuesta es si;
Si la segunda cadena es "vcxzxdcybfdstbywuefsas", la respuesta es no (ya que no están las letras "d", "o", o "g" ni en ese orden)
Pistas:

Debes usar las variantes de dos argumentos de las funciones pos() dentro de tu código.
No te preocupes por mayúsculas y minúsculas.
'''

word = input("Ingresa la palabra que deseas encontrar: ").upper()
strn = input("Ingresa la cadena en donde deseas buscar: ").upper()

found = True
start = 0

for ch in word:
	pos = strn.find(ch, start) 
	if pos < 0:
		found = False
		break
	start = pos + 1
if found:
	print("Si")
else:
	print("No")
	   