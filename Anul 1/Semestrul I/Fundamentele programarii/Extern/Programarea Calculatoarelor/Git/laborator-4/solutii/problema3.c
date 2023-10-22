#include <stdio.h>

void problema3()
{
    /*declaratii variabile*/
    FILE *in, *out;
    /*declaratii alte variabile*/
    /*optional - alocari dinamice de memorie*/
    in = fopen("date_3.in", "r");
    /*citire date din fisierul de intrare*/
    fclose(in);
    /*prelucrare date*/
    out = fopen("date_3.out", "w");
    /*scriere date prelucrate in fisierul de iesire*/
    fclose(out);
    /*optional - eliberarea altor resurse (de exemplu, dezalocari de memorie)*/
}
