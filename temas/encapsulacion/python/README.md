# Ejecución del programa
Este archivo se puede ejecutar al ejecutar la instruccción "python encapsulacion.py" en terminal desde el mismo directorio en el que esté situado el archivo.


# Explicación del código

## Ocultación de implementación de datos

Existen 3 clases que implementan exactamente lo mismo, una excursión con un atributo monitor, uno origen y uno destino. Excursionpublica la implementa con atributos publicos, Excursionprotected, con atributos protegidos (o su equivalente en Python, que es escribir el atributo empezando en \_), y Excursionprivada con atributos privados (o su equivalente en Python, que es escribir el atributo empezando en \_\_). Una vez definidas estas clases:
El siguiente código representa a la clase Excursionpublica, las otras 2 clases son exactamente iguales pero añaden los respectivos \_ o \_\_ antes de los nombres de los atributos:

```python
class Excursionpublica:

    monitor = 'Samuel'

    def __init__(self, origen, destino):

        self.origen = origen
 
        self.destino = destino
```

### Utilización de la clase con atributos públicos
Se crea una variable excursion de tipo Excursionpublica, y se muestra como se puede acceder y modificar los atributos de excursion sin problema alguno.
Véase en el código:

```python
excursion = Excursionpublica('Puerto Real', 'Jerez')

print(excursion.monitor)

print(excursion.destino)

excursion.destino = 'Sevilla'

print(excursion.destino)
```

### Utilización de la clase con atributos protegidos
La variable excursión pasa a ser protected y al ejecutar instrucciones de acceso o modificación de sus atributos se contempla que, aunque teóricamente no debiera ser así, Python no restringe el acceso o modificación a las variables protegidas, tan solo existe un weak warning por parte del framework que utilizo para trabajar con Python (por parte del propio intérprete Python no existe ningún problema para ejecutar el código).
Véase en el código:

```python
excursion = Excursionprotected('Puerto Real', 'Jerez')

print(excursion._monitor)

print(excursion._destino)

excursion._destino = 'Sevilla'

print(excursion._destino)
```

### Utilización de la clase con atributos privados
Al ejecutar las instrucciones siendo excursion un objeto de la clase Excursionprivada, el intérprete da error al tratar de ejecutar las órdenes de acceso o modificación de atributos privados.
Véase en el código (Comentado por los errores que este código causa):

```python
print(excursion.__monitor)

print(excursion.__destino)

excursion.__destino = 'Sevilla'

print(excursion.__destino)
```

### Salida al ejecutar estos 3 fragmentos de código

_Samuel_

_Jerez_

_Sevilla_

_Samuel_

_Jerez_

_Sevilla_

_Traceback (most recent call last):_
  
_File "C:\Users\friki\OneDrive\Escritorio\IISS\Practicas\Encapsulacion\encapsulacion.py", line 47, in <module>_
    
print(excursion.__monitor)

_AttributeError: 'Excursionprivada' object has no attribute '\_\_monitor'_

## Ocultación de implementación de operaciones/métodos de la misma manera que la ocultación de datos

Se crea la clase calculadora, que tendrá un método público multiplicar(), que hace uso de un método privado sumar():

```python
class Calculadora:
    def __init__(self, marca):
        self.marca = marca

    def __sumar(self, n1, n2):
        return n1 + n2

    def multiplicar(self, n1, n2):
        producto = 0
        for i in range(n2):
            producto = self.__sumar(producto, n1)
        return producto
```

El método multiplicar podrá ser llamado por cualquier calculadora, sin embargo el método sumar solo puede ser llamado en el contexto de la clase, entonces, al escribir el siguiente fragmento:

```python
C1 = Calculadora("Casio")
print(C1.multiplicar(4, 5))
print(C1.__sumar(4,5))
```

La salida será la siguiente:

_20_

_Traceback (most recent call last):_

_File "C:\Users\friki\OneDrive\Escritorio\IISS\Practicas\Encapsulacion\encapsulacion.py", line 73, in <module>_
    
print(C1.__sumar(4,5))
    
_AttributeError: 'Calculadora' object has no attribute '\_\_sumar'_

## Ocultación de operaciones/métodos

Tomando la clase Futbolista como la unica interfaz que podría ser visible para el cliente, se le podría así ocultar el funcionamiento del método carta_presentacion(), que será implementado en cada subclase de futbolista de una manera específica.
    
La clase Futbolista sería la siguiente:

```python
   class Futbolista(ABC):
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def carta_presentacion(self):
        pass
```
    
Esta clase es una clase abstracta, por lo cual no se puede instanciar ningún objeto de tipo Futbolista.
	
Tras esto, se escriben dos subclases de esta clase:
    
```python
class Delantero(Futbolista):
    def __init__(self, nombre, goles):
        super().__init__(nombre)
        self.goles = goles

    def carta_presentacion(self):
        print(f"Mi nombre es {self.nombre}, juego de delantero y esta temporada llevo {self.goles} goles.")
```
	
```python
class Defensa(Futbolista):
    def __init__(self, nombre, robos):
        super().__init__(nombre)
        self.robos = robos

    def carta_presentacion(self):
        print(f"Mi nombre es {self.nombre}, juego como defensa y esta temporada llevo {self.robos} robos de balón.")
```
	
Para comprobar el correcto funcionamiento de estas dos clases escribí el siguiente código:
	
```python
Leo = Delantero("Leo Messi", 40)
Mili = Defensa("Eder Militao", 124)
Leo.carta_presentacion()
Mili.carta_presentacion()
```
	
Tendrá la siguiente salida:
```
Mi nombre es Leo Messi, juego de delantero y esta temporada llevo 40 goles.
Mi nombre es Eder Militao, juego como defensa y esta temporada llevo 124 robos de balón.
```
    
# Conclusión
Python no es un lenguaje de programación pensado para utilizar encapsulación, de ahí que la forma en la que se implementa no sea la más avanzada posible, y sea más bien una forma similar a la de lenguajes como C, C++ o Java, para que aquellos programadores que deseen usar Python para programar de una manera parecida a la que lo harían con estos lenguajes tengan una equivalencia como la presentada en el código, aunque ni siquiera implementada de forma completamente equivalente a la de estos lenguajes.
    
La ocultación de operaciones de manera similar a lo que ocurre con la ocultación de atributos, al igual que en lenguajes más centrados a la orientación a objetos, sigue siendo muy útil para ocultar ciertos métodos al cliente, pudiendo utilizarlos en la propia clase.
	
La ocultación de la implementación operaciones/métodos se puede realizar de manera muy sencilla utilizando el pass y la herencia de la clase ABC y la etiqueta @abstractmethod (ambas de la biblioteca abc), lo cual permite especificar el funcionamiento de los métodos en cada superclase, y aún así seguir dando una interfaz común. Es muy similar al virtual en C++ o al abstract en Java.
