 class Farmacie
 {
     //sir de caracter ->pointer de tip char
     char *denumire;
     int nrAngajati;
     int nrLuni;
     //sir de nr reale->pointer de tip double
     double *caLuna;
     int id;
 public:
     //obligatoriu daca se va declara un tablou de farmacii
    Farmacie();
    Farmacie(char *denumire, int nrAngajati, int nrLuni, double *caLuna, int id);

    //date alocate dinamic->constructorul de copiere, operatorul =
    Farmacie(const Farmacie& sursa); //constructorul de copiere
    Farmacie& operator=(const Farmacie& sursa);
    Farmacie& operator++();//prefixata- >se aplica pe un obiect de tip farmacie
    Farmacie operator++(int a);//postfixata
    void afisare();


 };
