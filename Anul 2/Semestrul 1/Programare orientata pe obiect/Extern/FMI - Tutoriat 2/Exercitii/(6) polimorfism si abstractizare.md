# Exerciții rezolvate tutoriat 7

### Pentru fiecare dintre programele de mai jos, supneți dacă sunt corecte. În caz afirmativ, spuneți ce afișează, în caz negativ spuneți ce nu este corect și ce ați corecta.

1. Exercitiul 1
```C++
class P
{
public:
    virtual void show() = 0;
};
class Q : public P
{
    int x;
};
int main()
{
    Q q;
    return 0;
}
```

R: nu compileaza

Explicatie: Metoda ```show()``` din clasa de baza ```P``` este declarata ca fiind pur virtuala, deci pentru ca clasa derivata sa poata fi instantiata, are nevoie de o implementare in clasa derivata.

Solutie: Declaram functia ```show()``` din clasa de baza ca fiind doar virtuala.

```PS```: Nu este de ajuns sa eliminati ```= 0``` deoarece compilatorul va vedea metoda tot ca fiind lipsita de implementare. Trebuie adaugate si acoladele ```{}```. Programul compileaza si nu afiseaza nimic.

```C++
class P
{
public:
    virtual void show() {};
};
class Q : public P
{
    int x;
};
int main()
{
    Q q;
    return 0;
}
```

2. Exercitiul 2
```C++
class A
{
public:
    virtual void fun() { cout << "A" << endl; }
};
class B : public A
{
public:
    virtual void fun() { cout << "B" << endl; }
};
class C : public B
{
public:
    virtual void fun() { cout << "C" << endl; }
};
int main()
{
    A *a = new C;
    A *b = new B;
    a->fun();
    b->fun();
    return 0;
}
```

R: compileaza si afiseaza:
``` 
    C
    B
```

Explicatie: ```A``` este clasa de baza pentru ```B```, dar si pentru ```C```. Keyword-ul ```virtual``` din cele 2 clase derivate poate fi ignorat, deoarece are efect numai in clasa de baza. Metoda virtuala (din clasa de baza), suprascrisa la mostenire si apelata printr-un pointer in care se realizeaza procedeul de upcasting(```A *a = new C;``` si ```A *b = new B;```), va fi cea din clasa derivata.

3. Exercitiul 3
```C++
class A
{
protected:
    int x;
public:
    A(int i = -16) { x = i; }
    virtual A f(A a) { return x + a.x; }
    void afisare() { cout << x; }
};
class B : public A
{
public:
    B(int i = 3) : A(i) {}
    A f(A a) { return x + a.x + 1; }
};
int main()
{
    A *p1 = new B, *p2 = new A, *p3 = new A(p1->f(*p2));
    p3->afisare();
    return 0;
}
```

R: nu compileaza.

Explicatie: Chiar daca ```x``` in clasa de baza este ```prodected```, si mostenirea este de tip ```public```, in clasa ```B```, ```x``` este accesibil. In metoda ```f``` din clasa ```B```, instructiunea ```a.x``` va produce o eroare de compilare. ```B``` are acces la campul de date mostenit ```x```, dar pentru un obiect de tipul ```A```, ```x``` va ramane ```protected``` si inacesibil din afara clasei.

Solutie: Desi incalca principiul incapsularii, este permis sa propunem ca solutie schimbarea modificatorului de acces din ```protected``` in ```public```. Rezultatul afisat va fi ```-12```.

```C++
class A
{
public:
    int x;
public:
    A(int i = -16) { x = i; }
    virtual A f(A a) { return x + a.x; }
    void afisare() { cout << x; }
};
class B : public A
{
public:
    B(int i = 3) : A(i) {}
    A f(A a) { return x + a.x + 1; }
};
int main()
{
    A *p1 = new B, *p2 = new A, *p3 = new A(p1->f(*p2));
    p3->afisare(); // -12
    return 0;
}
```

4. Exercitiul 4
```C++
class Base
{
public:
    Base()
    {
        fun();
    }
    virtual void fun()
    {
        cout << "\nBase Function";
    }
};
class Derived : public Base
{
public:
    Derived() {}
    virtual void fun()
    {
        cout << "\nDerived Function";
    }
};
int main()
{
    Base *pBase = new Derived();
    delete pBase;
    return 0;
}
```

R: compileaza si afiseaza ```\nBase Function```

Explicatie: Metoda ```fun()``` este declarata ca fiind virtuala in clasa de baza. Fiind si suprascrisa in clasa derivata, la upcasting va fi apelata cea din clasa derivata.

5. Exercitiul 5
```C++
class A
{
protected:
    int x;
public:
    A(int i = -31) { x = i; }
    virtual A operator+(A a) { return x + a.x; }
};
class B : public A
{
public:
    B(int i = 12) { x = i; }
    B operator+(B b) { return x + b.x + 1; }
    void afisare() { cout << x; }
};
int main()
{
    A *p1 = new B, *p2 = new A;
    B *p3 = new A(p2->operator+(*p1));
    p3->afisare();

    return 0;
}
```

R: nu compileaza

