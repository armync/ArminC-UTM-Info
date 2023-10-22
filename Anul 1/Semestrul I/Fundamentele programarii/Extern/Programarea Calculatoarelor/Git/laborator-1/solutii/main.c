#include <stdio.h>

/*  & | 0  1
    ---------
    0 | 0  0
    1 | 0  1
*/
void l31()
{
    int nr;
    scanf("%d", &nr);
    if(nr & 1)
        printf("impar");
    else
        printf("par");
}

void l32()
{
    // n*8, n/4, n*10
    // n*10 = n*2*5 = n*2*(1+4) = n*2 + n*8

    /*
    12 = 8+4
    1100

    00011000  nr*2
    01100000  nr*8

    12 * 10 = 120

    10000000  128
    01111111  127
    01111000  120

    14 = 8+4+2
    1110

    00011100  nr*2
    01110000  nr*8
    --------
    10001100

    cu | am obtine
    01111100

    14 * 10 = 140

    10000000  128
    10000010  130
    10001010  138
    10001100  140
    */

    int nr;
    printf("nr=");
    scanf("%d", &nr);
    printf("nr*8: %d, nr/4: %d, nr*10: %d\n", nr << 3, nr >> 2, (nr << 1) + (nr << 3));
    //printf("nr*8: %d, nr/4: %d, nr*10: %d\n", nr << 3, nr >> 2, (nr << 1) ?? (nr << 3));
    // ca să facem și adunarea pe biți, ar trebui să facem
    // a ^ b
    // apoi trebuie adunat carry dacă (a & b) este diferit de 0
    // carry va fi (a & b) << 1; vom face xor cu rezultatul a ^ b
    // trebuie să facem asta recursiv până când nu mai avem carry
    // ... numai că aceste apeluri recursive sunt mai costisitoare dacă le facem din software
}

int main()
{
    //l31();
    l32();
    return 0;
}
