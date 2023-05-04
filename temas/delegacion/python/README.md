# Ejecución del programa
Los archivos se pueden ejecutar al escribir la orden en terminal "python persona_delegacion.py", o "python persona_herencia.py", estando situado en la misma carpeta que el respectivo archivo.
# Explicación del código
Ambos códigos implementan la misma funcionalidad, diferenciándose ambos códigos en la forma en la que la implementan, siendo en un caso usando herencia, y en el otro, usando delegación.
Nos encontramos en ambos códigos con la misma implementación de la clase Persona:
```python
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años.")
```
Esta clase representa una persona, que se crea con su nombre, edad y genero, y que tiene un método para presentarse.

Acto seguido se implementa una clase Estudiante.

En el caso de la herencia, la implementación es la siguiente:

```python
class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, grado, curso):
        super().__init__(nombre, edad, genero)
        self.grado = grado
        self.curso = curso

    def estudio(self):
        print("Estudio " + self.grado + " y estoy en el curso numero " + str(self.curso) + ".")
```

Estudiante en este caso, es una subclase de Persona; un objeto Estudiante se crea con el nombre, la edad y el genero de la persona, su grado y el curso en el que está. Un estudiante puede presentarse, y también puede decir que estudia.

También se implementa una clase Funcionario.

En el caso de la herencia, la implementación es la siguiente:

```python
class Funcionario(Persona):
    def __init__(self, nombre, edad, genero, puesto):
        super().__init__(nombre, edad, genero)
        self.puesto = puesto

    def trabajo(self):
        print(f"Tengo un puesto como funcionario/a, soy {self.puesto}.")
```

Funcionario es también una subclase de Persona; un objeto Funcionario se crea con el nombre, edad y género de la persona, y su puesto. Un funcionario puede presentarse y también puede decir cuál es su puesto.

Después se ejecuta el siguiente extracto de código:
```python
P = Persona("Manuel", 20, "M")
P.presentarse()
E = Estudiante("Lolo", 23, "M", "Ingeniería Informática", 4)
E.presentarse()
E.estudio()
F = Funcionario("Isabel", 34, "F", "policia")
F.presentarse()
F.trabajo()
```
Este extracto de código crea una persona, la cual se presenta; crea un estudiante, el cual se presenta y dice de qué estudia; y crea un funcionario, el cual se presenta y dice cuál es su puesto. La salida es la siguiente:

_Hola soy Manuel y tengo 20 años._

_Hola soy Lolo y tengo 23 años._

_Estudio Ingeniería Informática y estoy en el curso numero 4._

_Hola soy Isabel y tengo 34 años._

_Tengo un puesto como funcionario/a, soy policia._

En el caso de la delegación, la implementación de la clase Estudiante es la siguiente:

```python
class Estudiante:
    def __init__(self, persona, grado, curso):
        self.persona = persona
        self.grado = grado
        self.curso = curso

    def __getattr__(self, item):
        return getattr(self.persona, item)

    def estudio(self):
        print("Estudio " + self.grado + " y estoy en el curso numero " + str(self.curso) +".")
```

Y la implementación de la clase Funcionario es la siguiente:

```python
class Funcionario:
    def __init__(self, persona, puesto):
        self.persona = persona
        self.puesto = puesto

    def __getattr__(self, item):
        return getattr(self.persona, item)

    def trabajo(self):
        print(f"Tengo un puesto como funcionario/a, soy {self.puesto}.")
```

Estudiante en este caso, es una clase "independiente" de Persona, ya que para crear un objeto Estudiante no es necesario crearlo con sus datos personales, sino que se crea asociandole otro objeto Persona. Ocurre lo mismo con Funcionario.

Para poder delegar los métodos y atributos de Persona a Estudiante y a Funcionario se usa el \_\_getattr\_\_(), que permite que un objeto Estudiante o Funcionario realice los cambios pertinentes en los atributos del objeto Persona que tiene asociado, o que invoque sus métodos.

Después se ejecuta el siguiente extracto de código:
```python
P = Persona("Manuel", 20, "M")
P.presentarse()
PE = Persona("Lolo", 23, "M")
E = Estudiante(PE, "Ingeniería Informática", 4)
E.presentarse()
E.estudio()
PF = Persona("Isabel", 34, "F")
F = Funcionario(PF, "policia")
F.presentarse()
F.trabajo()
```

La salida que da este extracto de código es exactamente la misma que en el caso de la herencia. Como podemos ver, crea a las mismas personas, pero se asocia de una manera distinta.

# Conclusión

Python permite la implementación de la delegación de una manera muy sencilla, y es que se asocia directamente el objeto del que se van a delegar métodos y atributos, y se delegan estos métodos y atributos muy sencillamente con la operación \_\_getattr()\_\_.

En este caso es más recomendable el uso de delegación, puesto que permite mayor flexibilidad con los objetos Persona.

En el caso de la herencia, las personas solo se pueden crear como Persona base, como Estudiante, o como Funcionario. Si una persona deja de estudiar o deja de ser funcionaria, se borra del sistema como Estudiante o Funcionario, lo cual hace que se borre la Persona en sí del sistema.

Sin embargo, en el caso de la delegación, cuando una persona deja de estudiar o de ser funcionario, se puede borrar el objeto Estudiante o Funcionario sin necesidad de borrar a la Persona del sistema.
