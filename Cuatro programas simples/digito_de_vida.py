'''
Algunos dicen que el Dígito de la Vida es un dígito calculado usando 
el cumpleaños de alguien. Es simple: solo necesitas sumar todos los 
dígitos de la fecha. Si el resultado contiene más de un dígito, se debe 
repetir la suma hasta obtener exactamente un dígito. Por ejemplo:

1 Enero 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 es el dígito que buscamos y encontramos.

La tarea es escribir un programa que:

Le pregunté al usuario su cumpleaños (en el formato AAAAMMDD o AAAADMM o MMDDAAAA; en realidad, el orden de los dígitos no importa).
Dé como salida El Dígito de la Vida para la fecha ingresada.

'''

date = input("Ingresa tu fecha de cumpleaños (en el siguiente formato: AAAAMMDD o AAAADDMM, 8 dígitos): ")
if len(date) != 8 or not date.isdigit():
    print("Formato de fecha inválida.")
else:
    while len(date) > 1:
        the_sum = 0
        for dig in date:
            the_sum += int(dig)
        print(date)
        date = str(the_sum)
    print("Tu Dígito de la Vida es: " + date)