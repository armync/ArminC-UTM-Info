# Laborator 09: Apeluri de funcții

În acest laborator vom prezenta modul în care se realizează apeluri de funcții. Vom vedea cum putem folosi instrucțiunile `call` și `ret` pentru a realiza apeluri de funcții și cum folosim stiva pentru a transmite parametrii unei funcții.

Laboratorul este de forma *learn by doing*, partea practică alternând între secțiuni de tip tutorial, cu parcurgere pas cu pas și prezentarea soluției, și exerciții care trebuie să fie rezolvate.


## Cunoștințe și abilități ce vor fi dobândite

- Traducerea apelului și implementării unei funcții din limbajul C în limbaj de asamblare
- Transmiterea parametrilor in diferite arhitecturi.
- Folosirea instrucțiunilor `call` și `ret` pentru a realiza un apel de funcție
- Implementarea unei funcții în limbaj de asamblare
- Folosirea stivei pentru a transmite parametrii unei funcții
- Apelarea unei funcții externe (aflată în biblioteca standard C) din limbaj de asamblare

## Transmiterea Parametrilor

Cand vine vorba de a chema o functie cu parametri exista doua mari optiuni de plasare a acestora:

1. **Plasarea in registre** - aceasta metoda, in mod intuitiv, presupune transmiterea parametrilor cu ajutorul registrelor.

    **Avantaje**

    - Este foarte usor de folosit atunci cand numarul parametrilor este mic.
    - Este foarte rapida, intrucat parametrii sunt imediat accesibili din registre.

    **Dezavantaje**

    - Din cauza faptului ca exista un numar limitat de registre, numarul de parametri ai unei functii ajunge sa fie limitat.
    - E foarte probabil ca unele registre sa fie folosite in interiorul functiei apelate si devine necesara salvarea temporara a registrelor pe stiva inaintea apeluluide functie. Astfel, cel de-al doilea avantaj enumerat dispare, deoarece accesul la stiva presupune lucru cu memoria, adica latenta crescuta.

2. **Plasarea pe stivă** - aceasta metoda presupune push-uirea pe stiva a tuturor parametrilor.
    **Avantaje**

    - Poate fi transmis un numar mare de parametri.

    **Dezavantaje**

    - Este lenta intrucat se face acces la memorie.
    - Mai complicata din punct de vedere al accesului la parametri.

> **_NOTE:_**  Pentru arhitecturiile **32-bit** se foloseste metoda plasarii pe stiva, iar pentru cele **64-bit** se foloseste metoda plasarii in registre. Noi vom folosi conventia de la 32-bit architecture.


## Apelul unei funcții

Atunci când apelăm o funcție, pașii sunt următorii:
  - Punem argumentele pe stivă, apelul de tip push fiind în ordinea inversă în care sunt trimiși ca argumente funcției.
  - Apelăm `call`.
  - Restaurăm stiva la sfârșitul apelului.


### Funcționarea stivei

După cum știm, operațiile pe stivă sunt de două tipuri:

- `push val` în care valoarea `val` este plasată pe stivă
- `pop reg/mem` în care ce se găsește în vârful stivei se plasează în registru sau într-o zonă de memorie

În momentul în care se face `push` spunem că stiva **crește** (se adaugă elemente). Din motive ce vor fi explicate mai bine la SO, pointerul de stivă (indicat de registrul `esp` pe 32 de biți) scade in valoare atunci cand **stiva creste** (la `push`). Putem spune totusi ca aceasta contrazicere in numire vine de la faptul ca stiva este deregula reprezentata pe verticala si valorile mici se afla sus, iar valorile mari se afla jos.

La fel, în momentul în care facem `pop` spunem că stiva **scade** (se scot elemente). Acum pointer-ul de stivă (indicat de registrul `esp` pe 32 de biți) crește valoric.

