#include<iostream>
#include "TransportPersoane.h"
#include "Autovehicul.h"

using namespace std;

TransportPersoane::TransportPersoane():Autovehicul()
{
    this->nrLocuri = 0;
}

TransportPersoane::TransportPersoane(char* marca, int capacitatea, double putere, double masa, int nrLocuri)
:Autovehicul(marca, capacitatea, putere, masa)
{
    this->nrLocuri = nrLocuri;
}
//redefinita
void TransportPersoane::afisare()
{
    Autovehicul::afisare();
    cout<<"Nr locuri:"<<this->nrLocuri<<endl;
    cout<<"...................."<<endl;
}

int TransportPersoane::getNrLocuri()
{
    return nrLocuri;
}

void TransportPersoane::setNrLocuri(int val)
{
    this->nrLocuri = val;
}

//redefinire
double TransportPersoane::calculImpozit()
{
    return (this->capacitatea/200)*24;
}
//redefinire
double TransportPersoane::calculRovinieta()
{
    return (this->capacitatea)*0.04;
}
