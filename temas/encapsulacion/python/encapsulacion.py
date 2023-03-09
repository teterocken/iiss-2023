# Clase que implementa excursión con atributos públicos
class Excursionpublica:
    monitor = 'Samuel'

    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino


# Clase que implementa excursión con atributos protegidos
class Excursionprotected:
    _monitor = 'Samuel'

    def __init__(self, origen, destino):
        self._origen = origen
        self._destino = destino


# Clase que implementa excursión con atributos privados
class Excursionprivada:
    __monitor = 'Samuel'

    def __init__(self, origen, destino):
        self.__origen = origen
        self.__destino = destino


excursion = Excursionpublica('Puerto Real', 'Jerez')
print(excursion.monitor)
print(excursion.destino)
excursion.destino = 'Sevilla'
print(excursion.destino)
# Obviamente con la clase con atributos públicos no hay problema para acceder y modificar sus miembros

excursion = Excursionprotected('Puerto Real', 'Jerez')
print(excursion._monitor)
print(excursion._destino)
excursion._destino = 'Sevilla'
print(excursion._destino)

# Aunque teoricamente con la clase con atributos protected no debería poderse
# acceder y modificar los miembros, Python no lo prohibe, aunque si que existe un weak warning

excursion = Excursionprivada('Puerto Real', 'Jerez')
# print(excursion.__monitor)
# print(excursion.__destino)
# excursion.__destino = 'Sevilla'
# print(excursion.__destino)

# En el caso de la clase con miembros privados no se puede ni acceder ni modificar
# los miembros, he dejado las líneas comentadas, puesto que provoca un fallo el intentarlo
