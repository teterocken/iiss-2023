# Ejecución del programa
Abriendo una terminal en la misma carpeta donde se haye el código, ejecutar la orden "python Lambdas.py".

# Explicación del código

### Funciones lambda básicas

Se crea una función convencional y una función lambda que devuelven el cuadrado del número que reciben:
```python
def cuadrado(x):
    return x * x


cuadrado_lambda = lambda x: x * x
```

Después se hace lo mismo con una función que devuelve True si el número es par, y False en caso contrario:
```python
def es_par(x):
    if x % 2 == 0:
        return True
    else:
        return False


es_par_lambda = lambda x: True if x % 2 == 0 else False
```

Por último se hace lo mismo para una función que devuelve True si el número es impar, y False en caso contrario:
```python
def es_impar(x):
    return not es_par(x)


es_impar_lambda = lambda x: not es_par_lambda(x)
```

Una vez escrito esto se ejecutan las 6 funciones para comprobar que los resultados sean los esperados:
```python
print(cuadrado(3))
print(cuadrado_lambda(3))
print(es_par(100))
print(es_par_lambda(3))
print(es_impar(100))
print(es_impar_lambda(3))
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

### Tuple Generators

Se crea una lista, numeros, con los numeros (naturales) del 1 al 18, y una variable, suma\_objetivo que será igual a 23. Se generador\_duplas será una lista de duplas de números (distintos entre sí) de la lista numeros que suman un valor igual al de suma\_objetivo:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
suma_objetivo = 23

generador_duplas = ((x, y) for i, x in enumerate(numeros) for y in numeros[i+1:] if x + y == suma_objetivo)
```

Al aplicar esto, se puede recorrer la lista para ver las duplas generadas:

```python
for dupla in generador_duplas:
    print(dupla)
```

La salida será la siguiente:

```
(5, 18)
(6, 17)
(7, 16)
(8, 15)
(9, 14)
(10, 13)
(11, 12)
```

Además, no solo se pueden generar duplas, sino también 3-tuplas(p.ej):

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
suma_objetivo = 23

generador_tuplas = ((x, y, z) for i, x in enumerate(numeros) for j, y in enumerate(numeros[i+1:]) for z in
                    numeros[i+j+2:] if x + y + z == suma_objetivo)
```

La salida en este caso será:

```
(1, 4, 18)
(1, 5, 17)
(1, 6, 16)
(1, 7, 15)
(1, 8, 14)
(1, 9, 13)
(1, 10, 12)
(2, 3, 18)
(2, 4, 17)
(2, 5, 16)
(2, 6, 15)
(2, 7, 14)
(2, 8, 13)
(2, 9, 12)
(2, 10, 11)
(3, 4, 16)
(3, 5, 15)
(3, 6, 14)
(3, 7, 13)
(3, 8, 12)
(3, 9, 11)
(4, 5, 14)
(4, 6, 13)
(4, 7, 12)
(4, 8, 11)
(4, 9, 10)
(5, 6, 12)
(5, 7, 11)
(5, 8, 10)
(6, 7, 10)
(6, 8, 9)
```

# Conclusión

Las funciones lambda en Python permiten guardar en una variable una función, lo cual, en funciones tan sencillas como las de estos ejemplos permiten una implementación aún más rápida y sencilla.

Cabe destacar que el intérprete de Pycharm manda un weak warning recomendando no declarar las funciones lambda, sino hacerlo de la manera convencional.

Las list comprehensions permiten, mediante el uso de lambdas, elegir qué elementos, de otra lista en este caso, se guardan en una nueva lista, en función de lo que se le pida, en el ejemplo se guardan los que cumplen la condición x % 2 == 0. Esta no es más que una manera de aplicar funciones lambdas en un marco preestablecido, pues como se puede ver en el ejemplo, el resultado es el mismo que aplicar un bucle que recorra la lista en búsqueda de números pares para guardarlos en la nueva lista.

Las funciones map y reduce permiten utilizar funciones lambdas en sus respectivos cometidos, en el caso de map, aplicar la función para proyectar el contenido de una lista en otra lista aplicando el resultado de la función. En el caso de reduce permite utilizar el resultado de la función para reducir en un valor el contenido de una lista. En este caso, la suma de todos los contenidos de la lista.

Los filters permiten filtrar una lista según la función que se le pase, las cuales además pueden ser lambdas, como en este caso. En el ejemplo se filtra el contenido de la lista en una nueva lista, guardándose en la nueva lista solo los valores que cumplen la condición x % 2 == 1.

Los tuple generators sirven para, mediante el uso de funciones lambda, crear una lista de tuplas que cumplan la condición especificada, en este caso que los valores de la tupla sumen 23. La diferencia con respecto a las list comprehensions es que la función lambda especificada en este caso permite crear una lista de tuplas, lo cual sirve para cuando quieres almacenar que par, o que n-tupla de valores de la lista cumple la condición especificada. Sin embargo, las list comprehensions son útiles cuando se quiere crear una lista de valores únicos de la lista que se filtra respecto a la condición

# Refactoring

En la parte de funciones lambda básicas, las funciones se llamaban a(), c() y e(). Las funciones lambda eran guardadas en las variables b, d y f.
Esta nomenclatura no aclaraba para nada qué hace cada función, es por eso que cambié el nombre a cuadrado() y su respectiva cuadrado_lambda, es_par() y su respectiva es_par_lambda y es_impar() y su respectiva es_impar_lambda. Lo cual ahora sí aclara el funcionamiento de las funciones.

Además en el caso de las funciones que detectan impares, se podía reciclar el funcionamiento de las funciones que detectan pares, pues hacen todo lo contrario, así también se corrige el problema del código duplicado.

Cabe aclarar que en es_par_lamda podría haber usado la función es_par, pero quería enseñar también como se implementaba la función lambda.
