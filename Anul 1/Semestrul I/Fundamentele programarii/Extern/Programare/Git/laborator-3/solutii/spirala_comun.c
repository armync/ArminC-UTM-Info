#include <stdio.h>
#include <stdlib.h>

#include "laborator3.h"

void demoMatriceSpirala()
{
    int **indici;
    int n, m, i;
    n = 5, m = 5;
    indici = matriceSpiralaComun(n, m);
    for(i = 0; i < n*m; i++)
        printf("%d %d\n", indici[i][0], indici[i][1]);  // prelucrare indici

    // eliberare memorie
    for(i = 0; i < n*m; i++)
    {
        free(indici[i]);
    }
    free(indici);
}

int** matriceSpiralaComun(int n, int m)
{
    int i, j, k, iRand, iColoana, sens;
    int **indici = malloc(n*m*sizeof(int*));
    for(i = k = 0; i < m; i++)
    {
        indici[k] = malloc(2*sizeof(int));
        indici[k][0] = 0;
        indici[k++][1] = i;
    }

    sens = 1;
    iRand = 1;
    iColoana = m-1;

    for(i = n - 1; i >= 1; i--)
    {
        /*vertical*/
        for(j = iRand; j != iRand + i*sens; j+=sens)
        {
            indici[k] = malloc(2*sizeof(int));
            indici[k][0] = j;
            indici[k++][1] = iColoana;
        }
        iRand = iRand + (i-1)*sens;
        iColoana = iColoana - sens;

        /*orizontal*/
        for(j = iColoana; j != iColoana-(i+m-n)*sens; j-=sens)
        {
            indici[k] = malloc(2*sizeof(int));
            indici[k][0] = iRand;
            indici[k++][1] = j;
        }
        iColoana = iColoana - (i-1+m-n)*sens;
        iRand = iRand - sens;
        sens = -sens;
    }
    return indici;
}
