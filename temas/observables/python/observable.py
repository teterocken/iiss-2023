from rx.subject import Subject


class Observer:
    observers = []

    def __init__(self):
        self.observers.append(self)
        self.observables = {}

    def observe(self, nombre_evento, callback):
        self.observables[nombre_evento] = Subject()
        self.observables[nombre_evento].subscribe(callback)

    def notify(self, nombre_evento, data):
        if nombre_evento in self.observables:
            self.observables[nombre_evento].on_next(data)


class Evento:
    def __init__(self, nombre, data, autofire=True):
        self.nombre = nombre
        self.data = data
        if autofire:
            self.fire()

    def fire(self):
        for observer in Observer.observers:
            observer.notify(self.nombre, self.data)


class Cinepelicula(Observer):
    def __init__(self):
        print("¿Que pelicula desea ver?")
        Observer.__init__(self)

    def que_vemos(self, pelicula):
        print("Usted/es verán la película " + pelicula + ".")


class Cineentradas(Observer):
    def __init__(self):
        print("¿Cuantas entradas desea?")
        Observer.__init__(self)

    def cuantos_somos(self, entradas):
        print("Ha pedido " + entradas + " entradas.")


def main():
    pelicula_observer = Cinepelicula()
    pelicula = input()
    entradas_observer = Cineentradas()
    entradas = input()
    pelicula_observer.observe("Que comemos de primero", pelicula_observer.que_vemos)
    entradas_observer.observe("Y de segundo", entradas_observer.cuantos_somos)
    Evento("Que comemos de primero", pelicula)
    Evento("Y de segundo", entradas)


if __name__ == "__main__":
    main()
