/*
Calculează inversa și determinantul unei matrice pătratice prin transformări elementare
Nume: Micluța-Câmpeanu Marius
Grupa 152
2015-12-08

Actualizat 2019-11-03
*/

#include <stdio.h>

/**
Se citește o matrice A de dimensiuni N x N (1 <= N <= 16), (0 <= A[i][j] <16).
Să se calculeze determinatul matricei A.
*/

double a[100][200], det = 1;
int n;

void citire()
{
    int i, j;
    FILE *in = fopen("problema8.in", "r");
    fscanf(in, "%d", &n);
    for(i = 0; i < n; i++)
        for(j = 0; j < n; j++)
            fscanf(in, "%lf", &a[i][j]);
    fclose(in);

    // creare identitate
    for(i = n; i < 2*n; i++)
        a[i-n][i] = 1;
}

void afisare(int p)
{
    int i, j;
    for(i = 0; i < n; printf("\n"), i++)
        for(j = 0; j < n; j++)
            printf("%.*lf   ", p, a[i][j]);
}

void afisareInversa(int p)
{
    int i, j;
    for(i = 0; i < n; printf("\n"), i++)
        for(j = n; j < 2*n; j++)
            printf("%.*lf    ", p, a[i][j]);
}

void interschimbaLinii(int x, int y)
{
    int i;
    double z;
    for(i = 0; i < 2*n; i++)
    {
        z = a[x][i];
        a[x][i] = a[y][i];
        a[y][i] = z;
    }
}

void impartireLinieCuScalar(int line, double scalar)
{
    int i;
    for(i=0; i<2*n; i++)
        a[line][i]/=scalar;
}

void adunaLinii(int x, int y, double s)
{
    int i;
    for(i = 0; i < 2*n; i++)
        a[x][i] += s*a[y][i];
}

void calculareDeterminant()
{
    int i, j, k = 0;
    int r = 0;
    for(i = 0; i < n; i++, k++)
    {
        //face pivot 1 {
        if(!a[i][k])    //mută 0 mai jos
        {
            for(j = i; j < n; r++, j++)
            {
                if(a[j][k])
                {
                    interschimbaLinii(i, j);
                    det *= -1;
                    break;
                }
            }
        }
        if(!a[i][k])    //Nu am (mai) găsit pivot
        {
            det = 0;
            printf("Nu exista inversa");
            return;
        }
        if(a[i][k] != 1)
        {
            det *= a[i][k];
            impartireLinieCuScalar(i, a[i][k]);//}
        }
        for(j = k+1; j < n; j++)    //face 0 sub pivot
        {
            if(a[j][k])
            {
                if(a[j][k] != 1)
                {
                    det *= a[j][k];
                    impartireLinieCuScalar(j, a[j][k]);
                }
                adunaLinii(j, i, -1);
            }
        }
    }   //am adus matricea în forma eșalon, cu 1 pe diagonala principală
    for(i = n-1, k--; i >= 0; i--, k--)  //face 0 deasupra pivotului
    {
        for(j = i-1; j >= 0; j--)
        {
            if(a[j][k])
            {
                adunaLinii(j, i, -a[j][k]);
            }
        }
    }
}

void problema8()
{
    citire();
    calculareDeterminant();
    printf("Determinantul matricei este %f", det);
}
