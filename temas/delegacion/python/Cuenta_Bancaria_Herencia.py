class CuentaBancaria:
    def __init__(self, saldo, num_cuenta):
        self.saldo = saldo
        self.num_cuenta = num_cuenta

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("No posees suficientes fondos")


class Persona(CuentaBancaria):
    def __init__(self, saldo, nombre, num_cuenta, edad):
        super().__init__(saldo, num_cuenta)
        self.nombre = nombre
        self.edad = edad

    def imprimirinfobancaria(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años, y tengo {self.saldo} euros en mi cuenta con "
              f"numero {self.num_cuenta}.")


P1 = Persona(2000, "Paco", 3455099812431272, 23)
P1.depositar(350)
P1.imprimirinfobancaria()
P1.retirar(1000)
P1.imprimirinfobancaria()
