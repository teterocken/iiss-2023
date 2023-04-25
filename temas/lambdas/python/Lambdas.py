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
    return not c(x)


f = lambda x: not d(x)


print(a(3))
print(b(3))
print(c(100))
print(d(3))
print(e(100))
print(f(3))
