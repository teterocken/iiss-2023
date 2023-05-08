import asyncio
from time import time


async def contar():
    print("Uno")
    await asyncio.sleep(1)
    print("Dos")
    await asyncio.sleep(2)
    print("Tres")


async def main():
    tiempo_inicial = time()
    j = asyncio.gather(contar(), contar(), contar())
    x = 0
    for i in range(1000000000):
        x = x + 1
    print(x)
    tiempo_transcurrido = time() - tiempo_inicial
    print("Tiempo que tarda en ejecutar con el gather en j pero sin await " + str(tiempo_transcurrido))
    y = await j
    tiempo_transcurrido = time() - tiempo_inicial
    print("Tiempo que tarda en ejecutar llamando a j: " + str(tiempo_transcurrido))

    tiempo_inicial = time()
    x = 0
    for i in range(1000000000):
        x = x + 1
    print(x)
    tiempo_transcurrido = time() - tiempo_inicial
    print("Tiempo que tarda en ejecutar sin las llamadas a contar: " + str(tiempo_transcurrido))


if __name__ == "__main__":
    asyncio.run(main())
