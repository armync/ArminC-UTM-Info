# Laborator 4: Toolchain

## C basics: GOTOs

Un concept mai puțin abordat în tutoriale de C este instrucțiunea goto. Prin instrucțiunea goto, un program poate
sări în puncte intermediare în cadrul unei funcții. Aceste puncte intermediare se numesc label-uri (etichete).
Din punct de vedere al sintaxei, o eticheta consta dintr-un nume, urmat de caracterul `:`.

Un exemplu de cod:


 ```C
#include <stdio.h>

int main()
{
    int i, j, k;
    /* some code */
do_some_work:
    /* some other code */
    work();
    if (any_work())
        goto do_some_work;
    /* some code */
    return 0;
}
```

Programul execută un job prin work(). În caz că mai sunt alte joburi neterminate, executia programului sare la
eticheta do_some_work. do_some_work marcheaza punctul din program în care începe procesarea unui nou job. Pentru a
sări la acest punct se folosește instrucțiunea goto urmată de numele etichetei declarate. Prin diferite combinații
de if-uri si goto-uri se pot echivala alte instrucțiuni din C, cum ar fi else, for si while.

Codul dat exemplu mai sus ar putea fi un candidat care să înlocuiască o instrucțiune `do { … } while ();`:

```C
#include <stdio.h>

int main()
{
    int i, j, k;
    /* some code */
    do {
        /* some other code */
        work();
    } while (any_work());
    /* some code */
    return 0;
}
```

### The "WHYs" of goto

