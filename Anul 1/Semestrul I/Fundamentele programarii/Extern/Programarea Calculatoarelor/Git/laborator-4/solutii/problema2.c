#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define str(nr) #nr
#define xstr(nr) str(nr)

#define ADR_MAX 101
#define TIP_LOC_MAX 31
#define PROP_CASA_MAX 16

typedef struct
{
    unsigned int nrCamere : 3;
    unsigned short suprafata;

    union
    {
        unsigned char balcon;// : 1;
        unsigned char decomandat; // : 1;
        char casa[PROP_CASA_MAX];
    } informatii;

    char tipLocuinta[TIP_LOC_MAX];
    char adresa[ADR_MAX];
}
Locuinta;

/*int cmpLocuinteSuprafataDesc(const void *a, const void *b)
{
    const Locuinta *loc1 = a, *loc2 = b;
    return (loc1->suprafata > loc2->suprafata) - (loc1->suprafata < loc2->suprafata);
}*/

void problema2()
{
    //printf("sizeof(Locuinta): %zu\n", sizeof(Locuinta));

    /*declaratii variabile*/
    //unsigned char *garsoniereCuBalcon;
    int n, i, j, maxSuprafata;
    FILE *in, *out;
    Locuinta *locuinte;
    /*declaratii alte variabile*/
    //printf("sizeof(locuinte): %zu\n", sizeof(locuinte));

    /*optional - alocari dinamice de memorie*/
    in = fopen("date_2.in", "r");

    // citeste n din fisier
    fscanf(in, "%d\n", &n);
    /// aloca memorie pt n locuinte
    locuinte = malloc(sizeof(*locuinte) * n);

    /*citire date din fisierul de intrare*/
    char buf[13];
    int nr;
    for(i = 0; i < n; i++)
    {
        /// completeaza codul pt citirea locuintelor
        fgets(locuinte[i].adresa, ADR_MAX, in);
        locuinte[i].adresa[strlen(locuinte[i].adresa)-1] = '\0';
        fscanf(in, "%hu %" xstr(TIP_LOC_MAX) "s %d\n", &locuinte[i].suprafata, locuinte[i].tipLocuinta, &nr);
        //printf("adr: '%s', '%s'\n", locuinte[i].adresa, locuinte[i].tipLocuinta);
        locuinte[i].nrCamere = nr;
        if(!strcmp(locuinte[i].tipLocuinta, "casa"))
        {
            fgets(locuinte[i].informatii.casa, PROP_CASA_MAX, in);
            locuinte[i].informatii.casa[strlen(locuinte[i].informatii.casa)-1] = '\0';
        }
        else
        {
            fscanf(in, "%12s\n", buf);
            if(!strcmp(locuinte[i].tipLocuinta, "garsoniera"))
                locuinte[i].informatii.balcon = !strcmp(buf, "balcon");
            else
                locuinte[i].informatii.decomandat = !strcmp(buf, "decomandat");
        }
    }

    fclose(in);

    /*prelucrare date*/
    /// selecteaza doar garsonierele cu balcon
    /// sorteaza locuintele dupa suprafata

    out = fopen("date_2.out", "w");
    /*scriere date prelucrate in fisierul de iesire*/
    /// scrie rezultatul in fisier
    maxSuprafata = 0;
    j = -1;
    for(i = 0; i < n; i++)
    {
        if(!strcmp(locuinte[i].tipLocuinta, "garsoniera") && locuinte[i].informatii.balcon && locuinte[i].suprafata > maxSuprafata)
        {
            maxSuprafata = locuinte[i].suprafata;
            j = i;
        }
    }
    if(j == -1)
        fprintf(out, "Nu exista garsoniere cu balcon!\n");
    else
        fprintf(out, "Adresa garsonierei cu cea mai mare suprafata: %s\n", locuinte[j].adresa);
    fclose(out);
    /*optional - eliberarea altor resurse (de exemplu, dezalocari de memorie)*/
    /// elibereaza vectorul de locuinte
    free(locuinte);
}
