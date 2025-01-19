/*
Intr-o facultate, fiecarui student dintr-o serie ii sunt repartizate in cadrul primei
teme de laborator la Tehnici de programare cate 3 probleme dintr-o lista data.
Cunoscand timpii de evaluare ai fiecarei probleme dintre cele n din lista, precum
si distributia problemelor pe fiecare student in parte, ajutati profesorii evaluatori
sa stabileasca ordinea de evaluare a temelor astfel incat sa se minimizeze timpul
mediu de asteptare a notelor.
*/

#include <iostream>
using namespace std;

// structura pentru student
struct student
{
    int id; // id-ul studentului
    float tema_1, tema_2, tema_3; // timpul de evaluare pentru fiecare tema
};

// functie pentru a calcula timpul total de evaluare al unei teme
float timp_total(student x)
{
    return x.tema_1 + x.tema_2 + x.tema_3;
}

int main()
{
    int  n, i, j;
    student stud[100], aux; // vectorul de studenti si un element auxiliar pentru sortare

    cout << "Introdu numarul de studenti: ";
    cin >> n;

    // Citirea datelor pentru fiecare student
    for (i = 1; i <= n; i++)
    {
        cout << endl << "Introdu ID-ul studentului nr. " << i << ": ";
        cin >> stud[i].id;
        cout << "Introdu timpul de evaluare al temei nr. 1: ";
        cin >> stud[i].tema_1;
        cout << "Introdu timpul de evaluare al temei nr. 2: ";
        cin >> stud[i].tema_2;
        cout << "Introdu timpul de evaluare al temei nr. 3: ";
        cin >> stud[i].tema_3;
    }

    // ta: timpul total de asteptare pentru toti studentii
    // tm: timpul mediu de asteptare
    float ta = 0, tm = 0;

    cout << endl;
    cout << "Valori initiale:" << endl;
    cout << "ID" << "\t\t" << "T1" << "\t" << "T2" << "\t" << "T3" << "\t" << "Timp total evaluare" << "\t" << "Timp asteptare persoana" << endl;
    for (i = 1; i <= n; i++)
    {
        // se adauga la ta timpul total de evaluare pentru fiecare student
        ta += timp_total(stud[i]);
        // se adauga la tm timpul total de asteptare pentru fiecare student
        tm += ta;
        cout << stud[i].id << "\t\t" << stud[i].tema_1 << "\t" << stud[i].tema_2 << "\t" << stud[i].tema_3 << "\t" << timp_total(stud[i]) << "\t\t\t" << ta << endl;
    }
    cout << "Timpul mediu inital de asteptare: " << tm / n << endl;
    cout << endl;

    // sortare dupa timpul total de evaluare al fiecarui student
    for (i = 1; i < n; i++)
    {
        for (j = i + 1; j <= n; j++)
        {
            if (timp_total(stud[i]) > timp_total(stud[j]))
            {
                aux = stud[i];
                stud[i] = stud[j];
                stud[j] = aux;
            }
        }
    }
    ta = 0;
    tm = 0;
    cout << "Valori finale:" << endl;
    cout << "ID" << "\t\t" << "T1" << "\t" << "T2" << "\t" << "T3" << "\t" << "Timp total evaluare" << "\t" << "Timp asteptare persoana" << endl;
    for (i = 1; i <= n; i++)
    {
        // se adauga la ta timpul total de evaluare pentru fiecare student
        ta += timp_total(stud[i]);
        // se adauga la tm timpul total de asteptare pentru fiecare student
        tm += ta;
        cout << stud[i].id << "\t\t" << stud[i].tema_1 << "\t" << stud[i].tema_2 << "\t" << stud[i].tema_3 << "\t" << timp_total(stud[i]) << "\t\t\t" << ta << endl;
    }
    cout << "Timpul mediu optim de asteptare: " << tm / n << endl;

    return 0;
}

