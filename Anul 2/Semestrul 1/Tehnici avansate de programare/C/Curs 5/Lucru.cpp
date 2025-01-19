#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

struct Obiect
{
    int id;
    float castig, greutate;
};

bool cmpObiecte(Obiect ob1, Obiect ob2)
{
    return ob1.castig / ob1.greutate >= ob2.castig / ob2.greutate;
}

int main()
{
    Obiect* ob;
    int i, n;
    float total, G;

    ifstream fin("rucsac.txt");

    fin >> G;
    fin >> n;
    ob = new Obiect[n];
    for (i = 0; i < n; i++)
    {
        ob[i].id = i + 1;
        fin >> ob[i].castig >> ob[i].greutate;
    }

    fin.close();

    sort(ob, ob + n, cmpObiecte);

    cout << "Incarcarea optima a obiectelor in rucsac:" << endl;
    total = 0;
    for (i = 0; i < n; i++)
        if (ob[i].greutate <= G)
        {
            cout << "Obiectul " << ob[i].id << " -> 100%" << endl;
            G = G - ob[i].greutate;
            total = total + ob[i].castig;
        }
        else
        {
            float f = G / ob[i].greutate;
            cout << "Obiectul " << ob[i].id << " -> " << f * 100 << "%" << endl;
            G = 0;
            total = total + f * ob[i].castig;
            break;
        }

    cout << "Castigul maxim: " << total << endl;

    delete[] ob;

    return 0;
}
