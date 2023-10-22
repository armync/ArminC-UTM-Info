# Laborator 12: CTF

În acest laborator veți interacționa cu majoritatea noțiunilor prezentate pe parcursul semestrului prin intermediul unor taskuri de tip `Capture-The-Flag`. Acestea vor testa înțelegerea și stăpânirea metodelor și toolurilor specifice de analiză statică și dinamică, înțelegerea procesului de compilare, a limbajului de asamblare - sintaxă, regiștri, lucru cu memoria, funcții - dar și capacitatea de identificare și exploatare a unor vulnerabilități simple de tip buffer overflow.

## Exerciții

> **NOTE:** Fiecare dintre exerciții ascunde un flag cu formatul `iocla_{<string>}`

> **TIP:** În general, flagul va fi returnat ca și string de o funcție specială, `get_flag()`. Scopul exercițiilor nu implică a face reverse-engineering pe această funcție sau apel direct din cadrul debuggerului; se recomandă tratarea ei ca și Black Box.

> **TIP:** Pentru generarea payloadurilor la taskurile de tip buffer overflow, puteți folosi în terminal o comandă de tipul: `python -c 'import sys; sys.stdout.write("A"\*10 + b"\x00\x00\x00\x00" + ...)' | ./exec`.

### 1.1. Hidden in plain sight
Binarul `1-1-hidden-in-plain-sight/link` expune tot ce aveți nevoie. Găsiți un mod de a-l folosi.
> **TIP:** If you want a main function to be done right, you gotta do it yourself.

### 1.2. Hidden in plain sight ++
Investigați binarul `1-2-hidden-in-plain-sight/link2`. Modul în care poate fi executat nu mai este un mister, dar va fi puțin mai dificil să ajungeți la flag.
> **TIP:** Nu toate funcțiile sunt private.

### 2. Look at him go
Binarul `2-look-at-him-go/dynamic` este de data aceasta executabil și are ca unic scop obținerea flagului și plasarea lui undeva in memorie. No tricks here.
> **TIP:** GDB is your friend.

### 3. Playing God
Binarul `3-playing-god/dynamic2` vă cere să ghiciți un număr între 1 și 100000. Găsiți o cale mai bună de a-l afla.

### 4. Indirect business
Binarul `4-indirect-business/buff-ovf` conține o vulnerabilitate clasică. Folosiți inputul pentru a modifica datele în favoarea voastră.

### 5. RIP my buffers off
Binarul `5-rip-my-buffers-off/buff-ovf2` nu folosește funcția get\_flag(), dar oferă o oportunitate de a o apela.
> **TIP:** Unde se poate suprascrie o adresă de funcție?

### 6. Feeling chained
Urmăriți șirul de operații din funcțiile binarului `6-feeling-chained/buff-ovf3`. Identificați-le pe cele necesare și... deja știți cum se apelează.

## Bonus
### 7. ROP
`7-rop/rop` este un binar pe 64 de biți cu un simplu buffer overflow.

> **TIP:** Pe x86\_64 argumentele funcțiilor nu se mai găsesc pe stivă, ci în registre.

> **TIP:** Return-Oriented-Programming (ROP) este o tehnică de exploatare în care, având posibilitatea de a suprascrie adresa de return, executăm prin înlănțuire diverse porțiuni din codul existent, care se termină într-o instrucțiune `ret`. Aceste bucăți de cod se numesc `gadgeturi`.

> **TIP:** Pentru determinarea adresei unui gadget într-un binar, există tool-ul [ROPgadget](https://github.com/JonathanSalwan/ROPgadget). Alternativ, în `pwndbg`, puteți folosi o comandă de tipul `rop --grep "pop rsi"`.
