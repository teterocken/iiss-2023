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

Una vez escrito todo esto, se creará un objeto de cada Concrete Observer, y se pedirá al usuario los datos asociados a los eventos que querrán actualizar estos Concrete Observers:

```python
pelicula_observer = Cinepelicula()
    pelicula = input()
    entradas_observer = Cineentradas()
    entradas = input()
    pelicula_observer.observe("Que comemos de primero", pelicula_observer.que_vemos)
    entradas_observer.observe("Y de segundo", entradas_observer.cuantos_somos)
    Evento("Que comemos de primero", pelicula)
    Evento("Y de segundo", entradas)
```

Un ejemplo de salida sería el siguiente:
```
¿Que pelicula desea ver?
El Padrino
¿Cuantas entradas desea?
Tres
Usted/es verán la película El Padrino.
Ha pedido Tres entradas.
```

# Conclusión

Es muy sencillo implementar el patrón Observer en Python y añadirle la funcionalidad de los observables- Esto nos permite crear código como el del ejemplo, que permitirá una programación orientada a eventos un tanto rudimentaria gracias a la clase Evento, lo cual permite el uso de observables para poder actualizar al Concrete Observer cuando sea posible con los datos del correspondiente evento.
