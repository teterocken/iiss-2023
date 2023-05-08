class Observer:
    observers = []

    def __init__(self):
        self.observers.append(self)
        self.observables = {}

    def observe(self, nombre_evento, callback):
        self.observables[nombre_evento] = callback


class Event:
    def __init__(self, nombre, data, autofire=True):
        self.nombre = nombre
        self.data = data
        if autofire:
            self.fire()

    def fire(self):
        for observer in Observer.observers:
            if self.nombre in observer.observables:
                observer.observables[self.nombre](self.data)


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
    peli = Cinepelicula()
    pelicula = input()
    n_entr = Cineentradas()
    entradas = input()
    peli.observe("Que comemos de primero", peli.que_vemos)
    n_entr.observe("Y de segundo", n_entr.cuantos_somos)
    Event("Que comemos de primero", pelicula)
    Event("Y de segundo", entradas)


if __name__ == "__main__":
    main()
