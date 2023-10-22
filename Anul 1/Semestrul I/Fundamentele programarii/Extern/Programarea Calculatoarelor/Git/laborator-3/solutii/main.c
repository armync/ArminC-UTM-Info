/**
Anul universitar 2019-2020, actualizat 2020-2021
Programarea Calculatoarelor, anul I, semestrul 1
Laboratorul 3
Seria 15 (2019-2020), seria 16 (2020-2021)

Fișierul "Laborator 3_v2.pdf"
*/

#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <stdlib.h>

#include "laborator3.h"

int main()
{
    //problema1();
    //problema2();
    //problema4();
    //problema5();
    //problema6();
    //problema7();
    //problema8();
    //ex();

    testp3("-123", "33", 5, "-90");
    testp3("-123", "23", 5, "-100");
    testp3("-123", "24", 5, "-99");
    testp3("123", "-24", 5, "99");
    testp3("1123", "-24", 5, "1099");
    testp3("342", "-173", 5, "169");
    testp3("242", "-173", 5, "69");
    testp3("-342", "173", 5, "-169");
    testp3("-1", "-999", 5, "-1000");
    testp3("1", "999", 5, "1000");
    testp3("99", "99", 5, "198");
    testp3("109", "901", 5, "1010");
    testp3("101", "-101", 5, "0");
    testp3("101", "-102", 5, "-1");
    testp3("102", "-101", 5, "1");
    testp3("12345678900987654321234567890",
           "10000000000000000000000000011", 30,
           "22345678900987654321234567901");
    testp3("12345678900987654321234567890",
          "-10000000000000000000000000011", 30,
            "2345678900987654321234567879");
    testp3("0", "0", 5, "0");
    testp3("0", "-0", 5, "0");
    xtestp3("-0", "0", 5, "0");
    return 0;
}

void ex() {
    /*nr de biți de 1 din a*/
    int a, k;
    k = 0;
    scanf("%d", &a);
    while(a) {
        a = a & (a-1);
        k++;
    }
    printf("%d ", k);
}

void testp3(char *nr1, char *nr2, int n, char *rez) {
    char *suma;
    suma = problema3(nr1, nr2, n);
    assert(printf("%s ar trebui sa fie %s\n\n", suma, rez) && !strcmp(suma, rez));
    free(suma);
}

void xtestp3(char *nr1, char *nr2, int n, char *rez) {
    printf("Skipping test p3(%s, %s, %d) == %s\n", nr1, nr2, n, rez);
}
