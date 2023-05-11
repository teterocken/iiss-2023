from abc import ABC, abstractmethod


class Empleado(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    @abstractmethod
    def presentarse(self):
        pass


class Persona(Empleado):
    def __init__(self, nombre, edad, genero):
        super().__init__(nombre, edad, genero)

    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años.")


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


class Estudiante(Trabajador):
    def __init__(self, persona: Persona, grado, curso):
        super().__init__(persona)
        self.grado = grado
        self.curso = curso

    def presentarse(self):
        print("Me llamo " + self.empleado().nombre + ", soy estudiante, y tengo " + str(self.empleado().edad) + " años")

    def estudio(self):
        print("Estudio " + self.grado + " y estoy en el curso numero " + str(self.curso) + ".")


class Funcionario(Trabajador):
    def __init__(self, persona: Persona, puesto):
        super().__init__(persona)
        self.puesto = puesto

    def presentarse(self):
        print("Me llamo " + self.empleado().nombre + ", soy funcionario/a, de " + str(self.empleado().edad) + " años.")

    def trabajo(self):
        print(f"Tengo un puesto como funcionario/a, soy {self.puesto}.")


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

# ¿Puede una persona ser funcionario y estudiante a la vez?

Func_estudiante = Funcionario(PE, "bombero")
Func_estudiante.presentarse()
Func_estudiante.trabajo()
