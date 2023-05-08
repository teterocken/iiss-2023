# Ejecución del código

Bastará con situarse en terminal en el mismo directorio que el archivo y escribir en terminal la orden "python Observables.py".

# Explicación del código

Lo primero será crear una clase Observer, que guardará los eventos observables a partir del nombre del evento que se le pase que se desea observar:

```python
class Observer:
    observers = []

    def __init__(self):
        self.observers.append(self)
        self.observables = {}

    def observe(self, nombre_evento, callback):
        self.observables[nombre_evento] = callback
```

Tras esto, se crea una clase Evento, que guarda el nombre del evento, y los datos asociados a este nombre. Además, dispara una función que mira dentro de los observables de cada observer, si alguno está esperando la actualización del evento que tenga su nombre, para así actualizarlo con los datos asociados a este:

```python
class Evento:
    def __init__(self, nombre, data, autofire=True):
        self.nombre = nombre
        self.data = data
        if autofire:
            self.fire()

    def fire(self):
        for observer in Observer.observers:
            if self.nombre in observer.observables:
                observer.observables[self.nombre](self.data)
```

Tras esto se crean las siguientes clases, que serán dos Concrete Observers, uno que representa el observer que espera la actualización del evento de qué película le indica que quiere ver el cliente, y otro que espera el número de entradas que pedirá:

```python
class Cinepelicula(Observer):
    def __init__(self):
        print("¿Que pelicula desea ver?")
        Observer.__init__(self)

    def que_vemos(self, pelicula):
        print("Usted/es verán la película " + pelicula + ".")
```

```python
class Cineentradas(Observer):
    def __init__(self):
        print("¿Cuantas entradas desea?")
        Observer.__init__(self)

    def cuantos_somos(self, entradas):
        print("Ha pedido " + entradas + " entradas.")
```


