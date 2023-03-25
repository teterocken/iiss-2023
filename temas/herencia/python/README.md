# Ejecución del programa
Este archivo se puede ejecutar al ejecutar la instruccción "python Herencia_y_polimorfismo.py" en terminal desde el mismo directorio en el que esté situado el archivo.

# Explicación del código
Existe una superclase, Vehículo, de la que derivan tres subclases: Coche, Moto y Camión.

Vehículo contiene un constructor, que asigna al vehículo su marca, su modelo y su velocidad máxima.
Vehículo tiene un método acelerar(), que se implementa de manera básica:
```python
class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
       
    def acelerar(self):
        print(f"El/La {self.marca} {self.modelo} está acelerando.")
```

Coche, Moto y Camión tienen su constructor, mediante el que reutilizan el de Vehículo para asignarle al vehículo los 3 atributos previamente mencionados, y además se asignan su número de puertas en el caso de Coche, su cilindrada en caso de Moto, y su peso en el caso de Camión. Coche y Moto redefinen el comportamiento del método acelerar(), mientras que Camion no lo hace. Además implementaré la clase Guepardo para probar un ejemplo de duck typing en Python:

```python
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
```

Creamos la función llama_acelerar para probar que Python es un idioma que implementa el duck typing ("Si camina como un pato y habla como un pato, es un pato").
De esta forma, la función llama_acelerar no distinguirá el tipo del objeto que la llama, solo si implementa el método acelerar (no le importa recibir un vehículo o no, solo le importa si el objeto que recibe tiene un método acelerar):

```python
def llama_acelerar(x):
    x.acelerar()
```

De esta manera, cuando los cuatro ejecutan sus respectivos métodos acelerar():
```python
vehiculos = [Coche("Tesla", "Model X", 200, 4),
             Moto("Kawasaki", "Z400", 300, 1000),
             Camion("Volvo", "FH", 120, 19000),
             Guepardo(4)]

for vehiculo in vehiculos:
    llama_acelerar(vehiculo)
```

La salida es la siguiente:

_El/La Tesla Model X está acelerando. Sus 4 puertas están cerradas._

_El/La Kawasaki Z400 está acelerando. Tiene una cilindrada de 1000 CC._

_El/La Volvo FH está acelerando._

_El guepardo, de 4 años acelera muy rápido_

# Conclusión
A pesar de que Python no sea el mejor lenguaje para la programación orientada a objetos, la implementación de ejemplos de herencia y polimorfismo si es bastante adecuada, la herencia se puede realizar de una manera cómoda:

```python
class Subclase(Superclase)
```

Y el polimorfismo es también sencillo de implementar (no suele ser complicado usualmente en realidad, pero Python no es una excepción).

Aunque no sería el lenguaje de programación que elegiría para un gran proyecto por lo mal implementada que está la encapsulación; para proyectos pequeños en los que no haga falta una herencia demasiado amplia, que pueda a llegar a necesitar la diferenciación de atributos public, private o protected, no sería una mala opción.

Con el caso de Guepardo se puede comprobar que Python es un lenguaje de programación que implementa duck typing, sin ser Guepardo un derivado de la superclase Vehículo, hemos podido implementar una función que sirva para llamar al metodo acelerar() tanto para los vehículos como para el guepardo.
Es decir, podemos hacer pasar a Guepardo por un vehículo (pato) siempre que los métodos que se invoquen para los vehículos se puedan invocar de la misma forma para Guepardo (andar y hablar como un pato).
