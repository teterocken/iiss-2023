# Ejecución del código

Hay que situarse en la misma carpeta que el código y ejecutar la orden:

```
python Aspectos.py
```

Será también necesario tener instalada la biblioteca aspectlib:

```
pip install aspectlib
```

# Explicación del código

El código implementa una clase Hora, la cual tendrá un método setter para la hora y otro para minuto, y un método getter que imprime la hora completa:

```python
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
```

Tras esto, se implementan dos aspectos, cada uno para verificar que se introduce una hora o un minuto válido:

```python
@aspectlib.Aspect
def validarhora(self, h):
    if 0 <= h <= 23:
        yield
        print("Hora válida")
    else:
        yield
        print("Hora no válida")
```

```python
@aspectlib.Aspect
def validarminuto(self, m):
    if 0 <= m <= 59:
        yield
        print("Minuto válido")
    else:
        yield
        print("Minuto no válido")
```

Y se asocian estos aspectos a los métodos que modifican sus respectivos valores, es decir, los setters:

```python
aspectlib.weave(Hora.sethora, validarhora)
aspectlib.weave(Hora.setminuto, validarminuto)
```

Entonces, al escribir el siguiente código:

```python
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
```

La salida es la siguiente:

```
Hora válida
Minuto válido
Son las 02:48


Hora no válida
Minuto válido
Son las 26:12


Hora válida
Minuto no válido
Son las 09:0-13


Hora no válida
Minuto no válido
Son las 26:90
```

# Conclusión

Aspectlib permite marcar la creación de un aspecto con la anotación @aspectlib.Aspect. El método aspectlib.weave permite entrelazar la ejecución de una función con el aspecto a aplicarle.

En este caso, usamos 2 aspectos cuyos joinpoint son la asignación de un valor hora o minuto respectivamente, y sus advice serían de tipo before a esta asignación, que devolvería un mensaje que dice si la hora o el minuto son válidos o no.
