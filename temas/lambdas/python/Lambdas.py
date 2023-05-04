from functools import reduce
# Funciones lambda basicas


def cuadrado(x):
    return x * x


cuadrado_lambda = lambda x: x * x


def es_par(x):
    if x % 2 == 0:
        return True
    else:
        return False


es_par_lambda = lambda x: True if x % 2 == 0 else False


def es_impar(x):
    return not es_par(x)


es_impar_lambda = lambda x: not es_par_lambda(x)

print("Funciones lambda basicas:")
print(cuadrado(3))
print(cuadrado_lambda(3))
print(es_par(100))
print(es_par_lambda(3))
print(es_impar(100))
print(es_impar_lambda(3))


# List comprehensions

v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []
for n in v:
    if n % 2 == 0:
        pares.append(n)

pares_lc = [x for x in v if x % 2 == 0]

print("\nListas de pares de list comprehensions:")
print(pares)
print(pares_lc)


# Map-reduce

numeros = [1, 2, 3, 4, 5]

cuadrados = list(map(lambda x: x ** 2, numeros))

sumacuadrados = reduce(lambda x, y: x + y, cuadrados)

print("\nSuma de los cuadrados (map-reduce:")
print(sumacuadrados)


# Filters

vec = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

impares = list(filter(lambda x: x % 2 == 1, vec))

print("\nLista de impares de los filtros")
print(impares)


# Tuple generators

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
suma_objetivo = 23

generador_duplas = ((x, y) for i, x in enumerate(numeros) for y in numeros[i+1:] if x + y == suma_objetivo)

print("\nDuplas de numeros que suman 23 con tuple generators")
for dupla in generador_duplas:
    print(dupla)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
suma_objetivo = 23

generador_tuplas = ((x, y, z) for i, x in enumerate(numeros) for j, y in enumerate(numeros[i+1:]) for z in
                    numeros[i+j+2:] if x + y + z == suma_objetivo)

print("\n3-tuplas de numeros que suman 23 con tuple generators")
for tupla in generador_tuplas:
    print(tupla)
