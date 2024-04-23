'''
Como ya sabes, no hay obstáculos para usar la herencia múltiple en Python. 
Puedes derivar cualquier clase nueva de más de una clase definida previamente.

Solo hay un "pero". El hecho de que puedas hacerlo no significa que tengas que hacerlo.

No olvides que:

    Una sola clase de herencia siempre es más simple, segura y fácil de entender y mantener.

    La herencia múltiple siempre es arriesgada, ya que tienes muchas 
    más oportunidades de cometer un error al identificar estas partes de las 
    superclases que influirán efectivamente en la nueva clase.

    La herencia múltiple puede hacer que la anulación sea extremadamente 
    difícil; además, el emplear la función super() se vuelve ambiguo.

    La herencia múltiple viola el principio de responsabilidad única 
    (mas detalles aquí: https://en.wikipedia.org/wiki/Single_responsibility_principle) 
    ya que forma una nueva clase de dos (o más) clases que no saben nada una de la otra.

    Sugerimos encarecidamente la herencia múltiple como la última de todas las 
    posibles soluciones: si realmente necesitas las diferentes funcionalidades que 
    ofrecen las diferentes clases, la composición puede ser una mejor alternativa.
'''