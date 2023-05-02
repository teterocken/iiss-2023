# Ejecución del programa
Abriendo una terminal en la misma carpeta donde se haye el código, ejecutar la orden "python Lambdas.py".

# Explicación del código

### Funciones lambda básicas

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

### List comprehensions

Se crea una lista, v, con los numeros (naturales) del 1 al 10, y se crea una nueva lista, pares, que guarda solo los numeros pares de la lista v de una manera convencional:

```python
v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []
for n in v:
    if n % 2 == 0:
        pares.append(n)
```

Después se crea una lista, pares_lc, que también guardará los números pares de v, pero mediante el mecanismo de list comprehensions:

```python
pares_lc = [x for x in v if x % 2 == 0]
```

El contenido de las listas pares y pares_lc, será el mismo: [2, 4, 6, 8, 10]

### Map-reduce

Se crea una lista que contiene los números (naturales) del 1 al 5, se guarda el cuadrado de cada posicion de la lista en su respectiva posición de la lista cuadrados mediante el método map, después se guarda la suma de los cuadrados en la variable sumacuadrados, haciendo esta suma con el método reduce:

```python
numeros = [1, 2, 3, 4, 5]

cuadrados = list(map(lambda x: x ** 2, numeros))

sumacuadrados = reduce(lambda x, y: x + y, cuadrados)
```

La variable sumacuadrados guardará el valor 55.

### Filters

Se crea una lista, vec, con los numeros (naturales) del 1 al 10, al que se le aplicará un filter que hará que se guarde solo los numeros impares de la lista vec en la lista impares:

```python
vec = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

impares = list(filter(lambda x: x % 2 == 1, vec))
```

El contenido de impares será [1, 3, 5, 7, 9].

# Conclusión

Las funciones lambda en Python permiten guardar en una variable una función, lo cual, en funciones tan sencillas como las de estos ejemplos permiten una implementación aún más rápida y sencilla.

Cabe destacar que el intérprete de Pycharm manda un weak warning recomendando no declarar las funciones lambda, sino hacerlo de la manera convencional.

Las list comprehensions permiten, mediante el uso de lambdas, elegir qué elementos, de otra lista en este caso, se guardan en una nueva lista, en función de lo que se le pida, en el ejemplo se guardan los que cumplen la condición x % 2 == 0. Esta no es más que una manera de aplicar funciones lambdas en un marco preestablecido, pues como se puede ver en el ejemplo, el resultado es el mismo que aplicar un bucle que recorra la lista en búsqueda de números pares para guardarlos en la nueva lista.

Las funciones map y reduce permiten utilizar funciones lambdas en sus respectivos cometidos, en el caso de map, aplicar la función para proyectar el contenido de una lista en otra lista aplicando el resultado de la función. En el caso de reduce permite utilizar el resultado de la función para reducir en un valor el contenido de una lista. En este caso, la suma de todos los contenidos de la lista.

Los filters permiten filtrar una lista según la función que se le pase, las cuales además pueden ser lambdas, como en este caso. En el ejemplo se filtra el contenido de la lista en una nueva lista, guardándose en la nueva lista solo los valores que cumplen la condición x % 2 == 1.