Un sumar al acestui lucru este explicat foarte bine la acest [link](https://en.wikibooks.org/wiki/X86_Disassembly/The_Stack).

Spre exemplu, daca avem functia foo cu urmatoarea semnatura (in limbaj C):
```C
int foo(int a, int b, int c);
```
Apelul acestei functii va arata astfel:
```Assembly
mov ecx, [c]     ; luam valoarea parametrului c dintr-o zona de memorie
mov ebx, [b]
mov eax, [a]

push ecx         ; punem parametrii in ordine inversa, incepand cu c
push ebx         ; apoi b
push eax         ; apoi a
call foo         ; apelam functia
add esp, 12      ; restauram stiva
```

## Apelantul si Apelatul
Atunci când apelăm o funcție spunem că funcția care apelează (contextul care apelează) se cheamă **apelant** (sau **caller**), iar funcția apelată se cheamă **apelat** (sau **callee**). In paragraful anterior am discutat despre cum arată lucrurile la nivelul apelantului (cum construim stiva).

 Haideți să urmărim ce se întâmplă si la la nivelul apelatului. Până în momentul instrucțiunii `call` stiva conține parametrii funcției. Apelul `call` poate fi echivalat grosier următoarei secvențe:
```Assembly
push eip
jmp function_name
```

Adică și apelul `call` folosește în continuare stiva și salvează adresa următoarei instrucțiuni, cea de după `call` numită și instrucțiunea de retur sau adresa de retur (return address). Aceasta este necesară pentru a ști, în apelat, unde să revenim în apelant.


În apelat, la începutul său (numit preambul, preamble) se salvează frame pointer-ul (în arhitectura i386 este vorba de registrul `ebp`) urmând ca frame pointer-ul să refere adresa curentă de pe stivă (adică tocmai fostul frame pointer). Deși nu este obligatorie, salvarea frame pointer-ului ajută la debugging și este în cele mai multe cazuri folosită. Din aceste motive, orice apel de funcție va avea în general, preambulul:
```Assembly
push ebp
mov ebp, esp
```

Aceste modificări au loc în apelat. De aceea este responsabilitatea acestuia să restaureze stiva la vechea sa valoare. De aceea este uzuală existența unui epilog care să readucă stiva la starea sa inițială; acest epilog este:
```Assembly
leave
```
Dupa aceasta instructiune, stiva este ca la începutul funcției (adică imediat după call).

Pentru incheierea functiei, este necesar ca executia codului sa se intoarca (return) si sa continue sa execute de la instructiunea de dupa `call`-ul care a pornit functia. Acest lucru presupune sa influentam registrul `eip` si sa punem valoarea care a fost salvata pe stiva initial de apelul `call`. Acest lucru este indeplinit folosind instructiunea:
```Assembly
ret
```
care este grosier echivalentul instrucțiunii:
```Assembly
pop eip
```


Spre exemplu, definitia si corpul functiei foo, care realizeaza suma a 3 numere, vor arata astfel:

```Assembly
foo:
    push ebp
    mov ebp, esp

    mov eax, [ebp + 8]
    mov ebx, [ebp + 12]
    mov ecx, [ebp + 16]

    add eax, ebx
    add eax, ecx

    leave
    ret
```

### Remarcati:

1. O functie se defineste printr-un label.

2. Dupa preambulul functiei, stiva arata in felul urmator:

![function_stack1.jpg](./images/function_stack1.jpg)

3. De observat că pe parcursul execuției funcției, ceea ce nu se schimbă este poziția frame pointer-ul. Acesta este și motivul denumirii sale: pointează la frame-ul curent al funcției. De aceea este comun ca accesarea parametrilor unei funcții să se realizeze prin intermediul frame pointer-ului. Presupunând un sistem pe 32 de biți și parametri de dimensiunea cuvântului procesorului (32 de biți, 4 octeți) vom avea:

  - primul argument se găsește la adresa `ebp+8`
  - al doilea argument se găsește la adresa `ebp+12`
  - al treilea argument se găsește la adresa `ebp+16`
  - etc

    Acesta este motivul pentru care, pentru a obține parametrii funcției foo în registrele eax, ebx, ecx, folosim construcțiile:
```Assembly
    mov eax, dword [ebp+8]   ; primul argument in eax
    mov ebx, dword [ebp+12]  ; al doilea argument in ebx
    mov ecx, dword [ebp+16]  ; al treilea argument in ecx
```

4. Valoare de retur a unei functii se plaseaza in registre (in general in eax).
  - Daca valoarea de retur este pe **8 biti** rezultatul functiei se plaseaza in `al`.
  - Daca valoarea de retur este pe **16 biti** rezultatul functiei se plaseaza in `ax`.
  - Daca valoarea de retur este pe **32 biti** rezultatul functiei se plaseaza in `eax`.
  - Daca valoarea de retur este pe **64 biti** rezultatul se plaseaza in registrele `edx` si `eax`. Cei mai semnificativi 32 de biti se plaseaza in `edx`, iar restul in registrul `eax`.

    *De asemnea, in unele cazuri, se poate returna o adresa de memorie catre stiva/heap, sau alte zone de memorie, care refera obiectul dorit in urma apelului functiei.*

5. O functie foloseste aceleasi registre hardware, asadar, la iesirea din functie valorile registrelor nu mai sunt aceleasi. Pentru a evita aceasta situatie, se pot salva unele/toate registrele pe stiva.


> **_NOTE:_**  Deoarece limbajele de asamblare ofera mai multe oportunitati, exista necesitatea de a avea conventii de apelare a functiilor in x86. Diferenta dintre acestea poate consta in ordinea parametrilor, modul cum parametrii sunt pasati functiei, ce registre trebuiesc conservate de apelat sau daca apelantul ori apelatul se ocupa de pregatirea stivei. Mai multe detalii puteti gasi [aici](https://en.wikipedia.org/wiki/X86_calling_conventions) sau [aici](https://levelup.gitconnected.com/x86-calling-conventions-a34812afe097) daca wikipedia e prea mainstream pentru voi.

## Exerciții

> **_IMPORTANT:_**  În cadrul laboratoarelor vom folosi repository-ul de git al materiei [IOCLA](https://github.com/systems-cs-pub-ro/iocla). Repository-ul este clonat pe desktop-ul mașinii virtuale. Pentru a îl actualiza, folosiți comanda `git pull origin master` din interiorul directorului în care se află repository-ul (`~/Desktop/iocla`). Recomandarea este să îl actualizați cât mai frecvent, înainte să începeți lucrul, pentru a vă asigura că aveți versiunea cea mai recentă.Dacă doriți să descărcați repository-ul în altă locație, folosiți comanda `git clone https://github.com/systems-cs-pub-ro/iocla ${target}`. Pentru mai multe informații despre folosirea utilitarului git, urmați ghidul de la [Git Immersion](https://gitimmersion.com/)


### 0. Recapitulare: Șirul lui Fibonacci

Completați fișierul `fibo.asm` din arhivă pentru a realiza un program care afișează primele N numere din șirul lui Fibonacci.

Aveți voie să folosiți doar memorie alocată pe stivă.


### 1. Hello, world!

Deschideți fișierul `hello-world.asm`, asamblați-l și rulați-l. Observați afișarea mesajului *Hello, world!*

Remarcați că:

  - Programul `hello-world.asm` folosește apelul funcției `puts` (funcție externă modulului curent) pentru a efectua afișarea. Pentru aceasta pune argumentul pe stivă și apelează funcția.
  - Variabila `msg` din programul `hello-world.asm` conține octetul `10`. Acesta simbolizează caracterul *line-feed* (`\n`), folosit pentru a adăuga o linie nouă pe Linux.

Încheierea cu `\n` este, în general, utilă pentru afișarea șirurilor. Funcția `puts` pune automat o linie nouă după șirul afișat, însă aceasta trebuie adăugată explicit în cazul folosirii funcției `printf`.


### 2. Dezasamblarea unui program scris în C

După cum spuneam, în final, totul ajunge în limbaj de asamblare (ca să fim 100% corecți, totul ajunge cod mașină care are o corespondență destul de bună cu codul asamblare). Adesea ajungem să avem acces doar la codul obiect al unor programe și vrem să inspectăm modul în care arată.

Pentru a observa acest lucru, haideți să compilăm până la codul obiect un program scris în C și apoi să-l dezasamblăm. Este vorba de programul `test.c` din arhiva de laborator.

> **_NOTE:_**  Pentru a compila un fișier cod sursă C/C++ în linia de comandă, urmați pașii:
>
> 1. Deschideți un terminal. (shortcut `Ctrl+Alt+T`)
> 2. Accesați directorul în care aveți codul sursă.
> 3. Folosiți comanda
> ```Bash
> gcc -m32 -o <executabil> <nume-fisier>
> ```
> unde `<nume-fisier>` este numele fișierului iar `<executabil>` este executabilul rezultat.
>
> 1. Dacă doriți **doar** să compilați fișierul (**fără** să-l link-ați), atunci folosiți comanda
> ```Bash
> gcc -m32 -c -o <fisier-obiect> <nume-fisier>
> ```
> unde `<nume-fisier>` este numele fișierului iar `<fisier-obiect>` este fișierul obiect rezultat.

În cazul nostru, întrucât dorim doar să compilăm fișierul `test.c` la modulul obiect, vom accesa din terminal directorul în care se găsește fișierul și apoi vom rula comanda
```Bash
gcc -m32 -c -o test.o test.c
```
În urma rulării comenzii de mai sus în directorul curent vom avea fișierul obiect `test.o`.

Putem obține și forma în limbaj de asamblare a acestuia folosind comanda
```Bash
gcc -m32 -masm=intel -S -o test.asm test.c
```

În urma rulării comenzii de mai sus obținem fișierul `test.asm` pe care îl putem vizualiza folosind comanda
```Bash
cat test.asm
```

Pentru a dezasambla codul unui modul obiect vom folosi un utilitar frecvent întâlnit în lumea Unix: `objdump`. Pentru dezasamblare, vom rula comanda
```Bash
objdump -M intel -d <path-to-obj-file>
```
unde `<path-to-obj-file>` este calea către fișierul obiect `test.o`.

Veți obține un output similar celui de mai jos
```Bash
$ objdump -M intel -d test.o

test.o:     file format elf32-i386

Disassembly of section .text:

0000054d <second_func>:
 54d:   55                      push   ebp
 54e:   89 e5                   mov    ebp,esp
 550:   e8 a6 00 00 00          call   5fb <__x86.get_pc_thunk.ax>
 555:   05 ab 1a 00 00          add    eax,0x1aab
 55a:   8b 45 08                mov    eax,DWORD PTR [ebp+0x8]
 55d:   8b 10                   mov    edx,DWORD PTR [eax]
 55f:   8b 45 0c                mov    eax,DWORD PTR [ebp+0xc]
 562:   01 c2                   add    edx,eax
 564:   8b 45 08                mov    eax,DWORD PTR [ebp+0x8]
 567:   89 10                   mov    DWORD PTR [eax],edx
 569:   90                      nop
 56a:   5d                      pop    ebp
 56b:   c3                      ret

0000056c <first_func>:
 56c:   55                      push   ebp
 56d:   89 e5                   mov    ebp,esp
 56f:   53                      push   ebx
 570:   83 ec 14                sub    esp,0x14
 573:   e8 83 00 00 00          call   5fb <__x86.get_pc_thunk.ax>
 578:   05 88 1a 00 00          add    eax,0x1a88
 57d:   c7 45 f4 03 00 00 00    mov    DWORD PTR [ebp-0xc],0x3
 584:   83 ec 0c                sub    esp,0xc
 587:   8d 90 80 e6 ff ff       lea    edx,[eax-0x1980]
 58d:   52                      push   edx
 58e:   89 c3                   mov    ebx,eax
 590:   e8 4b fe ff ff          call   3e0 <puts@plt>
 595:   83 c4 10                add    esp,0x10
 598:   83 ec 08                sub    esp,0x8
 59b:   ff 75 f4                push   DWORD PTR [ebp-0xc]
 59e:   8d 45 08                lea    eax,[ebp+0x8]
 5a1:   50                      push   eax
 5a2:   e8 a6 ff ff ff          call   54d <second_func>
 5a7:   83 c4 10                add    esp,0x10
 5aa:   8b 45 08                mov    eax,DWORD PTR [ebp+0x8]
 5ad:   8b 5d fc                mov    ebx,DWORD PTR [ebp-0x4]
 5b0:   c9                      leave
 5b1:   c3                      ret

000005b2 <main>:
 5b2:   8d 4c 24 04             lea    ecx,[esp+0x4]
 5b6:   83 e4 f0                and    esp,0xfffffff0
 5b9:   ff 71 fc                push   DWORD PTR [ecx-0x4]
 5bc:   55                      push   ebp
 5bd:   89 e5                   mov    ebp,esp
 5bf:   53                      push   ebx
 5c0:   51                      push   ecx
 5c1:   e8 8a fe ff ff          call   450 <__x86.get_pc_thunk.bx>
 5c6:   81 c3 3a 1a 00 00       add    ebx,0x1a3a
 5cc:   83 ec 0c                sub    esp,0xc
 5cf:   6a 0f                   push   0xf
 5d1:   e8 96 ff ff ff          call   56c <first_func>
 5d6:   83 c4 10                add    esp,0x10
 5d9:   83 ec 08                sub    esp,0x8
 5dc:   50                      push   eax
 5dd:   8d 83 8e e6 ff ff       lea    eax,[ebx-0x1972]
 5e3:   50                      push   eax
 5e4:   e8 e7 fd ff ff          call   3d0 <printf@plt>
 5e9:   83 c4 10                add    esp,0x10
 5ec:   b8 00 00 00 00          mov    eax,0x0
 5f1:   8d 65 f8                lea    esp,[ebp-0x8]
 5f4:   59                      pop    ecx
 5f5:   5b                      pop    ebx
 5f6:   5d                      pop    ebp
 5f7:   8d 61 fc                lea    esp,[ecx-0x4]
 5fa:   c3                      ret
```

Există multe alte utilitare care permit dezasamblare de module obiect, majoritatea cu interfața grafică și oferind și suport pentru debugging. `objdump` este un utilitar simplu care poate fi rapid folosit în linia de comandă.

Este interesant de urmărit, atât în fișierul `test.asm` cât și în dezasamblarea sa, modul în care se face un apel de funcție, lucru despre care vom discuta în continuare.

### 3. Afișarea unui șir

Pentru afișarea unui string putem folosi macro-ul intern `PRINTF32`. Sau putem folosi o funcție precum `puts`. În fișierul `print-string.asm` este implementată afișarea unui string folosind macro-ul `PRINTF32`.

Urmărind fișierul `hello-world.asm` ca exemplu, implementați afișarea șirului folosind și `puts`.

> **_NOTE:_**  Urmăriți și indicațiile din secțiunea *"Apelul unei funcții"*.

### 4. Afișarea lungimii unui șir
Programul `print-string-len.asm` afișează lungimea unui șir folosind macro-ul `PRINTF32`. Calculul lungimii șirului `mystring` are loc în cadrul programului (este deja implementat).

Implementați programul pentru a face afișarea lungimii șirului folosind funcția `printf`.

La sfârșit veți avea afișată de două ori lungimea șirului: inițial cu apelul macro-ului `PRINTF32` și apoi cu apelul funcției externe `printf`.

> **_NOTE:_**  Gândiți-vă că apelul `printf` este de forma `printf("String length is %u\n", len);`. Trebuie să construiți stiva pentru acest apel.
>
> Pașii de urmat sunt:
>
> 1. Marcarea simbolului `printf` ca simbol extern.
> 2. Definirea șirului de formatare `"String length is %u", 10, 0`.
> 3. Realizarea apelului funcției `printf`, adică:
>     1. Punerea celor două argumente pe stivă: șirul de formatarea și lungimea.
>     2. Apelul `printf` folosind `call`.
>     3. Restaurarea stivei.
>
> Lungimea șirului se găsește în registrul `ecx`.

### 5. Afișarea șirului inversat

În fișierul `print-rev-string.asm` adăugați funcția `reverse_string` astfel încât să aveți un listing similar celui de mai jos:
```Assembly
[...]
section .text
global main

reverse_string:
    push ebp
    mov ebp, esp

    mov eax, dword [ebp+8]
    mov ecx, dword [ebp+12]
    add eax, ecx
    dec eax
    mov edx, dword [ebp+16]

copy_one_byte:
    mov bl, byte [eax]
    mov byte [edx], bl
    dec eax
    inc edx
    loopnz copy_one_byte

    inc edx
    mov byte [edx], 0

    leave
    ret

main:
    push ebp
    mov ebp, esp
[...]
```
> **_IMPORTANT:_**  Când copiați funcția `reverse_string` în programul vostru, rețineți că fucția începe la eticheta `reverse_string` și se oprește la eticheta `main`. Eticheta `copy_one_byte` este parte a funcției `reverse_string`.

Funcția `reverse_string` inversează un șir și are următoarea signatură: `void reverse_string(const char *src, size_t len, char *dst);`. Astfel ca primele `len` caractere și șirul `src` sunt inversate în șirul `dst`.

Realizați inversarea șirului `mystring` într-un nou șir și afișați acel nou șir.

> **_NOTE:_**  Pentru a defini un nou șir, recomandăm ca, în secțiunea de date să folosiți construcția
> ```Assembly
> store_string times 64 db 0
> ```
> Construcția creează un șir de 64 de octeți de zero, suficient pentru a stoca inversul șirului.
> Apelul echivalent în C al funcției este `reverse_string(mystring, ecx, store_string);`. În registrul `ecx` am presupus că este calculată lungimea șirului.
>
> Nu puteți folosi direct valoarea `ecx` în forma ei curentă. După apelul funcției `printf` pentru afișare numărului valoarea `ecx` se pierde. Ca să o păstrați, aveți două opțiuni:
> 1. Stocați valoarea registrului `ecx` în prealabil pe stivă (folosind `push ecx` înaintea apelului `printf`) și apoi să o restaurați după apelul `printf` (folosind `pop ecx`).
> 2. Stocați valoarea registrului `ecx` într-o variabilă globală, pe care o definiți în secțiunea `.data`.
>
> Nu puteți folosi un alt registru pentru că sunt șanse foarte mari ca și acel registru să fie modificat de apelul `printf` pentru afișarea lungimii șirului.

### 6. Implementarea funcției toupper

Ne propunem implementarea funcției `toupper` care traduce literele mici în litere mari. Pentru aceasta, porniți de la fișierul `toupper.asm` din arhiva de exerciții a laboratorului și completați corpul funcției `toupper`.

Șirul folosit este `mystring` și presupunem că este un șir valid. Acest șir este transmis ca argument funcției `toupper` în momentul apelului.

Faceți înlocuirea *in place*, nu este nevoie de un alt șir.

> **_NOTE:_**  Ca să traduceți o litera mică în literă mare, trebuie să **scădeți** `0x20` din valoare. Aceasta este diferența între litere mici și mari; de exemplu `a` este `0x61` iar `A` este `0x41`. Puteți vedea în [pagina de manual ascii](http://man7.org/linux/man-pages/man7/ascii.7.html).
>
> a să citiți sau să scrieți octet cu octet folosiți construcția `byte [reg]` așa cum apare și în implementarea determinării lungimii unui șir în fișierul `print-string-len.asm`, unde `[reg]` este registrul de tip pointer în care este stocată adresa șirului în acel punct.
>
> Vă opriți atunci când ați ajuns la valoarea `0` (`NULL` byte). Pentru verificare puteți folosi `test` așa cum se întâmplă și în implementarea determinării lungimii unui șir în fișierul `print-string-len.asm`.

### Bonus: toupper doar pentru litere mici

Implementați funcția `toupper` astfel încât translatarea să aibă loc doar pentru caractare reprezentând litere mici, nu litere mari sau alte tipuri de caractere.

### Bonus: rot13

Realizați și folosiți o funcție care face translatarea [rot13](https://rot13.com/) a unui șir.

### Bonus: rot13++

Implementați `rot13` pe un array de șiruri: șirurile sunt continue în memorie separate prin terminatorul de șir (`NULL`-byte, `0`). De exemplu: `ana\0are\0mere\0` este un array de trei șiruri.

Aplicați `rot13` pe caracterele alfabetice și înlocuiți terminatorul de șir cu spațiu (`' '`, blank, caracterul `32` sau `0x20`). Astfel, șirul inițial `ana\0are\0mere\0` se va traduce în `nan ner zrer`.

> **_NOTE:_**  Pentru a defini array-ul de șiruri care să conțină terminatorul de șir, folosiți o construcție de forma:
> ```Assembly
> mystring db "ana", 0, "are", 0, "mere", 0
> ```

> **_NOTE:_**  Va trebui să știți când sa vă opriți din parcurgerea array-ului de șiruri. Cel mai simplu este să definiți o variabilă de lungime în secțiunea `.data`, de forma
> ```Assembly
> len dd 10
> ```
> în care să rețineți fie lungimea totală a șirului (de la începutul până la ultimul `NULL`-byte), fie numărul de șiruri din array.

## Alte resurse
- [nasm](http://www.nasm.us/)