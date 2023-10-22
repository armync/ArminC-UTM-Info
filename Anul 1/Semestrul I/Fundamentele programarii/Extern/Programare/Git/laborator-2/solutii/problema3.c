/**
Se citesc întregii x, y, n, p. Să se copieze în x,
începând din poziția p, ultimii n biți din y și
să se afișeze noua valoare a lui x.

Observație: p trebuie să fie >= n
*/

#include <stdio.h>

void problema3()
{
    int x, y, n, p;
    printf("Introduceti x y n p:\n");
    scanf("%d %d %d %d", &x, &y, &n, &p);
    printf("%d\n",
           (
               (
                   ~(
                       (
                           65535 >> n
                       )
                       << n
                   )
                   & y
               )
               << (p - n)
           )
           | x
          );
}

/**
Explicații

x = 1110000000010000
y = 1100100100110100
n = 7
p = 9

rândul 12:  1111111111111111    65535
            0000000111111111    65535 >> 7
rândul 14:  1111111110000000    << 7
rândul 10:  0000000001111111    ~               mască pentru a lua ultimii n biți

            1100100100110100    y
rândul 16:  0000000000110100    & y             am aplicat masca
rândul 18:  0000000011010000    << 2            facem shiftare cu p-n pt că avem deja n biți pe care îi copiem
                                                aici este singurul loc unde facem o scădere

            1110000000010000    x
rândul 20:  1110000011010000    | x


Alte exemple:

x = 0001 0000 = 16
y = 0010 0101 = 37
n = p = 3
y = 3 -> se adună 5                             rezultat 21
y = 4 -> se adună 10 (5*2)                      rezultat 26


x = 0001 1010 = 26
y = 0010 0101 = 37
n = p = 3
y = 3 -> se adună 5                             rezultat 31
y = 4 -> nu se întâmplă nimic                   rezultat 26
y = 5 -> se adună 4 (celălalt bit e deja 1)     rezultat 30
*/
