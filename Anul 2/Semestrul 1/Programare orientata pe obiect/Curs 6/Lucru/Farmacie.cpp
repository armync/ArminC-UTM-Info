#include<iostream>
#include "Farmacie.h"
#include<string.h>

using namespace std;

Farmacie::Farmacie()
{
    this->denumire = NULL;
    this->caLuna = NULL;
    this->nrAngajati=0;
    this->nrLuni=0;
    this->id=-1;
}

Farmacie::Farmacie(char* denumire, int nrAngajati, int nrLuni, double caLuna[], int id)
{
    this->denumire = new char[strlen(denumire)];
    strcpy(this->denumire, denumire);
    this->nrAngajati = nrAngajati;
    this->nrLuni = nrLuni;

    this->caLuna = new double[nrLuni];
    for(int i=0; i<nrLuni; i++)
        this->caLuna[i] = caLuna[i];

    this->id = id;

}

Farmacie::Farmacie(const Farmacie& sursa)
{
    this->denumire = new char[strlen(sursa.denumire)];
    strcpy(this->denumire, sursa.denumire);
    this->nrAngajati = sursa.nrAngajati;
    this->nrLuni = sursa.nrLuni;

    this->caLuna = new double[sursa.nrLuni];
    for(int i=0; i<sursa.nrLuni; i++)
        this->caLuna[i] = sursa.caLuna[i];

    this->id = sursa.id;
}

Farmacie& Farmacie::operator=(const Farmacie& sursa)
{
    this->denumire = new char[strlen(sursa.denumire)];
    strcpy(this->denumire, sursa.denumire);
    this->nrAngajati = sursa.nrAngajati;
    this->nrLuni = sursa.nrLuni;

    this->caLuna = new double[sursa.nrLuni];
    for(int i=0; i<sursa.nrLuni; i++)
        this->caLuna[i] = sursa.caLuna[i];

    this->id = sursa.id;

    return *this;
}

Farmacie& Farmacie::operator++()
{
    this->nrAngajati++;
    return *this;
}

void Farmacie::afisare()
{
   cout<<this->id<<endl<<this->denumire<<endl<<this->nrAngajati<<endl<<this->nrLuni;

   for(int i=0; i<this->nrLuni; i++)
    cout<<caLuna[i]<<" ";

}


Farmacie Farmacie::operator++(int a)
{
    Farmacie cop = *this; //constructor de copiere
    this->nrAngajati++;

    return cop;

}

