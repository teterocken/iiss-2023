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


class Persona:
    def __init__(self, nombre, edad, cuenta):
        self.nombre = nombre
        self.edad = edad
        self.cuenta = cuenta

    def __getattr__(self, item):
        return getattr(self.cuenta, item)

    def imprimirinfobancaria(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años, y tengo {self.saldo} euros en mi cuenta con "
              f"numero {self.num_cuenta}.")


cuenta_banco = CuentaBancaria(2000, 3455099812431272)
P1 = Persona("Paco", 23, cuenta_banco)
P1.depositar(350)
P1.imprimirinfobancaria()
P1.retirar(1000)
P1.imprimirinfobancaria()
