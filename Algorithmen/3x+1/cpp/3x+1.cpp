#include <iostream>
#include <ctime>
using namespace std;

int main() {
    //boilerplate
    int_fast64_t max_n = 0;
    int max_count = 0;
    int start_time = clock();

    //prompt user for input
    int_fast64_t n;
    cout << "Enter a number: ";
    cin >> n;

    //calculate
    int count = 0;
    int_fast64_t i = n;
    while (i != 1) {
        if (i % 2 == 0) {
            i = i / 2;
        } else {
            i = 3 * i + 1;
        }
        count++;
    }

    //print result
    cout << "Starting number: " << n << endl;
    cout << "Number of iterations: " << count << endl;
    cout << "Execution time: " << (clock() - start_time) << "ms" << endl;
}
