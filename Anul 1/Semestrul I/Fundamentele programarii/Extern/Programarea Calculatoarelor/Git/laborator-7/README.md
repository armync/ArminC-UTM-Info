# Laboratorul 7

### ⚠ Puneți cât mai multe întrebări! Nu există întrebări greșite.
#### Semnalați orice fel de greșeli găsiți!

# Cuprins
## [Programe discutate](#programe-discutate)
## [Exerciții](#exerciții-1)
## [Întrebări, erori și orice nu a fost acoperit deja](#întrebări-erori-diverse)
## [Resurse recomandate](#resurse-recomandate-1)

## Programe discutate

### [Sortarea cu `qsort`](#sortarea-cu-qsort-1)
### [Căutarea cu `bsearch`](#căutarea-cu-bsearch-1)
### [Despre pointerii la funcții](#despre-pointerii-la-funcții-1)

### Sortarea cu [`qsort`](https://en.cppreference.com/w/c/algorithm/qsort)

Pentru a sorta un vector, fie implementăm noi sortarea, fie folosim o funcție de bibliotecă deja implementată care face asta pentru noi.

Programul de mai jos sortează descrescător un vector de numere folosind funcția `qsort` din `<stdlib.h>`: 
```c
#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b)
{
    int A = *((const int*)a);
    int B = *((const int*)b);
    if(A < B) return 1;
    if(A > B) return -1;
    return 0;
}

void afis(int *v, int n)
{
    for(int i = 0; i < n; ++i)
        printf("%d ", v[i]);
    printf("\n");
}

int main(void)
{
    int v[] = {5, 3, 7, 3, 2, 8, 2, 0, 1, 9, -1, 4};
    int n = sizeof(v) / sizeof(v[0]);
    afis(v, n);
    qsort(v, n, sizeof(v[0]), cmp);
    afis(v, n);
    return 0;
}
```
Observații:
- funcția `qsort` are 4 parametri:
  - `v` este vectorul de numere pe care vrem să îl sortăm
  - `n` este numărul de elemente al vectorului `v`
  - al treilea argument este `sizeof`-ul unui element din vector: este necesar să specificăm acest lucru, deoarece `qsort` vede vectorul ca fiind de tip `void*`!
  - al patrulea argument este o funcție comparator, adică un **pointer la funcție**
    - altfel spus, este numele unei funcții, *fără paranteze*
    - de ce fără paranteze? dacă punem paranteze, înseamnă că *apelăm* funcția, dar cu ce argumente? 🤔
    - ... exact, nu are sens să o apelăm *noi*
    - numele oricărei funcții este automat un pointer la funcția respectivă
    - dacă nu înțelegeți ce se întâmplă, nu vă panicați 😌 aveți încredere: puneți numele funcției fără paranteze
- orice **funcție comparator** are următoarele proprietăți:
  - primește ca argumente doi pointeri `const void*`, să le spunem `a` și `b`
    - de ce? deoarece nu vrem să modificăm elementele atunci când le comparăm
    - desigur, nu e obligatoriu să facem cast la `const int*`, puteam folosi `int*` (dar nu e frumos...)
    - repet: **nu modificăm** elementele în funcția comparator
  - întoarce `int`:
    - un întreg negativ dacă `a` trebuie să fie înaintea lui `b` în vectorul sortat
    - un întreg pozitiv dacă `a` trebuie să fie după `b`
    - `0` dacă `a` este echivalent cu `b`
  - pentru două valori fixate, funcția trebuie să întoarcă **același** rezultat dacă este apelată de mai multe ori
