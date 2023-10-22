#include <stdio.h>
#include <stdlib.h>

#include "laborator3.h"

#define RMAX 100
#define CMAX 100

/**
Să se parcurgă o matrice în spirală.
Exemplu: Pentru  1  2  3
                 4  5  6
                 7  8  9
                10 11 12
se va afiṣa 1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8.
*/

void solutie1();
void spiralPrint(int iRandFinal, int iColFinal, int a[RMAX][CMAX]);

void solutie2();
void matriceSpirala();
void genereazaFisierMatrice(int n, int m);

void solutie3();
void matriceSpiralaParcurgere();


void problema5()
{
    //solutie1();
    //solutie2();
    solutie3();
}

void solutie1()
{
    int matrice[RMAX][CMAX];
    int nrRanduri, nrColoana, i, j;
    printf("Numarul de randuri si de coloane: ");
    scanf("%d %d", &nrRanduri, &nrColoana);
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
    spiralPrint(nrRanduri, nrColoana, matrice);
}

/**
Explicații

Este destul de greu să explic această problemă folosind doar text (problema este destul de vizuală).

Recomand să vizionați un video precum acesta:
https://www.youtube.com/watch?v=siKFOI8PNKM&feature=youtu.be
(măcar partea în care discută ideea în sine a algoritmului).

Am luat exemplul de aici și l-am rescris într-un mod puțin mai clar. În mare, problema trebuie împărțită în 4 etape
(mereu când avem o problemă mai complexă, vrem să o spargem în bucăți mai mici). În principal noi
vom parcuge cele 4 laturi ale unei matrice, deci vom merge stânga->dreapta,
sus->jos, dreapta->stânga, jos->sus. La fiecare tur în jurul matricei vom da la o parte un nivel
din ea (adică un rând și coloana de pe fiecare parte).

Ne ocupăm de acest lucru cu 4 indici: iRandStart iColStart iRandFinal iColFinal. For-urile
din program sunt destul de clare odată ce le vizualizați (ele fac pe rând cele 4 parcugeri de care
am vorbit). După ce am parcurs stânga-> dreapta, trebuie să incrementăm indexul ce ține rândul
de start, după ce am parcurs sus->jos decrementăm indicele de coloane final, dreapta->stânga
decrementăm rândul de final, jos->sus incrementăm index de coloana de start.

Din nou, este destul de dificil de explicat în text. Vă propun să vă luați o matrice 3x3 și să scrieți
pe hârtie variabilele și afișările la fiecare iterație, după cum am facut la laborator cu căutarea binară.
*/


void solutie2()
{
    genereazaFisierMatrice(4, 3);
    matriceSpirala();
}

/**
Explicații soluție 2

Citirea și scrierea se realizează cu fișiere.


Această soluție se bazează pe următoarele observații.

Mai întâi considerăm cazul când matricea este pătrată (are același număr de linii și de coloane).
Lungimea laturilor de parcurs este n, n, n, n-1, n-1, n-2, n-2, ..., 3, 3, 2, 2.

Spre deosebire de soluția anterioară, vom folosi doar 2 indici: rândul și coloana
unde am ajuns cu parcurgerea: iRand, iColoana.

Cu excepția primei laturi, observăm regula că lungimea scade din 2 în 2: avem o parcurgere verticală, apoi una orizontală.
Pentru a nu repeta elementele din colțuri, după fiecare parcurgere vom muta variabila
iRand sau iColoana pe linia/coloana următoare.

Pentru a nu ieși din matrice, scădem 1 la lungimile menționate anterior: vom merge de la n-1 la 1.

Întrucât singura diferență dintre o parcurgere sus->jos și una jos->sus este dat de faptul că
facem o incrementare sau o decrementare, putem folosi o variabilă prin care reținem sensul de mers.

Deoarece în acest mod nu mai știm dacă se incrementează sau decrementează contorul din for,
va trebui să folosim operatorul != în condiția de oprire.

Pentru cazul când matricea nu este pătrată, trebuie efectuată diferența dintre numărul de linii
și numărul de coloane la parcurgerile pe orizontală. Această corecție este nrColoane - nrLinii:
dacă sunt mai multe coloane decât linii, numărul va fi pozitiv, vrem să avansăm mai mult;
dacă sunt mai puține coloane decât linii, atunci parcurgerea este mai scurtă.
*/


