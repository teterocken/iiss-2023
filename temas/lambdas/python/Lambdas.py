from functools import reduce
# Funciones lambda basicas


def a(x):
    return x * x


b = lambda x: x * x


def c(x):
    if x % 2 == 0:
        return True
    else:
        return False


d = lambda x: True if x % 2 == 0 else False


def e(x):
    if x % 2 == 0:
        return False
    else:
        return True


f = lambda x: False if x % 2 == 0 else True


print(a(3))
print(b(3))
print(c(100))
print(d(3))
print(e(100))
print(f(3))


# List comprehensions

v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []
for n in v:
    if n % 2 == 0:
        pares.append(n)

pares_lc = [x for x in v if x % 2 == 0]

print(pares)
print(pares_lc)


# Map-reduce

numeros = [1, 2, 3, 4, 5]

cuadrados = list(map(lambda x: x ** 2, numeros))

sumacuadrados = reduce(lambda x, y: x + y, cuadrados)

print(sumacuadrados)


# Filters

vec = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

impares = list(filter(lambda x: x % 2 == 1, vec))

print(impares)
