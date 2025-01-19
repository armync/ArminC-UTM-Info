# Exerciții rezolvate tutoriat 3

### Pentru fiecare dintre programele de mai jos, supneți dacă sunt corecte. În caz afirmativ, spuneți ce afișează, în caz negativ spuneți ce nu este corect și ce ați corecta.

1. Ex 1
```C++
class A
{
private:
    const int x = 5;
public:
    A() : x(2){}
    const int getX() const {
        return x;
    }
};
int main()
{
    A *obj = new A();
    cout << obj->getX();
    return 0;
}
```
R: corect: afiseaza 2

Explicatie: chiar daca variabila ```x``` este constanta, valoarea ei se poate schimba prin intermediul listei de initializare din constructor. 

2. Ex 2
```C++
class A
{
private:
    int x = 5;
public:
    A() : x(2){
        x = 6;
    }
    const int getX() const{
        return x;
    }
};
int main()
{
    A *obj = new A();
    cout << obj->getX();
    return 0;
}
```
R: corect: afiseaza 6

Explicatie: chiar daca getterul ```getX()``` este constant, poate accesa toate datele membre. Chiar daca si tipul returnat este ```const int``` valoarea lui nu este modificata in vreun fel la apel.

Dorim modificarea lui ```x``` prin valoarea returnata la apel, trebuie sa folosim referinta si sa eliminam ```const``` din declaratia metodei:

```C++
class A
{
    ... 
    int& getX() {
        return x;
    }
};
int main()
{
    A *obj = new A();
    cout << obj->getX()<<endl; // 6
    (obj->getX()) = 2;
    cout << obj->getX(); // 2
    return 0;
}
```

1. Ex 3
```C++
class Test
{
    Test self;
};
int main()
{
    Test t;
    return 0;
}
```
R: eroare de compilare

Explicatie: 
```
Declarația unei clase A:
- Poate conține obiecte statice de tipul clasei A. Ex: static Test self;
- Poate avea pointeri de tipul clasei A. Ex: Test *self;
- NU poate avea un obiect non static de tipul clasei A. (Deoarece: Dacă un obiect non static este membru, atunci declarația clasei este incompletă și compilatorul nu are cum să calculeze dimensiunea obiectelor clasei. Pentru un compilator, toți membri unei clase au o dimensiune fixă indiferent de tipul de date pe care îl indică.)
```

Corect:
```C++
class Test
{
    Test * self;
};
int main()
{
    Test t; //  nu afiseaza nimic
    return 0;
}
```

4. Ex 4
```C++
class Test
{
    static int x;
public:
    Test() { x++; }
    static int getX() { return x; }
};
int Test::x = 0;
int main()
{
    cout << Test::getX() << " ";
    Test t[5];
    cout << Test::getX();
}
```
R: corect: afiseaza 0 5

Explicatie: Cum ```x``` este ```static```, va avea aceeasi valoare pentru orice instanta a clasei. La fiecare apel al constructorului, valoarea lui ```x``` creste cu o unitate. La declaratia vectorului ```t[5]``` constructorul clasei este apelat de 5 ori, deci valoarea lui ```x``` va deveni 5.


5. Ex 5
```C++
class Test
{
private:
    static int count;
public:
    Test &fun();
};
int Test::count = 0;
Test &Test::fun()
{
    Test::count++;
    cout << Test::count << " ";
    return *this;
}
int main()
{
    Test t;
    t.fun().fun().fun().fun();
    return 0;
}
```
R: corect, afiseaza ```1 2 3 4```

Explicatie: La fel ca la exercitiul anterior, variabila ```count``` fiind statica va avea aceeasi valoare pentru orice instanta a clasei. Cum functia ```fun()``` este apelata de 4 ori, vor fi afisate consecutiv numerele de la 1 la 4.


6. Ex 6
```C++
class Cls
{
    int x;
public:
    Cls(int i) : x(i) {}
    const int &f()
    {
        return x;
    }
};
int main()
{
    Cls a(14);
    int b = a.f()++;
    cout << b << '\n';
    return 0;
}
```
R: eroare de compilare

Explicatie: functia ```f()``` returneaza o referinta constanta, deci rezultatul nu poate fi modificat. In functia ```main``` se incearca marirea rezultatului intors de functia ```f()``` cu o unitate, prin intermediul operatorului ```++```. 

Eliminam cuvantul cheie ```const``` din deifnitia tipului returnat de ```f()```. Rezultatul afisat va fi ```14``` deoarece intai pune valoarea returnata de ```a.f()``` apoi o mareste cu o unitate. 

```Tip: puteti sa priviti asa
a++ - intai pune valoarea lui a si apoi il mareste
++a - intai mareste a cu 1 si apoi il pune
```

Corect: 
```C++
class Cls
{
    int x;
public:
    Cls(int i) : x(i) {}
    int &f()
    {
        return x;
    }
};
int main()
{
    Cls a(14);
    int b = a.f()++; // 14 
    cout << b << '\n';
    return 0;
}
```

