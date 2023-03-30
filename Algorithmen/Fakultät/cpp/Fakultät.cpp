#include <iostream>
#include <time.h>
#include <cmath>

using namespace std;

int main()
{
    double n;
    cout << "Geben Sie eine natürliche Zahl ein: ";
    cin >> n;

    clock_t t1;
    t1 = clock();

    if (n == 0)
    {
        cout << 1;
    }
    else
    {
        double f = 1;
        for (int i = 1; i <= n; i++)
        {
            f *= i;
        }
        cout << f;
    }

    cout << "\nDie Berechnung dauerte " << (clock() - t1) * (pow(10, 6)) / CLOCKS_PER_SEC << " ns";
    return 0;
}