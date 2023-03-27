#include <iostream>
#include <cmath>
#include <ctime>
#include <gmpxx.h>

using namespace std;

//n = p*q
//find p and q

void print(string text) {
    cout << text << endl;
}

mpz_class gcd(mpz_class a, mpz_class b) {
    mpz_class temp;
    while (b != 0) {
        temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {

    mpz_class n;
    cout << "Bitte geben Sie eine Zahl ein: ";
    cin >> n;

    double t1 = clock();

    mpz_class g; mpz_class r; //g**r = m*N+1
    g = 8;
    r = 1;

    mpz_class temp = pow(g.get_mpz_t(), r.get_mpz_t());

    for (int i = 0; i < 100; i++) {
        r++;
        temp = pow(g.get_mpz_t(), r.get_mpz_t());
        if (temp % n == 1) {
            break;
        }
    }

    mpz_class m = pow(g.get_mpz_t(), r.get_mpz_t()) / n - 1;


    //(g^(r/2)+1)*(g^(r/2)-1) = m*n

    mpz_class factor_1 = (pow(g.get_mpz_t(), r / 2) + 1);
    mpz_class factor_2 = (pow(g.get_mpz_t(), r / 2) - 1);

    mpz_class gcd_factor_1 = gcd(factor_1, n);
    mpz_class gcd_factor_2 = gcd(factor_2, n);
    mpz_class common_divisor = gcd(gcd_factor_1, gcd_factor_2);

    double t2 = clock();

    print("Zeit: " + to_string((t2 - t1) / CLOCKS_PER_SEC) + " Sekunden");
};
