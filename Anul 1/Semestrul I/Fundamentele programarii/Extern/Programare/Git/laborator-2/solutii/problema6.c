#include <stdio.h>
//#include <stdbool.h>

void citeste(char *nume, char *format, void *input);
int respectaInegTriunghi(int a, int b, int c);

void problema6()
{
    int p, i, j, k;
    citeste("p", "%d", &p);
    for(i=1; i < p; i++)
        for(j=1; j < p-i; j++)
        {
            k = p - i - j;
            if(respectaInegTriunghi(i, j, k))
                printf("(%d, %d, %d)\n", i, j, k);
        }
}

void citeste(char *nume, char *format, void *input)
{
    printf("Introduceti %s: ", nume);
    scanf(format, input);
}

int respectaInegTriunghi(int a, int b, int c)
{
    if(a+b > c && a+c > b && b+c > a)
        return 1;
    return 0;
}

/**
Atenție!
Începând cu standardul C99, există tipul de date _Bool
Trebuie inclusă biblioteca <stdbool.h> pentru a avea disponibile bool și constantele true/false
bool este un macro către _Bool

printf("%d %d", sizeof(_Bool), sizeof(true));
va afișa 1 4
deoarece true și false sunt macro-uri definite ca int
*/
