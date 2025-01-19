#include <iostream>
#include <ctime>
using namespace std;

int main()
{
    long long int s = 0;
    int n = 25000;
    double t;

    t = clock();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            s = s + i + j;
        }
    }

    t = clock() - t;

    cout << "Timp de executare: " << t / CLOCKS_PER_SEC << "s" << endl;

    cout << "Suma este: " << s << endl;

    return 0;

}