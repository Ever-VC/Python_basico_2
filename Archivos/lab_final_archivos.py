'''
El profesor Jekyll dirige clases con estudiantes y regularmente toma notas en un archivo 
de texto (samplefile.txt). Cada línea del archivo contiene 3 elementos: el nombre del alumno, el apellido 
del alumno y el número de puntos que el alumno recibió durante ciertas clases.

Los elementos están separados con espacios en blanco. Cada estudiante puede aparecer 
más de una vez dentro del archivo del profesor Jekyll.

El archivo puede tener el siguiente aspecto:

John     Smith    5
Anna     Boleyn   4.5
John     Smith    2
Anna     Boleyn   11
Andrew   Cox      1.5

Tu tarea es escribir un programa que:

Pida al usuario el nombre del archivo del profesor Jekyll.
Lea el contenido del archivo y cuenta la suma de los puntos recibidos por cada estudiante.
Imprima un informe simple (pero ordenado), como este:
Andrew   Cox      1.5
Anna     Boleyn   15.5
John     Smith    7.0
Output

Nota:

Tu programa debe estar completamente protegido contra todas las fallas posibles: la inexistencia 
del archivo, el vacío del archivo o cualquier falla en los datos de entrada; encontrar 
cualquier error de datos debería causar la terminación inmediata del programa, y lo erróneo 
deberá presentarse al usuario.
Implementa y usa tu propia jerarquía de excepciones: la presentamos en el editor; la segunda 
excepción se debe generar cuando se detecta una línea incorrecta y la tercera cuando el archivo 
fuente existe pero está vacío.

Consejo: Emplea un diccionario para almacenar los datos de los estudiantes.
'''

# Una clase de la excepción base para nuestro código:
class StudentsDataException(Exception):
    pass


# Una excepción para líneas erróneas:
class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string


# Una excepción para un archivo vacío.
class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)


from os import strerror

# Un diccionario para los datos de los estudiantes:
data = { }

file_name = input("Ingresa el nombre del archivo de datos del estudiante: ")
line_number = 1
try:
    f = open('./Archivos/' + file_name, "rt")
    # Leer el archivo completo en la lista.
    lines = f.readlines()
    f.close()
    # ¿El archivo está vacío?
    if len(lines) == 0:
        raise FileEmpty()
    # Escanee el archivo línea por línea.
    for i in range(len(lines)):
        # Obtener la línea n.
        line = lines[i]
        # Divídirlo en columnas.
        columns = line.split()
        # Debe haber 3 columnas, ¿están ahí?
        if len(columns) != 3:
            raise WrongLine(i + 1, line)
        # Construye una clave a partir del nombre y apellido del estudiante.
        student = columns[0] + ' ' + columns[1]
        # Obtener puntos.
        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, line)
        # Actualizar el diccionario.
        try:
            data[student] += points
        except KeyError:
            data[student] = points
    # Imprimir resultados.
    for student in sorted(data.keys()):
        print(student,'\t', data[student])

except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
except WrongLine as e:
    print("Línea incorrecta #" + str(e.line_number) + " en el archivo fuente:" + e.line_string)
except FileEmpty:
    print("Archivo fuente vacío")
    