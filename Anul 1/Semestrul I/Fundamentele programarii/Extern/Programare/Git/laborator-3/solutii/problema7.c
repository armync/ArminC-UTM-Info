#include <stdio.h>

#define NMAX 100

/**
Se citește o matrice A de dimenisiuni N x N (1 <= N <= 100), (0 <= A[i][j] < 232).
Să se efectueze o rotire spre dreapta a matricei A.
Exemplu:
1  2    3  1
     =>
3  4    4  2
*/

void problema7()
{
    int n, i, j, x;
    int a[NMAX][NMAX];
    printf("Introduceti n: ");
    scanf("%d", &n);
    for(i = 0; i < n; i++)
        for(j = 0; j < n; j++)
        {
            printf("Introduceti a[%d][%d]: ", i, j);
            scanf("%d", &a[i][j]);
        }
    puts("");
    for(i = 0; i < n/2; i++)
    {
        x = a[i][i];
        /// rotire jos->sus, copierea se face în sens invers: sus->jos
        for(j = i; j < n-i-1; j++)
            a[j][i] = a[j+1][i];
        /// rotire dreapta->stânga
        for(j = i; j < n-i-1; j++)
            a[n-i-1][j] = a[n-i-1][j+1];
        /// rotire sus->jos
        for(j = n-i-2; j >= i; j--)
            a[j+1][n-i-1] = a[j][n-i-1];
        /// rotire stânga->dreapta
        for(j = n-i-2; j > i; j--)
            a[i][j+1] = a[i][j];
        a[i][i+1] = x;
    }
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            printf("%3d", a[i][j]);
        }
        printf("\n");
    }
}

/**
Exemplu:
6
 1  2  3  4  5  6
20 21 22 23 24  7
19 32 33 34 25  8
18 31 36 35 26  9
17 30 29 28 27 10
16 15 14 13 12 11

Rezultat:
 20  1  2  3  4  5
 19 32 21 22 23  6
 18 31 36 33 24  7
 17 30 35 34 25  8
 16 29 28 27 26  9
 15 14 13 12 11 10

Încă o rotație:
 19 20  1  2  3  4
 18 31 32 21 22  5
 17 30 35 36 23  6
 16 29 34 33 24  7
 15 28 27 26 25  8
 14 13 12 11 10  9
*/
