'''
Un módulo es un archivo que contiene definiciones y sentencias 
de Python, que se pueden importar más tarde y utilizar cuando sea necesario.
'''

# Importar un módulo en Python
import math

print(math.sqrt(16))# SALIDA: 4.0

# Importar un módulo con un alias
import math as m

print(m.sqrt(16))# SALIDA: 4.0

# Importar solo una función de un módulo
from math import sqrt

print(sqrt(16))# SALIDA: 4.0

# Importar todas las funciones de un módulo
from math import *

print(sqrt(16))# SALIDA: 4.0

# Importar varias funciones de un módulo
from math import sqrt, pow

print(sqrt(16))# SALIDA: 4.0
print(pow(2, 3))# SALIDA: 8.0

# Importar varias funciones de un módulo con un alias
from math import sqrt as raiz, pow as potencia

print(raiz(16))# SALIDA: 4.0
print(potencia(2, 3))# SALIDA: 8.0