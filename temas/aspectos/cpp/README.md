# Ejecución del código

Hay que situarse en la misma carpeta que el archivo cpp y ejecutar la orden "g++ -o Aspectos Aspectos.cpp". Tras esto, hay que ejecutar la orden "Aspectos.exe".

# Explicación del código

Primero, se creará una superclase Paciente:

```c++
class Paciente
{
	public:
		Paciente(string n): nombre(n) {}
		string nombre;	
};
```

De esta superclase, heredarán las clases Operado e Intervenido:

```c++
class Operado: public Paciente {
public:
	Operado(string n): Paciente(n) {}
    void operar() {
        cout << "Comienza la operacion" << endl;
    }
};
```

```c++
class Intervenido: public Paciente {
public:
	Intervenido(string n): Paciente(n) {}
    void intervenir() {
        cout << "Comienza la intervencion" << endl;
    }
};
```

Tras esto, se creará una clase Anestesista:

```c++
class Anestesista {
public:
    void anestesiar(Paciente* op) {
        cout << "Anestesiando a "<<op->nombre<<" antes de la operacion o intervencion"<<endl;
    }
};
```

Un paciente tendrá que ser anestesiado antes de una operación o intervención.

Aquí encontramos nuestro _concern_, ya que para ejecutar el método operar() o intervenir(), primero queremos que se anestesie al paciente. Así que estos 2 métodos serían nuestro joinpoint. Así que usaremos un advice de tipo _before_, dado que queremos que la anestesia ha de ir antes de la operación o intervención. He aquí la implementación del aspecto:

```c++
template <typename T>
class Aspect {
public:
    void before(T* obj, void (T::*method)()) {
        anest.anestesiar(obj);
        (obj->*method)();
    }

private:
    Anestesista anest;
};
```

Una vez escrito esto, solo queda ver como actúa este aspecto, definiendo un pointcut para Operado, y otro para Intervenido:

```c++
Operado op("Manolo");
Intervenido inte("Paco");
Aspect<Operado> aspectop;
Aspect<Intervenido> aspectint;
aspectop.before(&op, &Operado::operar);
aspectint.before(&inte, &Intervenido::intervenir);
```

Este código da la siguiente salida:

```
Anestesiando a Manolo antes de la operacion o intervencion
Comienza la operacion
Anestesiando a Paco antes de la operacion o intervencion
Comienza la intervencion
```
