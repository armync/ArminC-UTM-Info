# Exerciții rezolvate tutoriat 4

### Pentru fiecare dintre programele de mai jos, supneți dacă sunt corecte. În caz afirmativ, spuneți ce afișează, în caz negativ spuneți ce nu este corect și ce ați corecta.

1. Exercitiul 1
```C++
class A
{
public:
    void print() { cout << "A::print()"; }
};
class B : private A
{
public:
    void print() { cout << "B::print()"; }
};
class C : public B
{
public:
    void print() { A::print(); }
};
int main()
{
    C b;
    b.print();
}
```

R: eroare de compilare

Explicatie: Clasa ```B``` mosteneste ```private``` clasa ```A``` , deci metoda ```A::print()``` va deveni ```private``` in clasa ```B```, deci inaccesibila pentru orice tip de mostenire in clasa ```C```. 

Schimbam tipul de mostenire al clasei ```B``` in ```public/protected```. Programul va compila si va afisa ```A::print()```.

```C++
class A
{
public:
    void print() { cout << "A::print()"; }
};
class B : public A
{
public:
    void print() { cout << "B::print()"; }
};
class C : public B
{
public:
    void print() { A::print(); }
};
int main()
{
    C b;
    b.print(); // A::print()
}
```

2. Exercitiul 2

```C++
class base
{
public:
    void show() { cout << " In Base \n"; }
};
class derived : public base
{
    int x;
public:
    void show() { cout << "In derived \n"; }
    derived()
    {
        x = 10;
    }
    int getX() const { return x; }
};
int main()
{
    derived d;
    base *bp = &d;
    bp->show();
    cout << bp->getX();
    return 0;
}
```
R: eroare de compilare

Explicatie: Instructiunea ``` base *bp = &d;``` reprezinta un upcasting dinamic, deci ```bp-> show()``` va apela apela metoda din clasa de baza si va afisa ```In Base \n```. Metoda ```getX()``` se afla doar in clasa derivata, deci nu va putea fi apelata printr-un pointer de tipul clasei de baza.

Apelam metoda ```getX()``` prin intermediul instantei ```d``` care este de tipul clasei derivate.
Programul va compila si va afisa:

```
In Base
10
```

```C++
class base
{
public:
    void show() { cout << " In Base \n"; }
};
class derived : public base
{
    // public: void show() din base
    int x;
public:
    void show() { cout << "In derived \n"; }
    derived()
    {
        x = 10;
    }
    int getX() const { return x; }
};
int main()
{
    derived d;
    base *bp = &d;
    bp->show(); //  In Base
    cout << d.getX(); //10
    return 0;
}
```

3. Exercitiul 3

```C++
class B
{
    int x;
public:
    B(int v) { v = x; }
    int get_x() { return x; }
};

class D : private B
{
    int y;
public:
    D(int v) : B(v) {}
    int get_x() { return x; }
};
int main()
{
    D d(10);
    cout << d.get_x();
    return 0;
}
```

R: eroare de compilare

Explicatie: ```x``` este ```private``` in clasa de baza, deci la mostenire nu va fi accesibil in clasa derivata (apelul lui ```x``` din metoda ```int get_x() { return x; }``` din clasa derivata).

Schimbam modificatorul de acces a lui ```x```, din ```private``` (by default) in ```protected```. Programul va compila si afiseaza: ```0```, deoarece in constructorul clasei ```B```, lui ```x``` nu i se da valoarea lui ```v```, ci invers, deci ```x``` nu va fi initializat si va depinde de ce valoare primeste de la compilator (```0``` sau valoare aleatoare).

```C++
class B
{
protected:
    int x;
public:
    B(int v) { v = x; }
    int get_x() { return x; }
};
class D : private B
{
    int y;
public:
    D(int v) : B(v) {}
    int get_x() { return x; }
};
int main()
{
    D d(10);
    cout << d.get_x(); //0
    return 0;
}
```
4. Exercitiul 4

```C++
class B
{
    int a;
    B(int i = 0) { a = i; }
    int get_a() { return a; }
};
class D : protected B
{
public:
    D(int x = 0) : B(x) {}
    int get_a() { return B::get_a(); }
};
int main()
{
    D d(-89);
    cout << d.get_a();
    return 0;
}
```

