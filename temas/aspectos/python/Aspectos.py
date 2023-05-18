import aspectlib


class Hora:
    __hora = 0
    __minuto = 0

    def sethora(self, h):
        self.__hora = h

    def setminuto(self, m):
        self.__minuto = m

    def gethora(self):
        if self.__hora < 10:
            if self.__minuto < 10:
                print("Son las 0" + str(self.__hora) + ":0" + str(self.__minuto))
            else:
                print("Son las 0" + str(self.__hora) + ":" + str(self.__minuto))
        else:
            if self.__minuto < 10:
                print("Son las " + str(self.__hora) + ":0" + str(self.__minuto))
            else:
                print("Son las " + str(self.__hora) + ":" + str(self.__minuto))


@aspectlib.Aspect
def validarhora(self, h):
    if 0 <= h <= 23:
        yield
        print("Hora válida")
    else:
        yield
        print("Hora no válida")


@aspectlib.Aspect
def validarminuto(self, m):
    if 0 <= m <= 59:
        yield
        print("Minuto válido")
    else:
        yield
        print("Minuto no válido")


aspectlib.weave(Hora.sethora, validarhora)
aspectlib.weave(Hora.setminuto, validarminuto)

hora = Hora()
hora.sethora(2)
hora.setminuto(48)
hora.gethora()

print("\n")

hora.sethora(26)
hora.setminuto(12)
hora.gethora()

print("\n")

hora.sethora(9)
hora.setminuto(-13)
hora.gethora()

print("\n")

hora.sethora(26)
hora.setminuto(90)
hora.gethora()
