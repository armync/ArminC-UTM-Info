# Laboratorul 5

### ⚠ Puneți cât mai multe întrebări! Nu există întrebări greșite.
#### Semnalați orice fel de greșeli găsiți!

# Cuprins
## [Împărțirea ecranului](#împărțirea-ecranului-1)
## [Programe discutate](#programe-discutate-1)
## [Exerciții](#exerciții-1)
## [Întrebări, erori și orice nu a fost acoperit deja](#întrebări-erori-diverse)
## [Resurse recomandate](#resurse-recomandate-1)

## Împărțirea ecranului

## Programe discutate
[Înapoi la cuprins](#cuprins)

### [Directive de preprocesare](#directive-de-preprocesare-1)
### [Fișiere text](#fișiere-text-1)
### [Fișiere binare](#fișiere-binare-1)

### Directive de preprocesare
[Înapoi la programe](#programe-discutate-1)

Directivele de preprocesare care ne interesează sunt următoarele: [`#include`](#include), [`#define`](#define) și [compilarea condiționată](#compilare-condiționată).

#### `#include`

Această directivă este folosită pentru a copia conținutul fișierului dat ca parametru în fișierul curent.

Prima formă, cea cu paranteze ascuțite `<>`, va căuta în niște directoare predefinite, dependente de implementare, la care putem adăuga și noi alte directoare, folosind opțiunea `-Inume_director`.

Am compilat un fișier din linia de comandă cu `gcc -v main.c -Ilaborator-5` (remarcați rândul cu "laborator-5"):
```
ignoring duplicate directory "C:/Program Files/mingw-w64/x86_64-8.1.0-win32-seh-rt_v6-rev0/mingw64/lib/gcc/../../lib/gcc/x86_64-w64-mingw32/8.1.0/include"
ignoring nonexistent directory "C:/mingw810/x86_64-810-win32-seh-rt_v6-rev0/mingw64C:/msys64/mingw64/lib/gcc/x86_64-w64-mingw32/8.1.0/../../../../include"
ignoring duplicate directory "C:/Program Files/mingw-w64/x86_64-8.1.0-win32-seh-rt_v6-rev0/mingw64/lib/gcc/../../lib/gcc/x86_64-w64-mingw32/8.1.0/include-fixed"
ignoring duplicate directory "C:/Program Files/mingw-w64/x86_64-8.1.0-win32-seh-rt_v6-rev0/mingw64/lib/gcc/../../lib/gcc/x86_64-w64-mingw32/8.1.0/../../../../x86_64-w64-mingw32/include"
ignoring nonexistent directory "C:/mingw810/x86_64-810-win32-seh-rt_v6-rev0/mingw64/mingw/include"
#include "..." search starts here:
#include <...> search starts here:
 laborator-5
 C:/Program Files/mingw-w64/x86_64-8.1.0-win32-seh-rt_v6-rev0/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.1.0/include
 C:/Program Files/mingw-w64/x86_64-8.1.0-win32-seh-rt_v6-rev0/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.1.0/include-fixed
 C:/Program Files/mingw-w64/x86_64-8.1.0-win32-seh-rt_v6-rev0/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.1.0/../../../../x86_64-w64-mingw32/include
End of search list.
```
Din Code::Blocks, pașii sunt următorii:
1. Click dreapta pe numele proiectului
2. Selectăm `Build options...`
3. Selectăm tab-ul `Search directories`
4. Click pe butonul `Add`
5. Selectăm directorul care conține fișierele header de care avem nevoie
6. Ok, ok, repetăm pașii 4-6 până am adăugat toate directoarele necesare
7. Verificăm faptul că opțiunea este transmisă compilatorului: atunci când compilăm, verificăm ca în tab-ul `Build log` de jos să apară și opțiunea cu `-Inume_director`, unde `nume_director` este cel introdus la pasul 5.

Atenție! Acest proces selectează doar fișierele header, nu și implementarea! Pentru fișierele obiect corespunzătoare, dacă bibliotecile nu sunt de tip header-only, va trebui să ajutăm compilatorul să facă legăturile necesare, de exemplu prin opțiunea `-Lnume_director`, pe care le putem vedea în variabila `LIBRARY_PATH`. În plus, este posibil să fie necesară specificarea legăturilor cu opțiunea `-lnume_biblioteca` (L mic). Opțiunea `-L` doar îi spune linker-ului în ce directoare să caute fișierul obiect specificat cu opțiunea `-l`.

Pentru a vedea ce directoare conține variabila `LIBRARY_PATH`, o putem afișa folosind comanda `gcc -v --version`.

Pentru proiecte noi și complexe în C/C++ pentru care aveți nevoie de biblioteci externe, poate fi util [CMake](https://cmake.org/). Pentru situații și mai complicate, poate fi folosit un package manager.

🔎 Bibliotecile sunt de două feluri: statice și dinamice. Cele statice sunt adăugate în executabilul final, pe când cele dinamice trebuie să existe în momentul în care rulăm programul nostru.

#### `#define`
[Înapoi la directive](#directive-de-preprocesare-1)

[Această directivă](https://en.cppreference.com/w/c/preprocessor/replace) definește o constantă (cu valoare opțională) sau un macro de tip funcție.

În cazul constantelor, avantajele folosirii macro-urilor sunt:
- nu ocupă memorie în programul final
- pot fi "eliminate" cu `#undef` și eventual apoi redefinite
  - de exemplu, `true` este definit ca un macro, deoarece poate exista cod mai vechi care să definească această constantă în alt mod
- lipsa informației despre tip este atât un avantaj (putem obține cod mai generic), cât șî un dezavantaj, deoarece compilatorul nu ne poate ajuta
- pot fi folosite în instrucțiuni de tip `switch`
- putem declara vectori de lungime fixă:
  - dacă am folosi `const int n = 10; int v[n];`, atunci `v` ar fi un VLA, chiar dacă valoarea lui `n` este cunoscută la compilare

Ca dezavantaj care nu este precizat în curs:
- nu putem să le facem debugging cu debugger-ul, deoarece nu sunt generate simboluri de debugging
- [o alternativă](https://stackoverflow.com/questions/1674032/static-const-vs-define-vs-enum) este să folosim `enum` pentru astfel de constante, deși, în funcție de situație, `#define` are unele avantaje

O altă întrebuințare a macro-urilor este cea a verificării codului folosind [`assert`](https://en.cppreference.com/w/c/error/assert) din `<assert.h>`.

`assert` este un macro care primește ca parametru o expresie și oprește execuția programului dacă expresia este falsă, indicând numele fișierului și linia la care a fost încălcată aserțiunea (cu ajutorul macro-urilor `__FILE__` și `__LINE__`). Deoarece nu avem nevoie de aceste verificări atunci când considerăm programul gata, avem nevoie de un mecanism prin care să dezactivăm `assert`. Standardul C specifică definirea constantei `NDEBUG` înainte să includem `<assert.h>`.

Ca exemplu, vom scrie niște teste pentru problema următoare.

Se citeṣte un caracter de la tastatură. Să se verifice dacă este literă mare. Dacă da, să se transforme în literă mică ṣi să se afiṣeze. Altfel, să se rescrie caracterul tastat.

Implementarea o veți scrie voi, testele le-am scris eu:
```c
#include <stdio.h>
// #define NDEBUG
#include <assert.h>

char transforma_litera(char c)
{
    return c;
}

void verifica(char intrare)
{
    char rezultat = transforma_litera(intrare);

    switch(intrare)
    {
        case 'A':
            assert(rezultat == 'a');
            break;
        case 'Z':
            assert(rezultat == 'z');
            break;
        default:
            assert(rezulat == intrare);
            break;
    }    
}

void test_1()
{
    verifica('A');
    verifica('Z');
    verifica('a');
}

void problema_1()
{
    char c;
    scanf("%c", &c);
    printf("Rezultatul este %c.\n, transforma_litera(c));
}

int main()
{
    // teste
    test_1();
    // utilizarea functiei in mod normal
    // problema_1();
    return 0;
}
```
Observații:
- urmând această abordare, nu trebuie să pierdem timpul cu introdus datele de la tastatură atunci când testăm ce am implementat; vom trece la citirea de la tastatură numai la sfârșit, pentru câteva ultime verificări
- în modul prezentat mai sus, `assert` are două mari dezavantaje:
  - nu are un argument suplimentar pentru a afișa un mesaj
    - putem remedia acest lucru folosind o expresie de forma `assert(expresie && mesaj);`
    - totuși, implementarea macro-ului `assert` pe MinGW nu indică și numele funcției prin intermediul variabilei speciale `__func__`; eventual putem să ne definim noi un macro pentru aserțiuni care să includă și această informație
  - aserțiunile au loc la momentul execuției programului
    - după cum am tot menționat, C11 încă nu poate fi folosit cu succes; acesta include aserțiuni care au loc la momentul compilării, folosind cuvântul cheie [`_Static_assert`](https://en.cppreference.com/w/c/language/_Static_assert) sau macro-ul `static_assert` din `<assert.h>`
    - [există alternative în acest sens](https://stackoverflow.com/questions/174356/ways-to-assert-expressions-at-build-time-in-c), care folosesc construcții greșite atunci când condiția nu este îndeplinită: de exemplu, vectori de lungime negativă sau câmpuri de biți de lungime negativă, tocmai pentru a cauza erori la momentul compilării; dificultatea utilizării acestora constă în folosirea unor construcții care să furnizeze mesaje de eroare ușor de înțeles
- comentați linia din main cu `test_1()` și decomentați linia cu `problema_1()` pentru programul final
  - pentru programe mai mari, vom avea aceste funcții în fișiere separate, astfel încât putem evita cu totul includerea lor în executabilul final, deoarece codul de test nu va fi "link-uit"
  - desigur, pentru proiecte și mai mari, există biblioteci specializate

#### [Compilare condiționată](https://en.cppreference.com/w/c/preprocessor/conditional)
[Înapoi la directive](#directive-de-preprocesare-1)

[Aceste directive](https://en.cppreference.com/w/c/preprocessor/conditional) sunt utile pentru compilarea de cod specific pentru fiecare platformă în parte, cu scopul de a folosi apeluri de sistem care nu sunt disponibile prin biblioteca C standard.

De exemplu, pe Windows ar fi folosite apeluri din WinAPI, iar pentru restul lumii (\*nix-based) există apeluri din biblioteca C POSIX. Desigur, lucrurile pot fi mult mai variate.

Un alt [exemplu](https://stackoverflow.com/questions/1041866/what-is-the-effect-of-extern-c-in-c) este folosirea de cod scris în C, dar care poate fi compilat atât cu un compilator de C, cât și unul de C++:
- verificăm dacă există constanta `__cplusplus`
- adăugăm codul într-un bloc `extern "C" { /*restul codului*/ }`
- acești pași sunt necesari deoarece în C++ există supraîncărcare de funcții, dar în C nu
```c
#ifdef __cplusplus
extern "C" {
#endif

int f();

#ifdef __cplusplus
}
#endif
```

Un ultim exemplu are legătură cu secțiunea anterioară și folosește compilarea condiționată pentru a rula instrucțiuni de debugging sau nu:
```c
#ifdef NDEBUG
    #define assertm(expr, message) ((void)0)
#else
    #define assertm(expr, message) (
        printf("%s in function %s:\n", message, __func__), assert(expr)
    )
#endif // NDEBUG
```
Observații:
- `__func__` (C99) nu este un macro, ci o constantă predefinită ca șir de caractere de tip `static const char[]` și conține numele funcției curente
  - `__FUNCTION__` este o constantă predefinită (*nu macro*), nestandard, dar poate fi folosită dacă nu avem acces la un compilator compatibil cu C99
- macro-ul nu conține `;` la sfârșit pentru ca atunci când folosim macro-ul, acesta să apară ca un apel de funcție; o altă variantă folosind o construcție (mai puțin intuitivă) găsiți [aici](https://stackoverflow.com/questions/154136/why-use-apparently-meaningless-do-while-and-if-else-statements-in-macros)
  - exemplu de apel: `assertm(medie == 10, "expected medie to be 10");`
- într-un mod similar, am putea construi un macro pentru a avea aserțiuni la compilare (însoțite de un mesaj), care să dispară dacă definim o anumită constantă (`NDEBUG`)

#### Alte observații

Nu există definit în standardul C macro-ul `__CDECL__`. După investigații minuțioase 🧐, aceasta pare o născocire dintr-un curs de la UT Cluj, curs care conține **foarte multe greșeli**. Sunt oripilat 😱 de bazaconiile care se predau acolo, așa că nu voi pune link către acel "curs". Nu am reușit să identific sursa greșelii, deoarece acele materiale nu conțin **deloc** bibliografie. Voi menționa doar că încurajează folosirea header-ului *nestandard* `<conio.h>` în numeroase rânduri 🤮. Puteți trece fără griji la secțiunea următoare dacă nu vă interesează detaliile, nu pierdeți prea multe.

Și totuși, ce este acest misterios `__CDECL__` și de la ce vine :thinking:? "Apelul funcției urmărește convențiile C" nu are sens.

Întâi de toate, este vorba despre convențiile de transmitere a parametrilor la apelurile de funcții la nivel de limbaj de asamblare. De ce sunt importante aceste convenții? Pentru că ele determină ce parametri ajung pe stivă și ce parametri sunt încărcați direct în regiștri. Puteți citi mai multe detalii [aici](https://stackoverflow.com/questions/949862/what-are-the-different-calling-conventions-in-c-c-and-what-do-each-mean) sau pe pagina de [Wikipedia](https://en.wikipedia.org/wiki/X86_calling_conventions) despre câteva dintre convențiile posibile. Standardul C **nu stabilește deloc** acest aspect, ci este lăsat în grija compilatoarelor.

Dacă tot am amintit despre acest subiect, el poate fi relevant în următorul context, dacă aveți de scris compilatoare sau cod pentru dispozitive embedded: ordinea *evaluării* parametrilor unei funcții depinde de implementare. Astfel, compilatorul poate să aleagă să evalueze parametrii în așa fel încât să încarce într-un mod optim rezultatele în regiștri, încercând să evite cât mai mult transferuri suplimentare între memoria RAM și regiștri, ceea ce se traduce în [mai puțini cicli de procesor](https://stackoverflow.com/questions/12540418/why-is-the-order-of-evaluation-for-function-parameters-unspecified-in-c). Legătura cu convențiile de transmitere a parametrilor ar fi aceea a regiștrilor utilizați.

Acestea fiind spuse, fiecare compilator are libertatea să implementeze (sau nu) opțiuni pentru stabilirea explicită a convențiilor de transmitere a parametrilor. Întrucât această tiradă a pornit de la `cdecl`, ne vom referi doar la această convenție. Din ce m-am documentat, aceasta pare să fie convenția implicită pentru compilatorele mai populare. Pentru a seta această opțiune, ar fi următoarele macro-uri sau opțiuni *specifice fiecărui compilator*:
- [`gcc`](https://gcc.gnu.org/onlinedocs/gcc/x86-Function-Attributes.html) pare să folosească ce folosește și Intel, deși în headerele furnizate de MinGW am găsit `__cdecl` (macro pentru `__attribute__((__cdecl__))`)
- [`clang`](clang.llvm.org/docs/UsersManual.html) tot `__cdecl` (deși nu știu dacă am căutat unde trebuie)
- [`MSVC`](https://docs.microsoft.com/en-us/cpp/cpp/cdecl?view=vs-2019) tot `__cdecl`
- [`Intel C++ Compiler`](https://software.intel.com/content/www/us/en/develop/documentation/cpp-compiler-developer-guide-and-reference/top/compiler-reference/c-c-calling-conventions.html) are `__cdecl` pentru Windows, `__attribute((cdecl))` pentru Linux și MacOS

Și, cu toate acestea, nu am reușit să răspundem la întrebarea inițială. Tot ce am reușit să găsesc este faptul că macro-ul `__CDECL__` într-adevăr există, doar că este folosit de compilatorul inclus în [C++ Builder](http://docwiki.embarcadero.com/RADStudio/Sydney/en/Predefined_Macros). Acesta este succesorul lui [Borland C](https://en.wikipedia.org/wiki/Borland_C%2B%2B), care încă era folosit (sau cel puțin instalat) când eram la liceu.



### Fișiere text
[Înapoi la programe](#programe-discutate-1)

Ce este un fișier text?

Un fișier text este orice fișier pe care, dacă îl deschidem cu Notepad, conținutul "are sens". Orice alt fișier este un fișier binar.

La fel ca în cazul alocării dinamice, vă recomand ca, atunci când scrieți apelul de deschis fișiere, să îl scrieți și pe cel pentru închiderea fișierului, chiar dacă se ocupă sistemul de operare de asta.

Funcția [`fopen`](https://en.cppreference.com/w/c/io/fopen) primește ca parametru numele fișierului (șir de caractere) și modul de deschidere (șir de caractere) și întoarce un pointer către o structură de tip `FILE`, adică `FILE*`. Toate acestea sunt incluse în `<stdio.h>`.

Numele fișierului trebuie să fie calea relativă sau absolută a fișierului. Dacă creați fișierele cu <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>N</kbd> din Code::Blocks, puteți folosi direct numele fișierului (fără numele folderelor în care se află), deoarece se ocupă Code::Blocks de restul.

Exemplu:
- am creat fișierul `date.in`
- structura fișierelor în cadrul proiectului Code::Blocks este următoarea (folderul se numește "fisiere"):
```
fisiere
│   ceva.c
│   fisiere.cbp
│   fisiere.depend
│   fisiere.layout
│   date.in
│   main.c
│
├───bin
│   └───Debug
│           fisiere.exe
│
└───obj
    └───Debug
            main.o
```
- calea absolută este ceva asemănător cu `C:\Users\marius\Documents\facultate\ore\prog-calc\laborator-5\fisiere`
  - pe \*nix am avea ceva asemănător cu `/home/marius/facultate/ore/prog-calc/laborator-5/fisiere`
- calea relativă este `date.in`
  - dacă am executa noi direct executabilul din folderul `bin\Debug`, atunci calea relativă ar fi `..\..\date.in`, unde `..` semnifică folderul părinte
  - dacă executăm din folderul "fisiere", apelarea executabilului s-ar face cu calea `bin\Debug\fisiere`, iar calea relativă pentru fișier ar rămâne `date.in`

Ce se întâmplă dacă apare o eroare la deschiderea fișierului?
- vom primi înapoi un pointer `NULL`

Pentru a putea discuta ce erori pot apărea, vom menționa pe scurt modurile de deschidere pentru fișiere (tabel preluat din documentație):

Mod | Explicație | Acțiune la deschidere | Fișier inexistent
----|------------|---------|------------------
`r` | mod citire | citire de la început | eroare
`w` | mod scriere| șterge conținutul fișierului dacă există | creează fișierul dacă nu există
`a` | append, adaugă la sfârșit | scrie la sfârșit | creează fișierul dacă nu există
`r+`| citire/scriere | citire de la început | eroare
`w+`| citire/scriere | șterge conținutul fișierului dacă există | creează fișierul dacă nu există
`a+`| append/citire | scrie la sfârșit | creează fișierul dacă nu există

Modurile extinse, cele cu `+`, funcționează astfel:
- dacă ultima acțiune a fost una de citire, este necesar un apel la `fseek`, `fsetpos` sau `rewind` pentru a putea scrie
- dacă ultima acțiune a fost una de scriere, este necesar un apel la `fflush`, `fseek`, `fsetpos` sau `rewind` pentru a putea citi

De asemenea, toate modurile de mai sus pot avea opțional adăugat un `b` (ex: `rb`, `wb+` sau `w+b`), care specifică deschiderea fișierului în mod binar, deoarece fișierele sunt deschise implicit în mod text. Distincția dintre fișiere binare și fișiere text în modul de citire (acest `b`) are efect doar pe Windows, iar pentru modul binar se întâmplă următoarele:
- caracterele de rând nou nu sunt traduse în `\n`
  - pe Windows, rândul nou este `\r\n`: `CR` - Carriage Return, apoi `LF` - Line Feed
    - la citirea în mod text, `\r\n` este tradus în `\n`
    - la scrierea în fișier, `\n` este tradus în `\r\n`
  - pe Unix și pe MacOS(X) relativ noi: `\n`
  - pe macOS vechi: `\r` (deși este posibil să apară `\r` pe macOS noi dacă sunt folosite programe vechi)
- caracterul de control pentru sfârșit de fișier (`EOF`) pe Windows `\x1A` sau <kbd>Ctrl</kbd>+<kbd>Z</kbd>) nu este tratat special

Cu toate că nu are efect decât pe Windows faptul că precizăm modul de deschidere binar sau text, funcțiile `ftell` și `fseek` au comportament specific pentru fiecare mod (cel puțin teoretic).

Observație: standardul nu definește caracterul `t` pentru deschidere explicită în mod text. Orice alt caracter în afara celor de mai sus constituie 💥, unul dintre comportamente fiind cel de a ignora caracterele în plus.

Pentru a închide fișierul, vom folosi funcția [`fclose`](https://en.cppreference.com/w/c/io/fclose), care primește un `FILE*`. *NU* mai putem folosi acel pointer decât pentru a deschide din nou alt fișier. Dacă încercăm operații de citire/scriere/închidere cu un pointer după ce am închis fișierul asociat, avem 💥.

Prin urmare: **atunci când scriem apelul la `fopen`, scriem și apelul la `fclose` pentru a nu uita să închidem fișierul**.

```c
#include <stdio.h>

int main()
{
    const char *nume_fisier = "date.in";
    FILE *f = fopen(nume_fisier, "r");
    if(f == NULL)
    {
        printf("Fisierul %s nu exista!\n", nume_fisier);
        return 1;
    }
    fclose(f);
    return 0;
}
```
Observații:
- citirea din fișiere se face implicit folosind buffere, adică se încarcă datele în memorie (RAM) și se fac operații de I/O (citiri/scrieri) mai rar, deoarece acestea sunt *foarte* lente
- deschiderea fișierului într-un mod de scriere poate să eșueze dacă nu avem spațiu pe disc
- la fel și în cazul închiderii, deoarece atunci se golesc automat bufferele
- la un mod riguros, am putea verifica dacă a reușit `fclose` sau nu
- putem folosi funcția [`perror`](https://en.cppreference.com/w/c/io/perror) pentru a afișa cauza erorii

Până acum, am folosit două fișiere predefinite de tip `FILE*`:
- `stdin`, asociat intrării standard (tastatura)
- `stdout`, asociat ieșirii standard (ecranul)

Putem folosi variante ale funcțiilor folosite până acum pentru citirea/scrierea din/în fișiere, care au ca parametru suplimentar un `FILE*` (despre `fgets` am vorbit deja):
```c
#include <stdio.h>

int main()
{
    const char *nf = "numere.txt";
    FILE *f = fopen(nf, "w");
    if(f == NULL)
    {
        perror("Eroare la deschiderea fisierului pentru scriere");
        return 1;
    }

    for(int i = 0; i < 10; i += 2)
        fprintf(f, "%d %d\n", i, i/2);
    fputc('5', f);
    fputc('\n', f);
    fclose(f);
    fputs("Am scris fisierul!\n", stdout);  // nu pune '\n' la fel ca `puts`!

    f = fopen(nf, "r");
    if(f == NULL)
    {
        perror("Eroare la deschiderea fisierului pentru citire");
        return 1;
    }

    int a, b, nr;
    while((nr = fscanf(f, "%d %d", &a, &b)) == 2)
        fprintf(stdout, "%d -> %d\n", b, a);
    if(nr == 1)
        printf("%d\n", a);
    fclose(f);
    return 0;
}
```
Observații:
- **verificăm întotdeauna dacă citirea a reușit**
  - **nu este foarte relevant dacă am ajuns la sfârșitul fișierului; dacă apare o altă eroare, apelul la `feof` nu ne va spune nimic!**
  - există în schimb `ferror`
  - citiți mai multe [aici](https://stackoverflow.com/questions/5431941/why-is-while-feof-file-always-wrong)
- am putea verifica dacă operațiile de scriere în fișier au reușit
- dacă nu închideam fișierul pentru scriere înainte să încercăm să începem citirea, existau unele inconveniente:
  - fișierul deschis pentru scriere ar trebui închis pe ambele ramuri, indiferent dacă deschiderea fișierului pentru citire reușește sau nu
  - nu aveam ce să citim, dacă buffer-ul nu a fost golit (putem cere explicit asta cu [`fflush`](https://en.cppreference.com/w/c/io/fflush))
- **`fflush` este doar pentru stream-uri de ieșire** (altfel 💥), vedeți [aici](https://stackoverflow.com/questions/2979209/using-fflushstdin)
- este bine să închidem și fișierele deschise doar pentru citire, deoarece fiecare proces are o limită pentru câte fișiere poate avea deschise la un moment dat
- **nu folosiți header-ul nestandard `<conio.h>`** (existent doar pe Windows) dacă vreți programe portabile!
  - pentru console interactive, ar trebui folosite biblioteci specializate care să asigure portabilitatea
  - exemple de funcții din acest header: `getch`, `getche`, `putch`; bonus, nici documentația de la Microsoft nu le recomandă
  - posibil ca Herbert Schildt să fie vinovat pentru popularizarea acestei biblioteci în învățământ
  - [pe Windows încă merge](https://blog.codinghorror.com/the-works-on-my-machine-certification-program/) să le folosiți, însă pe orice altceva veți obține
```
main.c:10:19: fatal error: conio.h: No such file or directory
 #include <conio.h>
                   ^
compilation terminated.
```

⛔ **Nu am menționat deloc funcția `gets`, presupuneți că nu există!** ⛔

Chiar nu există în C11.

### Fișiere binare
[Înapoi la programe](#programe-discutate-1) | [Scriere](#scriere) | [Citire](#citire)

Una dintre definițiile fișierelor text este aceea că sunt organizate pe rânduri. Prin eliminare, fișierele binare nu au o organizare atât de evidentă, aceasta fiind stabilită pentru fiecare format în parte. Cazul extrem este să nu existe niciun fel de organizare și să fie doar un șir de bytes.

Este momentul să precizăm că extensia unui fișier nu este prea relevantă pentru conținutul fișierului, ci este doar o convenție. Nu există o metodă care să garanteze 100% că un fișier este de un anumit tip, însă un indiciu mult mai bun în acest sens este utilizarea [numerelor magice](https://en.wikipedia.org/wiki/File_format#Magic_number). Astfel, informația despre tipul fișierului este scrisă direct în conținutul fișierului.

Am precizat în secțiunea anterioară că modul de deschidere al unui fișier binar în limbajul C este obținut prin adăugarea literei `b`.

Pentru a citi/scrie din/în fișiere binare, există două funcții speciale: [`fread`](https://en.cppreference.com/w/c/io/fread) și [`fwrite`](https://en.cppreference.com/w/c/io/fwrite). Ambele funcții prelucrează datele în blocuri de lungime fixă.

#### Scriere
```c
#include <stdio.h>

int main()
{
    int a[] = { 123456789, 634, 42 };
    size_t nr, count;
    //float b[] = { 98765.4321, 1.41, 6.43, 1.2 };
    //double c[] = { 91.294655, 222.222 };

    FILE *f = fopen("fis.bin", "wb");
    count = sizeof(a) / sizeof(a[0])
    nr = fwrite(a, sizeof(a[0]), count, f);
    if(nr < count)
        perror("Eroare la scriere");
    //fwrite(c, sizeof(c[0]), sizeof(c) / sizeof(c[0]), f);
    //fwrite(b, sizeof(b[0]), sizeof(b) / sizeof(b[0]), f);
    fclose(f);
    return 0;
}
```
Observații:
- numirea fișierelor binare cu extensia ".bin" este doar o convenție
- fișierul va conține reprezentarea binară a numerelor întregi din vectorul `a` și nimic mai mult
  - nu există un caracter echivalent cu `EOF` de la fișierele text
- depinde de aplicație dacă este necesar să verificăm dacă scrierea a fost efectuată cu succes (prin valoarea întoarsă de `fwrite`)
  - o situație când scrierea nu reușește este când nu mai avem spațiu pe disc

Dacă încercăm să deschidem fișierul rezultat cu un editor de text, obținem ceva de neînțeles:
```
// fisierul fis.bin cu encoding Windows-1252
�[z  *   
// fisierul fis.bin cu encoding UTF-8
͛z  *   
```
- cu ocazia aceasta, putem vedea o caracteristică a fișierelor text despre care am vorbit într-un laborator anterior: encoding
  - în codificările mai vechi, un byte reprezintă un caracter, vedeți rândul 2
  - în codificările moderne, un caracter este codificat prin unul sau mai mulți bytes, motiv pentru care obținem ceva mai "scurt"
- desigur, ce am afișat mai sus nu are niciun sens: noi am scris niște numere întregi în mod binar și încercăm să le afișăm ca text
- pentru a vedea într-un mod mai coerent conținutul fișierelor binare, putem să îl deschidem din Code::Blocks cu Hex editor
  - trebuie să adăugăm fișierul în proiect: click dreapta pe numele proiectului sau din meniu `Project` -> `Add files...`
  - click dreapta pe fișierul "fis.bin", `Open with` -> `Hex editor`
- ceea ce veți obține poate să difere, deoarece reprezentarea binară depinde de platformă/compilator/procesor
  - în cazul meu, reprezentarea este little-endian, iar `sizeof(int) == 4`
```
15 CD 5B 07 7A 02 00 00 2A 00 00 00
^^^^^^^^^^^
- acesta este primul număr, 123456789, sau 0x075BCD15 (07 5B CD 15) în reprezentare big-endian
- observăm că mai sus octeții sunt în ordine "inversă", deoarece acolo sunt little-endian
- fiecare grupare de 2 "cifre" reprezintă un byte: avem afișarea în baza 16, deci fiecare "cifră" poate avea
  valori de la 0 la 15 (2^4 - 1); două astfel de "cifre" înseamnă de la 0 la 2^8 - 1, 8 biți, adică 1 octet

15 CD 5B 07 7A 02 00 00 2A 00 00 00
            ^^^^^^^^^^^
- al doilea număr, 634, sau 0x0000027A (00 00 02 7A) în reprezentare big-endian

2A în baza 10 este 2*16^1 + 10*16^0 = 32 + 10 = 42 (A este 10)
De asemenea, 42 este codul ASCII pentru caracterul '*', motiv pentru care îl vedem mai sus
Similar, 7A este codul ASCII pentru caracterul 'z'
```

De ce ambele caractere apar în ambele reprezentări, dar caracterul `[` apare doar în cazul ASCII?
Așa s-a nimerit. Este adevărat că UTF-8 este compatibil cu ASCII, doar că interpretarea în UTF-8 este următoarea:
- primul octet este 15 (`0001 0101`), înseamnă că avem o grupare de un octet, iar acesta este un caracter de control
  - mai exact, NAK, folosit în [protocoale de comunicare](https://en.wikipedia.org/wiki/Acknowledgement_(data_networks))
- al doilea octet este CD (`1100 1101`), adică un caracter reprezentat prin 2 octeți: `CD 5B` (sau `\xcd\x5b`)
  - acești octeți sunt o combinație invalidă în UTF-8 (cel puțin conform convertorului pe care l-am folosit)
  - `\xcd\x80` pare să fie următorul caracter valid: `̓`, ceea ce ar putea explica de ce vedem un fel de mic apostrof la al doilea semn de întrebare (următoarele sunt diacritice sau apostrofuri)
  - desigur, e vorba de o încercare a browser-ului să afișeze ceva, în ciuda erorilor
- apoi avem [07](https://en.wikipedia.org/wiki/Bell_character), un alt caracter de control, care scotea un sunet pe calculatoarele mai vechi
- 7A (0111 1010), deci `'z'` se va afișa la fel
- [02](https://en.wikipedia.org/wiki/C0_and_C1_control_codes#STX), alt caracter de control
- 00 sunt caractere nule
- 2A este caracterul `'*'`, apoi alte caractere nule

M-am folosit de tabelul de [aici](https://en.wikipedia.org/wiki/UTF-8#Description) și de acest [convertor](https://onlineutf8tools.com/convert-hexadecimal-to-utf8).

#### Citire
```c
#include <stdio.h>

enum { N = 3 };

void verif_sfarsit(FILE *f)
{
    printf("Suntem la pozitia %lu.\n", ftell(f));
    if(feof(f))
        puts("Am ajuns la sfarsitul fisierului!");
    else if(ferror(f))
        perror("Eroare la citire");
    else
        puts("Nu am citit tot fisierul.");
}

int main()
{
    int a[N];
    size_t i, nr;
    FILE *f = fopen("fis.bin", "rb");
    nr = fread(a, sizeof(a[0]), N, f);
    if(nr < N)
    {
        printf("Am incercat sa citim %d bytes, dar am citit %zu bytes.\n", N, nr);
        fclose(f);
        return 1;
    }
    verif_sfarsit(f);

    for(i = N; i > 0; --i)
        printf("%d ", a[i-1]);
    printf("\n");
    nr = fread(a, sizeof(a[0]), 1, f);
    if(nr < 1)
        verif_sfarsit(f);
    fclose(f);
    return 0;
}
/* daca totul merge bine, va afisa
Suntem la pozitia 12.
Nu am citit tot fisierul.
42 634 123456789
Suntem la pozitia 12.
Am ajuns la sfarsitul fisierului!
*/
```
Observații:
- dacă facem `fseek` în afara fișierului (intenționat sau nu) și nu efectuăm operații de citire/scriere, funcția `feof` nu va returna deloc eșec!
  - de ce? deoarece `fseek` șterge statusul referitor la ajungerea la `EOF`; de ce face asta? pentru că este o presupunere de bun-simț: dacă vrem să ne mutăm prin fișier, cel mai probabil nu ne mutăm în afara lui
- morala (din nou): verificăm ce ne întoarce funcția `fread` pentru a ști dacă citirea a reușit sau nu
  - dacă numărul de elemente întors de `fread` diferă de ce ne-am așteptat, există două situații:
    - am ajuns la sfârșitul fișierului: verificăm cu `feof`
    - alte erori de I/O: verificăm cu `ferror` și afișăm eroarea cu `perror`
  - apelul `feof` are sens numai **după** ce știm că avem erori de citire, iar asta aflăm prin rezultatul întors de funcțiile care efectuează citirea/scrierea, `fread`/`fwrite` în cazul fișierelor binare
  - am afișat numerele în sens invers pentru a varia lucrurile, dar și pentru a ilustra o greșeală frecventă:
    - `i` are tipul `size_t`, care este un întreg *fără* semn, deci condiția `i >= 0` ar fi mereu adevărată, deoarece operațiile de adunare/scădere sunt bine definite pentru întregii fără semn

Alte observații:
- dacă folosim alte funcții de scriere în cazul fișierelor binare (ex: `fprintf`, `fputs`), acestea vor scrie șiruri de caractere
  - de ce? deoarece caracterele asta înseamnă, reprezentarea acestora este ușor de citit de către om
- dacă argumentele funcției `memcpy` se suprapun, avem 💥; în cazul `memmove`, pot exista suprapuneri
- un exemplu de utilitate pentru `fseek` este citirea parțială a unui fișier de tip arhivă (de exemplu `.zip`):
  - putem extrage un singur fișier dintr-o arhivă mare, citind doar partea de care avem nevoie

## Exerciții
[Înapoi la cuprins](#cuprins)
- scrieți într-un fișier binar întregul cu semn `-1801150480` în baza 10 sau întregul fără semn `2493816816`
  - întregul trebuie să aibă un tip de date adecvat (minim 32 de biți)
  - deschideți fișierul cu un editor text cu encoding-ul UTF-8
  - dacă nu am greșit ceva, ar trebui să vedeți un emoji; dacă am greșit și sunteți pe o platformă big-endian, trebuie să inversați octeții
  - deschideți fișierul cu Hex editor și verificați faptul că acest caracter este codificat prin 4 octeți
  - folosiți modul de scriere pentru adăugare (`a` sau append) pentru a adăuga acest întreg la fișierul existent din exemplul dat
  - folosiți funcția `fseek` pentru a poziționa caracterul spre sfârșitul fișierului pentru a citi doar conținutul introdus anterior: citiți din nou fișierul și scrieți conținutul respectiv într-un alt fișier separat

Din PDF:
1. Să se construiască o structură ce conține următoarele date despre candidații la admitere: `nr_legitimatie`, `nume`, `nota_mate`, `nota_info`, `nota_bac`, `medie`, `admis` (Y/N).
2. Să se definească o macroinstrucțiune ce calculează media de admitere după regula: 80% media la examen, 20% media de bac.
3. Să se definească o constantă pentru pragul minim de promovabilitate egală cu 5.
4. Să se scrie o funcție care citește dintr-un fișier datele unui candidat, în afară de medie, admis și buget, și le adaugă unui vector al tuturor candidaților, păstrând ordinea alfabetică. Media și promovabilitatea vor fi calculate folosind definițiile de la punctele `2` și `3`. Numărul de candidați este citit din fișier. Numele se vor compara folosind funcția [`strcmp`](https://en.cppreference.com/w/c/string/byte/strcmp).
5. Să se scrie o funcție care primește un vector de candidați și îi introduce într-un fișier text, apoi o altă funcție care citește datele din fișier și le afișează.
6. Similar cu `5`, doar că veți folosi fișiere binare.

7, 8 etc. Cerințele 1-6 adaptate la problemele cu structuri din laboratorul anterior.

Folosiți mai multe fișiere pentru organizarea codului. Este suficient un fișier header.

Verificați codul de retur al funcțiilor de citire!

## Întrebări, erori, diverse
[Înapoi la cuprins](#cuprins)

* 🚧

## Resurse recomandate
- [cppreference.com](https://en.cppreference.com/w/c)
- [StackOverflow](https://stackoverflow.com/questions/tagged/c?tab=Votes)
- [C FAQ](http://c-faq.com/questions.html)
- [C99 standard](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf) (doar să îl răsfoiți un pic)

### Resurse de evitat
- Herbert Schildt și cărțile lui
- cursul de Programarea Calculatoarelor de la UT Cluj ținut de Ion Giosan (vedeți [aici](#alte-observații) de ce)
  - și am o vagă bănuială că e bine să evitați și cursul său de POO
