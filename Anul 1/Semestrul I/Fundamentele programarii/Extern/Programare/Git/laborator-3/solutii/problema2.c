#include <stdio.h>

/**
Se citesc: n, cele n elemente ale unui vector sortat crescător, apoi x și y două elemente din
vector. Să se afișeze toate elementele vectorului cuprinse între x și y.
Optim: folosiți căutarea binară.
Observație: https://research.googleblog.com/2006/06/extraextra-read-all-about-it-nearly.html
*/

int cautareBinara(int vec[], int key, int marimeVec)
{
    int low = 0;
    int high = marimeVec - 1;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        int midVal = vec[mid];
        if (midVal < key)
            low = mid + 1;
        else if (midVal > key)
            high = mid - 1;
        else
            return mid;
    }
    return -(low + 1);
}

void problema2()
{
    int marimeVec;
    printf("Introduceti marimea unui vector sortat: ");
    scanf("%d", &marimeVec);
    printf("\n");
    int vecSortat[marimeVec];
    for(int i=0; i<marimeVec; i++)
    {
        scanf("%d", &vecSortat[i]);
    }
    int x, y;
    printf("Introduceti doua elemente din vector: ");
    scanf("%d %d", &x, &y);
    int indexX = cautareBinara(vecSortat, x, marimeVec);
    int indexY = cautareBinara(vecSortat, y, marimeVec);
    for(int i=indexX; i<=indexY; i++)
    {
        printf("%d ", vecSortat[i]);
    }
}

/**
Explicații

Căutarea binară este mult mai eficientă decât un for pe toată lungimea vectorului cu un if inăuntru
ce întreabă dacă numărul de pe poziția i este mai mare decât X și mai mic decât Y.

Căutarea binară împarte vectorul sortat în două și pe baza valorii din mijloc, continuă în jumatatea din
stânga sau din dreapta (de aici și numele de “binară”). Astfel, găsim indicii celor două elemente și
putem să afișăm foarte ușor elementele intermediare.
*/