R: eroare de compilare

Explicatie: toate datele clasei ```B``` au ca modificator de acces ```private```(by default). Deci nu vor fi accesibile la mostenire, in clasa ```D```. Constructorul clasei ```D``` incearca sa apeleze constructorul clasei ```B```, care nu este accesibil fiind ```private``` in clasa ```B```.

Adaugam modificatorul ```public``` pentru consstructorul si metodele clasei ```B```. Programul va afisa: ```-89```.

```C++
class B
{
    int a;
public: //aici
    B(int i = 0) { a = i; }
    int get_a() { return a; }
};
class D : protected B
{
    // nu e nimic accesibil din B
public:
    D(int x = 0) : B(x) {}
    int get_a() { return B::get_a(); }
};
int main()
{
    D d(-89);
    cout << d.get_a(); //-89
    return 0;
}
```

5. Exercitiul 5
   
```C++
class B
{
protected:
    int x;
public:
    B(int i = 16) { x = i; }
    B f(B ob) { return x + ob.x; }
    void afisare() { cout << x; }
};
class D : public B
{
    // protected: x
    //public:  toti membrii public din B
public:
    B f(B ob)
    {
        return x + 1;
    }
};
int main()
{
    B *p1 = new D; //upcasting
    B *p2 = new B;
    B *p3 = new B(p1->f(*p2));
    p3->afisare(); //32
    return 0;
}
```
R: compileaza si afiseaza ```32```.

6. Exercitiul 6
```C++
class A
{
public:
    int x;
    A(int i = 0)
    {
        x = i;
    }
    A minus()
    {
        return 1 - x;
    }
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

Explicatie: ```p1``` este un pointer de tipul clasei de baza, iar la instructiunea ```*p1 = p1->minus()``` va referintia catre un obiect de tipul clasei de baza, deci instructiunea ```p1-> afisare()``` va cauta metoda ```afisare()``` din clasa de baza, care nu este implementata pentru aceasta. 

O solutie este sa implementam metoda ```afisare()``` si in clasa de baza. Programul va afisa ```-17```.

```C++
class A
{
public:
    int x;
    A(int i = 0)
    {
        x = i;
    }
    A minus()
    {
        return 1 - x;
    }
    void afisare() { cout << x; }
};
class B : public A
{
    // are acces la tot din clasa A
public:
    B(int i = 0) { x = i; }
    void afisare() { cout << x; }
};
int main()
{
    A *p1 = new B(18);
    *p1 = p1->minus();
    p1->afisare(); //-17
    return 0;
}
```

3. Exercitiul 7
```C++
class B
{
    int i;
public:
    B() { i = 1; }
    int get_i() { return i; }
};
class D : public B
{
    int j;
public:
    D() { j = 2; }
    int get_i() { return B::get_i() + j; }
};
int main()
{
    const int i = cin.get();
    
    if (i % 3)
    {
        D o;
    }
    else
    {
        B o;
    }
    cout << o.get_i();
    return 0;
}
```
R: eroare de compilare

Explicatie: Atunci cand declaram obiecte/variabile in interiorul unor acolade (if-uri/for-uri/etc..) le cream cu un scop local si vor fi distruse la terminarea executarii codului dintre acolade. Acest caz se intampla in cadrul lui ```if-else``` din ```main()```, unde ```D o;``` si ```B o;``` sunt create doar cu scop local si nu exista in afara if/else-lui. 

Putem rezolva asta declarand un obiect ```o```, de tipul ```B``` sau ```D``` in afara lui if-else, rezultatul afisat depinzand de tipul ales. Pentru ```D o ```, va apela getterul din clasa derivata(rezultatul afisat va fi ```3```), iar pentru ```B o``` va apela getterul din clasa de baza(rezultatul afisat va fi ```1```).


```C++
class B
{
    int i;
public:
    B() { i = 1; }
    int get_i() { return i; }
};
class D : public B
{
    // i nu e accesibil
    int j;
public:
    D() { j = 2; }
    int get_i() { return B::get_i() + j; }
};
int main()
{
    const int i = cin.get(); // input int

    if (i % 3)
    {
        D o;
    }
    else
    {
        B o;
    }
    D o;
    cout << o.get_i(); //3
    return 0;
}
```