- de ce să nu implementăm noi sortarea? pentru că ar trebui să fie mai simplu să folosim ceva gata făcut (dar nu dus la [extrem](https://devrant.com/rants/2477812/fucking-love-how-one-liner-packages-are-breaking-basically-the-entire-js-ecosyst))
- cu toate că funcția se numește `qsort`, standardul C nu obligă ca implementarea să folosească quick sort și, ce e și mai trist, nu garantează vreun nivel de complexitate (de exemplu `O(n logn)`; totuși, în general pare să fie o soluție mult mai eficientă decât o soluție scrisă de noi cu complexitate `O(n^2)` (2 `for`-uri)
- putem simplifica instrucțiunile de `return` din funcția comparator astfel: `return (A < B) - (A > B);`
  - nu vrem să facem scăderea direct `B - A`, deoarece există posibilitate de underflow/overflow
  - atenție la tipurile de date! `A` și `B` sunt întregi, nu pointeri către întregi: dacă folosim pointeri, posibil să avem nevoie de paranteze în plus pentru a nu scădea pointeri!

Sortarea unui vector de structuri după mai multe criterii:
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    enum { AMAR, ACRU, SARAT, DULCE } gust;
    int calorii;
    char nume[16];
} Aliment;

int cmp_aliment(const void *a, const void *b)
{
    Aliment A = *((const Aliment*)a);
    Aliment B = *((const Aliment*)b);
    if(A.gust > B.gust)
        return -1;
    if(A.gust < B.gust)
        return 1;
    return strcmp(A.nume, B.nume);
}

const char* afis_gust(Aliment a)
{
    switch(a.gust)
    {
        case AMAR:  return "AMAR";
        case ACRU:  return "ACRU";
        case SARAT: return "SARAT";
        case DULCE: return "DULCE";
        default:    return "??";
    }
}

void afis(Aliment *v, int n)
{
    for(int i = 0; i < n; ++i)
        printf("%-15s gust %-6s %3d de calorii\n", v[i].nume, afis_gust(v[i]), v[i].calorii);
    printf("\n");
}

int main(void)
{
    Aliment v[] = {
        { .nume = "lamai",         .gust = ACRU,  .calorii = 100 },
        { .nume = "cirese amare",  .gust = AMAR,  .calorii = 200 },
        { .nume = "alune cu sare", .gust = SARAT, .calorii = 400 },
        { .nume = "portocale",     .gust = DULCE, .calorii =  90 },
        { .nume = "piersici",      .gust = DULCE, .calorii = 300 },
        { .nume = "lamai",         .gust = ACRU,  .calorii = 120 },
    };
    int n = 6;
    afis(v, n);
    qsort(v, n, sizeof(Aliment), cmp_aliment);
    afis(v, n);
    return 0;
}
```
Observații:
- nu este necesar să comparăm după toate câmpurile din structură: în exemplul de mai sus, am ignorat câmpul `calorii`
- la afișare, dacă știm lungimea maximă a ceea ce vrem să afișăm, putem să o specificăm în specificatorul de conversie
  - alternativ, putem să transmitem aceste lungimi ca parametri separați:
  - `printf("%*s gust %*s %*d de calorii\n", -15, v[i].nume, -6, afis_gust(v[i]), 3, v[i].calorii);`
  - putem calcula programatic aceste lungimi ca să nu fie nevoie să le hardcodăm
- nu am folosit `else if` în funcția comparator deoarece nu este necesar `else` dacă înainte avem `return`
- enumerarea din structură este anonimă, însă putem accesa din afara structurii câmpurile enumerării, deoarece structurile în C nu limitează scopul

Pentru a ordona doar o parte dintr-un vector (de structuri), putem proceda astfel:
```c
qsort(v, n/3, sizeof(Aliment), cmp_aliment);
qsort(v+n/2, n/2, sizeof(Aliment), alta_functie_comparator);
```
Observații:
- în prima situație, ordonăm doar prima parte a unui vector, specificând un număr mai mic de elemente
- în cea de-a doua situație, trebuie să avem grijă **să nu ieșim din vector**:
  - vectorul (de fapt pointerul) transmis la `qsort` începe de la jumătatea vectorului inițial
  - asta înseamnă că numărul de elemente nu poate fi mai mare de `n/2`
- atenție la rotunjiri! în exemplul de mai sus, s-a nimerit ca împărțirile să fie exacte
- nu am folosit `sizeof(v) / sizeof(v[0])`, deoarece dacă `v` este deja pointer, prin `sizeof(v)` am obține dimensiunea pointerului

### Căutarea cu [`bsearch`](https://en.cppreference.com/w/c/algorithm/bsearch)
[Înapoi la programe](#programe-discutate)

Pentru completitudine, menționez și funcția `bsearch`, tot din `<stdlib.h>`.

Vom completa primul program din secțiunea anterioară cu următoarele:
```c
void caut(int x, int *v, int n)
{
    int *rez = bsearch(&x, v, n, sizeof(int), cmp);
    if(rez)
        printf("Am gasit %d la adresa %p\n", x, (void*)rez);
    else
        printf("Nu am gasit %d!", x);
}
```
Iar în funcția `main`, **după sortare**:
```c
caut(2, v, n);
caut(6, v, n);
```
Observații:
- vectorul transmis funcției `bsearch` trebuie să fie sortat; în caz contrar, 💥
- funcția comparator trebuie să fie aceeași (sau echivalentă) cu cea cu care am sortat! nu este obligatoriu să sortăm cu `qsort`, însă criteriul de ordonare a elementelor trebuie să fie același; altfel, căutarea eficientă într-un vector sortat folosind un alt criteriu decât cel de la sortare nu are sens
- funcția întoarce un pointer către elementul găsit din vector sau `NULL` dacă elementul căutat nu a fost găsit
- la fel ca la `qsort`, cu toate că funcția se numește `bsearch`, nu este obligatoriu (conform standardului) ca implementarea să folosească un algoritm de căutare binară

### Despre pointerii la funcții
[Înapoi la programe](#programe-discutate)

[Pointerii la funcții](https://en.cppreference.com/w/c/language/pointer#Pointers_to_functions) reprezintă un concept destul de avansat pentru anul I și nu trebuie să vă faceți griji prea mari dacă nu îi înțelegeți (eu i-am înțeles mai bine prin anul 3 sau 4). Dacă îi înțelegeți, felicitări!

**Numele unei funcții se convertește automat la un pointer la acea funcție.**

După cum le spune și numele, pointerii la funcții sunt niște pointeri. Pointeri un pic mai speciali. Ei ne permit să tratăm funcțiile ca pe variabile și să le transmitem ca parametri altor funcții sau să le reținem în vectori. Ulterior, apelăm funcțiile prin intermediul acestor pointeri.

**Cu ce ne ajută asta?**

Dacă avem mai multe funcții care diferă printr-o singură operație, acea operație ar putea fi înlocuită cu un pointer la funcție. Vom avea o singură funcție "mare" căreia îi transmitem ca parametru suplimentar diverși pointeri la funcții.

**De ce am vrea să facem asta?**

În majoritatea cazurilor, dacă avem același cod copiat în mai multe locuri, în momentul în care descoperim un bug, trebuie să reparăm bug-ul în toate locurile unde am copiat codul respectiv. Este destul de probabil ca, din neatenție, să uităm să înlocuim în unul din multele locuri în care am copiat codul.

**Exemplu: afișări**

Un exemplu de situație când sunt utili pointerii la funcții este atunci când dorim să afișăm în mod diferit aceeași informație:
```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void afis_simpla(int *v, int n)
{
    for(int i = 0; i < n; ++i)
        printf("%d ", v[i]);
    printf("\n");
}

void afis_timp(int *v, int n)
{
    printf("\n------------------------------------\n\n");
    time_t t = time(NULL);
    char buf[100];
    if(strftime(buf, sizeof(buf), "[%H:%M:%S %p] ", localtime(&t)))
        printf("%s", buf);
    afis_simpla(v, n);
    printf("\n------------------------------------\n");
}

int main(void)
{
    int v[] = {5, 3, 7, 3, 2, 8, 2, 0, 1, 9, -1, 4};
    int n = sizeof(v) / sizeof(v[0]);

    void (*func_afis)(int*, int);
    func_afis = afis_simpla;
    func_afis(v, n);

    func_afis = afis_timp;
    func_afis(v, n);
    return 0;
}
```
Observații:
- nu era necesar ca funcția `afis_timp` să afișeze funcția `afis_simpla`, putea să facă afișarea și în alt mod
- observați faptul că *apelarea în sine* s-a efectuat în mod identic: `func_afis(v, n);`, dar rezultatul obținut depinde de funcția către care arată `func_afis`
- să înțelegem sintaxa pentru pointeri la funcții, are 3 părți:
  - `void` este tipul de retur al funcției către care va fi pointerul
  - `(*func_afis)`, unde `func_afis` este numele pointerului la funcție, iar parantezele și `*` sunt necesare pentru a putea declara un pointer la funcție
    - fără paranteze, am obține o declarație de funcție!
    - `void *func_afis(int*, int);` ar însemna că declarăm o funcție care întoarce `void*`
  - `(int*, int)` reprezintă tipurile parametrilor funcției

**`typedef`**

Poate fi util să simplificăm codul folosind [`typedef`](https://en.cppreference.com/w/c/language/typedef), mai ales atunci când transmitem pointeri la funcții ca argumente către alte funcții:
```c
typedef void (*afis_pf)(int*, int);
typedef void afis_f(int*, int);

void test0(void (*func)(int*, int))
{
    int x[] = {1, 2, 3};
    func(x, 3);
}

void test1(afis_pf func)
{
    int x[] = {1, 2, 3};
    func(x, 3);
}

void test2(afis_f *func)
{
    int x[] = {1, 2, 3};
    func(x, 3);
}

int main(void)
{
    test0(afis_simpla);
    test0(&afis_simpla);
    test1(afis_simpla);
    test1(&afis_simpla);
    test2(afis_simpla);
    test2(&afis_simpla);
    test0(afis_timp);
    test1(afis_timp);
    test2(afis_timp);
    return 0;
}
```
Observații:
- operatorul `&` este opțional în cazul funcțiilor: întotdeauna are loc o [conversie](https://en.cppreference.com/w/c/language/conversion#Function_to_pointer_conversion) automată de la funcție la pointer la funcție
- `test0` nu se folosește deloc de `typedef`
- putem apela în funcțiile `test` funcția transmisă ca parametru astfel, deși este redundant: `(*func)(x, 3);`
- nu am reușit să aflu dacă `typedef`-ul de la `afis_f` este standard (sintaxă preluată de pe [Wikipedia](https://en.wikipedia.org/wiki/Function_pointer#Alternate_C_and_C++_Syntax))
  - atunci când apare ca parametru la o funcție, aparent este opțional să fie declarat ca pointer: `void test2(afis_f func)` pare să funcționeze la fel de bine
  - totuși, dacă declarăm o variabilă, este obligatoriu să fie pointer: `afis_f *af2 = afis_simpla;`
- echivalent, putem avea `afis_pf af1 = afis_simpla;`
- în schimb, `afis_pf *af11 = &afis_simpla;` este greșit, deoarece `&` nu face nimic asupra funcțiilor
  - `af11` este un pointer la pointer la funcție 😁
  - ce am putea face cu `af11` ar fi asta: `af11 = &af2;`, comportându-se ca un pointer "obișnuit"
  - ca să apelăm funcția, ar trebui neapărat să facem așa: `(*af11)(v, n);`

**Exemplu schițat: preprocesări**

Context: vrem să prelucrăm date din mai multe fișiere, însă acestea sunt salvate în formaturi diferite. Pentru a simplifica și mai mult exemplul, presupunem că au aceeași structură logică (un șir de numere întregi).

După ce facem citirea, prelucrarea este identică. Putem folosi pointerii la funcții pentru a apela funcții diferite de citire pentru fiecare fișier în parte, pe baza extensiei. În aceste situații nu este necesar să ne complicăm cu numerele magice menționate mai demult.
```c
void procesare(char *nume)
{
    char extensie[5];
    strcpy(extensie, nume + strlen(nume) - 4);
    int* (*citire)(char*, int*);
    if(!strcmp(extensie, ".csv"))
        citire = citire_csv;
    else if(!strcmp(extensie, ".xlsx"))
        citire = citire_xlsx;
    else
    {
        printf("Fisierul %s are extensie invalida!", nume);
        return;
    }
    int *date, n;
    date = citire(nume, &n);
    // prelucrare date
}
```
Observații:
- am presupus că există funcțiile `citire_csv` și `citire_xlsx`
- pointerii la funcții ne ajută să abstractizăm anumite aspecte ce țin de detalii de implementare sub o interfață comună
- exemplul este cam forțat, însă pointerii la funcții chiar sunt utili
- ... doar că este dificilă găsirea unui exemplu ușor de înțeles
- ce greșeală cu extensia este în exemplul de mai sus?

**Câteva exemple "clasice"**

O funcție de ordin înalt (high-order function) este o funcție care primește ca parametru o altă funcție (sau care întoarce o funcție).

Un exemplu simplu de **`map`**

Aplicăm o funcție `f` asupra fiecărui element din vector. Atunci când definim `map`, nu este necesar să specificăm ce face funcția `f`, ci doar modul în care e transformat un element (parametrii de intrare și tipul de retur).
```c
int* map(int *v, int n, int (*f)(int)) {
    int *w = malloc(n * sizeof(*v);
    for(int i = 0; i < n; i++)
        w[i] = f(v[i]);
    return w;
}
```

Un exemplu simplu de **`filter`**

După cum îi spune și numele, `filter` filtrează elementele din vector care respectă o anumită condiție.
```c
int* filter(int *v, int n, int *m, bool (*f)(int)) {
    int *w = malloc(n * sizeof(*v);
    int j = 0;
    for(int i = 0; i < n; i++)
        if(f(v[i])
            w[j++] = f(v[i]);
    *m = j;
    // eventual putem realoca la m elemente
    // sau cu realloc de fiecare data cu cate un element
    return w;
}
```

## Exerciții
[Înapoi la cuprins](#cuprins)


## Întrebări, erori, diverse
[Înapoi la cuprins](#cuprins)

* 🚧

## Resurse recomandate
- [cppreference.com](https://en.cppreference.com/w/c)
- [StackOverflow](https://stackoverflow.com/questions/tagged/c?tab=Votes)
- [C FAQ](http://c-faq.com/questions.html)
- [C99 standard](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf) (doar să îl răsfoiți un pic)
