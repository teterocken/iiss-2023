class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def acelerar(self):
        print(f"El/La {self.marca} {self.modelo} está acelerando.")


class Auto(Vehiculo):
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


vehiculos = [Auto("Toyota", "Corolla", 200, 4),
             Moto("Yamaha", "R1", 300, 1000),
             Camion("Volvo", "FH", 120, 19000)]

for vehiculo in vehiculos:
    vehiculo.acelerar()
