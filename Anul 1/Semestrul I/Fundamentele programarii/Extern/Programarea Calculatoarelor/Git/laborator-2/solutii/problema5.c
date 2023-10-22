/**
Se citesc numere naturale până la întâlnirea numărului 0. Să se afișeze toate
perechile de numere consecutive citite cu proprietatea că al doilea număr
reprezintă restul împărțirii primului număr la suma cifrelor sale.
*/

#include <stdio.h>

int sumaCifre(int nr);

void problema5()
{
    int citit, prec;
    printf("Introduceti nr:\n");
    scanf("%d", &citit);
    while(citit != 0)
    {
        prec = citit;
        printf("Introduceti nr:\n");
        scanf("%d", &citit);
        if(prec % sumaCifre(prec) == citit)
            printf("(%d, %d)\n", prec, citit);
    }
}

int sumaCifre(int nr)
{
    int s = 0;
    while(nr > 0)
    {
        s += nr%10;
        nr /= 10;
    }
    return s;
}

/**
Exemple:
76 11 1
9988 26 2
15 3
0
*/
