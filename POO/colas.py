'''
Probemos algo nuevo ahora. Una cola (queue) es un modelo de datos 
caracterizado por el término FIFO: primero en entrar, primero en salir. 
Nota: una cola (fila) regular que conozcas de las tiendas u oficinas 
de correos funciona exactamente de la misma manera: un cliente que 
llegó primero también es el primero en ser atendido.

Vamos a implementar la clase Queue con dos operaciones básicas:

put(elemento), que coloca un elemento al final de la cola.
get(), que toma un elemento del principio de la cola y lo 
devuelve como resultado (la cola no puede estar vacía para realizarlo correctamente).

Emplearemos una lista como tu almacenamiento (como lo hicimos con la pila).
put() debe agregar elementos al principio de la lista, mientras 
que get() debe eliminar los elementos del final de la lista.
Vamos a definir una nueva excepción llamada QueueError 
(elige una excepción de la cual se derivará) y generala 
cuando get() intente operar en una lista vacía.

También queremos que tenga un método sin parámetros que devuelva 
True si la cola está vacía y False de lo contrario.
'''
class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self,elem):
        self.queue.insert(0,elem)
        
    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError


class SuperQueue(Queue):
    def isempty(self):
        return len(self.queue) == 0


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")
    