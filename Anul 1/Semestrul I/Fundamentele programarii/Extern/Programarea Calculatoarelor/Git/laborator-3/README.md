# Laboratorul 3

### ⚠ Puneți cât mai multe întrebări! Nu există întrebări greșite.
#### Semnalați orice fel de greșeli găsiți!

# Cuprins
## [Programe discutate](#programe-discutate-1)
## [Instalare `cppcheck` și `valgrind`](#cppcheck-și-valgrind)
## [Exerciții](#exerciții-1)
## [Întrebări, erori și orice nu a fost acoperit deja](#întrebări-erori-diverse)
## [Resurse recomandate](#resurse-recomandate-1)

## Programe discutate
### [Conversii](#conversii-1)
### [Pointeri](#pointeri-1)
### [Tablouri unidimensionale](#tablouri-unidimensionale-1)
### [Matrice](#matrice-1)
### [Șiruri de caractere](#șiruri-de-caractere-1)

### Conversii

Conversiile de date sunt de două feluri: implicite și explicite.

#### [Conversii implicite](https://en.cppreference.com/w/c/language/conversion)

Acestea sunt realizate de compilator în mod automat, pe cât posibil **fără pierdere de informație**.

Tipuri de date întregi:
```c
char c      = 1;  // convertește întregul 1 la char cu posibila pierdere de informatie
short a     = 2;  // convertește întregul 1 la short cu posibila pierdere de informatie
int b       = 3;  // nu are loc conversie deoarece nu e nevoie
long c      = 4;  // tipul de date destinatie (long) este cel putin la fel de "incapator" ca int, deci nu are loc vreo schimbare
long long d = 5;  // la fel ca randul anterior
```

