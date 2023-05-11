# Ejecución del programa
Los archivos se pueden ejecutar al escribir la orden en terminal "python persona_delegacion.py", o "python persona_herencia.py", estando situado en la misma carpeta que el respectivo archivo.
# Explicación del código

Ambos códigos implementan la misma funcionalidad, un programa que permite crear personas base, personas estudiantes y personas funcionarias. La diferencia en el caso de la herencia es que hace falta crear dos clases abstractas para implementar un patrón Decorator que permita instanciar a una persona que pueda ser tanto estudiante como funcionaria. Las clases abstractas son las siguientes:

```python
class Empleado(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    @abstractmethod
    def presentarse(self):
        pass
```

```python
class Trabajador(Empleado):
    _empleado: Empleado

    @abstractmethod
    def __init__(self, persona: Persona):
        self._empleado = persona

    def empleado(self):
        return self._empleado

    @abstractmethod
    def presentarse(self):
        pass
```

Después ambas implementan una clase persona, con exactamente la misma funcionalidad, pero con la diferencia de que en el caso de la herencia la clase Persona hereda de la clase abstracta Empleado.

Herencia:
```python
class Persona(Empleado):
    def __init__(self, nombre, edad, genero):
        super().__init__(nombre, edad, genero)

    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años.")
```

Delegación:
```python
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años.")
```

Después, ambos códigos implementan las clases Estudiante y Funcionario (en el caso de la herencia especializan la función presentarse, en el caso de la delegación preferí dejar que llamasen al método de Persona, para mostrar mejor el potencial de getattr()).

Primero, en el caso de la herencia:

```python
class Estudiante(Trabajador):
    def __init__(self, persona: Persona, grado, curso):
        super().__init__(persona)
        self.grado = grado
        self.curso = curso

    def presentarse(self):
        print("Me llamo " + self.empleado().nombre + ", soy estudiante, y tengo " + str(self.empleado().edad) + " años")

    def estudio(self):
        print("Estudio " + self.grado + " y estoy en el curso numero " + str(self.curso) + ".")
```

```python
class Funcionario(Trabajador):
    def __init__(self, persona: Persona, puesto):
        super().__init__(persona)
        self.puesto = puesto

    def presentarse(self):
        print("Me llamo " + self.empleado().nombre + ", soy funcionario/a, de " + str(self.empleado().edad) + " años.")

    def trabajo(self):
        print(f"Tengo un puesto como funcionario/a, soy {self.puesto}.")
```

En el caso de la delegación:

```python
class Estudiante:
    def __init__(self, persona, grado, curso):
        self.persona = persona
        self.grado = grado
        self.curso = curso

    def __getattr__(self, item):
        return getattr(self.persona, item)

    def estudio(self):
        print("Estudio " + self.grado + " y estoy en el curso numero " + str(self.curso))
```

```python
class Funcionario:
    def __init__(self, persona, puesto):
        self.persona = persona
        self.puesto = puesto

    def __getattr__(self, item):
        return getattr(self.persona, item)

    def trabajo(self):
        print(f"Tengo un puesto como funcionario/a, soy {self.puesto}")
```

Tras esto, en ambos código escribí las siguientes líneas:

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

Las cuales, en el caso de la herencia dan la siguiente salida:
```
Hola soy Manuel y tengo 20 años.
Me llamo Lolo, soy estudiante, y tengo 23 años
Estudio Ingeniería Informática y estoy en el curso numero 4.
Me llamo Isabel, soy funcionario/a, de 34 años.
Tengo un puesto como funcionario/a, soy policia.
```

Y en el caso de la delegación:
```
Hola soy Manuel y tengo 20 años.
Hola soy Lolo y tengo 23 años.
Estudio Ingeniería Informática y estoy en el curso numero 4.
Hola soy Isabel y tengo 34 años.
Tengo un puesto como funcionario/a, soy policia.
```

Tras esto, quise probar como una persona podía ser tanto Estudiante como Funcionario, así que escribí en ambos códigos lo siguiente:
```python
Func_estudiante = Funcionario(PE, "bombero")
Func_estudiante.presentarse()
Func_estudiante.trabajo()
```

Lo cual devolvía la siguiente salida en el caso de la herencia:
```
Me llamo Lolo, soy funcionario/a, de 23 años.
Tengo un puesto como funcionario/a, soy bombero.
```

Y la siguiente salida en el caso de la delegación:
```
Hola soy Lolo y tengo 23 años.
Tengo un puesto como funcionario/a, soy bombero.
```

# Conclusión

Python permite la implementación de la delegación de una manera muy sencilla, y es que se asocia directamente el objeto del que se van a delegar métodos y atributos, y se delegan estos métodos y atributos muy sencillamente con la operación \_\_getattr()\_\_.

En este caso es más recomendable el uso de delegación, puesto que permite mayor flexibilidad con los objetos Persona, sin necesidad de la creación de 2 clases abstractas más.

Para conseguir que una persona pueda ser tanto estudiante como funcionaria, es mucho más comoda la implementación con la delegación, ya que, aunque con herencia se pueda conseguir la misma funcionalidad, se consigue de una manera mucho más compleja y que además, no deja de ser una "pseudodelegación".
