/*
Se citeste un numar natural n. Sa se afiseze toate numerele naturale formate din cifre distincte 
nenule care sunt mai mici decat n si au aceeasi suma a cifrelor precum numarul n
*/

#include <iostream>

using namespace std;

// Functie care verfifica daca un numar are cifre distincte si diferite de zero
bool ver_distinct(int num)
{
    int copie_num = num; // Salveaza valoarea originala a lui num
    int cifre[10] = {0}; // Matrice pentru a salva aparitiile fiecarei cifre

    // Creste numarul de aparitii pentru fiecare cifra
    while (num > 0)
    {
        int cifra = num % 10;
        if (cifra == 0)
        {
            return false;
        }
        cifre[cifra]++;
        num /= 10;
    }

    // Verifica daca numarul de cifre in numarul initial este egal cu cel al cifrelor distincte
    int cif_distincte = 0;
    for (int i = 0; i < 10; i++)
    {
        if (cifre[i] > 0)
        {
            cif_distincte++;
        }
    }

    // Verifica cate cifre sunt in numarul initial
    int k = 0;
    int temp_num = copie_num;
    while (temp_num > 0)
    {
        k++;
        temp_num /= 10;
    }

    return cif_distincte == k;
}


// Functie care verifica daca suma cifrelor unui numar este egala cu suma cifrelor a unui alt numar
bool ver_sum(int num1, int num2)
{
    int sum1 = 0, sum2 = 0;

    // Gaseste suma cifrelor numarului num1
    while (num1 > 0)
    {
        sum1 += num1 % 10;
        num1 /= 10;
    }

    // Gaseste suma cifrelor numarului num2
    while (num2 > 0)
    {
        sum2 += num2 % 10;
        num2 /= 10;
    }

    return sum1 == sum2;
}

// Functie care afiseaza, utilizand algoritmul backtracking, toate numerele naturale care au aceeasi suma a
// cifrelor ca si cele ale numarului N  si care sunt formate din cifre distincte si diferite de zero
void btk_numere(int N, int num, int lg, bool& solutie)
{
    // Daca numarul cifrelor in numarul actual este egal cu cel al numarului de cifre ale lui N,
    // verifica daca are aceeasi suma a cifrelor precum N, si le afiseaza in acest caz
    if (lg == 0)
    {
        if (ver_sum(num, N) && ver_distinct(num) && num < N)
        {
            if (!solutie)
            {
                cout << endl << "Solutiile sunt: " << endl;
                solutie = true;
            }
            cout << num << endl;
        }
        return;
    }

    // Incearca fiecare cifra posibila pentru pozitia curenta
    for (int i = 0; i <= 9; i++)
    {
        btk_numere(N, num * 10 + i, lg - 1, solutie);
    }

    /*
    N: numarul introdus initial de utilizator

    num * 10 + i : num este numarul format pana acum, i este cifra curenta incercata, si prin inmultirea cu 10+i se adauga cifra la numarul format pana acum

    lg - 1 : lg este numarul de cifre ramase pentru a fi adaugate, reduce numarul de cifre ramase cu 1
    
    solutie : un bool care indica daca a fost gasita o solutie sau nu

    */
}

int main()
{
    int N;
    cout << "Introdu un numar natural N: ";
    cin >> N;

    bool solutie = false;

    // Verifica catre cifre are numarul N
    int k = 0;
    int temp_N = N;
    while (temp_N > 0)
    {
        k++;
        temp_N /= 10;
    }

    // Apeleaza functia btk_numere avand ca argument numarul de cifre ale numarului N
    btk_numere(N, 0, k, solutie);

    if (!solutie)
    {
        cout << endl << "Nu exista nicio solutie valida pentru numarul " << N << endl;
    }

    return 0;
}
