/**
Se citesc 2 numere întregi x și n unde n este între 0 și 15. Să se afișeze:
bitul n din x,
numărul x în care se setează bitul n,
numărul x în care se șterge bitul n,
numărul x în care se complementează bitul n.
*/

#include <stdio.h>

void problema2()
{
    int x, n;
    printf("Introduceti x: ");
    scanf("%d", &x);
    printf("Introduceti n: ");
    scanf("%d", &n);

    printf("\nBitul %d este: %d\n",        n, (x >> n) & 1 );
    printf("Setam bitul %d: %d\n",         n, x | (1 << n) );
    printf("Stergem bitul %d: %d\n",       n, x & (65535 ^ (1 << n)) );
    printf("Complementare bitul %d: %d\n", n, x ^ (1 << n) );
}

/**
Explicații:

x >> n              shiftare la dreapta cu n biți
y & 1               obține ultimul bit din y

1 << n              în binar este 1 urmat de n zerouri
x | y               rezultatul are setați biții care sunt reuniunea biților setați în x sau y

65535               2**16 - 1, adică 16 de 1 în binar (cu x**y am notat x la puterea y)
65535 ^ (1 << n)    n de 1 în binar, adică 2**n - 1
x & y               biții comuni din x și y

x ^ y               0 ^ 0 = 0; 0 ^ 1 = 1; 1 ^ 0 = 1; 1 ^ 1 = 0
x ^ (1 << n)        dacă bitul n din 1 este 0, XOR cu 1 va fi 1; altfel, XOR cu 1 va fi 0
                    deci se complementează bitul n; restul de biți din (1 << n) sunt 0,
                    ceea ce înseamnă că ceilalți biți din x nu se vor schimba
*/

/**
Singura modificare față de rezolvarea anterioară este utilizarea unor variabile short int în loc de int
Astfel, modificarea bitului 15 va însemna schimbarea bitului de semn,
convenind că bitul 15 este bitul cel mai semnificativ (MSB - most significant bit)
*/
void problema2_v2()
{
    short int x, n;
    printf("Introduceti x: ");
    scanf("%hd", &x);
    printf("Introduceti n: ");
    scanf("%hd", &n);

    printf("\nBitul %hd este: %hd\n",        n, (x >> n) & 1 );
    printf("Setam bitul %hd: %hd\n",         n, x | (1 << n) );
    printf("Stergem bitul %hd: %hd\n",       n, x & (65535 ^ (1 << n)) );
    printf("Complementare bitul %hd: %hd\n", n, x ^ (1 << n) );
}
