#include <iostream>
#include <clocale>

using namespace std;

int Fakultaet(int n)
{
    if (n == 0)
        return 1;
    else
        return n * Fakultaet(n - 1);
}

int main()
{
    int n;
    setlocale(LC_ALL, "en_US.utf8");
    cout << "Geben Sie eine nat\u00FCrliche Zahl ein: ";
    cin >> n;
    cout << n << "! = " << Fakultaet(n) << endl;
    return 0;
}
