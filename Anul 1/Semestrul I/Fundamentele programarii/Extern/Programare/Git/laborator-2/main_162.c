#include <stdio.h>
#include <inttypes.h>
#include <limits.h>
#include <math.h>
#include <string.h>

#define eps 1e-5

void afis(int v[], int n)
{
    int i;
    printf("[");
    for(i = 0; i < n - 1; i++)
    {
        printf("%d, ", v[i]);
    }
    printf("%d]\n", v[i]);
    /* printf(" asd  %d  qef %d \n", v[3], v[3]); */
}

void l1() {
    int i, vec[10], vnou[5] = {25, 16};
    afis(vnou, 5);
    for(i = 0; i < 10; i++)
        vec[i] = 2*i;
    afis(vec, 10);
    for(i = 0; i < 10; i++)
        vec[i] = 10 - i;
    for(i = 0; i < 5; i++)
        vnou[i] = 10 - i;
    afis(vec, 10);
    afis(vnou, 5);
}

void l21() {

    double f = 0.1;
    for(int i = 0; i < 1000000; i++)
        f += 0.1;
    printf("%f\n", f);
    // nu comparam cu ==
    if(fabs(f - 100000.1) < eps)
        printf("ok\n");
}

// 100000.100000000873258 long double
// 100000.10000133289     double
// 100958.445             float :(

void l22() {
    printf("%u %u %u\n", sizeof(float), sizeof(double), sizeof(long double));
    printf("%llu\n", ULLONG_MAX);
}

void l23() {
    int nr;
    int* adr;
    nr = 15;
    printf("Variabila `nr` are valoarea %d si adresa %#p.\n", nr, (void*)&nr);
    /* afiseaza "Variabila `nr` are valoarea 15 si adresa 0x7ffde5e842ec." */

    nr = 25;  // putem schimba valoarea retinuta de o variabila
    adr = &nr;
    printf("Variabila `nr` are valoarea %d si adresa %p.\n", nr, (void*)adr);
    /* afiseaza "Variabila `nr` are valoarea 25 si adresa 0x7ffde5e842ec." */

    *adr = 35;  // asta se numeste dereferentiere si este operatia "inversa" celei de la linia 12: `adr = &nr;`
    printf("Variabila `nr` are valoarea %d si adresa %p.\n", nr, (void*)&nr);
    /* afiseaza "Variabila `nr` are valoarea 35 si adresa 0x7ffde5e842ec." */

    printf("Variabila `adr` are valoarea %p, adresa %p, iar prin dereferentiere obtinem %d.\n", (void*)adr, (void*)&adr, *adr);
    /* afiseaza "Variabila `adr` are valoarea 0x7ffde5e842ec, adresa 0x7ffde5e842f8, iar prin dereferentiere obtinem 35." */

    const int x = 3;
    // nu putem schimba valoarea retinuta de o constanta
    // x = 4;     // error: assignment of read-only variable 'x'

    // nu putem prelua adresa unei constante folosind o variabilă! tipul de date `const int` este diferit de tipul de date `int`
    // `adr` are tipul de date `int*`, deci retine adrese catre variabile de tip `int`, nu `const int`
    // pentru a retine adresa lui `x`, avem nevoie de un obiect de tip `const int*`
    // adr = &x;  // error: assignment discards 'const' qualifier from pointer target type

    nr = x;
    printf("Variabila `nr` are valoarea %d si adresa %p.\n", nr, (void*)&nr);
    /* afiseaza "Variabila `nr` are valoarea 3 si adresa 0x7ffde5e842ec." */

    printf("Variabila `x` are valoarea %d si adresa %p.\n", x, (void*)&x);
    /* afiseaza "Variabila `x` are valoarea 3 si adresa 0x7ffde5e842f4." */

    int const y = nr + 13, *adr_y;
    adr_y = &y;  // este ok, adr_y are tipul `const int*`
    printf("Variabila `y` are valoarea %d si adresa %p.\n", y, (void*)adr_y);
    /* afiseaza "Variabila `y` are valoarea 16 si adresa 0x7ffde5e842f0." */
}

void l24() {
    int a, b, citite;
    char c;
    char sir[20];
    float f;
    printf("Introduceti 2 nr intregi, un caracter si un nr real (in aceasta ordine, separate prin spatii): ");
    citite = scanf("%d %d %c %f", &a, &b, &c, &f);
    printf("Am citit %d variabile: acestea sunt: %d, %d, %c si %f.\n", citite, a, b, c, f);
    printf("Introduceti un sir de caractere: ");
    scanf("%19s", sir);
    printf("Am citit sirul %s de lungime %u.\n", sir, strlen(sir));
}

int main() {
    //l1();
    //l21();
    //l22();
    //l23();
    l24();
    return 0;
}

/* y = f(x1, x2); */
