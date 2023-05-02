# Ejecución del programa
Abriendo una terminal en la misma carpeta donde se haye el código, ejecutar la orden "python Lambdas.py".

# Explicación del código

## Funciones lambda básicas

Se crea una función convencional y una función lambda que devuelven el cuadrado del número que reciben:
```python
def a(x):
    return x * x


b = lambda x: x * x
```

Después se hace lo mismo con una función que devuelve True si el número es par, y False en caso contrario:
```python
def c(x):
    if x % 2 == 0:
        return True
    else:
        return False


d = lambda x: True if x % 2 == 0 else False
```

Por último se hace lo mismo para una función que devuelve True si el número es impar, y False en caso contrario:
```python
def e(x):
    if x % 2 == 0:
        return False
    else:
        return True


f = lambda x: False if x % 2 == 0 else True
```

Una vez escrito esto se ejecutan las 6 funciones para comprobar que los resultados sean los esperados:
```python
print(a(3))
print(b(3))
print(c(100))
print(d(3))
print(e(100))
print(f(3))
```

Lo cual proporciona la siguiente salida:

_9_

_9_

_True_

_False_

_False_

_True_

# Conclusión

Las funciones lambda en Python permiten guardar en una variable una función, lo cual, en funciones tan sencillas como las de estos ejemplos permiten una implementación aún más rápida y sencilla.

Cabe destacar que el intérprete de Pycharm manda un weak warning recomendando no declarar las funciones lambda, sino hacerlo de la manera convencional.
