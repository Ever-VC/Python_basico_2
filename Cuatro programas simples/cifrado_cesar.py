'''
Este cifrado fue (probablemente) inventado y utilizado por Cayo Julio César 
y sus tropas durante las Guerras Galas. La idea es bastante simple: cada letra del 
mensaje se reemplaza por su consecuente más cercano (A se convierte en B, B se 
convierte en C, y así sucesivamente). La única excepción es la Z, la cual se convierte en A.

Más detalles aquí: https://en.wikipedia.org/wiki/Caesar_cipher

El siguiente programa es una implementación muy simple (pero funcional) del algoritmo.
'''

# Cifrado César.
text = input("Ingresa tu mensaje: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

'''
Se ha escrito utilizando los siguientes supuestos:

Solo acepta letras latinas (nota: los Romanos no usaban espacios en blanco ni dígitos).
Todas las letras del mensaje están en mayúsculas (nota: los Romanos solo conocían las mayúsculas).
Veamos el código:

La línea 13: pide al usuario que ingrese un mensaje (sin cifrar) de una línea.
La línea 14: prepara una cadena para el mensaje cifrado (esta vacía por ahora).
La línea 15: inicia la iteración a través del mensaje.
La línea 16: si el carácter actual no es alfabético...
La línea 17: ...ignorala.
La línea 18: convierta la letra a mayúsculas (es preferible hacerlo a ciegas, en lugar de verificar si es necesario o no).
La línea 19: obtén el código de la letra e increméntalo en uno.
La línea 20: si el código resultante ha "dejado" el alfabeto latino (si es mayor que el código de la Z)...
La línea 21: ... cámbialo al código de la A.
La línea 22: agrega el carácter recibido al final del mensaje cifrado.
La línea 24: imprime el cifrado.
'''