#include<iostream>
#include "Autoturism.h"

using namespace std;

Autoturism::Autoturism():Autovehicul()
{
 this->nrUsi = 0;
}

Autoturism::Autoturism(char* marca, int capacitate, double putere, double masa, int nrUsi)
:Autovehicul(marca, capacitate, putere, masa)
{
  this->nrUsi = nrUsi;
}
//redefinire
double Autoturism::calculImpozit()
{
    return (this->capacitatea/200)*8;
}
//redefinire
double Autoturism::calculRovinieta()
{
    return (this->capacitatea)*0.02;
}

int Autoturism::getNrLocuri()
{
    return nrUsi;
}

void Autoturism::setNRLocuri(int val)
{
    this->nrUsi = val;
}

//redefinita
void Autoturism::afisare()
{
    //apel din clasa de baza
    Autovehicul::afisare();
    cout<<"Nr usi: "<<this->nrUsi<<endl;
    cout<<".........................."<<endl;
}

