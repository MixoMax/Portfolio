#include <iostream>
#include <cmath>
#include <ctime>

using namespace std;

int to_int(char* str) {
    int i = 0;
    while (*str != '\0') {
        i = i * 10 + (*str - '0');
        str++;
    }
    return i;
}

bool is_prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int_fast64_t s, k;

    cout << "Ab welcher Zahl sollen Primzahlen berechnet werden? " << endl;
    cin >> s;

    cout << "Bis zu welcher Zahl sollen Primzahlen berechnet werden? " << endl;
    cin >> k;

    cout << "Primzahlen von " << s << " bis " << k << ":" << endl;

    double start = clock();

    for (int i = s; i <= k; i++) {
        if (is_prime(i)) cout << i << endl;
    }

    double end = clock();
    int_fast64_t time_ms = (end - start) / CLOCKS_PER_SEC * 1000;
    cout << "Laufzeit: " << time_ms << " ms" << endl;


    return 0;
}