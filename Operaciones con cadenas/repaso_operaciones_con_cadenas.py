#Concatenar cadenas con el operador +
str1 = 'a'
str2 = 'b'

print(str1 + str2) # SALIDA: ab

#Repetir cadenas con el operador *
str1 = 'a'

print(str1 * 3) # SALIDA: aaa

#Indexando cadenas
the_string = 'Python'

for i in range(len(the_string)):
    print(the_string[i], end=' ') # SALIDA: P y t h o n

#Indexando cadenas al revés
the_string = 'Python'

for i in range(len(the_string)):
    print(the_string[-i - 1], end=' ') # SALIDA: n o h t y P

#Iterando sobre una cadena
the_string = 'Python'

for char in the_string:
    print(char, end=' ') # SALIDA: P y t h o n

#Rebanando cadenas
alpha = "abdefg"

print(alpha[1:3]) # SALIDA: bd
print(alpha[3:]) # SALIDA: efg
print(alpha[:3]) # SALIDA: abd
print(alpha[3:-2]) # SALIDA: e
print(alpha[-3:4]) # SALIDA: e
print(alpha[::2]) # SALIDA: adf
print(alpha[1::2]) # SALIDA: beg

#Operador in verifica si una subcadena esta en una cadena
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet) # SALIDA: True
print("F" in alphabet) # SALIDA: False
print("1" in alphabet) # SALIDA: False
print("ghi" in alphabet) # SALIDA: True
print("Xyz" in alphabet) # SALIDA: False

#Operador not in verifica si una subcadena no esta en una cadena
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet) # SALIDA: False
print("F" not in alphabet) # SALIDA: True
print("1" not in alphabet) # SALIDA: True
print("ghi" not in alphabet) # SALIDA: False
print("Xyz" not in alphabet) # SALIDA: True