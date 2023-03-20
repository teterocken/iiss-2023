# **Ejecución del programa**
Este archivo se puede ejecutar al ejecutar la instruccción "python encapsulacion.py" en terminal desde el mismo directorio en el que esté situado el archivo.


# **Explicación del código**
Existen 3 clases que implementan exactamente lo mismo, una excursión con un atributo monitor, uno origen y uno destino. Excursionpublica la implementa con atributos publicos, Excursionprotected, con atributos protegidos (o su equivalente en Python, que es escribir el atributo empezando en \_), y Excursionprivada con atributos privados (o su equivalente en Python, que es escribir el atributo empezando en \_\_). Una vez definidas estas clases:
El siguiente código representa a la clase Excursionpublica, las otras 2 clases son exactamente iguales pero añaden los respectivos \_ o \_\_ antes de los nombres de los atributos:

_class Excursionpublica:_

    _monitor = 'Samuel'_

    _def __init__(self, origen, destino):_

        _self.origen = origen_
 
        _self.destino = destino__

## Utilización de la clase con atributos públicos
Se crea una variable excursion de tipo Excursionpublica, y se muestra como se puede acceder y modificar los atributos de excursion sin problema alguno.
Véase en el código:

Ejecución de la clase pública:

_excursion = Excursionpublica('Puerto Real', 'Jerez')_

_print(excursion.monitor)_

_print(excursion.destino)_

_excursion.destino = 'Sevilla'_

_print(excursion.destino)_

## Utilización de la clase con atributos protegidos
La variable excursión pasa a ser protected y al ejecutar instrucciones de acceso o modificación de sus atributos se contempla que, aunque teóricamente no debiera ser así, Python no restringe el acceso o modificación a las variables protegidas, tan solo existe un weak warning por parte del framework que utilizo para trabajar con Python (por parte del propio intérprete Python no existe ningún problema para ejecutar el código).
Véase en el código:

_excursion = Excursionprotected('Puerto Real', 'Jerez')_

_print(excursion.\_monitor)_

_print(excursion.\_destino)_

_excursion.\_destino = 'Sevilla'_

_print(excursion._destino)_

## Utilización de la clase con atributos privados
Al ejecutar las instrucciones siendo excursion un objeto de la clase Excursionprivada, el intérprete da error al tratar de ejecutar las órdenes de acceso o modificación de atributos privados, de ahí el hecho de que se hallen comentadas.
Véase en el código (Comentado por los errores que este código causa):

_print(excursion.\_\_monitor)_

_print(excursion.\_\_destino)_

_excursion.\_\_destino = 'Sevilla'_

_print(excursion.\_\_destino)_


# Conclusión
Python no es un lenguaje de programación pensado para utilizar encapsulación, de ahí que la forma en la que se implementa no sea la más avanzada posible, y sea más bien una forma similar a la de lenguajes como C, C++ o Java, para que aquellos programadores que deseen usar Python para programar de una manera parecida a la que lo harían con estos lenguajes tengan una equivalencia como la presentada en el código, aunque ni siquiera implementada de forma completamente equivalente a la de estos lenguajes.
