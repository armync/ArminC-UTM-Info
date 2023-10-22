/**
Scrieți un program care primește ca input de la tastatură scrierea unui număr
în baza 2 și calculează direct scrierea acestuia în baza 16 (nu mai trece prin
baza intermediară 10). Realizați acest lucru inversând cele două baze
(input – scrierea în baza 16, output – scrierea în baza 2).

Funcțiile rezolvaSimplu() și rezolvaInv() ar trebui să fie clare și ușor de înțeles.

Celelalte 3 variante de rezolvare folosesc pointeri la funcții
pentru a nu repeta codul din funcția rezolva() dacă dorim să schimbăm implementarea funcției printHex().
Puteți să le ignorați dacă nu le înțelegeți.
*/

#define N 17
#define N_CACHE 22

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Nr
{
    char b2[5];
    char b16;
};

void rezolvaSimplu();
void rezolvaInv();
void rezolva(void (*printFunc)(char *));
void printHex(char *grup);
void printHex1(char *grup);
void printHex2(char *grup);
void printBin(char c);

void problema4Simplu()
{
    rezolvaSimplu();
    rezolvaInv();
}

void problema4_v0()
{
    rezolva(printHex);
}

void problema4_v1()
{
    rezolva(printHex1);
}

void problema4_v2()
{
    rezolva(printHex2);
}

void rezolvaSimplu()
{
    char x[N];
    unsigned int i;

    printf("Introduceti x in binar: ");
    scanf("%16s", x);
    printf("x in hexa este 0x");
    for(i=0; i<strlen(x); i+=4)
    {
        printHex(x+i);
    }
    puts("");
}

void rezolvaInv()
{
    char x[N];
    unsigned int i;

    printf("Introduceti x in hex (fara 0x la inceput): ");
    scanf("%16s", x);
    printf("x in binar este ");
    for(i=0; i<strlen(x); i++)
    {
        printBin(x[i]);
    }
}

void rezolva(void (*printFunc)(char *c))
{
    char x[N];
    unsigned int i;

    printf("Introduceti x in binar: ");
    scanf("%16s", x);
    printf("x in hexa este 0x");
    for(i=0; i<strlen(x); i+=4)
    {
        printFunc(x+i);
    }
}

void printHex(char *c)
{
    if(strncmp(c, "0000", 4) == 0)
    {
        printf("0");
    }
    else if(strncmp(c, "0001", 4) == 0)
    {
        printf("1");
    }
    else if(strncmp(c, "0010", 4) == 0)
    {
        printf("2");
    }
    else if(strncmp(c, "0011", 4) == 0)
    {
        printf("3");
    }
    else if(strncmp(c, "0100", 4) == 0)
    {
        printf("4");
    }
    else if(strncmp(c, "0101", 4) == 0)
    {
        printf("5");
    }
    else if(strncmp(c, "0110", 4) == 0)
    {
        printf("6");
    }
    else if(strncmp(c, "0111", 4) == 0)
    {
        printf("7");
    }
    else if(strncmp(c, "1000", 4) == 0)
    {
        printf("8");
    }
    else if(strncmp(c, "1001", 4) == 0)
    {
        printf("9");
    }
    else if(strncmp(c, "1010", 4) == 0)
    {
        printf("A");
    }
    else if(strncmp(c, "1011", 4) == 0)
    {
        printf("B");
    }
    else if(strncmp(c, "1100", 4) == 0)
    {
        printf("C");
    }
    else if(strncmp(c, "1101", 4) == 0)
    {
        printf("D");
    }
    else if(strncmp(c, "1110", 4) == 0)
    {
        printf("E");
    }
    else
    {
        printf("F");
    }
}

void printHex1(char *c)
{
    if(c[0] == '0')
    {
        if(c[1] == '0')
        {
            if(c[2] == '0')
            {
                if(c[3] == '0')
                    printf("0");
                else
                    printf("1");
            }
            else
            {
                if(c[3] == '0')
                    printf("2");
                else
                    printf("3");
            }
        }
        else
        {
            if(c[2] == '0')
            {
                if(c[3] == '0')
                    printf("4");
                else
                    printf("5");
            }
            else
            {
                if(c[3] == '0')
                    printf("6");
                else
                    printf("7");
            }
        }
    }
    else
    {
        if(c[1] == '0')
        {
            if(c[2] == '0')
            {
                if(c[3] == '0')
                    printf("8");
                else
                    printf("9");
            }
            else
            {
                if(c[3] == '0')
                    printf("A");
                else
                    printf("B");
            }
        }
        else
        {
            if(c[2] == '0')
            {
                if(c[3] == '0')
                    printf("C");
                else
                    printf("D");
            }
            else
            {
                if(c[3] == '0')
                    printf("E");
                else
                    printf("F");
            }
        }
    }
}

const struct Nr cache[N_CACHE] =
{
    {"0000", '0'},
    {"0001", '1'},
    {"0010", '2'},
    {"0011", '3'},
    {"0100", '4'},
    {"0101", '5'},
    {"0110", '6'},
    {"0111", '7'},
    {"1000", '8'},
    {"1001", '9'},
    {"1010", 'A'},
    {"1011", 'B'},
    {"1100", 'C'},
    {"1101", 'D'},
    {"1110", 'E'},
    {"1111", 'F'},
    {"1010", 'a'},
    {"1011", 'b'},
    {"1100", 'c'},
    {"1101", 'd'},
    {"1110", 'e'},
    {"1111", 'f'}
};

void printHex2(char *grup)
{
    int i;
    for(i = 0; i < N_CACHE; i++)
    {
        if(strncmp(grup, cache[i].b2, 4) == 0)
            printf("%c", cache[i].b16);
    }
}

void printBin(char c)
{
    int i;
    for(i = 0; i < N_CACHE; i++)
    {
        if(c == cache[i].b16)
            printf("%s", cache[i].b2);
    }
}
