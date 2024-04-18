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
    
'''
El uso de la comprensión de listas puede hacer que el código sea más delgado. Puedes hacer eso si quieres.

Presentemos nuestra versión:

La línea 16: pide al usuario que ingrese una línea llena de cualquier cantidad de números (los números pueden ser flotantes).
La línea 17: divide la línea en una lista con subcadenas.
La línea 18: se inicializa la suma total a cero.
La línea 19: como la conversión de cadena a flotante puede generar una excepción, es mejor continuar con la protección del bloque try-except.
La línea 20: itera a través de la lista...
La línea 21: ... e intenta convertir todos sus elementos en números flotantes; si funciona, aumenta la suma.
La línea 22: todo está bien hasta ahora, así que imprime la suma.
La línea 23: el programa termina aquí en caso de error.
La línea 24: imprime un mensaje de diagnóstico que muestra al usuario el motivo de la falla.
El código tiene una debilidad importante: muestra un resultado falso cuando el usuario ingresa una línea vacía. ¿Puedes arreglarlo?
'''