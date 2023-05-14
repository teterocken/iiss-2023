#include <iostream>
#include <optional>
#include <fstream>
#include <string>

using namespace std;

optional<int> encontrarposicion(int v[], int tam, int x) {
    for (int i = 0; i < tam; i++) {
        if (v[i] == x) {
            return i;
        }
    }
    return nullopt;
}

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

int main() {
    int v[] = {1, 32, 33, 47, 51};
    int tam = sizeof(v) / sizeof(int);

    optional<int> pos = encontrarposicion(v, tam, 37);

    if (pos.has_value()) cout<<"Numero encontrado en la posicion: "<<pos.value()<<endl;
	else cout<<"Numero no encontrado"<<endl<<endl<<endl<<endl<<endl;
	
	
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
}

