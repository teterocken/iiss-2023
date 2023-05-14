# Ejecución del programa

Será necesario ejecutar en una terminal localizada en el mismo directorio que el archivo cpp y el archivo numeros.txt la siguiente orden:

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
else cout<<"Numero no encontrado"<<endl<<endl<<endl<<endl<<endl;
```

Devolverá la siguiente salida en el caso del ejemplo:

_Numero no encontrado_

Si en lugar de 37, se le hubiese pasado a la función el valor 33, la salida sería:

_Numero encontrado en la posicion: 2_

Ahora el siguiente ejemplo, se muestra como puede usarse optional para tratar con streams de datos, en este caso, un fichero de texto.
	
Para empezar tenemos una función que va a recibir cada linea del fichero de texteo y la va a convertir a entero (un entero envuelto en un optional), y que en caso de que no pueda transformar la linea a entero, devuelve un valor nullopt, como el visto en el ejemplo anterior:

```c++
optional<int> sacarnumero (const string& cad)
{
	try
	{
		return stoi(cad);
	} catch(const std::invalid_argument& e)
	{
		cerr<<"Argumento no valido, no se puede extraer un entero de esa linea."<<endl;
		return nullopt;
	}
}
```
	
Tras esto, creamos la siguiente estructura, que permitirá procesar el fichero numeros.txt línea por línea:
	
```c++
ifstream file("numeros.txt");
	if(file.is_open())
	{
		string linea;
		int i = 1;
		while(getline(file, linea))
		{
			optional<int> numero = sacarnumero(linea);
			if(numero.has_value())
			{
				cout<<"El numero de la linea "<<i<<" es: "<<numero.value()<<endl;
			} else
			{
				cout<<"Error al convertir la linea "<<i<<" a entero\n";
			}
			i++;
		}
	} else
	{
		cout<<"No se puede abrir el archivo\n";
	}
```
	
En el caso del fichero numeros.txt entregado, la salida sería la siguiente:

```
El numero de la linea 1 es: 13
El numero de la linea 2 es: 12
El numero de la linea 3 es: 16
El numero de la linea 4 es: 34
El numero de la linea 5 es: 123
El numero de la linea 6 es: 53634
Argumento no valido, no se puede extraer un entero de esa linea.
Error al convertir la linea 7 a entero
El numero de la linea 8 es: 123
```
    
# Conclusión

En C++, es muy posible encontrarse con que se devuelva un valor null, como por ejemplo al no cubrir todas las ramas de return que pueda tener una función.
Es por esto, que al tener una biblioteca como optional se pueden evitar muchos fallos que puedan ser provocados por recibir algún valor null, al no cubrir todas las posibles decisiones lógicas en una función.

Lo bueno que tiene esta biblioteca, es que te permite cubrir valores en un "manto", que te permite esquivar errores provocados por devolver un valor no válido al desnudo, y además, en caso de que no haya errores, desenvolver los valores del "manto" es una tarea muy sencilla, lo cual no complica la codificación, factor clave para la expansión de su uso.