1. Ex 7
```C++
class A
{
    int x;
    static int y;
public:
    A(int i, int j) : x(i), y(j){}

    int f() const;
};
int A::y;
int A::f() const
{
    return y;
}
int main()
{
    const A a(21, 2);
    cout << a.f();
    return 0;
}
```
R: eroare de compilare 

Explicatie: valoarea membrului static ```y``` nu poate fi modificata prin intermediul listei de intializare din constructor. Poate fi modificata doar prin intermediul unei metode statice. 

Putem folosi modificarea acesteia in constructor.

Corect: 
```C++
class A
{
    int x;
    static int y;
public:
    A(int i, int j) : x(i){
        y = j;
    }

    int f() const;
};
int A::y;
int A::f() const
{
    return y;
}
int main()
{
    const A a(21, 2);
    cout << a.f(); // afiseaza: 2
    return 0;
}
```

8. Ex 8
```C++
class A
{
    int x, *y;
public:
    A(int i)
    {
        x = i;
        y = new int[x];
    }
    A(A &a)
    {
        x = a.x;
        y = new int[x];
    }
    int getX() const
    {
        return x;
    }
};
int f(A a)
{
    return a.getX();
}
int main()
{
    const A a(5);
    cout << (a.getX() == f(a));
    return 0;
}
```
R: eroare de compilare

Explicatie: obiectul ```a``` este declarat ca fiind constant, parametrul functiei ```f(A a)``` este dat prin valoare ceea ce este ok, problema apare la apel cand este apelat ```copy constructorul``` cand ajunge in parametrul functei ```f```. In ```copy constructor``` primeste perametrul prin referinta neconstanta, ceea ce inseamna ca ii indica compilatorului ca poate modifica oricand acel obiect transmis ca parametru la apel. 

Rolzvam elimand cuvantul cheie ```const``` din declaratia instantei ```a``` din ```main()```.

Corect: 
```C++
class A
{
    int x, *y;
public:
    A(int i)
    {
        x = i;
        y = new int[x];
    }
    A(A &a)
    {
        x = a.x;
        y = new int[x];
    }
    int getX() const
    {
        return x;
    }
};
int f(A a)
{
    return a.getX();
}
int main()
{
    A a(5);
    cout << (a.getX() == f(a)); // afiseaza 1
    return 0;
}
```

9. Ex 9
```C++
class Cls
{
    int x;
public:
    Cls(int i = 0)
    {
        cout << 1;
        x = i;
    }
    Cls(Cls &ob)
    {
        cout << 2;
        x = ob.x;
    }
    int getX() const
    {
        return x;
    }
};
Cls &f(Cls &c)
{
    return c;
    
}
int main()
{
    Cls r;
    Cls s = f(f(f(r)));
    cout << s.getX();
    return 0;
}
```
R: corect, afiseaza 120

Explicatie: Functia ```f``` primeste succesiv apeluri cu rezultatul apelului ei, iar cum apelul este realizat prin referinta atat la tipul parametrului, la tipul returnat, cat si in parametrul copy constructorului, nu va aparea nicio problema, deoarece nu sunt create obiecte cu caracter constant. 

1.  Ex 10
```C++
class Cls
{
    static int i;
    int j;
public:
    Cls(int x = 7)
    {
        j = x;
    }
    static int imp(int k)
    {
        Cls a;
        return i + k + a.j; // 0 + 5 + 7
    }
    int getJ() const
    {
        return j;
    }
};
int Cls::i;
int main()
{
    int k = 5;
    cout << Cls::imp(k);
    return 0;
}
```
R: corect, afiseaza 12

Explicatie: metoda ```imp(int k)``` este statica, deci poate accesa variabila statica care are valoarea ```0``` data default de compilator la initilizare in lipsa altei valori initiale. Se creeaza un obiect de tipul clasei in metoda, deci nu foloseste pointerul ```this``` si fiind metoda a clasei poate accesa membrii privati cum este in istructiunea ```a.j```.


11. Ex 11
```C++
class Cls
{
    int x;
public:
    Cls(int i = 32)
    {
        x = i;
    }
    int f() const
    {
        return x++;
    }
};
int main()
{
    const Cls d(-15);
    cout << d.f();
    return 0;
}
```
R: eroare de compilare

Explicatie: metoda ```f()``` este declarata ca fiind constanta, deci nu are voie sa modifice nimic la datele memebre ale lui ```this```. Intructiunea ```x++``` este echivalenta cu ```this -> x++```, deci va produce o eroare de compilare. 

Indepartam cuvantul cheie ```const``` din definitia functiei ```f```, dar si din declararea obiectului ```d``` din main, deoarece un obiect constant poate accesa numai metode constante. Afiseaza ```-15``` deoarece secventa ```return x++``` presupune intai returnarea valorii lui x, apoi marirea ei cu o unitate.


Corect: 
```C++
class Cls
{
    int x;
public:
    Cls(int i = 32)
    {
        x = i;
    }
    int f() 
    {
        return x++;
    }
};
int main()
{
    Cls d(-15);
    cout << d.f(); //-15
    return 0;
}
```

12. Ex 12
```C++
int &fun()
{
    static int a = 10;
    return a;
}
int main()
{
    int &y = fun(); //10
    y = y + 30;
    cout << fun();//40
    return 0;
}
```
R: corect, afiseaza 40

