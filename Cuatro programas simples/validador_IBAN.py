'''
El cuarto programa implementa (en una forma ligeramente simplificada) un algoritmo 
utilizado por los bancos Europeos para especificar los números de cuenta. El estándar 
llamado IBAN (Número de cuenta bancaria internacional) proporciona un método simple y 
bastante confiable para validar los números de cuenta contra errores tipográficos simples 
que pueden ocurrir durante la reescritura del número, por ejemplo, de documentos en 
papel, como facturas o facturas en las computadoras.

Puedes encontrar más detalles aquí: https://en.wikipedia.org/wiki/International_Bank_Account_Number.

Un número de cuenta compatible con IBAN consta de:

Un código de país de dos letras tomado del estándar ISO 3166-1 (por ejemplo, FR para 
Francia, GB para Gran Bretaña DE para Alemania, y así sucesivamente).
Dos dígitos de verificación utilizados para realizar las verificaciones de validez: pruebas 
rápidas y simples, pero no totalmente confiables, que muestran si un número es 
inválido (distorsionado por un error tipográfico) o válido.
El número de cuenta real (hasta 30 caracteres alfanuméricos; la longitud de esa parte depende del país).
El estándar dice que la validación requiere los siguientes pasos (según Wikipedia):

(Paso 1) Verificar que la longitud total del IBAN sea correcta según el país (este programa no 
         lo hará, pero puedes modificar el código para cumplir con este requisito si lo deseas; pero debes 
         enseñar al código a conocer todas las longitudes utilizadas en Europa).
(Paso 2) Mueve los cuatro caracteres iniciales al final de la cadena (es decir, el código 
         del país y los dígitos de verificación).
(Paso 3) Reemplaza cada letra en la cadena con dos dígitos, expandiendo así la cadena, donde 
         A = 10, B = 11 ... Z = 35.
(Paso 4) Interpreta la cadena como un entero decimal y calcula el residuo de ese número dividiéndolo 
         entre 97. Si el residuo es 1, pasa la prueba de verificación de dígitos y el IBAN puede ser válido.
         
Observa el código en el editor. Analicémoslo:
'''

# Validador IBAN.

iban = input("Ingresa un IBAN, por favor: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("Has introducido caracteres no válidos.")
elif len(iban) < 15:
    print("El IBAN ingresado es demasiado corto.")
elif len(iban) > 31:
    print("El IBAN ingresado es demasiado largo.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("El IBAN ingresado es válido.")
    else:
        print("El IBAN ingresado no es válido.")
    
'''
Línea 36: pide al usuario que ingrese el IBAN (el número puede contener espacios, ya que mejoran significativamente la legibilidad del número...
Línea 37: ... pero remueve los espacios de inmediato).
Línea 39: el IBAN ingresado debe constar solo de dígitos y letras, de lo contrario...
Línea 40: ... muestra un mensaje.
Línea 41: el IBAN no debe tener menos de 15 caracteres (esta es la variante más corta, utilizada en Noruega).
Línea 42: si es más corto, se informa al usuario.
Línea 43: además, el IBAN no puede tener más de 31 caracteres (esta es la variante más larga, utilizada en Malta).
Línea 44: si es más largo, se le informa al usuario.
Línea 45: se comienza con el procesamiento.
Línea 46: se mueven los cuatro caracteres iniciales al final del número y se convierten todas las letras a mayúsculas (paso 02 del algoritmo).
Línea 47: esta es la variable utilizada para completar el número, creada al reemplazar las letras con dígitos (de acuerdo con el paso 03 del algoritmo).
Línea 48: iterar a través del IBAN.
Línea 49: si el carácter es un dígito...
Línea 50: solo se copia.
Línea 51: de lo contrario...
Línea 52: ... conviértelo en dos dígitos (observa cómo se hace aquí).
Línea 53: la forma convertida del IBAN está lista: ahora se convierte en un número entero.
Línea 54: ¿el residuo de la división de iban2 entre 97 es igual a 1?
Línea 55: si es así, entonces el número es correcto.
Línea 56: de lo contrario...
Línea 57: ... el número no es válido.
Agreguemos algunos datos de prueba (todos estos números son válidos; puedes invalidarlos cambiando cualquier carácter).

Inglés: GB72 HBZU 7006 7212 1253 00
Francés: FR76 30003 03620 00020216907 50
Alemán: DE02100100100152517108
Si eres residente de la UE, puedes usar tu propio número de cuenta para hacer pruebas.
'''