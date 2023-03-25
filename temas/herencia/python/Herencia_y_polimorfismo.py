class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def acelerar(self):
        print(f"El/La {self.marca} {self.modelo} está acelerando.")


def llama_acelerar(x):
    x.acelerar()


class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, numero_puertas):
        super().__init__(marca, modelo, velocidad_maxima)
        self.numero_puertas = numero_puertas

    def acelerar(self):
        print(f"El/La {self.marca} {self.modelo} está acelerando. Sus {self.numero_puertas} puertas están cerradas.")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, cilindrada):
        super().__init__(marca, modelo, velocidad_maxima)
        self.cilindrada = cilindrada

    def acelerar(self):
        print(f"El/La {self.marca} {self.modelo} está acelerando. Tiene una cilindrada de {self.cilindrada} CC.")


class Camion(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, peso):
        super().__init__(marca, modelo, velocidad_maxima)
        self.peso = peso


class Guepardo:
    def __init__(self, edad):
        self.edad = edad

    def acelerar(self):
        print(f"El guepardo, de {self.edad} años acelera muy rápido")


vehiculos = [Coche("Tesla", "Model X", 200, 4),
             Moto("Kawasaki", "Z400", 300, 1000),
             Camion("Volvo", "FH", 120, 19000),
             Guepardo(4)]

for vehiculo in vehiculos:
    llama_acelerar(vehiculo)