Explicatie: La instrucțiunea ```B *p3 = new A(p2->operator+(*p1));``` se încearcă un downcasting în mod implicit(care nu se poate realiza), dar se poate forța, realizându-l în mod explicit prin instructiunea ```B *p3 = (B*) new A(p2->operator+(*p1));```. Porgramul compileaza si afiseaza ```-19```.

```C++
class A
{
protected:
    int x;
public:
    A(int i = -31) { x = i; }
    virtual A operator+(A a) { return x + a.x; }
};
class B : public A
{
public:
    B(int i = 12) { x = i; }
    B operator+(B b) { return x + b.x + 1; }
    void afisare() { cout << x; }
};
int main()
{
    A *p1 = new B, *p2 = new A;
    B *p3 = (B*) new A(p2->operator+(*p1));
    p3->afisare(); // -19

    return 0;
}
```

6. Exercitiul 6
```C++
class B
{
    int i;
public:
    B() { i = 1; }
    virtual int get_i() { return i; }
};
class D : virtual public B
{
    int j;
public:
    D() { j = 2; }
    int get_i() { return B::get_i() + j; }
};
class D2 : virtual public B
{
    int j2;
public:
    D2() { j2 = 3; }
    int get_i() { return B::get_i() + j2; }
};
class MM : public D, public D2
{
    int x;
public:
    MM() { x = D::get_i() + D2::get_i(); }
    int get_i() { return x; }
};
int main()
{
    B *o = new MM();
    cout << o->get_i() << "\n";
    MM *p = dynamic_cast<MM *>(o);
    if (p)
        cout << p->get_i() << "\n";
    D *p2 = dynamic_cast<D *>(o);
    if (p2)
        cout << p2->get_i() << "\n";
    return 0;
}
```

R: compileaza si afiseaza:
```
7
7
7
```

Explicatie: Mai întâi se crează un obiect de tipul clasei ```MM``` asupra căruia se aplică procedeul de upcasting, având un pointer de tipul clasei de baza. În timpul creării obiectului este apelat constructorul clasei ```B``` care își inițializează câmpul ```i``` cu ```1```, apoi constructorul clasei ```D``` care își inițializează câmpul ```j``` cu ```2``` și apoi constructorul clasei ```D2``` care își inițializează câmpul ```j2``` cu ```3```, iar apoi este apelat și constructorul clasei ```MM``` care apelează în mod metodele ```get_i()``` din clasele ```D``` și ```D2``` și face suma rezultatelor, metode care și ele la rândul lor apelează ```get_i()``` din clasa B și la care adună ```j```și ```j2```. Deci pentru ```D1``` avem valoarea ```3``` și pentru ```D2``` avem valoarea ```4```, iar suma lor este 7(de aici și primul 7). Metoda ```get_i()``` este o metodă virtuală și este suprascrisă în toate clasele care o moștenesc, deci se va apela metoda ```get_i()``` din clasa ```MM``` și va întoarce valoarea ```7```. Apoi instrucțiunea ```MM *p = dynamic_cast<MM *>(o);``` realizează un downcasting și astfel se afișează din nou ```7```(este apelat ```get_i()``` din ```MM```, adica dupa ```dynamic_cast``` pointerul ```p2``` de tipul ```D```, o sa pointeze catre aceeasi zona de memorie catre care arata pointerul ```o```, care contine un obiect de tipul ```MM```). De asemenea, un downcasting este realizat și la instrucțiunea ```D *p2 = dynamic_cast<D *>(o);``` care afișează din nou valoarea ```7```. Practic, ```int get_i()``` din ```MM``` va fi apelat de 3 ori, afisand mereu valoarea ```7```.

7. Exercitiul 7
```C++
class A
{
protected:
    static int x;
public:
    A(int i = 0) { x = i; }
    virtual A schimb() { return (7 - x); }
};
class B : public A
{
public:
    B(int i = 0) { x = i; }
    void afisare() { cout << x; }
};
int A::x = 5;
int main()
{
    A *p1 = new B(18);
    *p1 = p1->schimb();
    ((B *)p1)->afisare();
    return 0;
}
```

R: compileaza si afiseaza ```-11```.

Explicatie: ```x``` din ```A```, fiind ```static``` este initializat primul cu valoarea ```5```. La instructiunea ```A *p1 = new B(18);``` este creat un obiect de tipul ```B``` in memorie, deci sunt apelati constructorii, in ordine, de la baza spre derivata. Astfel ```x``` din ```A``` ia valoarea ```18```. Metoda ```schimb()``` este virtuala, dar nu este suprascrisa in clasa derivata, deci va fi apelata cea din clasa de baza. Dupa apelul acesteia, pointerul ```p1``` va arata catre o zona de memorie cu un obiect de tipul ```A```, care va avea ```x``` egal cu ```7-18``` adica ```-11```. Instructiunea ```((B *)p1)->afisare();``` realizeaza un downcasting cu succes si afiseaza valoarea lui ```x```, ( declarat ca fiind ```protected``` in clasa de baza, impreuna cu mostenirea de tip ```public``` fiind accesibil in metoda ```afisare``` din clasa ```B```).

