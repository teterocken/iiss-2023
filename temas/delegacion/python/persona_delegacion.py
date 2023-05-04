class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años.")


class Estudiante:
    def __init__(self, persona, grado, curso):
        self.persona = persona
        self.grado = grado
        self.curso = curso

    def __getattr__(self, item):
        return getattr(self.persona, item)

    def estudio(self):
        print("Estudio " + self.grado + " y estoy en el curso numero " + str(self.curso))


class Funcionario:
    def __init__(self, persona, puesto):
        self.persona = persona
        self.puesto = puesto

    def __getattr__(self, item):
        return getattr(self.persona, item)

    def trabajo(self):
        print(f"Tengo un puesto como funcionario/a, soy {self.puesto}")


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
