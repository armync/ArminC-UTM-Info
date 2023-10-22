#include <stdio.h>
#include <limits.h>
#include <inttypes.h>
#include <float.h>
#include <math.h>

#define eps 1e-5

void afisare(int v[], int n) {
    int i;
    printf("[");
    for(i = 0; i < n - 1; i++)
    {
        printf("%d, ", v[i]);
    }
    printf("%d", v[i]);
    puts("]");
}

void l1(void) {
    int n = 20;
    int v[n], i;

    for(i = 0; i < n; i++)
    {
        v[i] = i + 5;
    }
    afisare(v, n);
    for(i = 0; i < n; i++)
    {
        v[i] = i + 15;
    }
    afisare(v, n);
    /*
    for(int $(i) = $(n); $(i) >= $(zero); $(i)--)
    {
        |
    }
    for(int i = n; i >= 2; i--)
    {

    }*/
}

void l21(void) {
    printf("%u\n", CHAR_BIT);
    printf("%u %d %d%c", sizeof(char), CHAR_MIN, CHAR_MAX, 10);
    for(signed char c = 0; c < 127; c++)
        printf("%d %c\n", c, c);
}

void l22(void) {
    int x, y;
    int *adr;

    x = 3;
    printf("x este %d si are adresa %p\n", x, (void*)&x);
    adr = &x;
    printf("adr este %p, prin dereferentiere obtinem %d si are adresa %p\n", (void*)adr, *adr, (void*)&adr);
    //adr = &y;
    *adr = 4;
    printf("x este %d si are adresa %p\n", x, (void*)&x);    printf("adr este %p, prin dereferentiere obtinem %d si are adresa %p\n", (void*)adr, *adr, (void*)&adr);

    printf("Introdu y: ");
    int citite = fscanf(stdin, "%x", &y);
    if(citite > 0)
        fprintf(stdout, "%x (%d)\n", y, y);
    else
        puts("eroare la citire :(");
}

void l23(void) {
    printf("%"PRIu64"\n", ULLONG_MAX);
    printf("%E\n", LDBL_MAX);
    printf("%u %u %u\n", sizeof(float), sizeof(double), sizeof(long double));
    double f = 0;
    for(int i = 0; i < 1000000; i++)
        f += 0.1;
    if(fabs(f - 100000.0) < eps)
        printf("%f", f);
    else
        printf("nu e foarte exact");
}
// 100958.343750
// 100000.0000013329        double
// 100000.000000000873257   long double

int main(void) {
    //l1();
    //l21();
    //l22();
    l23();
    return 0;
}
