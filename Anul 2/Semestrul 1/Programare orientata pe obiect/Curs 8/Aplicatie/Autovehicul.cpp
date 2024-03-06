#include<iostream>
#include<string.h>
#include "Autovehicul.h"

using namespace std;

Autovehicul::Autovehicul()
{
    this->marca = new char[4];
    strcpy(this->marca, "###");

    this->capacitatea = 0;
    this->putere=0.0;
    this->masa = 0.0;
}

Autovehicul::Autovehicul(char* marca, int capacitatea, double putere, double masa)
{
    this->marca = new char[strlen(marca) +1];
    strcpy(this->marca, marca);

    this->capacitatea = capacitatea;
    this->putere = putere;
    this->masa = masa;
}

Autovehicul::~Autovehicul()
{
    if(marca)
    {
        delete []marca;
    }
}

Autovehicul::Autovehicul(const Autovehicul& ob)
{
    this->marca = new char[strlen(ob.marca) +1];
    strcpy(this->marca, ob.marca);

    this->capacitatea = ob.capacitatea;
    this->putere = ob.putere;
    this->masa = ob.masa;
}

void Autovehicul::setMarca(char* val)
{
    if(marca)
        delete []marca;

    this->marca = new char[strlen(val) + 1];
    strcpy(this->marca, val);
}

void Autovehicul::setCapacitate(int val)
{
    this->capacitatea = val;
}

void Autovehicul::setPutere(double val)
{
    this->putere = val;
}

void Autovehicul::setMasa(double val)
{
    this->masa = masa;
}

char* Autovehicul::getMarca()
{
    return marca;
}

int Autovehicul::getCapacitate()
{
    return capacitatea;
}

double Autovehicul::getPutere()
{
    return putere;
}

double Autovehicul::getMasa()
{
    return masa;
}

void Autovehicul::afisare()
{
    cout<<"Marca: "<<marca<<endl;
    cout<<"Capacitate: "<<capacitatea<<endl;
    cout<<"Putere: "<<putere<<endl;
    cout<<"Masa: "<<masa<<endl;

}



