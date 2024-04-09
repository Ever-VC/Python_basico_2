#Funcion min() retorna el caracter con el valor ASCII mas bajo
print(min("aAbByYzZ")) # SALIDA: A
var = 'Los Caballeros Que Dicen "Ni!"'
print('[' + min(var) + ']') # SALIDA: [ ]

var = [0, 1, 2]
print(min(var)) # SALIDA: 0

#Funcion max() retorna el caracter con el valor ASCII mas alto
print(max("aAbByYzZ")) # SALIDA: z
var = 'Los Caballeros Que Dicen "Ni!"'
print('[' + max(var) + ']') # SALIDA: [r]

var = [0, 1, 2]
print(max(var)) # SALIDA: 2

#Funcion index() permite encontrar la primera ocurrencia de una subcadena en una cadena
print("aAbByYzZ".index("b")) # SALIDA: 2
print("aAbByYzZ".index("Z")) # SALIDA: 7
print("aAbByYzZ".index("Z", 3)) # SALIDA: 7

#Funcion count() permite contar cuantas veces aparece una subcadena en una cadena
print("abcabcabc".count("b")) # SALIDA: 3
print('abcabcabc'.count("d")) # SALIDA: 0

#Funcion replace() permite reemplazar una subcadena por otra
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org")) # SALIDA: www.pythoninstitute.org
print("This is it!".replace("is", "are")) # SALIDA: Thare are it!

#Funcion split() permite dividir una cadena en una lista de cadenas
print("The string".split()) # SALIDA: ['The', 'string']
print("The string".split('i')) # SALIDA: ['The str', 'ng']

#Funcion join() permite unir una lista de cadenas con una cadena separadora
print(" ".join(["join", "me", "please"])) # SALIDA: join me please
print("***".join(["join", "me", "please"])) # SALIDA: join***me***please

#Funcion list() permite convertir una cadena en una lista
print(list("abcabc")) # SALIDA: ['a', 'b', 'c', 'a', 'b', 'c']

#Funcion upper() permite convertir una cadena a mayusculas
print("aBcD".upper()) # SALIDA: ABCD

#Funcion lower() permite convertir una cadena a minusculas
print("aBcD".lower()) # SALIDA: abcd

#Funcion capitalize() permite convertir la primera letra de una cadena en mayuscula
print("aBcD".capitalize()) # SALIDA: Abcd

#Funcion title() permite convertir la primera letra de cada palabra en mayuscula
print("aBcD".title()) # SALIDA: Abcd

#Funcion swapcase() permite intercambiar mayusculas por minusculas y viceversa
print("aBcD".swapcase()) # SALIDA: AbCd

#Funcion strip() permite eliminar los espacios en blanco a ambos lados de una cadena
print("[" + "   aleph   ".strip() + "]") # SALIDA: [aleph]

#Funcion lstrip() permite eliminar los espacios en blanco a la izquierda de una cadena
print("[" + "   aleph   ".lstrip() + "]") # SALIDA: [aleph   ]

#Funcion rstrip() permite eliminar los espacios en blanco a la derecha de una cadena
print("[" + "   aleph   ".rstrip() + "]") # SALIDA: [   aleph]

#Funcion ljust() permite justificar una cadena a la izquierda en un ancho especifico
print("A".ljust(3)) # SALIDA: A
print("A".ljust(3, "-")) # SALIDA: A--

#Funcion rjust() permite justificar una cadena a la derecha en un ancho especifico
print("A".rjust(3)) # SALIDA: A
print("A".rjust(3, "-")) # SALIDA: --A

#Funcion center() permite centrar una cadena en un ancho especifico
print("A".center(3)) # SALIDA: A
print("A".center(3, "-")) # SALIDA: -A-

#Funcion zfill() permite rellenar una cadena con ceros a la izquierda
print("42".zfill(5)) # SALIDA: 00042
print("-42".zfill(5)) # SALIDA: -0042

#Funcion format() permite formatear una cadena
print("Art: {0:5d}, Price per unit: {1:8.2f}".format(453, 59.058)) # SALIDA: Art:   453, Price per unit:    59.06
print("Art: {a:5d}, Price per unit: {p:8.2f}".format(a=453, p=59.058)) # SALIDA: Art:   453, Price per unit:    59.06

#Funcion format_map() permite formatear una cadena
print("Art: {0:5d}, Price per unit: {1:8.2f}".format_map({"0": 453, "1": 59.058})) # SALIDA: Art:   453, Price per unit:    59.06

#Funcion isalnum() verifica si una cadena contiene solo caracteres alfanumericos
print("12345".isalnum()) # SALIDA: True
print("abcde".isalnum()) # SALIDA: True

#Funcion isalpha() verifica si una cadena contiene solo caracteres alfabeticos
print("12345".isalpha()) # SALIDA: False
print("abcde".isalpha()) # SALIDA: True

#Funcion isdigit() verifica si una cadena contiene solo digitos
print("12345".isdigit()) # SALIDA: True
print("abcde".isdigit()) # SALIDA: False

#Funcion islower() verifica si una cadena contiene solo caracteres en minusculas
print("12345".islower()) # SALIDA: False
print("abcde".islower()) # SALIDA: True

#Funcion isupper() verifica si una cadena contiene solo caracteres en mayusculas
print("12345".isupper()) # SALIDA: False
print("ABCDE".isupper()) # SALIDA: True

#Funcion istitle() verifica si una cadena contiene solo palabras con la primera letra en mayuscula
print("12345".istitle()) # SALIDA: False
print("Abcde".istitle()) # SALIDA: False

#Funcion isspace() verifica si una cadena contiene solo espacios en blanco
print("12345".isspace()) # SALIDA: False
print("     ".isspace()) # SALIDA: True

#Funcion startswith() verifica si una cadena comienza con una subcadena
print("12345".startswith("123")) # SALIDA: True
print("12345".startswith("45")) # SALIDA: False

#Funcion endswith() verifica si una cadena termina con una subcadena
print("12345".endswith("345")) # SALIDA: True
print("12345".endswith("12")) # SALIDA: False

#Funcion find() permite encontrar la primera ocurrencia de una subcadena en una cadena
print("12345".find("3")) # SALIDA: 2
print("12345".find("6")) # SALIDA: -1

#Funcion rfind() permite encontrar la ultima ocurrencia de una subcadena en una cadena
print("12345".rfind("3")) # SALIDA: 2
print("12345".rfind("6")) # SALIDA: -1
