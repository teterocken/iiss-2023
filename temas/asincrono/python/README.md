# Ejecución del programa

El archivo se puede ejecutar escribiendo en terminal dentro de la misma carpeta del archivo "python Asincrona.py"

# Explicación del código

Se crea una función que se usará como una corrutina del main. Esta función contará hasta 3, esperando 1 segundo entre el uno y el dos, y 2 segundos entre el dos y el tres:

```python
async def contar():
    print("Uno")
    await asyncio.sleep(1)
    print("Dos")
    await asyncio.sleep(2)
    print("Tres")
```

Después, tomaremos tiempos de cuanto se tarda en ejecutar el código que contiene guardar un gather de 3 llamadas a la función contar() en una variable (se ejecuta 3 veces la función simultáneamente) y un bucle que da 1000000000 iteraciones, y cuanto tarda en ejecutarse si se espera a que termine la ejecución de ese gather contenido en esa variable. He aquí el fragmento de código:

```python
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
```

Y la salida que se obtiene es la siguiente:

```
1000000000
Tiempo que tarda en ejecutar con el gather en j pero sin await 40.20618748664856
Uno
Uno
Uno
Dos
Dos
Dos
Tres
Tres
Tres
Tiempo que tarda en ejecutar llamando a j: 43.222944021224976
```

Se puede contemplar que tarda 3 segundos más una vez se espera a que termine la ejecución del gather alojado en x, esto se debe a los 3 segundos de espera (sleep) que tienen las funciones contar().

Después se cronometra cuanto tarda la ejecución de solo el bucle, para poder ver si el hecho de que comience la ejecución de los métodos contar() afecta a lo que tarda en ejecutarse el bucle:

```python
tiempo_inicial = time()
    x = 0
    for i in range(1000000000):
        x = x + 1
    print(x)
    tiempo_transcurrido = time() - tiempo_inicial
    print("Tiempo que tarda en ejecutar sin las llamadas a contar: " + str(tiempo_transcurrido))
```

Y la salida es la siguiente:

```
1000000000
Tiempo que tarda en ejecutar sin las llamadas a contar: 38.55795335769653
```

# Conclusión

El hecho de que en el último caso se ejecute más rápido, no se debe a que la asincronía esté mal implementada, sino al retardo que supone crear corrutinas con el gather, pero se puede ver como los tiempos son similares.

Asyncio es una biblioteca que permite la creación de códigos en python utilizando la programación asíncrona, y que da varios métodos para facilitar esta tarea. En el código se ve el caso de la etiqueta async (que marca las funciones que serán llamadas como corrutinas), el método sleep(), que detiene la ejecución del programa el tiempo que se le indique, el método gather que se utiliza para llamar simultaneamente a una función (corrutina) varias veces o a varias funciones.
