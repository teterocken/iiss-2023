#include <iostream>
#include <string>

using namespace std;

class Paciente
{
	public:
		Paciente(string n): nombre(n) {}
		string nombre;	
};

class Operado: public Paciente {
public:
	Operado(string n): Paciente(n) {}
    void operar() {
        cout << "Comienza la operacion" << endl;
    }
};

class Intervenido: public Paciente {
public:
	Intervenido(string n): Paciente(n) {}
    void intervenir() {
        cout << "Comienza la intervencion" << endl;
    }
};

class Anestesista {
public:
    void anestesiar(Paciente* op) {
        cout << "Anestesiando a "<<op->nombre<<" antes de la operacion o intervencion"<<endl;
    }
};

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

int main() {
    Operado op("Manolo");
    Intervenido inte("Paco");
    Aspect<Operado> aspectop;
    Aspect<Intervenido> aspectint;
    aspectop.before(&op, &Operado::operar);
    aspectint.before(&inte, &Intervenido::intervenir);
}