Explicatie: functia ```f``` returneaza o referinta catre un intreg ```int&```, deci fiecare modificare facuta asupra rezultatului functiei se va vedea in valoarea lui ```a```. Variabila ```y``` din main retine referinta rezultatului returnat de ```f```, deci orice modificare asupra lui ```y``` se va vedea in variabila ```a``` din functia ```f```.


13. Ex 13
```C++
class A
{
    int aid;
public:
    A(int x)
    {
        aid = x;
    }
    void print()
    {
        cout << "A::aid = " << aid;
    }
};
class B
{
    int bid;
public:
    static A a;
    B(int i) { bid = i; }
};

int main()
{
    B b(10);
    b.a.print();
    return 0;
}
```
R: eroare de compilare

Explicatie: data membru statica ```a``` din clasa ```B``` nu a fost intializata.

Adaugam initializarea ei in afara clasei.

Corect: 
```C++
class A
{
    int aid;
public:
    A(int x)
    {
        aid = x;
    }
    void print()
    {
        cout << "A::aid = " << aid;
    }
};
class B
{
    int bid;
public:
    static A a;
    B(int i) { bid = i; }
};
A B::  a(0); //aici
int main()
{
    B b(10);
    b.a.print(); // A::aid = 0
    return 0;
}
```

14. Ex 14
```C++
class A
{
    int id;
    static int count;
public:
    A()
    {
        count++;
        id = count;
        cout << "constructor called " << id << endl;
    }
    ~A()
    {
        cout << "destructor called " << id << endl;
    }
};
int A::count = 0;
int main()
{
    A a[2];
    return 0;
}
```
R:corect, afiseaza

```
constructor called 1
constructor called 2
destructor called 2
destructor called 1
```

Explicatie: La declaratia vectorului ```a``` cu doua elemente este apelat de 2 ori constructorul, apoi se apeleaza in ordinea inversa crearii destructorul pentru fiecare instanta. Data membra ```id``` primeste valoarea curenta a staticului ```count``` corespunzator fiecarei instante create.  


15. Ex 15
```C++
class Test
{
private:
    int x;
    static int count;
public:
    Test(int i = 0) : x(i) {}
    Test(const Test &rhs) : x(rhs.x) { ++count; }
    static int getCount() { return count; }
};
int Test::count = 0;
Test fun()
{
    return Test();
}
int main()
{
    Test a = fun(); 
   
    cout << Test::getCount(); 
    return 0;
}
```
R: corect, afiseaza 0 sau 2(depinde de compilator daca face ```copy elision``` sau nu)

Explicatie: Instrucțiunea ```Test a = fun();``` poate sau nu să apeleze constructorul de copiere. Deci, ieșirea poate fi 0 sau 2. Acest fenomen se întâmplă când compilatorul realizează o optimizare ce se numeste ```copy elision```, iar constructorul de copiere nu va fi apelat.
Dacă nu se realizează ```copy elision```, va fi apelat constructorul de copiere.

Compilare cu g++ forțată să NU folosească copy elision: ```g++ -fno-elide-constructors main.cpp -o main.out```.

Compilare cu g++ cu standardul din 2017 care garantează că se va folosi copy elision:```g++ -std=c++17 main.cpp -o main.out```.

Mai multe despre copy elision gasiti [aici](https://en.cppreference.com/w/cpp/language/copy_elision).

16. Ex 16
```C++
int a = 2;
class Test
{
    int &t = a;
public:
    Test(int &t) : t(t) {}
    int getT() { return t; }
};
int main()
{
    int x = 20;
    Test t1(x);
    cout << t1.getT() << endl;
    x = 30;
    cout << t1.getT() << endl;
    return 0;
}
```
R: corect, afiseaza

```
20
30
```

Explicatie: La crearea obiectului ```t1(x)``` lui ```x``` este transmis ca parametru prin referinta in constructor, deci orice modificare asupra lui x se va vedea asupra valorii catre care referintiaza ```t```.


17. Ex 17
```C++
class Point
{
private:
    int x;
    int y;
public:
    Point(int i = 0, int j = 0);
    Point(const Point &t);
};
Point::Point(int i, int j)
{
    x = i;
    y = j;
    cout << "Normal Constructor called\n";
}
Point::Point(const Point &t)
{
    y = t.y;
    cout << "Copy Constructor called\n";
}
int main()
{
    Point *t1, *t2;
    t1 = new Point(10, 15);
    t2 = new Point(*t1);
    Point t3 = *t1;
    return 0;
}
```
R: corect, afiseaza:

```
Normal Constructor called
Copy Constructor called
Copy Constructor called
```

Explicatie: La instructiunea ```Point *t1, *t2;```  nu se apeleaza niciun constructor, deoarece sunt declarati doar pointeri, deci nu este intializata si zona de memorie catre care acestia pointeaza. La urmatoarea instructiune ```t1 = new Point(10, 15);``` este apelat constructorul cu cei 2 parametrii, iar la ```t2 = new Point(*t1);``` si ```Point t3 = *t1;``` este apelat copy constructorul pentru fiecare.



