'''
-> Histograma de frecuencia de caracteres <-

Un archivo de texto contiene algo de texto (nada inusual) pero necesitamos saber 
con qué frecuencia aparece cada letra en el texto. Tal análisis puede ser útil en 
criptografía, por lo que queremos poder hacerlo en referencia al alfabeto latino.

Tu tarea es escribir un programa que:

Pida al usuario el nombre del archivo de entrada.
Lea el archivo (si es posible) y cuente todas las letras latinas (las letras mayúsculas y minúsculas se tratan como iguales).
Imprima un histograma simple en orden alfabético (solo se deben presentar recuentos distintos de cero).
Crea un archivo de prueba para tu código y verifica si tu histograma contiene resultados válidos.

Suponiendo que el archivo de prueba llamado `lab_1_prueba.txt` contiene solo una línea con:

aBc

El resultado esperado debería verse de la siguiente manera:

a -> 1
b -> 1
c -> 1

Consejo: Creemos que un diccionario es un medio perfecto de recopilación de datos para almacenar los recuentos. 
Las letras pueden ser las claves mientras que los contadores pueden ser los valores.
'''

from os import strerror

# Inicializa 26 contadores para cada letra latina.
# Nota: hemos usado una comprensión para esto.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Ingresa el nombre del archivo a analizar: ")
try:
    file = open('./Archivos/Procesando_archivos/' + file_name, "rt")
    for line in file:
        for char in line:
            # Si es una letra...
            if char.isalpha():
                # ... lo trataremos en minúsculas y actualizaremos el contador apropiado.
                counters[char.lower()] += 1
    file.close()
    # Imprimamos los contadores.
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
    