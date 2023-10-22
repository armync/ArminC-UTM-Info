#include <stdio.h>

#include "laborator4.h"

struct St1
{
};

struct St2
{
    struct St1 s1;
} var2;

typedef struct St3
{
    char x : 1;
} St4;

typedef struct St5
{
    short x : 1;
};

typedef struct St6
{
    int x : 1;
} St6;

typedef struct
{
    double x; // double x : 9; eroare!
} St7;

typedef int OurInt;

void testeStructuri()
{
    struct St1 var1;

    struct St3 var3;
    //St3 var3_1;  // eroare
    // var1 = var3; // eroare

    St4 var4;
    //St5 var5;    // eroare
    struct St5 var5;

    struct St6 var6;
    St6 var6_1;
    St7 var7;
    //struct St7 var7_1; // eroare

    int x;
    OurInt y = 0;
    x = y;    // ok
    printf("St1: %d\n", sizeof(var1));
    printf("St2: %d\n", sizeof(var2));
    printf("St3: %d\n", sizeof(var3));
    printf("St4: %d\n", sizeof(var4));
    printf("St5: %d\n", sizeof(var5));
    printf("St6: %d\n", sizeof(var6));
    printf("St6: %d\n", sizeof(var6_1));
    printf("St7: %d\n", sizeof(var7));
    printf("x: %d\n", x);
}

/*
union are aceleasi reguli ca struct
*/

/*
enum nu are typedef!
*/

/*
problema 4 din Laborator4.pdf
sau problema 6 din Laborator4_v2.pdf

daca foloseam int, sizeof() ar fi fost 4 octeti pentru ca se face aliniere

mod de utilizare:

struct DosarAngajat d;
d.copieBuletin = 0;
d.copieLicenta = 1;
*/

struct DosarAngajat
{
    unsigned char copieBuletin : 1;
    unsigned char copieCertificatCasatorie : 1;
    unsigned char copieLicenta : 1;
    unsigned char copieMaster : 1;
    unsigned char copieDoctor : 1;
    unsigned char copieFisaLichidare : 1;
    unsigned char copieCertificatNastereCopii : 1;
    unsigned char arhiva : 1;  // bonus
};

void problema4()
{
    printf("%d", sizeof(struct DosarAngajat));
}

int main()
{
    //testeStructuri();
    //problema1();
    problema2();
    //problema3();
    //problema4();
    return 0;
}
