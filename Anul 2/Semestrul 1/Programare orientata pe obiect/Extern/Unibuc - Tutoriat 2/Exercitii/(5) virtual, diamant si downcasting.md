# Exerciții rezolvate tutoriat 5

### Pentru fiecare dintre programele de mai jos, supneți dacă sunt corecte. În caz afirmativ, spuneți ce afișează, în caz negativ spuneți ce nu este corect și ce ați corecta.

1. Exercitiul 1
```C++
class B
{
protected:
    int x;
public:
    B() { x = 78; }
};
class D1 : virtual public B
{
public:
    D1() { x = 15; }
};
class D2 : virtual public B
{
public:
    D2() { x = 37; }
};
class C : public D2, public D1
{
public:
    int get_x() { return x; }
};
int main()
{
    C ob;
    cout << ob.get_x();
    return 0;
}
```

R: compileaza, afiseaza: 15

Explicatie: Clasa ```C``` mosteneste ```D2``` si ```D1``` in aceasta ordine, deci aceasta va fi si ordinea constructorilor apelati la mostenire: ```B -> D2 -> D1 -> C```. Astfel valoarea lui ```x``` se schimba in felul urmator: ```x = 78 -> 37 -> 15```.

2. Exercitiul 2
```C++
class A
{
public:
    int x;
    A(int i = 0) { x = i; }
    virtual A minus() { return (1 - x); }
};
class B : public A
{
public:
    B(int i = 0) { x = i; }
    void afisare() { cout << x; }
};
int main()
{
    A *p1 = new B(18); 
    *p1 = p1->minus(); 
    p1->afisare();
    return 0;
}
```

R: eroare de compilare

Explicatie: prin intermediul lui ```p1``` se produce upcasting, deci ```p1``` va apela doar metodele din clasa de baza (```A```). In clasa ```A``` nu este definita si metoda ```afisare```, deci va produce o eroare de compilare apelul ei din ```main```.

Cele doua posibile rezolvari sunt:
1. Adaugam o metoda ```void afisare()``` si in clasa ```A```.
2. Folosim operatorul ```dynamic_cast<>()```(deoarece in clasa de baza exista cel putin o metoda virtuala) pentru apelul metodei ```afisare()``` din ```main```.

Ambele vor avea ca rezultat ```1-x```(din apelul metodei ```minus```), adica ```-17```.

```C++
// Varianta 1
class A
{
public:
    int x;
    A(int i = 0) { x = i; }
    virtual A minus() { return (1 - x); }
    void afisare() { cout << x; }
};
class B : public A
{
public:
    B(int i = 0) { x = i; }
    void afisare() { cout << x; }
};
int main()
{
    A *p1 = new B(18); // x= 18
    *p1 = p1->minus(); // rezultat: A(x = -17)
    p1->afisare(); // -17
    return 0;
}

// Varianta 2
class A
{
public:
    int x;
    A(int i = 0) { x = i; }
    virtual A minus() { return (1 - x); }
};
class B : public A
{
public:
    B(int i = 0) { x = i; }
    void afisare() { cout << x; }
};
int main()
{
    A *p1 = new B(18); // x= 18
    *p1 = p1->minus(); // rezultat: A(x = -17)
    dynamic_cast< B* >(p1)->afisare(); // -17
    return 0;
}
```

3. Exercitiul 3
```C++
class A
{
public:
    int x;
    A(int i = 0) { x = i; }
    virtual A minus() { cout << x; }
};
class B : public A
{
public:
    B(int i = 0) { x = i; }
    void afisare() { cout << x; }
};
int main()
{
    A *p1 = new A(18); // NU este upcasting
    *p1 = p1->minus();
    dynamic_cast<B *>(p1)->afisare();
    return 0;
}
```

R: eroare la rulare(runtime): ```Segmentation fault```(apare de obicei cand sunt apeluri facute prin obiecte/prointeri/referinte ```NULL```)

Explicatie: Programul compileaza, afiseaza valoarea ```18``` in urma apelului metodei ```minus```, dar castarea nu se realizeaza cu succes, deorece programul nu ppoate converti un obiect din memorie de tipul ```A```, in ceva de tipul ```B```. Castingul ar fi fost realizat cu succes daca prin ```p1``` s-ar fi realizat upcasting: ```A *p1 = new B(18)```. Astfel, secventa ```dynamic_cast<B *>(p1)``` va avea valoarea ```NULL``` la rularea programului, deci ```NULL -> afisare();``` nu se poate realiza si implicit programul se va opri.

Ca programul sa nu mai aiba erori la rulare, folosim procedeul de upcasting prin ```p1``` : ``` A *p1 = new B(18);```. Rezultatul afisat va fi o valoare random data de compilator, deoarece functia minus returneaza un obiect random din memorie de tipul ```A```, neintializat in vreun fel (nu apare ```return ...```).

```C++
class A
{
public:
    int x;
    A(int i = 0) { x = i; }
    virtual A minus() { cout << x; }
};
class B : public A
{
public:
    B(int i = 0) { x = i; }
    void afisare() { cout << x; }
};
int main()
{
    A *p1 = new B(18); // x = 18 
    *p1 = p1->minus(); // obiect random 
    dynamic_cast<B *>(p1)->afisare(); // valoare random 
    return 0;
}
```

4. Exercitiul 4
```C++
class A
{
public:
    int x;
    A(int i = 13) { x = i; }
};
class B : virtual public A
{
public:
    B(int i = 15) { x = i; }
};
class C : virtual public A
{
public:
    C(int i = 17) { x = i; }
};
class D : public A
{
public:
    D(int i = 19){x = i;}
};
class E : public B, public C, public D
{
public:
    int y;
    E(int i, int j) : D(i), B(j){y = x + i + j;}
    E(E &e) { y = -e.y; }
};
int main()
{
    E e1(1, 2), e2 = e1;
    cout << e2.y;
    return 0;
}
```

R: eroare de compilare

Explicatie: Mostenire multipla, de tip diamant, cu 3 clase. ```B``` si ```C``` sunt mostenite ```virtual public```, dar ```C``` este doar de tip ```public```. Deci, in clasa ```E```, compilatorul nu stie catre care ```x```  sa faca referire: cel venit pe ramura ```B-C``` (comun pentru ca au mostenire virtuala din ```B```) sau cel venit pe ramura mostenirii lui ```D```.

```
Schema mostenirii:

                     A
               /     |       \
        (v) B      (v) C       D
               \     |       /
                     E


```
Problema se rezolva prin adaugarea keyword-ului ```virtual``` si la mostenirea clasei ```D```. Va compila si afisa valoarea ```-4```.

```C++
class A
{
public:
    int x;
    A(int i = 13) { x = i; }
};
class B : virtual public A
{
public:
    B(int i = 15) { x = i; }
};
class C : virtual public A
{
public:
    C(int i = 17) { x = i; }
};
class D : virtual public A
{
public:
    D(int i = 19){x = i;}
};
class E : public B, public C, public D
{
public:
    int y;
    E(int i, int j) : D(i), B(j){y = x + i + j;}
    E(E &e) { y = -e.y; }
};
int main()
{
    E e1(1, 2), e2 = e1;
    cout << e2.y; // -4
    return 0;
}
```
