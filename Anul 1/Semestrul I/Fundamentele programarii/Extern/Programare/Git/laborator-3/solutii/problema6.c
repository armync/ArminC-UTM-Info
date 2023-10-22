#include <stdio.h>
#include <stdlib.h>

#include "laborator3.h"

/**
Să se creeze o matrice patratică, în spirală, după regulile:
- numerele pornesc de la 1, din 1 in 1, în ordine crescătoare;
- după fiecare număr neprim x se adaugă cel mai mic divizor propriu al său,
  după care se continuă cu x+1.

Exemplu:
1    2    3    4    2
11   12   2    13   5
2    16   2    14   6
10   3    15   2    2
3    9    2    8    7
*/

int divizorPropriu(int x)
{
    int d;
    if(x <= 2)
        return 0;
    for(d = 2; d <= x/2; d++)
        if(x%d == 0)
            return d;
    return 0;
}

void problema6()
{   int mat[10][10], v[100];
    int **indici;
    int n, m, i, j, k, h;
    // generare vector
    n = m = 5;
    j = 1;
    for(i = 0; i < n*n; i++)
    {
        v[i] = j;
        k = divizorPropriu(j);
        if(k) {
            i++;
            v[i] = k;
        }
        j++;
    }

    indici = matriceSpiralaComun(n, m);
    h=0;
    for(i = 0; i < n*m; i++)
    {
        j = indici[i][0];
        k = indici[i][1];
        mat[j][k] = v[h++];
    }
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < m; j++)
            printf("%3d", mat[i][j]);
        puts(""); // rand nou
    }
    for(i = 0; i < n*m; i++)
    {
        free(indici[i]);
    }
    free(indici);
}
