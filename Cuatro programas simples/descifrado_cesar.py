'''
La operación inversa ahora debería ser clara para ti: solo presentamos el 
código tal como está, sin ninguna explicación.

Observa el código. Comprueba cuidadosamente si funciona. Usa el criptograma del programa "cifrado_cesae".
'''

# Cifrado César - descifrando un mensaje.
cipher = input('Ingresa tu criptograma: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)