Ce conversii au loc aici?
```c
int f(short s, bool d)
{
    char c = s - d;
    return c;
}

// exemplu de apelare din main sau din alta functie:
long l = f('x', 4);
```
- la apelul funcției, fiecare argument este convertit la tipul de date al parametrilor formali: 'x' este convertit la `short`, 4 este convertit la `bool`
- în expresiile aritmetice, se face conversia la cel mai "mare" tip de date (mai multe detalii [aici](https://en.cppreference.com/w/c/language/conversion#Integer_promotions): este vorba de tipul de date cu rangul cel mai mare)
  - astfel, avem `short` - `bool`; întrucât aceste tipuri sunt mai mici ca rang decât `int`, expresia este convertită la `int`
  - după evaluarea expresiei, rezultatul de tip `int` se convertește la `char`, întrucât acesta e tipul de date al "destinației"
    - această conversie poate avea loc cu pierdere de informație!
- se mai face o conversie la `return`, deoarece funcția `f` "promite" că întoarce un `int`
- ultima conversie are loc pentru convertirea rezultatului primit de la funcție de tip `int` la tipul de date destinație `long`

Alte situații de luat în considerare:
- conversiile între tipuri de date întregi cu semn și întregi fără semn ("implementation-defined") de același rang sau de ranguri diferite
- operatorul modulo (`%`) are obligatoriu operanzi întregi
- au loc conversii implicite și la operațiile pe biți
- rotunjirile au loc *de obicei* către cea mai apropiată valoare care poate fi reprezentată de tipul către care se face conversia

Aflați mai multe detalii în [documentație](https://en.cppreference.com/w/c/language/conversion#Integer_conversions), deoarece sunt prea multe cazuri particulare pentru a le scrie și aici.

Conversii la/de la `bool` (mai corect este `_Bool`, dar presupunem că am inclus `<stdbool.h>`):
```c
int x = true;  // x devine 1
x = false;  // x devine 0
x = 0.5;    // x este 0

bool z;
z = 0.5;   // z este 1, adică true
z = 0.0;   // z este 0, adică false
z = NULL;  // z este 0
```
Așadar, orice nu este zero devine 1 pentru tipuri de date de tip `bool`. [Ca fapt divers](https://stackoverflow.com/questions/8014161/in-c-how-much-space-does-a-bool-boolean-take-up-is-it-1-bit-1-byte-or-someth), `sizeof(_Bool)` este cel puțin 1, dar `sizeof(true)` și `sizeof(false)` sunt egale cu `sizeof(int)`.

Excludem cazurile cu numere complexe, puteți citi despre ele în documentație. Conversiile cu numere reale au loc astfel:
- dacă un operand este `long double`, ceilalți operanzi sunt convertiți la `long double`
- altfel, dacă un operand este `double`, ceilalți operanzi sunt convertiți la `double`
- altfel, dacă un operand este `float`, ceilalți operanzi sunt convertiți la `float`
- constantele reale (de exemplu `1.0`) sunt implicit `double`
- dacă un operand este `NaN`, rezultatul este `NaN`
- `NaN` nu este egal cu `NaN`

#### [Conversii explicite](https://en.cppreference.com/w/c/language/cast)

Conversiile explicite se realizează cu ajutorul operatorului de conversie (cast) și sunt necesare în anumite situații.

Am văzut deja un prim exemplu atunci când am afișat un pointer în primul laborator: `printf("%p", (void*)&nr);`. În acest exemplu, operatorul de cast este `(void*)` și este aplicat asupra expresiei `&nr`. Conversia nu afectează `&nr`.

Un exemplu în care o conversie explicită produce modificări:
```c
int x = 5 * (short)1.5;  // x este 5, deoarece 1.5 este convertit la `short` și devine 1
x = 5 * 1.5; // x este 7
```

Observații:
- adunarea și înmulțirea (și celelalte operații matematice) sunt asociative de la stânga la dreapta
- dacă avem `a + b + c`, expresia va fi tratată ca `(a + b) + c`, iar `a`, `b` și `c` pot fi la rândul lor expresii
- `c` poate fi evaluată înaintea expresiei `a`
- cu toate acestea, conversiile au loc de la stânga la dreapta, ceea ce [poate cauza sau nu un overflow](https://stackoverflow.com/questions/31630953/the-order-of-multiplications):
  - `0 * INT_MAX * INT_MAX` întoarce 0 după cum e de așteptat
  - `INT_MAX * INT_MAX * 0` produce overflow, chiar dacă aparent întoarce tot 0 (primim și warning)
  - dacă avem `INT_MAX * (INT_MAX * 0)`, nu mai primim warning

### [Pointeri](https://en.cppreference.com/w/c/language/pointer)
[Înapoi la programe](#programe-discutate-1)

Pointerii sunt tipuri de date derivate care se pot referi la alte obiecte (variabile, funcții). Această referire se referă la adresa de memorie și se obține cu operatorul `&`. Obținerea "înapoi" a obiectului către care se face referire prin pointer se face cu operatorul de dereferențiere `*`.

Exemplu:
```c
#include <stdio.h>

void schimba(double *x)
{
    *x += 2.0;  // dereferențierea pointerului x
}

int main()
{
    double z = 1.0;
    printf("z este %.3f\n", z);
    schimba(&z);  // trimitem ca parametru adresa lui z, deoarece functia schimba primeste un double*, adica o adresa catre un double
    printf("z este %.3f\n", z);
    schimba(&z);
    schimba(&z);
    printf("z este %.3f\n", z);
    return 0;
}
```

Încă un exemplu:
```c
#include <stdio.h>

void schimba(double *x)
{
    *x += 2.0;
}

int main()
{
    double z = 1.0;
    double *adr;
    adr = &z;
    // sau
    // double z = 1.0, *adr;
    // adr = &z;
    // sau
    // double z = 1.0, *adr = &z;
    printf("z este %.3f\n", z);
    schimba(&z);
    printf("z este %.3f\n", z);
    schimba(adr);
    printf("z este %.3f\n", z);
    printf("*adr este %.3f\n", *adr);
    return 0;
}
```

Putem avea pointeri la pointeri (și tot așa):
```c
#include <stdio.h>

void schimba(double **x)
{
    **x += 2.0;
}

int main()
{
    double z = 1.0, *adr = &z;
    printf("z este %.3f\n", z);
    schimba(&adr);
    printf("z este %.3f\n", z);
    printf("*adr este %.3f\n", *adr);
    return 0;
}
```

Putem avea pointeri care nu arată către ceva anume și pointeri care arată către "nimic":
```c
#include <stdio.h>

int main()
{
    double *a;
    // if(a == NULL)   // aici a are o valoare nedeterminată deoarece este neinitializata!
    //    printf("a nu arata catre nimic\n");
    // else
    //    printf("a nu este initializat, dar este diferit de 0\n");
        // printf(" si contine intamplator valoarea %p", (void*)a);  // accesarea unei variabile neinitializate este comportament nedefinit!!!
    // dereferentierea unui pointer neinitializat este comportament nedefinit!!!
    // printf("*a poate fi %.3f\n", *a);

    a = NULL;
    // dereferentierea unui pointer NULL este comportament nedefinit!!!
    // printf("*a poate fi %.3f\n", *a);
    printf("Un pointer NULL are de obicei valoarea %p\n", (void*)a);
    return 0;
}
```
Observații:
- 💥 **Dereferențierea unui pointer neinițializat este comportament nedefinit!!!** 💥
- 💥 **Accesarea unei variabile neinițializate (pointer sau altceva) este comportament nedefinit!!!** 💥
  <details>
    <summary>De fapt, vă mint un pic, dar e pentru o cauză nobilă 😇 </summary>
    Pedantic, valoarea este doar <a href=https://stackoverflow.com/questions/25074180/is-aa-or-a-a-undefined-behaviour-if-a-is-not-initialized>nedeterminată</a>, iar dacă luăm adresa (cu <code>&</code>), atunci ar fi ok, dar <a href=http://blog.frama-c.com/index.php?post/2013/03/13/indeterminate-undefined>nu e bine</a> să ne bazăm pe asta.

    Valoarea nespecificată poate să însemne că la o citire are o valoare, iar la următoarea citire are altă valoare.

    De ce? Pentru că poate fi alocată o dată într-un registru al procesorului, iar ulterior în alt registru.

    Valorile din regiștri nu au adresă; luând adresa (o simplă instrucțiune <code>&a;</code>), ar fi forțată astfel inițializarea cu ceva "constant".

    Numai atunci când folosim o valoare nedeterminată într-o funcție de bibliotecă (de exemplu `printf`) avem comportament nedefinit 👻
  </details>
- 💥 **Dereferențierea unui pointer `NULL` este comportament nedefinit!!!** 💥
- o variabilă neinițializată poate avea *orice* valoare, nu ne putem baza pe faptul că un pointer neinițializat este sau nu `NULL`
- un pointer de tip `void*` este convertit implicit la orice alt pointer
  - reciproca nu este adevărată, a se vedea `printf` cu `%p`
- `sizeof(int*)` nu este neapărat egal cu `sizeof(int)`
- pointerii către obiecte nu au neapărat același `sizeof` cu pointerii către funcții (despre pointeri la funcții vom vorbi în laboratorul 8 sau 9)
- deși atunci când afișăm un pointer cu `%p` este afișată o adresă de memorie, standardul specifică doar afișarea unei reprezentări a pointerului sub forma unui șir de caractere *dependent de implementare*
- singurele garanții oferite de standardul C sunt: `sizeof(void*) == sizeof(char*)` și `sizeof(char) == 1`
- în situațiile întâlnite în facultate, pointerii către obiecte de tipuri diferite vor avea cel mai probabil același `sizeof`
  - ca particularizare pe Windows pe 64 de biți:
    - dacă aveți MinGW simplu, atunci `sizeof(void*) == 4`
    - dacă aveți mingw-w64, atunci `sizeof(void*) == 8`
    - [Detalii] pentru a afla ce versiune aveți, din `cmd` scrieți `gcc --verbose` și căutați `Target`
      - pentru primul caz, va afișa (printre altele) `Target: mingw32`
      - pentru al doilea caz, va afișa (printre altele) `Target: x86_64-w64-mingw32`
  - sistemele de operare pe 32 de biți nu pot avea în mod normal mai mult de 4GB memorie RAM, deoarece pointerii sunt folosiți pentru accesarea memoriei, `sizeof(void*) == 4` și 2^32 = 4.294.967.296 octeți

### [Tablouri unidimensionale](https://en.cppreference.com/w/c/language/array)
[Înapoi la programe](#programe-discutate-1)

Pentru moment, nu vorbim despre tablouri alocate dinamic.

Un tablou unidimensional (sau vector) reprezintă o colecție/grupare de obiecte de același tip, alocate la adrese consecutive de memorie.

În limbajul C, accesarea elementelor unui vector se face cu operatorul `[]`. Primul element este pe poziția 0, iar cu operatorul `sizeof` aflăm dimensiunea vectorului:
```c
#include <stdio.h>

int main()
{
    int v[5], i;
    for (i = 0; i < 5; ++i)
        v[i] = i + 1;
    for (i = 0; i < 5; ++i)
        printf("%d ", v[i]);
    printf("\nVectorul v ocupă %zu bytes.\n", sizeof(v));
    // Comentariul de mai jos este invechit! Intre timp (octombrie 2020), msvcrt.dll a fost actualizat
    // in urma unui update de Windows, iar acest cod nu mai da warning nici pe Windows :D

    // pe Windows nu se poate printa portabil cu sizeof (care intoarce tipul size_t) si nu putem scapa de warnings
    // o varianta un pic mai portabila este urmatoarea (este necesar header-ul <inttypes.h>)
    // printf("\nVectorul v ocupă %" PRIu64 " bytes.\n", sizeof(v));
    return 0;
}
```

Observații:
- începând cu octombrie 2020, `%zu` este portabil și pe Windows (cel puțin pe Windows 10) 🤩
- `PRIu64` este un macro portabil pentru a afișa `long long unsigned int` și devine `llu` pe sisteme de operare bazate pe Unix sau `I64u` pe Windows
- sintaxa `"text1" "text2" "text3"` devine `"text1text2text3"` după etapa de preprocesare (mai exact, etapa 6 de [aici](https://en.cppreference.com/w/c/language/translation_phases))

Putem [inițializa un vector](https://en.cppreference.com/w/c/language/array_initialization) la momentul declarării folosind sintaxa cu acolade (sau cu ghilimele dacă este un șir de caractere):
```c
#include <stdio.h>

int main()
{
    int i, v[5] = {1, 2, 3, 4, 5};
    for (i = 0; i < 5; ++i)
        printf("%d ", v[i]);
    // eroare! accesam zone de memorie invalide
    // printf("%d %d\n", v[-1], v[5]);
    // eroare! scriem intr-o zona de memorie invalida
    // v[5] = 10;
    return 0;
}
```

Observații:
- dacă nu avem nevoie de elemente în plus, putem omite numărul de elemente din declarație: `int v[] = {1, 2, 3, 4, 5};`
- dacă specificăm mai puține elemente în lista de inițializare, [celelalte vor fi inițializate cu zero](https://stackoverflow.com/questions/2589749/how-to-initialize-array-to-0-in-c#comment57710439_2589751): cu `int v[5] = {1, 2, 3};`, în `v` vom avea `1, 2, 3, 0, 0`
- `int v[5] = {};` este invalid, trebuie să scriem cel puțin `int v[5] = {0};` dacă vrem să inițializăm toate elementele cu 0
- apropo, nu putem avea `int v[];`, dar putem avea `extern int v[];`, care reprezintă un tip incomplet și este o variabilă declarată în alt fișier sursă
- accesarea unor elemente din afara vectorului reprezintă, ați ghicit, comportament nedefinit 💥
  - "dar programul încă merge dacă ies un pic afară din vector": e ca și cum ai merge pe marginea prăpastiei; dacă ai noroc, nu pățești nimic, însă nu e bine să te bazezi pe asta
- scrierea unor valori într-un element din afara vectorului reprezintă și ea (mai e nevoie să spun?) comportament nedefinit 💥

[Vectorii pot fi convertiți la pointeri](https://en.cppreference.com/w/c/language/array#Array_to_pointer_conversion). Pointerul rezultat arată către primul element din vector. Spre deosebire de `sizeof` pe vector, `sizeof` pe pointer întoarce doar dimensiunea primului element. Un argument de tip vector este de fapt interpretat ca un pointer:
```c
#include <stdio.h>

void afis(int x[5], int n)  // linia 3
{
    int i;
    for (i = 0; i < n; ++i)
        printf("%d ", x[i]);
    puts("");
}

int main()
{
    int v[5] = {0, 1, 2};
    int *p;
    p = v;
    printf("p are sizeof %zu\n", sizeof(p));  // 8, dar formal este sizeof(int*)
    printf("v are sizeof %zu\n", sizeof(v));  // 20, dar formal este sizeof(int) * 5
    afis(v, 5);
    afis(p, 5);
    return 0;
}
```

Observații:
- linia 3 este interpretată ca `void afis(int *x, int n)`, așadar în funcția `afis` nu avem disponibilă dimensiunea vectorului (cu un `sizeof`) și trebuie să transmitem un parametru separat în acest scop
- dacă vă place mai mult, puteți scrie ca `void afis(int x[], int n)` pentru a nu vă induce în eroare acel `5` de la linia 3 care este ignorat de compilator
- dacă folosim `sizeof` într-o funcție care primește un tablou, primim următorul warning:
  - `warning: 'sizeof' on array function parameter 'x' will return size of 'int *' [-Wsizeof-array-argument]`
- un pointer către un întreg poate fi privit ca un vector cu un singur element
- pe de altă parte, `int *v = {1, 2, 3};` este invalid (primim și warning)
- **numele unui vector este un pointer constant către adresa primului element**
  - este constant deoarece nu îl putem modifica: nu putem scrie `s4 = s3;` sau `s3 = s2;` - încercați!
  - în schimb, putem scrie `s2 = s3;`, deoarece `s2` este pointer!

Standardul C99 introduce vectori de lungime variabilă (VLA - variable length arrays), iar standardul următor C11 aproape îi elimină. Aceștia nu pot fi inițializați cu sintaxa cu acolade, dar îi putem folosi pentru a aloca pe stivă un număr de elemente stabilit la execuție (citiți și observațiile!):
```c
#include <stdio.h>

void afis(int *x, int n)
{
    int i;
    for (i = 0; i < n; ++i)
        printf("%d ", x[i]);
    puts("");
}

int main()
{
    for(int j = 0; j < 3; ++j)
    {
        int n;
        printf("Introduceti n: ");
        scanf("%d", &n);
        int v[n], *p;
        p = v;
        printf("VLA de %d elemente are sizeof %zu\n", n, sizeof(v));
        for(int i = 0; i < n; ++i)
            v[i] = n - i;
        afis(v, n);
        afis(p, n);
    }
    return 0;
}
```

Observații:
- în interiorul blocului `for`, vectorul `v` are de fiecare dată altă dimensiune
- la fel ca la vectorii normali, atunci când transmitem un VLA unei funcții, acesta este convertit într-un pointer către primul element din vector
- VLA nu ar trebui folosiți în mod uzual ⚠, întrucât nu aduc multe avantaje:
  - dacă alocăm puține elemente, putem stabili dimensiunea maximă la momentul compilării
  - dacă avem nevoie de multe elemente, oricum nu putem folosi VLA, ci va fi nevoie de alocare dinamică
  - VLA sunt alocați tot pe stivă


### Matrice
[Înapoi la programe](#programe-discutate-1)

O matrice (sau tablou bidimensional) este un vector de vectori. Știm despre vectori că elementele sunt alocate la adrese consecutive de memorie. Similar, vectorii din matrice sunt și ei alocați la adrese consecutive de memorie, adică fiecare vector este în continuarea celui de dinaintea sa.

```c
#include <stdio.h>

int main()
{
    int nr_trotuare, locuri, i, j;
    nr_trotuare = 2;
    locuri = 10;
    _Bool parcare[nr_trotuare][locuri];
    for (i = 0; i < nr_trotuare; ++i)
        for (j = 0; j < locuri; ++j)
        {
            // scanf("%d", &parcare[i][j]);   // linia 12
            parcare[i][j] = ((i+j)%3 == 0);
        }
            

    for (j = 0; j < locuri; ++j, puts(""))
        for (i = 0; i < nr_trotuare; ++i)
            parcare[i][j] ? printf("[x]\t") : printf("[ ]\t");
    return 0;
}
```

Observații:
- operatorul `<cond> ? <expr_adev> : <expr_fals>` evaluează condiția `<cond>` și întoarce expresia `<expr_adev>` dacă `<cond>` este adevărată sau `<expr_fals>` în caz contrar
- diferența dintre `if/else` și `? :` este aceea că a doua reprezintă o expresie, adică întoarce o valoare
- în exemplul de mai sus, nu ne interesează valoarea și am folosit operatorul acesta pentru că este mai concis
- dacă voiam să preluăm valoarea, aveam `int caractere_afisate = parcare[i][j] ? printf("[x]\t") : printf("[ ]\t");`, ceea ce nu puteam face la fel de simplu cu o instrucțiune `if/else`
- dacă doriți să citiți valorile matricei de la tastatură, decomentați linia 12 și comentați linia următoare
  - `scanf` nu poate citi în mod explicit `_Bool`, de aceea citim sub formă de `int` și ne folosim de conversiile implicite

### Șiruri de caractere
[Înapoi la programe](#programe-discutate-1)

În limbajul C, un șir de caractere este un vector de caractere, urmate la sfârșit de caracterul special `'\0'`, numit terminator de șir ("Null-terminated string").

La modul general, un caracter poate fi definit ca cea mai mică unitate de informație: de exemplu, o literă (`ă`), un simbol (`?`) sau un emoji (🤔). Un caracter este codificat printr-un singur byte sau *prin mai mulți bytes*, proces care poartă numele de encoding (codificare). Cu alte cuvinte, caracterele sunt un concept mai abstract, iar felul în care acestea sunt stocate de calculator este realizat cu ajutorul unui encoding.

Un exemplu de encoding este Windows-1252, folosit pe majoritatea calculatoarelor din facultate. Acest encoding are o corespondență de 1 la 1 între caractere și bytes: un caracter este stocat într-un singur byte. Valorile primelor 127 de caractere se numesc coduri ASCII, iar valorile pentru următoarele 128 se numesc coduri din ASCII extins. Putem avea cel mult 255 de caractere, deoarece vom rezerva unul pentru caracterul special `'\0'`. Cam puțin, nu-i așa?

Prin urmare, nu prea ne ajunge un singur byte pentru a codifica un caracter. După mulți ani de dezbateri, s-a ajuns la un consens. În prezent, cea mai folosită codificare este **UTF-8**. Citiți [aici](http://utf8everywhere.org/) mai multe despre avantajele sale (sau nu, ca să nu vă speriați). Pe scurt, fiecare caracter este codificat prin 1, 2, 3 sau 4 bytes (cel puțin în prezent).

Din aceste motive, în C avem:
- caracterele clasice reprezentate printr-un singur byte (byte strings - ce veți folosi în facultate)
- caractere multibyte
- caractere wide (să le spun caractere late??), care sunt reprezentări ale caracterelor multibyte

Din cauza numeroaselor probleme de portabilitate, prelucrarea șirurilor de caractere ar trebui realizată cu biblioteci specializate, deoarece limbajul C nu oferă ceva suficient de portabil în acest sens.

În continuare, ne vom limita la caractere clasice:
```c
#include <stdio.h>
#include <string.h>  /* pentru strlen */

void afis(char *s, char *nume)
{
    char *p = s;
    printf("Sirul %s este %s si are lungimea %zu\n", nume, s, strlen(s));
    while(*p != '\0')
    {
        printf("(%c) cu valoarea %d\n", *p, *p);
        p++;
    }
    puts("\n-----------------\n");
}

int main()
{
    char s1[] = "qwe";  // contine si '\0', are tipul char[4] si poate fi modificat
    afis(s1, "s1");
    char *s2 = "rty";   // contine si '\0', nu poate fi modificat!  https://en.cppreference.com/w/c/language/array_initialization
    afis(s2, "s2");
    char s3[6] = "uio"; // contine si '\0' si poate fi modificat
    afis(s3, "s3");

    for(int i = 0; i < 6; ++i)
        printf("(%c) cu valoarea %d\n", s3[i], s3[i]);
    puts("\n-----------------\n");

    // atentie!!
    char s4[3] = "rew";  // nu contine '\0'
    // afis(s4, "s4");  // !!!
    for(int i = 0; i < 3; ++i)
        printf("(%c) cu valoarea %d\n", s4[i], s4[i]);
    puts("\n-----------------\n");

    char* sir = "un sir\tde\ncaractere";
    printf(sir);
    puts("\n-----------------\n");

    char zi[15];
    puts("\nCe zi este azi?");
    scanf("%14s", zi);
    printf("Am citit %s!\n\n", zi);

    int ch;
    while ((ch = getchar()) != '\n' && ch != EOF); // linia 46

    // scanf se oprese dupa primul spatiu
    // daca vrem sa citim si spatii, folosim fgets
    char propozitie[100];
    printf("Introduceti propozitia: ");
    fgets(propozitie, 100, stdin);
    printf("Am citit: \"");
    fputs(propozitie, stdout);
    puts("\"\nGata!");
    return 0;
}
```

Observații:
- `s1` este un vector de caractere alocat static și inițializat asemănător cu sintaxa cu acolade:
  - echivalentul este `char s1[] = {'q', 'w', 'e', '\0'};`
- `s2` este un pointer către un literal de tip șir de caractere (string literal); modificarea unui string literal reprezintă comportament nedefinit 💥 
- `s3` este asemănător cu `s1` și se aplică aceeași regulă de mai sus cu inițializarea cu 0 a celorlalte elemente:
  - echivalentul este `char s1[] = {'q', 'w', 'e', '\0', '\0', '\0'};`
- `s4` **nu conține `'\0'`**; dacă afișați `s4[3]` cu `%d`, cel mai probabil nu veți obține 0 corespunzător `'\0'`; și chiar dacă ați obține 0, este comportament nedefinit deoarece accesați un element din afara vectorului
- spre deosebire de `s2`, șirurile `s1`, `s3` și `s4` pot fi modificate
- pentru a putea folosi funcțiile de prelucrare pentru șiruri de caractere (de exemplu `strlen`), este obligatoriu ca șirul de caractere să aibă cel puțin un `'\0'`
  - în caz contrar, se accesează zone invalide de memorie până la întâlnirea unui caracter `'\0'`
- `sir` este doar ca să nu aveți impresia că șirurile de caractere nu pot conține spații
- dacă vrem să citim șiruri de caractere cu `scanf`, **specificăm obligatoriu lungimea maximă**; [alternativ, folosim **`fgets`**](https://stackoverflow.com/questions/58403537/what-can-i-use-for-input-conversion-instead-of-scanf)
  - funcția `scanf` se oprește la primul caracter alb (exemple: `' '`, `'\n'`) și este problematic dacă vrem să citim și altceva, deoarece comportamentul citirii spațiilor diferă pentru fiecare specificator de conversie
  - `scanf` completează întotdeauna șirul cu `'\0'`
  - nu citim cu `scanf("%14s", &zi);`, deoarece `zi` este un vector, dar este și un **pointer** la adresa primului element
    - `&zi` are tipul `char(*)[15]`, adică un pointer la un vector de caractere de 15 elemente
    - `zi` are tipul `char[15]`, echivalent cu `char*` la transmiterea ca parametru unei funcții
  - funcția `fgets` primește un șir de caractere, numărul maxim de caractere + 1 (`nr`) pe care vrem să îl citim și locul de unde citim (fișier, tastatură etc)
    - numărul de caractere va fi de obicei lungimea șirului de caractere în care citim: `fgets` citește `nr - 1` caractere, apoi completează cu `'\0'`
    - `fgets` se oprește la rând nou (`'\n'`), iar șirul citit va conține acest caracter `'\n'`; dacă ne încurcă, îl putem șterge ulterior
    - dacă există mai mult de `nr - 1` caractere, citirea se oprește după acele `nr - 1` caractere, iar șirul nu va conține caracterul de rând nou
  - în ambele cazuri, trebuie să avem deja alocat spațiul pentru șirul de caractere
  - un pointer către un șir de caractere literal nu poate fi folosit, deoarece nu avem voie să modificăm zona respectivă!
- la linia 46 vrem să [eliminăm caracterul de rând nou](https://stackoverflow.com/questions/40554617/while-getchar-n) care a rămas de la `scanf`
  - fără acest pas, `fgets` va citi doar acel `'\n'` rămas de dinainte! (de aceea este de preferat să citim doar cu `fgets`)
  - de asemenea, adăugăm condiția cu `EOF` (end of file) pentru situația în care are loc o eroare la citirea de la tastatură sau dacă vrem să oprim citirea prin folosirea unui caracter de control: <kbd>Ctrl</kbd> + <kbd>Z</kbd> pe Windows, respectiv <kbd>Ctrl</kbd> + <kbd>D</kbd> pe Unix
  - utilizarea `fflush` pentru dispozitive de intrare [nu are sens!](https://stackoverflow.com/questions/2979209/using-fflushstdin)

Despre șiruri de caractere vom mai discuta într-un laborator separat, deoarece este un subiect vast.

## `cppcheck` și `valgrind`
[Înapoi la cuprins](#cuprins)

Puteți instala ușor [`cppcheck`](http://cppcheck.sourceforge.net/#download) pe Windows.

Vestea proastă este că nu am găsit vreun instrument de verificare a memoriei pentru Windows *care să și meargă*. Există [DrMemory](http://www.drmemory.org/) cu care m-am chinuit câteva ore să îl fac să meargă, apoi am renunțat.

Dacă aveți deja ceva Unix-based, atunci ar trebui să fie relativ ușor cu `valgrind`: fie din package manager, fie instalat din [sursă](https://valgrind.org/downloads/repository.html). Pentru macOS nu pare să fie atât de simplu, vedeți de exemplu [aici](https://www.gungorbudak.com/blog/2018/04/28/how-to-install-valgrind-on-macos-high-sierra/). Altfel, mai există varianta opțiunii de compilator `-fsanitize=address` (dacă primiți erori, încercați [asta](https://stackoverflow.com/questions/37970758/how-to-use-addresssanitizer-with-gcc/40215639#40215639)). Sau folosiți varianta 1 de mai jos și nu trebuie să instalați nimic.

Vestea bună e că aveți alte trei alternative (alegeți una singură):
1. [Folosiți GitHub cu GitHub Actions/Travis/altceva similar (sau GitLab)](#din-browser) - varianta recomandată și **nu trebuie să instalați nimic**
2. [Instalați WSL (Windows Subsystem for Linux)](#wsl)
3. [Instalați o mașină virtuală de Linux](#mașină-virtuală)


#### Din browser
Pași de urmat pentru GitHub cu GitHub Actions. Dacă doriți alte variante, le voi adăuga și pe acelea:
- vă creați un cont pe GitHub
- creați un repository
- dați pe `Actions`, apoi click pe `set up a workflow yourself`

În fișierul respectiv veți scrie următoarele:
```
TBA
```

- TBA restul pașilor

#### WSL
- `Control Panel` -> `Turn Windows features on or off` -> bifați `Windows Subsystem for Linux`
- încercați întâi să urmați pașii de aici: https://docs.microsoft.com/en-us/windows/wsl/install-win10 (apoi de căutat pe net în funcție de eroare)
- ☹ am instalat mai demult și între timp s-au schimbat lucrurile, posibil să nu vă meargă...

#### Mașină virtuală
- folosiți VirtualBox sau VMWare Player
- descărcați un ISO cu ce distribuție doriți

<!--
Laboratorul 4:
### Structuri
### `typedef`
### Uniuni
### Câmpuri de biți
### Alocare dinamică

Laboratorul 5:
### Directive de preprocesare
### Fișiere text
### Fișiere binare

Laboratorul 6:
### Șiruri de caractere
### Generarea numerelor aleatoare

Laboratorul 7:
### Sortare cu qsort
### Căutare binară cu bsearch
### Recapitulare pentru test

// test 1

Laboratorul 8: // săpt 9
### Structuri autoreferite
### Funcții matematice

Laboratorul 9:
### Pointeri la funcții

Laboratorul 10:
### Recapitulare pentru test
sau
### Argumente din linia de comandă
### Variabile de mediu
### Funcții cu număr variabil de argumente

// test 2
-->

## Exerciții
[Înapoi la cuprins](#cuprins)

- modificați exemplul cu matricea astfel încât parcarea să fie afișată "orizontal" în loc de "vertical"

Exerciții din PDF:
1. Se citesc `n`, `m` și apoi două mulțimi `A` și `B` cu `n`, respectiv `m` numere întregi cuprinse între `[-x, x]`, `x <= 2000`. Să se afișeze numărul de elemente comune mulțimii.
- indicație: mulțimile `A` și `B` nu se vor memora - se va crea un vector de frecvență; în codul de mai jos, `vf` este un vector de frecvență:
```c
int vf[11] = {0}, nr, i;
do
{
    printf("Introduceti un numar de la 0 la 10 (-1 pentru oprire): ");
    scanf("%d", &nr);
    ++vf[nr];
} while(nr != -1);

for(i = 0; i <= 10; ++i)
    printf("%d apare de %d ori.\n", i, v[i]);
```
- 🚧 teste

2. Se citesc: `n`, cele `n` elemente ale unui vector sortat crescător, apoi `x` și `y` două elemente din vector. Să se afișeze toate elementele vectorului cuprinse între `x` și `y`. Indicație: folosiți căutarea binară:
```c
int cautare_binara(int *v, int x, int st, int dr)
{
    if(st > dr)     return -1;
    if(v[st] == x)  return st;
    if(v[dr] == x)  return dr;

    int mijloc = (st + dr) / 2;
    if(v[mijloc] == x)
        return mijloc;
    else if(x < v[mijloc])
        return cautare_binara(v, x, st, mij - 1);  // caut doar in stanga
    else
        return cautare_binara(v, x, mij + 1, dr);  // caut doar in dreapta
}
```
- 🚧 teste

3. Se  citesc `x`, `y`, două numere mari (fiecare având peste 20 de cifre). Să se calculeze suma lor (folosind vectori).
  a) Numerele sunt naturale
  b) Numerele sunt întregi
  - explicație: numerele mari le vom citi ca pe niște șiruri de caractere, apoi parcurgem în același timp vectorii de la dreapta la stânga, întrucât cifra cea mai nesemnificativă va fi în dreapta
  - trebuie propagat un `1` dacă suma depășește 10
  - numerele întregi pot avea același semn sau semne diferite
  - 🚧 **teste** (din cauză că nu aveam teste am trimis o soluție greșită ☹ )

4. Se citesc de la tastatură `m` și `n` naturale nenule reprezentând dimensiunile unei matrice și apoi se citesc elementele matricei. Să se construiască și să se afișeze matricea transpusă.
```
A =  1  2  3 
     4  5  6

A^T =  1   4
       2   5
       3   6
```
- 🚧 teste

5. Să se parcurgă o matrice în spirală.

Exemplu: pentru matricea de mai jos se va afișa `1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8`:
```
   1      2     3
   4      5     6
   7      8     9
   10    11    12
```
- 🚧 teste

6. Să se creeze o matrice patratică, în spirală, după regulile:
  - numerele pornesc de la 1, din 1 în 1, în ordine crescătoare
  - după fiecare număr neprim `x`, se adaugă cel mai mic divizor propriu al său, după care se continuă cu `x + 1`.

Exemplu:
```
 1   2   3   4   2
11  12   2  13   5
 2  16   2  14   6
10   3  15   2   2
 3   9   2   8   7
```
- 🚧 teste

7. Se citește o matrice `A` de dimenisiuni `N x N` (`1 <= N <= 100`), (`0 <= A[i][j] < 2^32`). Să se efectueze o rotire spre dreapta a matricei `A`.

Exemplu:
```
1   2        3   1
        =>
3   4        4   2
```
- 🚧 teste

## Întrebări, erori, diverse
[Înapoi la cuprins](#cuprins)

* 🚧

## Resurse recomandate
- [cppreference.com](https://en.cppreference.com/w/c)
- [StackOverflow](https://stackoverflow.com/questions/tagged/c?tab=Votes)
- [C FAQ](http://c-faq.com/questions.html)
- [C99 standard](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf) (doar să îl răsfoiți un pic)
- [Rezumat cu funcții pe care trebuie să le evitați (e.g. `gets`)](http://www.gidnetwork.com/b-56.html)
