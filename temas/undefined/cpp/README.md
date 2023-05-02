# Ejecución del programa

Será necesario ejecutar en una terminal localizada en el mismo directorio que el archivo cpp la siguiente orden:

_g++ -o Optional Optional.cpp_

O en su defecto, si el compilador detecta una versión de C++ anterior a C++17, la siguiente orden:

_g++ -std=c++17 -o Optional Optional.cpp_

Valdría la versión C++17 o superior (es en la que se añade la biblioteca optional). Cabe destacar que en caso de estar usando el compilador GCC, habrá que usar la versión del mismo 7.0 o superior.

Una vez ejecutada la anterior orden, se creará un archivo ejecutable, que se ejecutará con la orden:

_Optional.exe_

# Explicación del código

Dentro del main, se crea un vector, v, que contiene una secuencia cualquiera de enteros, y una variable entera, tam, que guarda el numero de elementos de v:

```c++
int v[] = {1, 32, 33, 47, 51};
int tam = sizeof(v) / sizeof(int);
```

Una vez hecho esto se crea una variable de tipo optional<int>, pos, que llamará a una función que devuelve la posición en el vector del número que se le diga, pasándole en este orden, el vector, su tamaño, y el número a encontrar:
```c++
optional<int> pos = encontrarposicion(v, tam, 37);
```

Esta función está implementada de la siguiente manera:

```c++
optional<int> encontrarposicion(int v[], int tam, int x) {
    for (int i = 0; i < tam; i++) {
        if (v[i] == x) {
            return i;
        }
    }
    return nullopt;
}
```

Esta función devuelve el valor entero de la posición si encuentra el número (envuelto en un optional<int>), y el valor nullopt si no encuentra el número; esta ultima variable representa una variable opcional no inicializada, o en lo que en un caso sin uso de optional hubiese sido un valor null.

Ahora, para poder diferenciar si se ha devuelto posición o no, se usa la función booleana asociada a las variables optional _has\_value()_, que devolverá true si la variable tiene un valor asociado, y false en caso contrario. Para recuperar este valor será también necesaria la función value(), que devuelve el valor envuelto del que hablé antes.

Entonces, el siguiente fragmento de código:

```c++
if (pos.has_value()) cout<<"Numero encontrado en la posicion: "<<pos.value()<<endl;
else cout<<"Numero no encontrado"<<endl;
```

Devolverá la siguiente salida en el caso del ejemplo:

_Numero no encontrado_

Si en lugar de 37, se le hubiese pasado a la función el valor 33, la salida sería:

_Numero encontrado en la posicion: 2_

# Conclusión

En C++, es muy posible encontrarse con que se devuelva un valor null, como por ejemplo al no cubrir todas las ramas de return que pueda tener una función.
Es por esto, que al tener una biblioteca como optional se pueden evitar muchos fallos que puedan ser provocados por recibir algún valor null, al no cubrir todas las posibles decisiones lógicas en una función.

Lo bueno que tiene esta biblioteca, es que te permite cubrir valores en un "manto", que te permite esquivar errores provocados por devolver un valor no válido al desnudo, y además, en caso de que no haya errores, desenvolver los valores del "manto" es una tarea muy sencilla, lo cual no complica la codificación, factor clave para la expansión de su uso.
