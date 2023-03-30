#include <iostream>
#include <ctime>

using namespace std;

bool isEven(int n) {
    int *p = &n;
    int lastBit = *p & 1;
    return lastBit == 0;
}

bool isEven2(int n) {
    return n % 2 == 0;
}

int main() {
    int_fast64_t n;
    cin >> n;

    double time = clock();
    
    if (isEven(n)) {
        cout << "even" << endl;
    } else {
        cout << "odd" << endl;
    }

    double end_time = clock();

    cout << "Time: " << (end_time - time) * 1000 / CLOCKS_PER_SEC << " ms" << endl;

    time = clock();

    if (isEven2(n)) {
        cout << "even" << endl;
    } else {
        cout << "odd" << endl;
    }

    end_time = clock();

    cout << "Time: " << (end_time - time) * 1000 / CLOCKS_PER_SEC << " ms" << endl;

    return 0;
}