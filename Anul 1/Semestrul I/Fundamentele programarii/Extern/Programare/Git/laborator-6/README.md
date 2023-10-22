# Laboratorul 6

### ⚠ Puneți cât mai multe întrebări! Nu există întrebări greșite.
#### Semnalați orice fel de greșeli găsiți!

# Cuprins
## [Șiruri de caractere](#programe-discutate)
## [Exerciții](#exerciții-1)
## [Întrebări, erori și orice nu a fost acoperit deja](#întrebări-erori-diverse)
## [Resurse recomandate](#resurse-recomandate-1)

## Programe discutate

### [Localizare](#localizare-1)
### [Caractere mici și mari](#caractere-mici-și-mari-1)
### [Clasificarea caracterelor](#clasificarea-caracterelor-1)
### [Despre spații](#despre-spații-1)
### [Conversii](#conversii-1)
### [Modificări](#modificări-1)
### [Examinări](#examinări-1)
### [Unicode și altele](#diverse)

### Localizare

[Localizarea](https://en.wikipedia.org/wiki/Locale_(computer_software)) reprezintă niște parametri care determină comportamentul pentru foarte multe dintre funcțiile de prelucrare a șirurilor de caractere. Concret, aceasta se referă, printre altele, la:
- traducerea unor mesaje într-o anumită limbă
- modul de ordonare al caracterelor ([collation](https://en.wikipedia.org/wiki/Collation))
- formatul în care sunt afișate datele calendaristice
- alegerea separatorului zecimal (punct sau virgulă)

În limbajul C, funcția pentru a afla și a seta localizarea este [`setlocale`](https://en.cppreference.com/w/c/locale/setlocale) (header-ul `<locale.h>`):
- primul argument este un macro pentru [categoria de localizare](https://en.cppreference.com/w/c/locale/LC_categories); pentru toate categoriile, folosim `LC_ALL`
- al doilea argument este șirul de caractere pentru localizare
  - acesta conține limba și/sau setul de caractere/codificarea (depinde de sistemul de operare, compilator, mediu)
  - `NULL` întoarce localizarea curentă fără a modifica nimic
  - `""` întoarce localizarea implicită a sistemului
- întoarce localizarea curentă sub forma unui șir de caractere: cea existentă, cea setată sau `NULL` în caz de eroare
  - nu avem voie să modificăm șirul de caractere primit! 💥
  - putem să folosim șirul de caractere primit ca parametru pentru un apel ulterior la `setlocale`, de exemplu pentru a seta la loc valoarea inițială
- o problemă pe care o au funcțiile de localizare din limbajul C o reprezintă utilizarea unei stări globale!
  - astfel, sunt foarte dificil de scris și utilizat programe care doresc să folosească mai multe localizări, mai ales în programe care folosesc multiple fire de execuție (multi-threading)
  - deși probabil nu veți avea de-a face cu localizare în limbajul C, este bine să cunoașteți aceste aspecte, deoarece ele sunt valabile într-o oarecare măsură în multe alte contexte

Localizarea implicită a programului este `"C"` și reprezintă o localizare minimală. De obicei, caracterele sunt codificate cu coduri ASCII, iar în aceste situații, caracterele corespunzătoare valorilor 0-127 ar trebui să fie aceleași în toate programele. Nu ne putem baza pe ce reprezintă valorile 128-255.

Categoriile de localizare:
- `LC_COLLATE` determină ordinea caracterelor: în codificarea implicită (`"C"`), ordinea este determinată de codurile ASCII
  - astfel, `a` este mai "mare" decât `A` în localizarea `"C"`, însă poate fi mai "mic" din punctul de vedere al omului
  - acest aspect este foarte relevant, deoarece puteți obține rezultate neintuitive atunci când aveți de ordonat diverse date
  - detalii în secțiunea următoare
- `LC_CTYPE` determină modul de clasificare al caracterelor: vedeți următoarele 3 secțiuni din laborator
- `LC_MONETARY` determină șirul de caractere afișat ca monedă
- `LC_NUMERIC` determină caracterul folosit pentru separatorul zecimal
- `LC_TIME` determină modul de afișare a datei și timpului

```c
#include <stdio.h>
#include <locale.h>
#include <time.h>

void detalii_loc(void)
{
    struct lconv *loc = localeconv();

    printf("Simbol moneda: %s\n", loc->currency_symbol);
    printf("Abreviere moneda: %s\n", loc->int_curr_symbol);
    printf("Separator zecimal: %s\n", loc->decimal_point);
    printf("Separator pentru mii: %s\n", loc->thousands_sep);

    time_t t = time(NULL);
    char buf[100];
    if(strftime(buf, sizeof(buf), "%A %c", localtime(&t)))
        printf("Timp local: %s\n", buf);
    else
        puts("Eroare afisare data/timp");
}

int main(void)
{
    printf("Localizarea initiala este %s\n", setlocale(LC_ALL, NULL));
    detalii_loc();

    printf("Localizarea implicita a sistemului este %s\n", setlocale(LC_ALL, ""));
    detalii_loc();

    puts(setlocale(LC_MONETARY, "American"));
    // sau "en_US.iso88591" in loc de "American"
    detalii_loc();

    puts(setlocale(LC_ALL, "Romanian"));
    //puts(setlocale(LC_ALL, "ro_RO.iso88592"));
    detalii_loc();
    return 0;
}
```
Observații:
- este dificil de obținut un cod portabil
- ca al doilea argument la `setlocale`, pentru codificări pe un singur byte avem:
  - pe sistemele Windows, codificările 125x (code pages): implicit, ar trebui să fie 1252; pentru română, avem 1250 (din terminal, `chcp 1250`); acestea corespund (oarecum) standardelor ISO/IEC 8859-1 și ISO/IEC 8859-2
  - pe sistemele Unix, ar trebui să transmitem limba și regiunea, urmată de `.` și de standardul ISO: vedeți comentariile
- în cazul UTF-8, ar trebui să putem folosi același șir de caractere indiferent de sistemul de operare
  - totuși, pe Windows, terminalul nu are fonturi disponibile pentru a afișa orice caractere din UTF-8
- trebuie să avem instalate localizările respective pentru ca programul să afișeze ceva în mod diferit
- am afișat ce întoarce `setlocale` pentru a verifica dacă argumentul al doilea este valid
- funcția [`localeconv`](https://en.cppreference.com/w/c/locale/localeconv) ne întoarce o structură de tip [`lconv`](https://en.cppreference.com/w/c/locale/lconv), cu ajutorul căreia putem folosi diverse elemente specifice unei localizări
- funcția [`strftime`](https://en.cppreference.com/w/c/chrono/strftime) transformă structura de tip `struct tm` întoarsă de [`localtime`](https://en.cppreference.com/w/c/chrono/localtime) într-un șir de caractere

### Caractere mici și mari
[Înapoi la programe](#programe-discutate)

Pentru a determina dacă un caracter single-byte este mic sau mare, putem folosi funcțiile [`islower`](https://en.cppreference.com/w/c/string/byte/islower) și [`isupper`](https://en.cppreference.com/w/c/string/byte/isupper) (`<ctype.h>`). Parametrul trebuie să poată fi reprezentat ca un `unsigned char`. Valoarea returnată este zero dacă condiția nu este îndeplinită.

Dacă un caracter este o literă mică, acesta poate fi convertit la o literă mare folosind funcția [`toupper`](https://en.cppreference.com/w/c/string/byte/toupper); similar, există funcția [`tolower`](https://en.cppreference.com/w/c/string/byte/tolower). Dacă acel caracter nu este literă mare sau mică, se returnează nemodificat caracterul primit ca parametru.

Cu localizarea `"C"`, numai `abcdefghijklmnopqrstuvwxyz` sunt considerate litere mici și numai `ABCDEFGHIJKLMNOPQRSTUVWXYZ` sunt considerate litere mari. Alte localizări pot defini și alte caractere ca fiind litere mici sau mari.

De exemplu, litera `ă` nu este nici literă mică, nici literă mare în localizarea `"C"`. Desigur, este ambiguu și ce înțelegem prin litera `ă`, deoarece are reprezentări diferite: în codificarea ISO 8859-2 este reprezentată printr-un singur byte, iar în UTF-8 este reprezentată prin 2 bytes.
```c
#include <stdio.h>
#include <ctype.h>
#include <wctype.h>
#include <locale.h>

void lower_upper(unsigned char c)
{
    printf("islower(%c) (%#x): %d\n", c, c, islower(c));
    printf("isupper(%c) (%#x): %d\n", c, c, isupper(c));
    unsigned char conv;
    if(islower(c))
        conv = toupper(c);
    else if(isupper(c))
        conv = tolower(c);
    else
        return;
    printf("islower(%c) (%#x): %d\n", conv, conv, islower(conv));
    printf("isupper(%c) (%#x): %d\n", conv, conv, isupper(conv));

    unsigned char conv2;
    if(islower(conv))
        conv2 = toupper(conv);
    else
        conv2 = tolower(conv);
    printf("conv_back(%c): %c\n", conv, conv2);
}

int main(void)
{
    unsigned char c = '\xc3';
    lower_upper(c);
    puts(setlocale(LC_ALL, "romanian_Romania.1250"));
    lower_upper(c);
    lower_upper('\xaa');
    wchar_t wc = L'î';
    wprintf(L"mic? %d\nmare? %d\nwupper: %c\nwlower: %c\n", iswlower(wc), iswupper(wc), towupper(wc), towlower(wc));
    return 0;
}

```
Observații:
- caracterul `'\xc3'` corespunde caracterului `'Ă'` în codificarea ISO 8859-2 sau Windows-1250
- caracterul `ă` (`'\xe3'`) poate fi introdus direct în codul sursă doar dacă salvăm fișierul cu encoding-ul ISO 8859-2 sau Windows-1250; implicit, salvarea fișierelor se face cu codificarea UTF-8! dacă folosiți un sistem de operare mai vechi, aceasta este posibil să fie ISO 8859-1 sau Windows-1252
  - trebuie să faceți distincția între codificarea fișierului sursă și codificarea utilizată în program
- în cazul în care nu era deja evident, în codificarea ASCII nu putem avea decât valori între 0 și 127
- dacă scriem caracterul `ă` direct în sursă și salvăm fișierul cu codificarea UTF-8, atunci acesta va fi reprezentat prin 2 bytes: `'\xc4'` și `'\x83'`; totuși, dacă facem asta, `'ă'` nu mai este un caracter pe un singur byte, ci este un caracter multi-byte
  - sesizați problema? 🤔
  - funcțiile `isupper`/`islower` primesc ca argument un `unsigned char`!
  - asta înseamnă că nu putem determina dacă acest caracter este mic sau mare
  - în acest scop, există caractere multi-byte și șiruri de caractere "late"
  - `wprintf(L"%c", towupper(L'ă'));`
    - trebuie incluse headere speciale (`<wchar.h>`, eventual `<wctype.h>`)
    - `L` în fața unui caracter literal `char`/șir de caractere literal `char*` îl transformă în literal "lat"
    - acestea corespund codificărilor folosite mai demult (ex: UTF-16), mai ales pe Windows
    - nu funcționează cu `ș` și `ț`!
    - `'\xaa'` este `ș` cu sedilă!
- totuși, din experimentele mele, nu am reușit să obțin ceva suficient de util cu caracterele "late", întrucât variantele "late" ale funcțiilor de prelucrare a fișierelor din biblioteca C standard nu par să funcționeze corect cu MinGW, ceea ce le face cam inutile
- ele există mai mult din motive istorice
- soluția:
  - pentru operații simple, mai bine ne implementăm noi funcționalitățile de care avem nevoie
  - pentru operații complicate, căutăm biblioteci specializate
  - funcțiile din biblioteca C standard sunt **inutile** pentru situații în care nu vrem să ne limităm la ASCII, adică în orice situație practică, dar probabil nu vă veți lovi de aceste probleme în timpul facultății
  - excepție: inevitabil, avem nevoie în aplicații care au fost făcute mai demult cu aceste concepte oribile

Alte observații:
- în codificările pe un singur byte, **nu avem caracterele `ș` și `ț`**, deoarece indivizii de la Unicode (inainte de 1999) și cei de la ISO/IEC care s-au ocupat de standardizări au considerat că pot fi folosite caracterele cu sedilă `ş` și `ţ`; au presupus că diferența este insesizabilă pe ecrane cu rezoluție mică și că cei care furnizează fonturile ar trebui să facă afișările în mod diferit, ceea ce nu s-a întâmplat în realitate
- astfel, pentru a putea folosi caracterele `ș` și `ț` (și variantele lor `Ș` și `Ț`), ar trebui să folosim codificarea UTF-8

### Clasificarea caracterelor
[Înapoi la programe](#programe-discutate)

În header-ul `<ctype.h>` avem o multitudine de funcții pentru clasificarea caracterelor după diverse criterii. Am văzut două dintre acestea în secțiunea precedentă. Menționez încă o dată că localizarea influențează comportamentul acestor funcții. În contextul UTF-8, trebuie folosite funcții echivalente din biblioteci specializate.

```c
#include <stdio.h>
#include <ctype.h>
#include <locale.h>

void afis_clasificare(void)
{
    for (int ndx=0; ndx<=255; ndx++)
    {
        printf("%c %d (0x%02x):\t", ndx, ndx, ndx);
        if(isalnum(ndx)) printf("alnum\t");
        if(isalpha(ndx)) printf("alpha\t");
        if(islower(ndx)) printf("lower\t");
        if(isupper(ndx)) printf("upper\t");
        if(isdigit(ndx)) printf("digit\t");
        if(isxdigit(ndx)) printf("xdigit\t");
        if(iscntrl(ndx)) printf("cntrl\t");
        if(isgraph(ndx)) printf("graph\t");
        if(isspace(ndx)) printf("space\t");
        if(isblank(ndx)) printf("blank\t");
        if(isprint(ndx)) printf("print\t");
        if(ispunct(ndx)) printf("punct");
        printf("\n");
    }
}

int main(void)
{
    afis_clasificare();
    puts(setlocale(LC_ALL, "romanian_Romania.1250"));
    afis_clasificare();
    return 0;
}
```
Observații:
- pentru codificarea ASCII (localizarea `"C"`), nu există caractere cu valori după 127, motiv pentru care nu se afișează nimic
- funcția `isblank` este introdusă în standardul C99
- puteți citi [documentația](https://en.cppreference.com/w/c/string/byte#Character_classification) atunci când aveți nevoie de ceva specific
- în mod curios, caracterul `µ` (`'\xb5'`) în localizarea de mai sus este și caracter alfabetic, și semn de punctuație
- tot în localizarea de mai sus, caracterul tab `'\t'` (`'\x09'`) este considerat caracter printabil, dar în localizarea `"C"` nu

### Despre spații
[Înapoi la programe](#programe-discutate)

Am menționat în secțiunea precedentă funcțiile din biblioteca C standard care ne pot ajuta să detectăm caractere albe (whitespace). Totuși, acestea funcționează doar pentru caractere ASCII! În Unicode, există mult mai multe caractere pentru spații: vedeți lista [aici](https://en.wikipedia.org/wiki/Whitespace_character#Unicode).

În mod neașteptat, funcția [`iswspace`](https://en.cppreference.com/w/c/string/wide/iswspace) pare să funcționeze corect. Cu toate acestea, există unele caractere "dubioase" care nu sunt considerate de Unicode ca fiind caractere albe, consecința fiind că nu sunt considerate spații nici de funcția `iswspace`. Probabil cel mai întâlnit astfel de caracter este [ZWJ (zero-width joiner)](https://en.wikipedia.org/wiki/Zero-width_joiner), utilizat pentru combinarea a două caractere pentru a le afișa în mod diferit.

Câteva utilizări:
- combinarea a două emoji-uri (emoji-urile pot fi considerate caractere pe 4 bytes)
- combinarea unor caractere în unele limbi
- trimiterea de mesaje goale
- formatarea tabelelor Markdown pe GitHub

Partea mai puțin fericită este că aceste caractere albe pot cauza multe dificultăți în validarea datelor. Nu trebuie să vă preocupe rezolvarea acestor probleme acum, ci doar să știți ce să căutați când veți avea nevoie de asta.

### Conversii
[Înapoi la programe](#programe-discutate)

Până acum, am făcut conversii de la numere la șiruri de caractere folosind funcțiile `printf` și `fprintf`. Similar cu `fprintf`, există și funcția [`snprintf`](https://en.cppreference.com/w/c/io/fprintf) (C99), care primește un buffer de tip `char*` în loc de `FILE*` ca prim argument. Acel buffer trebuie alocat anterior.

🚮 **Evitați** funcția `sprintf`, deoarece este la fel de periculoasă ca `gets`, întrucât există pericol de buffer overflow. Ca fapt divers, funcția `itoa` nu este standard 👽, cu toate că `atoi` este funcție standard.
```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char buf[100];
    snprintf(buf, sizeof(buf), "%d %f ~$> |\n\n%c\t%.3f ?!", -10, 1.23, 'a', 543.21251);
    puts(buf);

    char *buf2;
    int len;
    len = snprintf(NULL, 0, "%d %f ~$> |\n\n%c\t%.3f ?!", -10, 1.23, 'a', 543.21251);
    buf2 = malloc(sizeof(*buf2) * (len + 1));
    snprintf(buf2, len + 1, "%d %f ~$> |\n\n%c\t%.3f ?!", -10, 1.23, 'a', 543.21251);
    puts(buf2);
    free(buf2);
    return 0;
}
```
Observații:
- toți specificatorii de format sunt aceiași ca în cazul funcțiilor `printf`/`fprintf`
- există un truc pentru a afla dimensiunea buffer-ului, apelând întâi `snprintf` cu `NULL` și `0`
- desigur, am putea să verificăm și celelalte valori de retur ale `snprintf`
- funcția nestandard `itoa` avea și parametru pentru bază, însă putem să ne implementăm noi această funcționalitate sau să preluăm o implementare existentă dacă avem nevoie de conversii în baze arbitrare
- în unele situații, convertirea multor numere în șiruri de caractere poate fi costisitoare, caz în care vom folosi biblioteci specializate

<!-- https://github.com/jeaiii/itoa -->
<!-- https://github.com/fmtlib/fmt -->

În sens invers, dorim să convertim un șir de caractere la un număr întreg sau real. Toate funcțiile cu `long long` sunt introduse în C99.

Pe de o parte, avem funcțiile `atof` și `atoi`/`atol`/`atoll`. `a` vine de la alfabetic, `f` de la `float`, `i` de la `integer`, `l` de la `long`, `ll` de la `long long`. Deși aceste funcții fac ce trebuie atunci când șirul de caractere dat ca parametru conține date valide, ele întorc valoarea `0.0` sau `0` în caz de eroare, ceea ce nu este deloc util, din moment ce nu putem ști în acea situație dacă am dat de o eroare sau nu. Singurul lor avantaj este că sunt mai ușor de folosit.

Pe de altă parte, avem funcțiile [`strtol`/`strtoll`](https://en.cppreference.com/w/c/string/byte/strtol), [`strtoul`/`strtoull`](https://en.cppreference.com/w/c/string/byte/strtoul) și [`strtof` (C99)/`strtod`/`strtold` (C99)](https://en.cppreference.com/w/c/string/byte/strtof). Acestea ne furnizează un mecanism de detecție a erorilor de conversie:
- `strtol` & co setează variabila specială `errno` (`<errno.h>`) la `ERANGE` în caz de eroare de interval (overflow sau underflow)
  - dacă nu a putut fi efectuată vreo conversie, dar nici nu avem eroare de interval, se va întoarce 0: pentru a determina dacă acest `0` este rezultatul unei conversii sau al unei erori, vom folosi un argument suplimentar care ne va spune poziția din șirul de caractere la care s-a ajuns
    - dacă pointer-ul rezultat este diferit de cel trimis ca parametru, conversia a avut succes
    - dacă pointer-ul rezultat este identic cu cel trimis ca parmetru, avem eroare
  - spre deosebire de `atoi`, putem specifica baza de conversie
- `strtod` & co întorc niște [valori speciale](https://en.cppreference.com/w/c/numeric/math/HUGE_VAL) în caz de eroare de interval: putem compara cu aceste valori pentru a detecta astfel de erori
  - pentru alte tipuri de erori, folosim același procedeu descris mai sus cu argumentul suplimentar

Ca fapt divers, am putea folosi funcția `sscanf`, însă aceasta poate fi [mai lentă](https://stackoverflow.com/questions/22865622/atoi-vs-atol-vs-strtol-vs-strtoul-vs-sscanf).

```c
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <inttypes.h>
#include <math.h>

int main(void)
{
    char sir[] = "123 456.76 0 eroare";
    long nr1; long long nr2; int nr3, nr4;
    nr1 = atol(sir);
    nr2 = atoll(sir + 4);
    nr3 = atoi(sir + 11);
    nr4 = atoi(sir + 13);
    printf("%ld\t%s\n%"PRId64"\t%s\n%d\t%s\n%d\t%s\n", nr1, sir, nr2, sir+4, nr3, sir+11, nr4, sir+13);

    char *ptr, *sf;
    ptr = sir;
    errno = 0;
    nr1 = strtol(ptr, &sf, 0);
    if(ptr == sf)
    {
        printf("Eroare la conversie: `%s`\n", ptr);
        return 1;
    }
    if(errno == ERANGE)
    {
        perror("eroare la conversie");
        return 1;
    }
    if(errno)
    {
        perror("alta eroare la strtol");
        return 1;
    }
    printf("Citit %ld; sirul ramas: `%s`\n", nr1, ptr);
    double nrf;

    do
    {
        ptr = sf;
        errno = 0;
        nrf = strtod(ptr, &sf);
        if(ptr == sf)
        {
            printf("Eroare la conversie: `%s`\n", ptr);
            break;
        }
        if(errno == ERANGE) // sau if(nrf == HUGE_VAL)
        {
            perror("eroare la conversie");
            break;
        }
        printf("Citit %f; sirul ramas: `%s`\n", nrf, ptr);
    } while(ptr != sf);
    return 0;
}
```
Observații:
- `strtol` întoarce `long`, nu `int`; trebuie verificat pe implementare dacă `sizeof(int) == sizeof(long)`
- deși funcțiile `atoi` & co sunt mai ușor de folosit, este imposibil să distingem între un `0` corect și un `0` provenit dintr-o eroare de citire
- codul cu `strtol` este mai complex, însă știm cu siguranță când avem erori de conversie
- pentru siguranță, este bine ca de fiecare dată să setăm `errno` la 0 înainte de funcții care îl modifică, pentru a avea garanția că verificăm ce trebuie
- am preferat să verificăm `errno` și nu să comparăm cu `HUGE_VAL`, deoarece acel macro este valabil doar pentru tipuri de date `double`; pentru alte tipuri de date trebuie folosite alte constante, însă verificarea valorii `errno` este la fel și pentru `float`, și pentru `double`, și pentru `long double`

### Modificări
[Înapoi la programe](#programe-discutate)

Reluăm din laboratorul 3: ce înseamnă un șir de caractere?

În limbajul C, un șir de caractere este un vector de caractere, unde ultimul caracter este `'\0'`, numit terminator de șir. Putem aloca un vector mai mare decât dimensiunea șirului de caractere, însă funcțiile care prelucrează șiruri de caractere se opresc la `'\0'`. Astfel, este **obligatoriu** ca șirurile de caractere să aibă terminator de șir. În caz contrar, avem comportament nedefinit 💥, deoarece sunt accesate zone invalide de memorie.

```c
char sir1[] = "asd";  // echivalent cu char sir1[4] = {'a', 's', 'd', '\0'};
char *sir2 = "asd";  // NU este complet echivalent cu randul de mai sus, deoarece sir2 este un pointer
// sir2[1] = 'b';   // comportament nedefinit! nu avem voie sa modificam un literal
                   // dar putem face atribuirea urmatoare
sir2 = sir1;      // deoarece facem ca pointerul sir2 sa arate catre altceva!
```

Ce știm despre vectori și pointeri?

Numele unui vector reprezintă un pointer constant către adresa de început a vectorului. De ce este important acel "constant"? Deoarece nu putem copia vectori element cu element folosind atribuirea obișnuită.

```c
char vec1[10] = "qwertyuio";
char vec2[10] = "asdfghjkl";
// vec1 = vec2;  // eroare la compilare!
```

De ce nu putem copia vectori pur și simplu?

Un vector este transformat într-un pointer imediat ce apare într-o expresie. De ce se întâmplă asta?

Pentru că limbajul este destul de vechi și lucrurile se pot complica foarte mult dacă copierea vectorilor ar fi posibilă în mod direct: dacă elementele vectorului sunt la rândul lor vectori, și ele trebuie copiate element cu element și tot așa. Plus că ar trebui verificat că au aceeași dimensiune. Mai mult, limbajul C a evoluat din limbajul B, iar unele anomalii sau chichițe provin din nevoia de a păstra compatibilitatea cu programe scrise în B (a se citi înainte de 1970).

<details>
  <summary>Arheologie</summary>

  Dacă vreți să mergeți direct la sursă, găsim detalii <a href=https://www.bell-labs.com/usr/dmr/www/chist.html>aici</a>:
  <blockquote cite="https://www.bell-labs.com/usr/dmr/www/chist.html">
    <p>The solution constituted the crucial jump in the evolutionary chain between typeless BCPL and typed C. It eliminated the materialization of the pointer in storage, and instead caused the creation of the pointer when the array name is mentioned in an expression. The rule, which survives in today's C, is that values of array type are converted, when they appear in expressions, into pointers to the first of the objects making up the array.
      <br><br>
      This invention enabled most existing B code to continue to work, despite the underlying shift in the language's semantics.</p>
    <br>
    -- Dennis M. Ritchie, History of C
  </blockquote>

  Alte detalii puteți citi <a href=https://stackoverflow.com/questions/35597019/cs-aversion-to-arrays/35598701#35598701>aici</a> și <a href=https://stackoverflow.com/questions/3437110/why-do-c-and-c-support-memberwise-assignment-of-arrays-within-structs-but-not>aici</a>. Structurile au fost adăugate ulterior. Un <a href=https://stackoverflow.com/questions/6966570/why-declare-a-struct-that-only-contains-an-array-in-c>truc</a> pentru a copia vectori ar fi să le "ascundem" în niște structuri, însă de obicei nu vrem să facem asta dacă vectorii au multe elemente.
</details>

Revenind... Putem copia pointerii, dar copierea se face prin valoare, ceea ce înseamnă că se copiază adresa dintr-un pointer în alt pointer. Atunci când avem nevoie de o copie, vrem ca această copiere să se realizeze element cu element, nu să copiem adrese.

```c
char sir[] = "teste";
char *p = sir;
p[0] = 'p';
printf("Sirul initial: %s\nSirul p:\n", sir, p);
```

În codul de mai sus nu are loc decât o copiere de pointeri. Modificând șirul prin `p` se modifică și șirul inițial.

Am putea folosi o instrucțiune repetitivă, însă există funcții predefinite care îndeplinesc acest scop: [`strcpy`](https://en.cppreference.com/w/c/string/byte/strcpy) și[`strncpy`](https://en.cppreference.com/w/c/string/byte/strncpy) (`<string.h>`):
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char *nume = "Mega Byte", *nume2 = "Vitamina C", *nume3 = "main.c";
    char copie[20];
    strcpy(copie, nume);
    copie[2] = 't';
    printf("Sirul initial: %s\nCopia: %s\n", nume, copie);
    strncpy(copie, nume2 + 4, 4);
    copie[0] = 'v';
    //copie[4] = '\0';
    printf("Sirul initial: %s\nCopia: %s\n", nume2, copie);
    strncpy(copie, nume3, 15);
    copie[0] = 'r';
    printf("Sirul initial: %s\nCopia: %s\n", nume3, copie);
    return 0;
}
```
Observăm că `strncpy` nu pune `'\0'` dacă nu copiază tot șirul! Cel mai sigur este să punem de fiecare dată `'\0'` pe poziția `nr`, pentru că nu este greșit să scriem din nou această valoare; prin `nr` mă refer la ultimul parametru de la `strncpy`.

Alte observații:
- ar trebui să fie ușor să reținem ordinea argumentelor, deoarece este aceeași ca la atribuirea obișnuită: `destinatie = sursa;`
- șirul sursă și șirul destinație **nu au voie să se suprapună** 💥: construcțiile întâlnite în liceu de forma `strcpy(s, s + 1)` pentru a șterge caractere dintr-un șir sunt **complet greșite**
- șirul sursă trebuie să aibă terminator de șir! altfel, 💥
  - excepție în cazul `strncpy` dacă se copiază mai puține caractere decât dimensiunea sursei, deși putem determina dimensiunea sursei dacă aceasta nu are `'\0'` numai în cazul în care este un vector
  - totuși, mult mai sigur și sănătos este să avem `'\0'`
- șirul destinație trebuie să aibă alocat suficient spațiu! trebuie să fie cel puțin `nr`! în caz contrar, 💥
- dacă `nr` este mai mare decât `strlen(sursa)`, atunci restul de octeți (până sunt scriși `nr` octeți) din destinație sunt completați cu `'\0'` (ultima copie din exemplul de mai sus)

O altă operație destul de comună cu șirurile de caractere este concatenarea: avem [`strcat`](https://en.cppreference.com/w/c/string/byte/strcat) și [`strncat`](https://en.cppreference.com/w/c/string/byte/strncat).
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char *sufix = "t", *sufix2 = "-am";
    char destinatie[20] = "trecu";
    strcat(destinatie, sufix);
    printf("Destinatie: %s\nSursa: %s\n", destinatie, sufix);
    strncat(destinatie, sufix2, 2);
    printf("Destinatie: %s\nSursa: %s\n", destinatie, sufix2);
    //strncat(destinatie, sufix2, 20);  // nu concateneaza mai mult de lungimea lui sufix2, desi am specificat 20
    //printf("Destinatie: %s\nSursa: %s\n", destinatie, sufix2); // am comentat doar pt ca trecut-a-am nu are sens
    return 0;
}
```
Observații:
- ambele funcții adaugă `'\0'` la final <!-- (e greșit în curs, citiți documentația) -->
- `strncat` scrie cel mult `nr + 1` caractere, deoarece adaugă `'\0'`! se oprește când dă de `'\0'` în șirul sursă
- dacă nu avem alocat suficient spațiu în șirul destinație, 💥
- și sursa, și destinația trebuie să aibă terminator de șir! altfel, 💥
- șirurile sursă și destinație nu au voie să se suprapună! 💥

### Examinări
[Înapoi la programe](#programe-discutate)

Am menționat o primă funcție de examinare a șirurilor de caractere în secțiunea anterioară: [`strlen`](https://en.cppreference.com/w/c/string/byte/strlen). Foarte important: am mai spus, dar repet că șirurile de caractere **trebuie să conțină terminatorul de șir**. De ce? Deoarece toate funcțiile care prelucrează șiruri de caractere se bazează pe asta. Fără acest caracter, avem comportament nedefinit 💥, deoarece se va umbla prin memorie până se va găsi un byte care să fie 0.

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char sir1[] = "test";
    char *sir2 = "test";
    printf("strlen: %zu, sizeof: %zu\n", strlen(sir1), sizeof(sir1));
    printf("strlen: %zu, sizeof: %zu\n", strlen(sir2), sizeof(sir2));
    return 0;
}
```
Observații:
- `strlen` întoarce lungimea șirului, **fără** `'\0'`
- deși au aceeași lungime (aflată cu `strlen`), `sir1` și `sir2` nu au același `sizeof`, deoarece `sir2` este un simplu pointer
- `sizeof` este determinat întotdeauna la compilare și nu evaluează argumentele (singura excepție: VLA - nu e cazul aici)

Căutarea unui caracter într-un șir de caractere o facem cu [`strchr`](https://en.cppreference.com/w/c/string/byte/strchr) sau [`strrchr`](https://en.cppreference.com/w/c/string/byte/strrchr). Căutarea unui subșir o facem cu [`strstr`](https://en.cppreference.com/w/c/string/byte/strstr):
```c
#include <stdio.h>
#include <string.h>

void caut(char *sir, char ch)
{
    char *p;
    p = strchr(sir, ch);
    if(p != NULL)
        printf("strchr(%s, %c): %s\n", sir, ch, p);
    else
        printf("Nu am gasit %c in %s!\n", ch, sir);
}

int main(void)
{
    char sir[] = "unde o fi acul in caru' cu fn?";
    char c1 = 'a', c2 = 'l', c3 = 'A';
    caut(sir, c1);
    caut(sir, c3);
    
    char *p;
    p = strrchr(sir, c2);
    if(p != NULL)
        printf("strrchr(%s, %c): %s\n", sir, c2, p);
    else
        printf("Nu am gasit %c in %s!\n", c2, sir);
    
    char *acul = "acul";
    if((p = strstr(sir, acul)) != NULL)
        printf("Am gasit acul in carul cu fn la pozitia %td!\n%s\n", p - sir, p);
    else
        printf("Nu am gasit subsirul!\n");
    return 0;
}
```
Observații:
- putem căuta și după `'\0'`
- în caz de succes, este util să primim un pointer la caracterul găsit, deoarece putem continua cu alte operații de prelucrare de la poziția respectivă; majoritatea funcțiilor de prelucrare a șirurilor de caractere întorc un astfel de pointer
- diferența dintre doi pointeri este de tip [`ptrdiff_t`](https://en.cppreference.com/w/c/types/ptrdiff_t) și se afișează cu `%td` sau `%tu`

În curs este prezentată funcția `strtok` și vine de la "string tokenization". Tokenizarea este procesul de împărțire a unui șir de caractere în tokeni (token-uri?).

Un exemplu din limbaje naturale este împărțirea unui text în cuvinte sau în silabe (depinde la ce nivel este realizată tokenizarea). Cuvintele (sau silabele) astfel obținute se numesc tokeni. Un mod uzual de tokenizare este după spații și semne de punctuație.

Paranteză: pentru unele limbaje naturale nu funcționează această abordare, un exemplu fiind limba chineză.

Un alt exemplu este împărțirea unui cod sursă în identificatori, operatori și așa mai departe, toți aceștia fiind numiți la modul general tokeni în acest context. Acesta este motivul pentru care majoritatea limbajelor de programare ignoră de obicei spațiile, acestea fiind utile doar pentru a simplifica procesul de tokenizare. Spre deosebire de limbajele naturale, limbajele de programare (submulțime a limbajelor formale) pot fi procesate fără a avea ambiguități.

#### Un exemplu concret

Vrem să împărțim șirul de caractere "Astazi este o zi minunata; daca maine ploua, imi iau umbrela (maine). Dar daca e soare?" în cuvintele: `Astazi`, `este`, `o`, `zi`, `minunata` etc.

Ca separatori, vom folosi spații și semne de punctuație: vom folosi șirul ` ;,().?!`.

Nu voi folosi funcția `strtok` deoarece a fost deja prezentată în curs și prezintă mai multe dezavantaje:
- folosește o variabilă statică (declarată cu `static`) pentru a reține starea curentă a șirului prelucrat
  - consecința este că nu poate fi folosită în programe multi-threading!
- distruge șirul de caractere de intrare primit ca parametru
  - pentru a evita acest lucru, ar trebui să facem prelucrarea pe o copie, ceea ce consumă resurse!

Exemplul este adaptat din cel din documentația pentru [`strpbrk`](https://en.cppreference.com/w/c/string/byte/strpbrk) ("string pointer break"):
```c
#include <stdio.h>
#include <string.h>
 
int main(void)
{
    const char* str = "hello world, friend of mine!";
    const char* sep = " ,!";
 
    unsigned int cnt = 0;
    do {
        const char *str0 = str;
        str = strpbrk(str, sep); // find separator
        if(str == NULL)
            break;

        char word[50];
        strncpy(word, str0, str - str0);
        word[str - str0] = '\0';

        if(strlen(word))
            printf("%s\n", word);
        else
            --cnt;  // word is an empty word

        if(str) str += strspn(str, sep); // skip separator
        ++cnt; // increment word count
    } while(str && *str);
 
    printf("There are %u words\n", cnt);
}
```
Observații:
- funcția `strpbrk` ne întoarce poziția în șir a primului separator din lista de separatori
- funcția [`strspn`](https://en.cppreference.com/w/c/string/byte/strspn) sare peste toți separatorii întâlniți, până ajunge la începutul următorului cuvânt
  - se avansează un pointer cât timp caracterul curent face parte din lista de separatori
  - funcția ne întoarce numărul de caractere care separă cuvintele
- folosim variabila `str0` pentru a reține poziția anterioară din șirul inițial: aceasta va arăta spre începutul unui cuvânt
- împreună cu ce ne întoarce `strpbrk`, facem diferența și obținem lungimea cuvântului
- ce putem face acum? copiem cuvântul cu `strncpy` într-un vector temporar
  - presupunem că nu există cuvinte mai mari de 50 de caractere (dacă e cazul, putem aloca dinamic)
    - ... cu toate că [în unele limbi](https://en.wikipedia.org/wiki/Longest_words) se pot forma cuvinte de lungime arbitrară
  - nu e frumos ce am făcut pentru că am hardcodat constanta (`50`) pentru a simplifica exemplul; voi să nu faceți așa :smile:
- punem `'\0'` la sfârșit, deoarece nu ne putem baza pe `strncpy` pentru asta
- decrementăm numărul de cuvinte dacă lungimea cuvântului este 0: putem întâlni această situație dacă șirul nu începe cu un cuvânt
- ne oprim dacă am ajuns la sfârșitul șirului sau dacă `strpbrk` nu mai găsește nimic, caz în care întoarce `NULL`
- altă funcție de căutare pe care puteți să o încercați este [`strcspn`](https://en.cppreference.com/w/c/string/byte/strcspn); nu vă dau spoilere

Pentru un ultim exemplu, vom compara două șiruri de caractere folosind funcția [`strcmp`](https://en.cppreference.com/w/c/string/byte/strcmp).

Această funcție **nu** este influențată de localizare (\*) și compară două șiruri de caractere lexicografic, adică literă cu literă (sau caracter cu caracter), pe baza codurilor ASCII (asta se întâmplă cu localizarea implicită `"C"`), de la stânga la dreapta. Aceste comparații au loc cât timp literele sunt egale. Ca o analogie, puteți să vă gândiți că e ca ordinea din dicționar, însă este generalizată, deoarece putem compara și cifre sau semne de punctuație.

`strcmp` întoarce:
- o valoare negativă, dacă primul șir este mai mic din punct de vedere lexicografic decât al doilea șir
- zero, dacă șirurile au toate caracterele egale
- o valoare pozitivă, dacă primul șir este mai mare din punct de vedere lexicografic decât al doilea șir

Similar cu alte funcții prezentate anterior, există și funcția [`strncmp`](https://en.cppreference.com/w/c/string/byte/strncmp) care scanează cel mult `nr` caractere din fiecare șir. Această funcție are aceleași convenții pentru valorile de retur ca `strcmp`, comparând (cel mult) primele `nr` caractere.

În unele situații (nu în cele întâlnite în facultate), ordinea lexicografică folosind codurile ASCII poate să fie "ciudată": caracterul `c` este mai mare decât caracterul `C`. Utilizarea unei alte localizări decât cea implicită (`"C"`) poate să afecteze modul de ordonare al caracterelor, însă este necesară utilizarea altor funcții: `strcoll` (de la "string collation") și `strxfrm` (de la ??? habar nu am, nu am găsit; probabil "x-form" sau "x-transform", cu `x` pentru "orice").

```c
#include <stdio.h>
#include <string.h>
#include <locale.h>

void afis(const char *locale)
{
    const char* s1 = "notă mică👎";
    const char* s2 = "👍notă MARE";

    printf("In the %s locale: ", locale);
    if(strcoll(s1, s2) < 0)
        printf("%s before %s\n", s1, s2);
    else
        printf("%s before %s\n", s2, s1);
 
    printf("In lexicographical comparison: ");
    if(strcmp(s1, s2) < 0)
        printf("%s before %s\n", s1, s2);
    else
        printf("%s before %s\n", s2, s1);
}

int main(void)
{
    afis("default C");
    puts(setlocale(LC_COLLATE, "ro_RO.utf8"));
    afis("RO");
}
/*
Dacă vă merg font-urile și aveți instalată localizare UTF-8, ar trebui să se afișeze:
In the default C locale: notă mică👎 before 👍notă MARE
In lexicographical comparison: notă mică👎 before 👍notă MARE
ro_RO.utf8
In the RO locale: 👍notă MARE before notă mică👎
In lexicographical comparison: notă mică👎 before 👍notă MARE
*/
```
Observații:
- este necesară salvarea fișierului cu encoding UTF-8
- exemplul este oarecum eronat, deoarece `strcmp` și `strcoll` fac comparații la nivel de byte, nu la nivel de caracter (👍 este un caracter pe 4 bytes în UTF-8: `0xF0`, `0x9F`, `0x91` și `0x8D`)
- aceste funcții primesc ca argumente `char*`, nu `unsigned char*`, însă în cazul `strcmp`/`strncmp`, caracterele sunt interpretate ca `unsigned char`
  - `👍` este "mai mare" decât litera `n`, întrucât `0xF0` este 240 ca extended ASCII și este evident mai mare ca `n` (acesta e mai mic decât 128)
- utilizarea localizării `"C"` este de preferat, deoarece are un comportament determinist, care nu depinde de localizare
  - dezavantajul este că prelucrarea se face la nivel de byte și în unele situații s-ar putea să "taie" un caracter, dar nu le putem avea pe toate `¯\_(ツ)_/¯`

De ce nu am folosit funcția `strxfrm`? Și ce face funcția asta?

Teoretic, această funcție transformă un șir de caractere într-o formă "normalizată" pentru a putea face ulterior comparații cu `strncmp` ca și cum am compara cu `strcoll`, în ideea că această normalizare ar face comparațiile ulterioare mai rapide. Deși standardul C specifică faptul că `strxfrm` + `strncmp` ar trebui să dea aceleași rezultate cu `strcoll`, realitatea contrazice aceste mărețe idealuri.

Cea mai populară implementare de pe Linux a bibliotecii C standard, [`glibc`](https://en.wikipedia.org/wiki/GNU_C_Library), are (sau avea) un bug în `strxfrm` sau în `strcoll` (sau în ambele??), detalii [aici](https://bugzilla.redhat.com/show_bug.cgi?id=1320356). Asta a cauzat, printre altele, [probleme](http://wiki.postgresql.org/wiki/Abbreviated_keys_glibc_issue) de performanță în Postgres (o bază de date destul de cunoscută). Chiar dacă versiuni noi de `glibc` repară aceste probleme, durează destul de mult ca noile versiuni să fie adoptate la scară largă. Exemplu de adoptare lentă: renunțarea la Windows XP sau Windows 7.

Concluzia: folosiți `strcmp`/`strncmp`, însă e bine să știți unde să căutați sau [de la ce](https://en.wikipedia.org/wiki/Collation) să plecați atunci când comparațiile între șiruri de caractere nu funcționează cum v-ați aștepta.

<!--
https://en.cppreference.com/w/c/string/byte/strcoll
https://blog.anayrat.info/en/2017/11/19/postgresql-10-icu-abbreviated-keys/
https://postgresql.verite.pro/blog/2018/07/25/icu-extension.html
-->

### Diverse
[Înapoi la programe](#programe-discutate)

#### Despre Unicode și UTF-8

Unicode este un standard pentru a obține codificări pentru **toate** caracterele/simbolurile posibile (sau cât mai multe). Acesta nu are legătură cu reprezentarea lor pe bytes. În standardul Unicode, fiecărui caracter îi este alocat un "codepoint" unic (îl putem considera un fel de ID) printr-o legătură 1 la 1. Unicode se ocupă cu organizarea și alocarea acestor codepoints.

Codificarea UTF-8 transpune aceste codepoints abstracte într-o formă concretă și face legătura între un codepoint și unul sau mai mulți bytes.

În prezent, un codepoint în UTF-8 este reprezentat prin unul sau mai mulți bytes. Această codificare este la nivel de byte, ceea ce înseamnă că nu contează dacă suntem pe o platformă little-endian sau big-endian, deoarece citirea trebuie efectuată byte cu byte, deci acești bytes nu sunt grupați în vreun fel când are loc citirea (spre deosebire de citirea/scrierea din/în fișiere binare a numerelor întregi, de exemplu).

Această codificare a fost concepută în așa fel încât primul byte să ne spună și pe câți bytes este caracterul din care am început să citim; exemplu de cod [aici](https://stackoverflow.com/a/21745211).

O bibliotecă foarte cunoscută care oferă prelucrări pe șiruri de caractere funcționale cu Unicode este [ICU](https://github.com/unicode-org/icu).

**Concluzia** și cu ce trebuie să rămâneți: textul nu este doar ASCII!

#### Despre funcțiile "sigure"

Dacă v-ați uitat prin documentație (sau dacă folosiți Visual Studio), probabil ați aflat de existența unor funcții precum `scanf_s` sau altele cu sufixul `_s`. În teorie, acestea ar trebui să prevină erori comune de programare, de exemplu erori de ieșire din vector și altele care să cauzeze buffer overflow.

Acestea au fost implementate inițial ca funcții nestandard de către cei de la Microsoft. Probabil la insistențele Microsoft, acestea au fost incluse până la urmă în standardul C11 ca funcții opționale, însă ordinea parametrilor este diferită, ceea ce face ca implementarea lor să nu respecte standardul.

Alte compilatoare cunoscute (printre care și `gcc`) nu au considerat că are rost să le implementeze. Corect ar fi să spunem `glibc`, deoarece cu MinGW par să meargă (nu am verificat ordinea parametrilor). Întrucât aceste funcții nu au fost adoptate de prea multă lume (și [au avut motive](https://stackoverflow.com/questions/372980/do-you-use-the-tr-24731-safe-functions) pentru această decizie), le putem ignora, cel puțin dacă ne interesează să avem un cod cât de cât portabil.

## Exerciții
[Înapoi la cuprins](#cuprins)

- înlocuiți șirul de caractere din exemplul cu `strpbrk` cu șirul de caractere dat ca exemplu, cel cu `Astazi este o zi...`

Din PDF:

1. Se citește de pe prima linie a unui fișier o literă. Se citește apoi din fișier un text. Să se scrie textul eliminând din toate cuvintele litera citită de pe prima linie:
    * a. într-un fișier nou;
    * b. la sfârșitul fișierului din care se citește.

2. Se citesc de pe prima linie a unui fișier două litere separate prin spațiu. Se citește pe următoarea linie un text. Să se rescrie textul înlocuind din toate cuvintele litera citită de pe prima linie cu cea de-a doua literă. Se va suprascrie fișierul din care s-a citit.

3. Se citește dintr-un fișier un text. Să se înlocuiască fiecare cuvânt cu unul care are inversate majusculele cu minusculele și viceversae (de ex, cuvântul "infORmaTică" va fi înlocuit cu "INForMAtTICĂ"). Să se realizeze operaţia folosind un singur fișier. Observație: folosiți localizarea ISO8859-2 sau Windows-1250 pentru a putea inversa corect caracterul `ă`. Limitarea este că nu avem `ș` și `ț`, dar ne mulțumim și cu atât.

4. Scrieți un program care afișează cele mai frecvente litere care apar într-un fișier. Programul nu va face distincție între literele mari și mici. Dacă există mai multe litere care apar de cele mai multe ori în fișier, programul le va afișa pe toate. Dacă nu există nici o literă în fișier, programul va afișa un mesaj corespunzător.

5. Se citește dintr-un fișier un text și de la tastatură se introduce un cuvânt. Să se scrie într-un fișier toate cuvintele care conţin cuvântul citit.

## Întrebări, erori, diverse
[Înapoi la cuprins](#cuprins)

* 🚧

## Resurse recomandate
- **[un articol despre Unicode scris în 2003 de unul dintre cofondatorii StackOverflow](https://www.joelonsoftware.com/articles/Unicode.html)**
- [cppreference.com](https://en.cppreference.com/w/c)
- [StackOverflow](https://stackoverflow.com/questions/tagged/c?tab=Votes)
- [C FAQ](http://c-faq.com/questions.html)
- [C99 standard](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf) (doar să îl răsfoiți un pic)
