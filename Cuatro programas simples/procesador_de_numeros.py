'''
El tercer programa muestra un método simple que permite ingresar una línea 
llena de números y sumarlos fácilmente. Nota: la función input(), combinada 
junto con las funciones int() o float(), no es lo adecuado para este propósito.

El procesamiento será extremadamente fácil: queremos que se sumen los números.

Observa el código en el editor. Analicémoslo.

El emplear listas por comprensión puede hacer que el código sea más pequeño. Puedes hacerlo si quieres.

Presentemos nuestra versión:
'''
#Procesador de Números.

line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")