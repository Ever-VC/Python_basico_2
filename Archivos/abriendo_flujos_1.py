'''
stream = open(file, mode = 'r', encoding = None)

El nombre de la función (open) habla por si mismo; si la apertura es exitosa, la función 
devuelve un objeto stream; de lo contrario, se genera una excepción (por ejemplo, 
FileNotFoundError si el archivo que vas a leer no existe);

El primer parámetro de la función (file) especifica el nombre del archivo que se asociará al stream.

El segundo parámetro (mode) especifica el modo de apertura utilizado para el stream; es 
una cadena llena de una secuencia de caracteres, y cada uno de ellos tiene su propio significado 
especial (más detalles pronto).

El tercer parámetro (encoding) especifica el tipo de codificación (por ejemplo, UTF-8 cuando se 
trabaja con archivos de texto).

La apertura debe ser la primera operación realizada en el stream.

Nota: el modo y los argumentos de codificación pueden omitirse; en dado caso, se tomarán sus valores 
predeterminados. El modo de apertura predeterminado es leer en modo de texto, mientras que la 
codificación predeterminada depende de la plataforma utilizada.


-> Modos para abrir los flujos o streams: <-

r modo de apertura: lectura

    * El stream será abierto en modo lectura.
    * El archivo asociado con el stream debe existir y tiene que ser legible, de lo contrario la función open() generará una excepción.
    
w modo de apertura: escritura

    * El stream será abierto en modo escritura.
    * El archivo asociado con el stream no necesita existir. Si no existe, se creará; si existe, se 
    truncará a la longitud de cero (se borra); si la creación no es posible (por ejemplo, debido a 
    permisos del sistema) la función open() generará una excepción.
    
a modo de apertura: adjuntar

    * La transmisión se abrirá en modo de adición;
    * El archivo asociado con el stream no necesita existir; si no existe, se creará; si existe, el cabezal 
    de grabación virtual se establecerá al final del archivo (el contenido anterior del archivo permanece intacto).
    
r+ modo de apertura: lectura y actualización

    * El stream será abierto en modo lectura y actualización.
    * El archivo asociado con el stream debe existir y tiene que permitir escritura, de lo contrario la función open() generará una excepción.
    * Se permiten operaciones de lectura y escritura en el stream.
    
w+ modo de apertura: escritura y actualización

    * El stream será abierto en modo escritura y actualización.
    * El archivo asociado con el stream no necesita existir; si no existe, se creará; el contenido anterior del archivo permanece intacto.
    Se permiten operaciones de lectura y escritura en el stream.


-> Selección de los modos de texto y binario <-

Si hay una letra [b] al final de la cadena del modo significa que el stream se debe abrir en el modo binario.

Si la cadena del modo termina con una letra [t] el stream es abierto en modo texto.

El modo texto es el comportamiento predeterminado que se utiliza cuando no se especifica ya sea modo binario o texto.

Finalmente, la apertura exitosa del archivo establecerá la posición actual del archivo (el cabezal virtual de lectura/escritura) 
antes del primer byte del archivo si el modo no es a y después del último byte del archivo si el modo es [a].


┌--------------------------------------------------------┐
| Modo texto | Modo binario |         Descrición         |
|------------|--------------|----------------------------|
|     rt     |      rb      |          lectura           |
|     wt     |      wb      |          escritura         |
|     at     |      ab      |          adjuntar          |
|     r+t    |      r+b     |  lectura y actualización   |
|     w+t    |      w+b     |  escritura y actualización |
└--------------------------------------------------------┘


EXTRA  
También puedes abrir un archivo para su creación exclusiva. Puedes hacer esto usando el modo de apertura [x]. 
Si el archivo ya existe, la función open() generará una excepción.

-> Abriendo el flujo (stream) por primera vez <-
Imagina que queremos desarrollar un programa que lea el contenido del archivo de texto llamado: 
prueba_1.txt.

¿Cómo abrir ese archivo para leerlo? Aquí está el fragmento del código:

'''

try:
    stream = open("prueba_1.txt", "rt")
    # aquí se procesa el archivo
    stream.close()
except Exception as e:
    print("No se puede abrir el arrchivo:", e)
    
'''
¿Que está pasando aqui?

    Hemos abierto el bloque try-except ya que queremos manejar los errores de tiempo de ejecución suavemente.
    Se emplea la función open() para intentar abrir el archivo especificado (ten en cuenta la forma en que hemos especificado el nombre del archivo).
    El modo de apertura se define como texto para leer (como texto es la configuración predeterminada, podemos omitir la t en la cadena de modo).
    En caso de éxito obtenemos un objeto de la función open() y lo asignamos a la variable del stream.
    Si open() falla, manejamos la excepción imprimiendo la información completa del error (es bueno saber qué sucedió exactamente).
'''