#include <iostream>
#include <ctime>

using namespace std;

int main()
{

    int n, m, iterations, i;
    int_fast64_t fib;
    int *ptr_n = &n, *ptr_m = &m;

    cout << "Enter the first number: ";
    cin >> n;
    cout << "Enter the second number: ";
    cin >> m;
    cout << "Enter the number of iterations: ";
    cin >> iterations;

    double start = clock();

    //calculation

    for (i = 0; i < iterations; i++)
    {
        fib = *ptr_n + *ptr_m;
        *ptr_n = *ptr_m;
        *ptr_m = fib;

        if (fib < 0)
        {
            cout << "Integer Overflow";
            break;
        }
        else
        {
            cout << i << "\t" <<  fib << endl;
        }

    }

    double end = clock();

    cout << "\nTime: " << (end - start) / 1000 * CLOCKS_PER_SEC << "ms" << endl;

}
