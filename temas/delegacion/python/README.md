# Ejecución del programa
Los archivos se pueden ejecutar al escribir la orden en terminal "python Cuenta_Bancaria_Delegacion.py", o "python Cuenta_Bancaria_Herencia.py", estando situado en la misma carpeta que el respectivo archivo.
# Explicación del código
Ambos códigos implementan la misma funcionalidad, diferenciándose ambos códigos en la forma en la que la implementan, siendo en un caso usando herencia, y en el otro, usando delegación.
Nos encontramos en ambos códigos con la misma implementación de la clase CuentaBancaria:
```python
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
```
Esta clase representa una cuenta bancaria, que se crea con un saldo inicial y un numero de cuenta, y que tiene métodos para ingresar y para retirar (en caso de que sea posible) la cantidad señalada.

Acto seguido se implementa una clase Persona, que representará a una persona propietaria de esa cuenta bancaria.

En el caso de la herencia, la implementación es la siguiente:
```python
class Persona(CuentaBancaria):
    def __init__(self, saldo, nombre, num_cuenta, edad):
        super().__init__(saldo, num_cuenta)
        self.nombre = nombre
        self.edad = edad

    def imprimirinfobancaria(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años, y tengo {self.saldo} euros en mi cuenta con "
              f"numero {self.num_cuenta}.")
```

Persona en este caso, es una subclase de CuentaBancaria; un objeto Persona se crea con el nombre y la edad de la persona, su saldo y su numero de cuenta.

Después se ejecuta el siguiente extracto de código:
```python
P1 = Persona(2000, "Paco", 3455099812431272, 23)
P1.depositar(350)
P1.imprimirinfobancaria()
P1.retirar(1000)
P1.imprimirinfobancaria()
```
Este extracto de código crea una persona y llama 2 veces al método que imprime su información, tras haber realizado un ingreso y una retirada. La salida es la siguiente:

_Soy Paco, tengo 23 años, y tengo 2350 euros en mi cuenta con numero 3455099812431272._

_Soy Paco, tengo 23 años, y tengo 1350 euros en mi cuenta con numero 3455099812431272._

En el caso de la delegación, la implementación de la clase Persona es la siguiente:
```python
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
```

Persona en este caso, es una clase "independiente" de CuentaBancaria, ya que para crear un objeto Persona no es necesario crearlo con sus datos bancarios, sino que se crea con asociandole otro objeto CuentaBancaria.

Para poder delegar los métodos y atributos de CuentaBancaria a Persona se usa el _getattr_, que permite que un objeto persona realice los cambios pertinentes en el objeto CuentaBancaria que tiene asociado.

Después se ejecuta el siguiente extracto de código:
```python
cuenta_banco = CuentaBancaria(2000, 3455099812431272)
P1 = Persona("Paco", 23, cuenta_banco)
P1.depositar(350)
P1.imprimirinfobancaria()
P1.retirar(1000)
P1.imprimirinfobancaria()
```

Este extracto de código crea una persona y llama 2 veces al método que imprime su información, tras haber realizado un ingreso y una retirada, lo mismo que en el caso de la herencia. Sin embargo en este caso, hay que crear primero el objeto CuentaBancaria, y después, asociarlo con la Persona que se crea. La salida es la siguiente (es la misma que en el caso de la herencia):

_Soy Paco, tengo 23 años, y tengo 2350 euros en mi cuenta con numero 3455099812431272._

_Soy Paco, tengo 23 años, y tengo 1350 euros en mi cuenta con numero 3455099812431272._

# Conclusión
Aunque en este caso tan sencillo la diferencia no se note tanto, hay muchos motivos por el que el utilizar delegación en casos como este es mucho más conveniente que usar herencia.

En primer lugar, desde un punto de vista de diseño, el hecho de que una clase Persona sea una subclase de una clase CuentaBancaria, carece de un gran sentido, aunque no sea incorrecto.

En segundo lugar, si los constructores de CuentaBancaria y Persona necesitasen de un número muy extenso de atributos, en el caso de la herencia podría ser un lío, debido a la falta de cohesión entre los atributos que pudiese pedir el constructor de Persona (pediría los de CuentaBancaria, más los específicos de una persona).

Sin embargo, en el caso de la delegación, la cohesión sería mucho mayor, puesto que se crearía la cuenta bancaria, y después se le asociaría como un atributo más a Persona.

En tercer lugar, el código de delegación es mucho más flexible y reutilizable.

Sería muy sencillo por ejemplo, poder asociarle un objeto CuentaPlayStore a persona, con un propio monedero y distintos métodos, y, por ejemplo, otra clase CuentaInstagram, con métodos como publicarFoto() o darLikeAFoto(Foto).

Sin embargo, realizar esto en el caso de la herencia sería de una complejidad demasiado alta.
