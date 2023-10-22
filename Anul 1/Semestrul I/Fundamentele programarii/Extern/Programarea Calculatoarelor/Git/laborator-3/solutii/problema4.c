#include <stdio.h>

/**
Se citesc de la tastatură m și n naturale nenule reprezentând dimensiunile unei matrice și
apoi se citesc elementele matricei. Să se construiască ṣi să se afiṣeze matricea transpusă.
*/

void problema4()
{
    int nrRanduri, nrColoana, i, j;
    printf("Numarul de randuri si de coloane: ");
    scanf("%d %d", &nrRanduri, &nrColoana);
    int matrice[nrRanduri][nrColoana];
    int transpusa[nrRanduri][nrColoana];

    printf("\nElementele matricei:\n");
    for(i = 0; i < nrRanduri; ++i)
    {
        for(j = 0; j < nrColoana; ++j)
        {
            printf("Elementul %d %d: ",i+1, j+1);
            scanf("%d", &matrice[i][j]);
        }
    }
    printf("\nMatricea: \n");
    for(i = 0; i < nrRanduri; ++i)
    {
        for(j = 0; j < nrColoana; ++j)
        {
            printf("%d ", matrice[i][j]);
            if (j == nrColoana-1)
                printf("\n\n");
        }
    }

    for(i = 0; i < nrRanduri; ++i)
    {
        for(j = 0; j < nrColoana; ++j)
        {
            transpusa[j][i] = matrice[i][j];
        }
    }

    printf("\nMatricea transpusa:\n");
    for(i = 0; i < nrColoana; ++i)
    {
        for(j = 0; j < nrRanduri; ++j)
        {
            printf("%d ",transpusa[i][j]);
            if(j == nrRanduri-1)
            {
                printf("\n\n");
            }
        }
    }
}

/**
Explicații

Codul este plin de afișări, pentru fiecare element citit și apoi pentru toată matricea. Ce vrem cu
adevărat să vedem este:

for(i =0; i < nrRanduri; ++i)
{
    for(j = 0; j < nrColoana; ++j)
    {
        transpusa[j][i] = matrice[i][j];
    }
}

Nu este mult de zis. Când copiem datele din matricea citită în matricea transpusă, inversăm indicii
astfel încât în transpusă să se scrie pe coloană și apoi pe linie.
Disclaimer: Știu că varianta mea este puțin ineficientă pentru că ținem matricea în memorie
de 2 ori (pentru matrice mari, poate fi o problemă).
*/