Această instrucțiune nu doar că adesea lipsește din tutorialele de C, dar se fac
recomandări împotriva abordării ei deoarece de cele mai multe ori duce la cod ofuscat
(greu de înțeles, întreținut și depanat). Există totuși cazuri în care este folosita.
În codul kernel-ului de Linux (exemplu), instrucțiunile de goto sunt folosite ca o formă
de try-catch din limbaje de nivel mai înalt (precum C++, Java, C#, etc.). Exemplu:

```C
int process_data_from_mouse_device(...)
{
    int err;
    int x, y;

    /* >>try<< instructions */
    err = init_communication_with_mouse();
    if (err)
        goto error;

    err = get_x_coord_from_mouse(&x);
    if (err)
        goto error;

    err = get_y_coord_from_mouse(&y);
    if (err)
        goto error;

    err = announce_upper_layers_of_mouse_movement(x, y);
    if (err)
        goto error;

    err = close_communication_with_mouse();
    if (err)
        goto error;

    return 0;

    /* >>catch<< instructions' exceptions */
error:
    print_message("Failed to get data from mouse device. Error = %d", err);
    return err;
}
```

Acest cod încearcă să proceseze datele venite de la un mouse și să le
paseze altor părți superioare din kernel care le-ar putea folosi. În caz că apare vreo
eroare, se afișează un mesaj de eroare și se termină procesarea datelor. Codul pare corect,
dar nu este complet. Nu este complet pentru că în caz că apare o eroare în mijlocul funcției,
comunicația cu mouse-ul este lăsată deschisă. O variantă îmbunătățită ar fi următoarea:

```C
int process_data_from_mouse_device(...)
{
    int err;
    int x, y;

    /* >>try<< instructions */
    err = init_communication_with_mouse();
    if (err)
        goto error;

    err = get_x_coord_from_mouse(&x);
    if (err)
        goto error_close_connection;

    err = get_y_coord_from_mouse(&y);
    if (err)
        goto error_close_connection;

    err = announce_upper_layers_of_mouse_movement(x, y);
    if (err)
        goto error_close_connection;

    err = close_communication_with_mouse();
    if (err)
        goto error;

    return 0;

    /* >>catch<< instructions' exceptions */
error_close_connection:
    close_communication_with_mouse();
error:
    print_message("Failed to get data from mouse device. Error = %d", err);
    return err;
}
```

În varianta îmbunătățită, dacă apare o eroare, se face și o parte de curățenie:
conexiunea cu mouse-ul va fi închisă, și apoi codul va continua cu tratarea generală a oricărei
erori din program (afișarea unui mesaj de eroare).

>**NOTE**: De ce abordează acest curs/laborator un astfel de subiect?<br>
Când vom studia limbajul de asamblare vom observa că o bună parte din workflow seamănă cu un program format din goto-uri,
chiar dacă majoritatea instrucțiunilor unui limbaj de nivel înalt, chiar și precum C, sunt inexistente. Gândirea și
programarea cu goto-uri ne pregătește pentru lucrul în limbajul de asamblare.

>**WARNING**: În orice alt caz, această formă de programare ar trebui evitată pe cât posibil.
![goto.png]( https://imgs.xkcd.com/comics/goto.png)

În cadrul laboratoarelor vom folosi:
- asamblorul [NASM](https://www.nasm.us/)
- linkerul din cadrul suitei gcc

Pentru analiza codului si debugging vom folosi `gdb` si `Ghidra`.

## Ghidra

**Ghidra** este o unealtă foarte utilă pentru investigarea programelor si `reverse engineering`.

#### Dezasamblare
Procesul de dezasamblare este utilizat pentru obținerea unui fișier care conține cod de asamblare,
pornind de la un fișier binar. Acest proces este întotdeauna posibil, deoarece codul mașină specific
procesorului are o corespondență directă cu codul de asamblare. De exemplu, operația `add eax, 0x14`,
prin care la valoarea registrului eax se adaugă 20, se reprezintă întotdeauna folosind codul
binar `83 c0 14`.


#### Decompilare
Utilitarul Ghidra poate fi folosit chiar și pentru decompilare. Decompilatorul poate fi folosit
pentru a obține codul sursă într-un limbaj (relativ) de nivel înalt, care atunci când va fi
compilat va produce un executabil al cărui comportament va fi la fel ca executabilul original.
Prin comparație, un dezasamblor traduce un program executabil în limbaj de asamblare în mod exact,
pentru că există relația de 1:1 între cod mașină și limbaj de asamblare.<br>

Veți utiliza cele două opțiuni în cadrul laboratorului de astăzi, pentru a analiza niște binare simple.

## Exerciții

>**WARNING**:
În cadrul laboratoarelor vom folosi repository-ul de git al materiei
IOCLA - [https://github.com/systems-cs-pub-ro/iocla](https://github.com/systems-cs-pub-ro/iocla).
Repository-ul este clonat pe desktop-ul
mașinii virtuale. Pentru a îl actualiza, folosiți comanda `git pull origin master` din interiorul
directorului în care se află repository-ul (`~/Desktop/iocla`). Recomandarea este să îl actualizați
cât mai frecvent, înainte să începeți lucrul, pentru a vă asigura că aveți versiunea cea mai recentă.
Dacă doriți să descărcați repository-ul în altă locație, folosiți comanda
`git clone https://github.com/systems-cs-pub-ro/iocla ${target}`.
Pentru mai multe informații despre folosirea utilitarului `git`, urmați ghidul de la [Git Immersion](https://gitimmersion.com/).

### 1. Online C Compiling

Un tool interesant pentru a observa cum se traduce codul C în limbaj de asamblare este Compiler Explorer.

1. Intrați pe [Compiler Explorer](https://gcc.godbolt.org/).
2. Încărcați programul “sum over array” din exemple (accesibile folosind butonul de load, în formă de dischetă).
3. Asigurați-vă că `x86-64 gcc 4.8.2` este selectat la `Compiler:`.
4. Folosiți opțiunea `-m32` (la `Compiler options`) pentru a afișa cod în limbaj de asamblare pe 32 de biți (față de 64 de biți în mod implicit).
5. Dacă vedeți mesajul `<Compilation failed>`, adăugați opțiunea `-std=c99`.
6. În continuare codul este destul de greoi. Pentru a putea fi mai human-readable adăugați opțiunea `-O2` la opțiunile de compilare (`Compiler options`).
7. Se poate observa existența simbolurilor `.L3:` și `.L4:`. Acestea reprezintă puncte fixe în program, label-uri, destul de asemănătoare cu ceea ce se găsește și în C.
8. Treceți, pe rând, prin compilatoarele corespunzătoare următoarelor arhitecturi: ARM, ARM64, AVR, PowerPC. `Atenție`: pentru ARM, ARM64 și AVR va trebuie să renunțați la flag-ul -m32 setat anterior. Se poate observa cum codul generat diferă de la o arhitectură la alta.
9. Mai încercați și următoarele compilatoare: `clang` și `icc`. După cum se poate observa, deși este același cod C și aceeași arhitectură, codul generat diferă. Acest lucru se întâmplă pentru că fiecare compilator poate avea o strategie de optimizare și generare de cod diferită.

>**NOTE**:
[clang](https://clang.llvm.org/) este un compilator open-source de C\C++. Adesea este folosit în IDE-uri datorită mesajelor de eroare de compilare foarte sugestive pe care le produce.

>**NOTE**: `icc` este compilatorul de C\C++ al celor de la compania Intel.


Scrieți în zona Code editor următoarea secvență de cod:
```C
int simple_fn(void)
{
    int a = 1;
    a++;
    return a;
}
```
Observați codul în limbaj de asamblare atunci când opțiunile de compilare (`Compiler options`) sunt `-m32`, respectiv atunci când opțiunile de compilare sunt `-m32 -O2`. Observați ce efect au opțiunile de optimizare asupra codului în limbaj de asamblare generat.


### 2. C: Warm-up GOTOs

Intrați în directorul `2-warm-up-gotos`.<br>

**2.1** Modificați codul sursă din fișierul `bogosort.c`, aflat în directorul `a-bogosort`, ([Bogosort](https://en.wikipedia.org/wiki/Bogosort)) prin înlocuirea instrucțiunii `break` cu o instrucțiune `goto` astfel încât funcționalitatea să se păstreze.

**2.2** În mod asemănător modificați instrucțiunea `continue` din `ignore_the_comments.c`, aflat în directorul `b-ignore_the_comments`, astfel încât funcționalitatea codului să se păstreze.


>**WARNING**: Când scrieți cod cu etichete (label-uri) țineți cont de următoarele recomandări de indentare:
- Nu indentați etichetele (label-urile). “Lipiți-le” de marginea din stânga a ecranului de editare.
- O etichetă este singură pe linie. Nu există cod după etichetă.
- Nu țineți cont de etichete în indetarea codului. Codul trebuie indendat în același mod și cu etichete și fără etichete.
- Puneți o linie liberă înaintea liniei care conține o etichetă.


>**NOTE**: [Caz](https://stackoverflow.com/questions/3517726/what-is-wrong-with-using-goto/3517765#3517765) în care goto poate fi util

### 3. C: GOTOs

Intrați în directorul `3-goto-algs`.<br>

Pentru algoritmii de mai jos scrieți cod în C fără a folosi:

- definiții / apeluri de funcţii (exceptând scanf() şi printf())
- else
- for
- while
- do {} while;
- construcțiile if care conțin return
- if-uri imbricate

Singura instrucțiune permisă în cadrul unui if este `goto`.

În alte cuvinte, tot codul trebuie să fie scris în interiorul funcției main, iar modificarea fluxului de control (saltul la altă zonă de cod) se face doar prin intermediul secvențelor de tipul `if (conditie) goto eticheta;` sau `goto eticheta;`.

**3.1** Implementați maximul dintr-un vector (`a-vector_max/vector_max.c`) folosind cod C și constrângerile de mai sus.

**3.2** Implementați căutare binară (`b-binary_search/binary_search.c`) folosind cod C și constrângerile de mai sus.

>**WARNING**: Reiterăm ideea că scenariile de utilizare ale instrucțiunii goto sunt limitate. Exercițiile acestea au valoare didactică pentru a vă acomoda cu instrucțiuni de salt (jump) pe care le vom folosi în dezvoltarea în limbaj de asamblare.

### 4. Tutorial Ghidra: Decompilare

Intrați în directorul `4-tutorial-ghidra`.<br>

În cadrul acestui exercițiu dorim să analizăm funcționalitatea unui binar simplu, care cere introducerea unei parole corecte pentru obținerea unei valori secrete.

>**WARNING**: Pentru a rula Ghidra, intrați într-o fereastră de terminal și utilizați comanda `ghidra`.

Pentru început, când rulăm Ghidra ne va apărea o fereastră cu proiectele noastre curente.

![ghidra-initial.png](assets/ghidra-initial.png)

Putem să creăm un nou proiect și să îi dăm un nume corespunzător. Pentru asta vom folosi: `File → New Project` (sau folosind combinația de taste `CTRL + N`).

![ghidra-added-project.png](assets/ghidra-added-project.png)

După ce am creat proiectul, ca să adăugăm fisierul executabil putem să folosim `File → Import file`, sau să tragem fișierul în directorul pe care l-am creat. Ghidra ne va sugera formatul pe care l-a detectat, precum și compilatorul folosit, în cazuri mai speciale probabil va trebui să schimbăm aceste configurări, dar pentru scopul acestui tutorial, ce ne sugerează Ghidra este perfect.

![ghidra-added-file.png](assets/ghidra-added-file.png)

Următorul pas este să analizăm binarul pe care l-am importat. Putem să apăsăm dublu click pe acesta. Ghidra ne va întreba daca vrem să îl analizăm. Pentru a face acest lucru, vom apăsa `Yes` și apoi `Analyze`.

![ghidra-analyzed.png](assets/ghidra-analyzed.png)

Dupa ce executabilul a fost analizat, Ghidra afișează o interpretare a informațiilor binare, care include și codul dezasamblat al programului. În continuare, putem de exemplu să încercam să decompilăm o funcție. În partea stângă a ferestrei avem secțiunea `Symbol Tree`; dacă deschidem `Functions`, putem observa că Ghidra ne-a detectat anumite funcții, chiar și funcmain-ul în cazul acestui binar. Astfel dacă dăm dublu click pe main, ne apare în dreapta funcția main decompilată și în fereastra centrală codul în limbajul de asamblare aferent.

![ghidra-main.png](assets/ghidra-main.png)

Putem să observăm acum că decompilarea nu este tocmai 1:1 cu codul sursă (din fișierul `crackme.c`), dar ne da o idee destul de bună a acestuia. Urmărind codul decompilat, observăm că funcția main are doi parametri de tip long, care se numesc `param_1` și `param_2`, în loc de prototipul normal `main(int argc, char *argv[])`. Al doilea parametru al main-ului este de tip “vector de pointeri către date de tip caracter” (care este interpretat în mod generic ca “vector de șiruri de caractere”). Mai jos este o perspectivă generică asupra modului de reprezentare al vectorului pentru un sistem de 64 de biți. În reprezentarea de pe a doua linie, interpretați `argp` ca fiind `char *argp = (char *)argv`, pentru a avea sens calculul `argp + N`.

| argv[0]  |      argv[1]  |  argv[2]  |
|----------|:-------------:|----------:|
|   argp   |    argp + 8   | argp + 16 |


Diferența de tip a parametrilor main-ului este una legată de interpretare: binarul este compilat pentru arhitectura amd64 (care este extensia arhitecturii x86 pentru 64 de biți), iar dimensiunea unui [cuvânt de procesor](https://en.wikipedia.org/wiki/Word_(computer_architecture)) este de 8 octeți (sau 64 de biți). Dimensiunea unui cuvânt de procesor se reflectă în dimensiunea unui pointer, dar și în dimensiunea unui parametru unic (dacă parametrul este mai mic de un cuvânt, se face automat extensia până la dimensiunea unui cuvânt). Totodată, printr-o coincidență, dimensiunea unei variabile de tip `long` este tot de 64 de biți (dimensiunile [tipurilor de date](https://en.wikipedia.org/wiki/C_data_types) în C nu sunt bine stabilite, fiind definite doar niște limite inferioare pentru date). Acest lucru face ca interpretarea celor doi parametri să fie ca `long`, deoarece toți parametrii, indiferent de tip (int sau pointer) se manipulează identic. Calculul `param_2 + 8` este folosit pentru a calcula adresa celui de-al doilea pointer din vectorul `argv` (adică `argv[1]`). Pentru un program compilat pentru arhitectura x86 de 32 de biți, adresa lui `argv[1]` ar fi fost `param_2 + 4`.

Folosind informațiile din codul decompilat putem să ne dăm seama că programul așteaptă o parolă ca argument și aceasta trebuie să fie din 8 caractere și caracterul de pe poziția 3 trebuie să fie 'E'. Deci putem să îi punem ca input o parolă de genul “AAAEAAAA”.

### 5. Reverse: Old hits

Intrați în directorul `5-old-hits`.<br>

Folosind informațiile noi dobândite despre `Ghidra`, dar și cele învățate anterior despre folosirea gdb, analizați binarul și obțineți informația secretă.
Programul generează o valoare aleatoare și vă cere să ghiciți o altă valoare calculată pe baza valorii aleatoare.<br>

Mult succes!
