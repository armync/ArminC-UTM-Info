#include <stdio.h>

union Codec
{
    short int intreg;
    char octeti[2];
} c;

short int codec1(short int i)
{
    c.intreg = i;
    c.octeti[0] = c.octeti[0] ^ c.octeti[1];
    c.octeti[1] = c.octeti[0] ^ c.octeti[1];
    c.octeti[0] = c.octeti[0] ^ c.octeti[1];
    return c.intreg;
}

void codec2(short int *i)
{
    char o;
    c.intreg = *i;
    o = c.octeti[0];
    c.octeti[0] = c.octeti[1];
    c.octeti[1] = o;
    *i = c.intreg;
}

void problema1()
{
    short int n;
    printf("n = ");
    scanf("%hd", &n);
    n = codec1(n);
    printf("Dupa ce bitii au fost inversati: %hd\n", n);
    codec2(&n);
    printf("Dupa ce bitii au fost inversati: %hd\n", n);

    /*
    Atentie!
    nu facem cu scaderi si adunari
    pentru a evita probleme de overflow sau underflow
    */
}
