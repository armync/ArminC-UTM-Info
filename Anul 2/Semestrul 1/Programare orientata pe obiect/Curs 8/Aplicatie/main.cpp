#include <iostream>
#include "Autovehicul.h"
#include "Autoturism.h"
#include "TransportPersoane.h"
#include <fstream>
#include<string.h>
#include<stdlib.h>

using namespace std;

int main()
{
    /*
    //polimorhism
    Autovehicul *ob = new Autoturism("Seat", 1600, 100, 2.7, 5);
    //ob = new Autovehicul();

    //Autoturism obAuto;
    ob->afisare();
    cout<<ob->calculImpozit();

    Autovehicul *tp = new TransportPersoane("Auto", 3600, 100, 4.8, 50);

    tp->afisare();
    */

    ifstream fin("autovehiule.in");

    Autovehicul *ta[10];

    char linie[500];
    char marca[50];
    int capacitatea;
    double masa;
    double puterea;
    int data;

    char* p;

    int index=0;

    while(fin.getline(linie, 500))
    {
         p = strtok(linie, " ");
         strcpy(marca, p);

         p=strtok(NULL, " ");
         capacitatea = atoi(p);

         p = strtok(NULL, " ");
         puterea = atof(p);

         p = strtok(NULL, " ");
         masa = atof(p);

         p = strtok(NULL, " ");
         data = atoi(p);

         if(masa<=3.5)
           ta[index++] = new Autoturism(marca, capacitatea, puterea, masa, data);
         else
          ta[index++] = new TransportPersoane(marca, capacitatea, puterea, masa, data);
    }

    fin.close();

    for(int i=0; i<index; i++)
        ta[i]->afisare();

    ofstream fout("taxe.csv");
    fout<<"Marca"<<","<<"Impozit"<<","<<"Rovinieta"<<endl;

    for(int i=0; i<index; i++)
        fout<<ta[i]->getMarca()<<","<<ta[i]->calculImpozit()<<","<<ta[i]->calculRovinieta()<<endl;


    return 0;
}
