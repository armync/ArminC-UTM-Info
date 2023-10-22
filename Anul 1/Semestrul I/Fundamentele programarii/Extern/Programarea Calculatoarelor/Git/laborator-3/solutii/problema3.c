#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/**
Se citesc x, y, două numere mari (fiecare având peste 20 de cifre).
Să se calculeze suma lor (folosind vectori).
    1. Numerele sunt naturale.
    2. Numerele sunt întregi.
*/

int charToInt(char a)
{
    if( a >= '0' && a <= '9')
        return a - '0';
    return 0;
}

char* problema3(char *numar1, char *numar2, int n)
{
    char *rez;
    int *rezultat;
    rez = malloc(sizeof(*rez) * (n+1));
    rezultat = malloc(sizeof(*rezultat) * (n+1));
    int lungimeNumar1, lungimeNumar2;
    int i, j, k, imin, jmin, jStart, carry, semn1, semn2, sum;
    int c1, c2;
    printf("Primul numar: %s\n", numar1);
    printf("Al doilea numar: %s\n", numar2);

    semn1 = semn2 = 1;
    imin = jmin = 0;

    lungimeNumar1 = strlen(numar1);
    lungimeNumar2 = strlen(numar2);
    if(numar1[0] == '-') {
        imin = 1;
        semn1 = -1;
    }
    if(numar2[0] == '-') {
        jmin = 1;
        semn2 = -1;
    }

    //printf("s1=%d, s2=%d\n", semn1, semn2);
    carry = k = 0;
    int sgn;
    if(semn1*semn2 == -1) {
        sgn = lungimeNumar1-imin -lungimeNumar2+jmin;
        if(sgn >= 1)
            sgn = semn1;
        else if(sgn <= -1)
            sgn = -semn1;
        else { //if(!sgn) // același nr de cifre
            int q = imin, r = jmin;
            // buclă pentru a determina numărul cel mai mare
            while(q < lungimeNumar1 && r < lungimeNumar2 && numar1[q++] == numar2[r++]);
            sgn = numar1[q-1] >= numar2[r-1] ? semn1 : -semn1;
        }
    }
    else
        sgn = semn1;

    for(i = lungimeNumar1-1, j = lungimeNumar2-1; i >= imin && j >= jmin; i--, j--) {
        c1 = charToInt(numar1[i]);
        c2 = charToInt(numar2[j]);

        //printf("i: %d j: %d; n1[i]: %d, n2[j] %d, sgn: %d\n", i, j, c1, c2, sgn);
        sum = c1*semn1*sgn + c2*semn2*sgn + carry;
        if(semn1*semn2 == -1) {
            if(sum < 0) {
                carry = -1;
                sum += 10;
            }
            else
                carry = 0;
        }
        else {
            sum = abs(sum);
            if(sum > 9) {
                carry = 1;
                sum -= 10;
            }
            else
                carry = 0;
        }

        //printf("sum: %d, carry: %d\n", sum, carry);
        rezultat[k++] = sum;
    }

    while(i >= imin) {
        sum = carry + charToInt(numar1[i--]); //printf("i: %d, sum: %d, carry: %d\n", i+1, sum, carry);
        rezultat[k++] = sum % 10;
        carry = sum > 9;
    }
    while(j >= jmin) {
        sum = carry + charToInt(numar2[j--]); //printf("j: %d, sum: %d, carry: %d\n", j+1, sum, carry);
        rezultat[k++] = sum % 10;
        carry = sum > 9;
    }
    if(carry)
        rezultat[k++] = carry;

    //printf("Rezultat: ");

    jStart = 0;
    if(sgn == -1) {
        //printf("-");
        rez[0] = '-';
        jStart++;
    }

    int init = rezultat[k-1], any = 0;
    for(j = k-1; j >= 0; j--) {
        if(init == 0) {
            init = rezultat[j];
            if(init == 0) {
                jStart--;
                continue;  // sărim peste zerourile de început
            }
        }
        any = 1;
        //printf("r[%d]=%d\n", j, rezultat[j]);
        //printf("%d\n", k-j-1+jStart);
        rez[k-j-1+jStart] = rezultat[j]+'0';
    }
    if(!any) {
        jStart++;
        rez[k-1+jStart] = '0';
    }
    rez[k+jStart] = '\0';
    free(rezultat);
    return rez;
}

/**
Explicații (prof Andrei Pătrașcu)

Am făcut o funcție ce convertește un char la int. Cifrele se află între 48 și 57 în codul ASCII. Dacă
iterăm prin aceste valori și convertim valoarea numerică a lui i în caracter, putem găsi cifra
reprezentată în variabila a și să returnăm valoarea acesteia ca fiind i-48.

Codul este deceptiv de simplu. Ținem cele două numere în 2 vectori de caractere. Le inversăm
pozițiile incă de la început (gândiți-vă la modul în care le citim). Le luăm lungimile și apoi luăm
lungimea maximă pentru a itera până la valoarea acesteia. Cât timp iteratorul i este mai mic decât
ambele lungimi, facem adunările corespunzătoare, altfel doar copiem valoarea din numărul 1 sau
numărul 2 în rezultat. La final păstrăm într-o variabilă carry excesul de la această adunare, pentru a
fi utilizat la urmatoarea iterație.

Trebuie să mai punem încă o dată adunarea excesului după acest for, apoi doar afișăm vectorul
rezultat, dar în mod invers pentru că am inversat la început, înainte să facem suma.


Explicații (Marius M)
De adăugat.
*/
