'''
-> Histograma de frecuencia de caracteres ordenado <-
El código anterior necesita ser mejorado. Está bien, pero tiene que ser mejor.

Tu tarea es hacer algunas enmiendas, que generen los siguientes resultados:

El histograma de salida se ordenará en función de la frecuencia de los caracteres (el contador más grande debe presentarse primero).
El histograma debe enviarse a un archivo con el mismo nombre que el de entrada, pero con la extensión '.hist' (debe concatenarse con el nombre original).
Suponiendo que el archivo de prueba `samplefile_2.txt`contiene solo una línea con:

cBabAa

El resultado esperado debería verse de la siguiente manera:

a -> 3
b -> 2
c -> 1

Consejo: Emplea una lambda para cambiar el ordenamiento.
'''

from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Ingresa el nombre del archivo a analizar: ")
try:
    file = open('./Archivos/Procesando_archivos/' + file_name, "rt")
    for line in file:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    file.close()
    file = open('./Archivos/Procesando_archivos/' + file_name + '.hist', 'wt')
    # Nota: hemos utilizado una lambda para acceder a los elementos del directorio y se ha establecido reverse a True para obtener un orden válido.
    for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
        c = counters[char]
        if c > 0:
            file.write(char + ' -> ' + str(c) + '\n')
    file.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
    