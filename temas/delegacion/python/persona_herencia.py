class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años.")


class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, grado, curso):
        super().__init__(nombre, edad, genero)
        self.grado = grado
        self.curso = curso

    def estudio(self):
        print("Estudio " + self.grado + " y estoy en el curso numero " + str(self.curso))


class Funcionario(Persona):
    def __init__(self, nombre, edad, genero, puesto):
        super().__init__(nombre, edad, genero)
        self.puesto = puesto

    def trabajo(self):
        print(f"Tengo un puesto como funcionario/a, soy {self.puesto}")


P = Persona("Manuel", 20, "M")
P.presentarse()
E = Estudiante("Lolo", 23, "M", "Ingeniería Informática", 4)
E.presentarse()
E.estudio()
F = Funcionario("Isabel", 34, "F", "policia")
F.presentarse()
F.trabajo()

# ¿Puede una persona ser funcionario y estudiante a la vez?

Func_estudiante = Funcionario("Lolo", 23, "M", "bombero")
Func_estudiante.presentarse()
Func_estudiante.trabajo()
