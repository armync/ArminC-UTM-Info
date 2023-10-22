/**
Pentru valori întregi citite de la tastatură
să se tipărească valoarea corespunzătoare în binar.
*/

#include <stdio.h>

void afiseazaBinar(int y);

void problema1()
{
    int x;
    printf("Introduceti x: ");
    scanf("%d", &x);
    afiseazaBinar(x);
    printf("\n");
}

void afiseazaBinar(int y)
{
    if(y > 0)
    {
        afiseazaBinar(y >> 1);     /// împărțire la 2
        printf("%d", y & 1);        /// restul împărțirii la 2
    }
}
