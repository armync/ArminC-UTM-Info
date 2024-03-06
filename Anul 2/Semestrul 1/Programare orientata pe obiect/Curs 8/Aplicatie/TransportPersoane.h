#include "Autovehicul.h"

//contract: clasa ofera implementare pentru toate func virtuale pure
class TransportPersoane:public Autovehicul
{
    int nrLocuri;
public:
    TransportPersoane();
    TransportPersoane(char *marca, int capacitatea,
                      double putere, double masa, int NrLocuri);

    void afisare();
    int getNrLocuri();
    void setNrLocuri(int val);

    //redefinire functii virtuale pure
    double calculImpozit();
    double calculRovinieta();


};
