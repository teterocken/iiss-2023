class Empleado:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        pass


class Persona(Empleado):
    def __init__(self, nombre, edad, genero):
        super().__init__(nombre, edad, genero)

    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años.")


class Trabajador(Empleado):
    _empleado: Empleado

    def __init__(self, empleado: Empleado):
        self._empleado = empleado

    def empleado(self):
        return self._empleado

    def presentarse(self):
        pass


class Estudiante(Trabajador):
    def __init__(self, empleado: Empleado, grado, curso):
        super().__init__(empleado)
        self.grado = grado
        self.curso = curso

    def presentarse(self):
        print("Me llamo " + self.empleado().nombre + ", soy estudiante, y tengo " + str(self.empleado().edad) + " años")

    def estudio(self):
        print("Estudio " + self.grado + " y estoy en el curso numero " + str(self.curso) + ".")


class Funcionario(Trabajador):
    def __init__(self, empleado: Empleado, puesto):
        super().__init__(empleado)
        self.puesto = puesto

    def presentarse(self):
        print("Me llamo " + self.empleado().nombre + ", soy funcionario/a, de " + str(self.empleado().edad) + " años.")

    def trabajo(self):
        print(f"Tengo un puesto como funcionario/a, soy {self.puesto}.")


P = Persona("Manuel", 20, "M")
P.presentarse()
EE = Empleado("Lolo", 23, "M")
E = Estudiante(EE, "Ingeniería Informática", 4)
E.presentarse()
E.estudio()
EF = Empleado("Isabel", 34, "F")
F = Funcionario(EF, "policia")
F.presentarse()
F.trabajo()

# ¿Puede una persona ser funcionario y estudiante a la vez?

Func_estudiante = Funcionario(EE, "bombero")
Func_estudiante.presentarse()
Func_estudiante.trabajo()
