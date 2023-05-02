#include <iostream>
#include <optional>

using namespace std;

optional<int> encontrarposicion(int v[], int tam, int x) {
    for (int i = 0; i < tam; i++) {
        if (v[i] == x) {
            return i;
        }
    }
    return nullopt;
}

int main() {
    int v[] = {1, 32, 33, 47, 51};
    int tam = sizeof(v) / sizeof(int);

    optional<int> pos = encontrarposicion(v, tam, 37);

    if (pos.has_value()) cout<<"Numero encontrado en la posicion: "<<pos.value()<<endl;
	else cout<<"Numero no encontrado"<<endl;

    return 0;
}

