#include<iostream>
#include<iomanip>
#include<fstream>
#include<algorithm>
using namespace std;
//structura Spectacol permite memorarea informațiilor despre un
//spectacol: numărul de ordine inițial (ID), ora de început (ts)
//și ora de terminare (tf) – ambele ore fiind memorate în minute
//față de miezul nopții
struct Spectacol
{
    int ID, ts, tf;
};

//funcție comparator utilizată pentru a sorta un tablou cu elemente
//de tip Spectacol în ordinea crescătoare a orelor de terminare
bool cmpSpectacole(Spectacol p, Spectacol q)
{
    return p.tf <= q.tf;
}

int main()
{
    //n = numărul de spectacole date, k = numărul maxim de
    //spectacole programate, iar hs, ms, hf, mf = variabile
    //utilizate pentru a citi un interval orar de forma hh:mmhh:mm
    int i, k, n, hs, ms, hf, mf;

    //variabila aux este folosita pentru a citi in gol
    //caracterele ':' si '-' dintr-un interval orar
    char aux;

    //S = spectacolele date, P = spectacolele planificate
    Spectacol* S, * P;

    //datele de intrare se citesc din fișierul "spectacole.txt"
    //care conține pe prima linie numărul de spectacole n, iar pe
    //fiecare din următoarele n linii câte un interval de
    //desfășurare al unui spectacol (de forma hh:mm-hh:mm)
    ifstream fin("spectacole.txt");
    fin >> n;
    S = new Spectacol[n];
    P = new Spectacol[n];
    for (i = 0; i < n; i++)
    {
        // 10:20-11:30
        fin >> hs >> aux >> ms >> aux >> hf >> aux >> mf;
        //ID-ul unui spectacol este numărul său de ordine inițial
        S[i].ID = i + 1;
        //ora de început și ora de terminare se transformă în minute
        //față de miezul nopții
        S[i].ts = hs * 60 + ms;
        S[i].tf = hf * 60 + mf;
    }
    fin.close();

    //sortăm spectacolele în ordinea crescătoare a orelor de
    //terminare
    sort(S, S + n, cmpSpectacole);

    //planificăm primul spectacol, deci numărul k al spectacolelor
    //planificate devine 1
    P[0] = S[0];
    k = 1;
    //pentru fiecare spectacol rămas, verificăm dacă începe după
    //ultimul spectacol programat și, în caz afirmativ, îl adăugăm
    //și pe el în planificarea optimă
    for (i = 1; i < n; i++)
        if (S[i].ts >= P[k - 1].tf)
            P[k++] = S[i];

    //afișăm soluția optimă determinată
    cout << "O planificare cu numar maxim de " << k
        << " spectacole:\n" << endl;
    for (i = 0; i < k; i++)
        cout << "S" << P[i].ID << " -> " << setfill('0') <<
        setw(2)
        << P[i].ts / 60 << ":" << setfill('0') << setw(2)
        << P[i].ts % 60 << "-" << setfill('0') << setw(2)
        << setfill('0') << setw(2) << P[i].tf / 60 << ":"
        << setfill('0') << setw(2) << P[i].tf % 60 << endl;
    delete[]S;
    delete[]P;
    return 0;
}
