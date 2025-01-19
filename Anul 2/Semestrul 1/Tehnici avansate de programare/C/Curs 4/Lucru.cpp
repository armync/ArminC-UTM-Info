#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

struct Persoana
{
    int id, ts;
};

bool cmpPersoane(Persoana p1, Persoana p2)
{
    return p1.ts <= p2.ts;
}

int main()
{
    Persoana* p;
    int i, n;
    float tmi, tmo, scrt;

    ifstream fin("persoane.txt");

    fin >> n;
    p = new Persoana[n];
    tmi = scrt = 0;
    for (i = 0; i < n; i++)
    {
        p[i].id = i + 1;
        fin >> p[i].ts;
        scrt = scrt + p[i].ts;
        tmi = tmi + scrt;
    }
    tmi = tmi / n;
    cout << "Timpul mediu de servire initial: " << tmi << endl << endl;

    fin.close();

    sort(p, p + n, cmpPersoane);

    cout << "Asezarea optima a persoanelor la ghiseu:" << endl;
    tmo = scrt = 0;
    for (i = 0; i < n; i++)
    {
        cout << "Persoana " << p[i].id << ": " << p[i].ts << " minute" << endl;
        scrt = scrt + p[i].ts;
        tmo = tmo + scrt;
    }
    tmo = tmo / n;


    cout << "Timpul mediu de servire minim: " << tmo << endl;

    delete[] p;

    return 0;
}