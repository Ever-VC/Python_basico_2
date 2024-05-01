'''
-> Cerrando los flujos (streams) <-
La última operación realizada en un stream (esto no incluye a los streams stdin, stdout, y 
stderr pues no lo requieren) debe ser cerrarlo.

Esa acción se realiza mediante un método invocado desde dentro del objeto del stream: stream.close().

    * El nombre de la función es fácil de entender close(), es decir cerrar.
    * La función no espera argumentos; el stream no necesita estar abierto.
    * La función no devuelve nada pero genera una excepción IOError en caso de un error.
    * La mayoría de los desarrolladores creen que la función close() siempre tiene éxito y, por lo tanto, no 
    hay necesidad de verificar si ha realizado su tarea correctamente.

Esta creencia está solo parcialmente justificada. Si el stream se abrió para escribir y luego se 
realizó una serie de operaciones de escritura, puede ocurrir que los datos enviados al stream aún no s
e hayan transferido al dispositivo físico (debido a los mecanismos de cache o buffer).

Dado que el cierre del stream obliga a los bufers a descargarse, es posible que dichas descargas 
fallen y, por lo tanto, close() falle también.

Ya hemos mencionado fallas causadas por funciones que operan con los streams, pero no mencionamos 
nada sobre cómo podemos identificar exactamente la causa de la falla.

La posibilidad de hacer un diagnóstico existe y es proporcionada por uno de los componentes de excepción 
de los streams. Hablaremos acerca de ellos a continuación.
'''