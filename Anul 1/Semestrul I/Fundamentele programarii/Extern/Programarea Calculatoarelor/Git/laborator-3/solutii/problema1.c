#include <stdio.h>

/**
Se citesc n, m și apoi două mulțimi A și B cu n, respectiv m numere întregi cuprinse între [-x,x],
x <= 2000. Să se afișeze numărul de elemente comune mulțimii.
(Indicație: mulțimile A și B nu se vor memora - se va crea un vector de frecvență).
*/

void problema1()
{
    int vectorFrecventa[4001];
    int marimeN, marimeM;
    printf("Introduceti cardinalele pentru cele doua multimi:");
    scanf("%d %d", &marimeN, &marimeM);
    for(int i=0; i<marimeN; i++)
    {
        int x;
        scanf("%d", &x);
        vectorFrecventa[x+2000] = 1;
    }
    int contorElementeComune = 0;
    for(int i=0; i<marimeM; i++)
    {
        int x;
        scanf("%d", &x);
        if (vectorFrecventa[x+2000] == 1)
            contorElementeComune++;
    }
    printf("Avem %d elemente comune",contorElementeComune);
}

/**
Explicații

Ideea vectorului de frecvență este simplă. Dat fiind faptul că noi avem o plajă de valori fixă
(-2000 >= x <= 2000), putem face un vector ce va avea o intrare corespunzătoare pentru fiecare
posibilitate.

Putem asigna valoarea unu pe pozițiile unde avem elementul în mulțime (țineți minte că
mulțimile nu au elemente duplicate). Când citim a doua mulțime, dacă găsim deja valoarea unu pe
poziția respectivă, putem incrementa un contor de elemente comune.

Folosim indexul vectorului drept x+2000 pentru că maparea valorilor este (pozitia 0 = -2000),
(pozitia 1 = -1999)....(pozitia 2000 = 0)....(pozitia 3999 = 1999), (pozitia 4000 = 2000).

Am văzut că mulți dintre noi am afișat de fapt elementele comune la laborator. Este destul de mică
diferența de cod oricum (schimbăm if-ul din al doilea for). Nu mai incrementăm contorul, ci afișăm
direct vectorFrecventa[x+2000].
*/
