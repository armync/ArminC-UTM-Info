#include <iostream>
#include "Farmacie.h"

using namespace std;

int main()
{
    double ca[] = {4.5, 6.7, 8.7};
    Farmacie ob("Dr Max", 12, 3, ca, 111);

    ob.afisare();
   // (++ob).afisare();
   (ob++).afisare();
   ob.afisare();

    return 0;
}