void solutie3()
{
    genereazaFisierMatrice(4, 3);
    matriceSpiralaParcurgere();
}

/**
Explicație soluție 3

Soluția este similară cu cea anterioară, dar am folosit o funcție separată pentru a genera
indicii de parcurgere în spirală pentru o matrice cu n linii și m coloane.

Funcția este matriceSpiralaComun(int n, int m) și va fi folosită și în problema 6.
Din acest motiv am inclus fișierul header laborator3.h

Întrucât funcția ne întoarce un vector de indici, acesta este alocat dinamic,
deci va trebui să eliberăm memoria în mod explicit.
*/


void spiralPrint(int iRandFinal, int iColFinal, int a[RMAX][CMAX])
{
    int i, iRandStart = 0, iColStart = 0;
    while (iRandStart < iRandFinal && iColStart < iColFinal)
    {
        /* stanga-> dreapta */
        for (i = iColStart; i < iColFinal; ++i)
        {
            printf("%d ", a[iRandStart][i]);
        }
        iRandStart++;
        /* sus->jos */
        for (i = iRandStart; i < iRandFinal; ++i)
        {
            printf("%d ", a[i][iColFinal-1]);
        }
        iColFinal--;
        /* dreapta->stanga */
        if (iRandStart < iRandFinal)
        {
            for (i = iColFinal-1; i >= iColStart; --i)
            {
                printf("%d ", a[iRandFinal-1][i]);
            }
            iRandFinal--;
        }
        /* jos->sus */
        if (iColStart < iColFinal)
        {
            for (i = iRandFinal-1; i >= iRandStart; --i)
            {
                printf("%d ", a[i][iColStart]);
            }
            iColStart++;
        }
    }
}


void matriceSpirala()
{
    int n, m, i, j, iRand, iColoana, sens;
    int matrice[50][50];
    FILE *in, *out;

    in = fopen("matrice.in", "r");
    fscanf(in, "%d %d", &n, &m);
    for(i = 0; i < n; i++)
        for(j = 0; j < m; j++)
            fscanf(in, "%d", &matrice[i][j]);
    fclose(in);

    out = fopen("matrice.out", "w");
    for(i = 0; i < m; i++)
        fprintf(out, "%d ", matrice[0][i]);

    sens = 1;
    iRand = 1;
    iColoana = m-1;

    for(i = n - 1; i >= 1; i--)
    {
        /*vertical*/
        for(j = iRand; j != iRand + i*sens; j+=sens)
            fprintf(out, "%d ", matrice[j][iColoana]);
        iRand = iRand + (i-1)*sens;
        iColoana = iColoana - sens;

        /*orizontal*/
        for(j = iColoana; j != iColoana-(i+m-n)*sens; j-=sens)
            fprintf(out, "%d ", matrice[iRand][j]);
        iColoana = iColoana - (i-1+m-n)*sens;
        iRand = iRand - sens;
        sens = -sens;
    }

    fclose(out);
}

void genereazaFisierMatrice(int n, int m)
{
    FILE *out;
    int i, j;
    out = fopen("matrice.in", "w");
    fprintf(out, "%d %d\n", n, m);
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < m; j++)
            fprintf(out, "%3d", i*m + j + 1);
        fprintf(out, "\n");
    }
    fclose(out);
}


void matriceSpiralaParcurgere()
{
    int **indici;
    int n, m, i, j, k;
    int matrice[50][50];
    FILE *in, *out;

    in = fopen("matrice.in", "r");
    fscanf(in, "%d %d", &n, &m);
    for(i = 0; i < n; i++)
        for(j = 0; j < m; j++)
            fscanf(in, "%d", &matrice[i][j]);
    fclose(in);

    indici = matriceSpiralaComun(n, m);

    out = fopen("matrice.out", "w");

    for(k = 0; k < n*m; k++)
    {
        i = indici[k][0];
        j = indici[k][1];
        fprintf(out, "%d ", matrice[i][j]);
    }
    fclose(out);

    for(i = 0; i < n*m; i++)
    {
        free(indici[i]);
    }
    free(indici);
}
