#include "Autovehicul.h"

class Autoturism:public Autovehicul
{
    int nrUsi;
public:

    Autoturism();
    Autoturism(char *marca, int capacitate, double putere,
               double masa, int nrUsi);

    double calculImpozit();
    double calculRovinieta();

    int getNrLocuri();
    void setNRLocuri(int val);

    void afisare();

};
