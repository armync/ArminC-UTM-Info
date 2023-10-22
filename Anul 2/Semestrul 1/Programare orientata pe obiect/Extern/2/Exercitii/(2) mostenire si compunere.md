# Exerciții rezolvate tutoriat 3

### Pentru fiecare dintre programele de mai jos, supneți dacă sunt corecte. În caz afirmativ, spuneți ce afișează, în caz negativ spuneți ce nu este corect și ce ați corecta.

1. Ex 1
```C++
#include <iostream>
using namespace std;

class B1 { public: int x; };
class B2 { public: int y; };
class B3 { public: int z; };
class B4 { public: int t; };
class D: public B1, private B2, protected B3, B4 { public: int u; };
int main() {
    D d;
    cout << d.u;
    cout << d.x;
    cout << d.y;
    cout << d.z;
    cout << d.t;
    return 0;
}
```
R: GRESIT: eroare de compilare

Explicatie:
```
class D : public B1 => x si u sunt public in D
class D : private B2 => y in D este private, iar u e public => y inaccesibil printr-o instanta a lui D
class D : protected B3 => z in D este protected, iar u e public  => z inaccesibil printr-o instanta a lui D
class D : B4 => t in D este private, iar u e public  => t inaccesibil printr-o instanta a lui D
```

Corect: schimbam tipurile de mostenire ale lui B2, B3, B4
```C++
class B1 { public: int x; };
class B2 { public: int y; };
class B3 { public: int z; };
class B4 { public: int t; };
class D: public B1,  public B2,  public B3,  public B4 { public: int u; }; //aici
int main() {
    D d;
    cout << d.u;
    cout << d.x;
    cout << d.y;
    cout << d.z;
    cout << d.t;
    return 0;
    // afiseaza valori aleatoare pentru fiecare
}
```
2. Ex 2
```C++
#include <iostream>
using namespace std;

class B
{
protected:
    int a;
public:
    B() { a = 7; }
};
class D : public B
{
public:
    int b;
    D() { b = a + 7; }
};
int main()
{
    D d;
    cout << d.b;
    return 0;
}
```
R: CORECT: afiseaza: 14

E: ```a``` este ```protected``` in clasa de baza, iar mostenirea este de tip ```public```, deci isi va pastra modificatorul de acces ```protected``` si in clasa derivata, deci este accesibil in constructorul clasei derivate.

3. Ex 3
```C++
#include <iostream>
using namespace std;

class cls1
{
protected:
    int x;
public:
    cls1(int i = 10) { x = i; }
    int get_x() { return x; }
};
class cls2 : cls1
{
public:
    cls2(int i) : cls1(i) {}
};
int main()
{
    cls2 d(37);
    cout << d.get_x();
    return 0;
}
```
R: GRESIT: eroare de compilare

E: tipul de mostenire este ```private```(by default), astfel tot ce e din clasa de baza devine ```private``` in clasa derivata. Deci, metoda ```get_x()``` devine ```private``` pentru o instanta a ```cls2```, deci nu este accesibila.

Corect: modificam tipul de mostenire in ```public```.
```C++
class cls1
{
protected:
    int x;
public:
    cls1(int i = 10) { x = i; }
    int get_x() { return x; }
};
class cls2 : public cls1 //aici
{
public:
    cls2(int i) : cls1(i) {}
};
int main()
{
    cls2 d(37);
    cout << d.get_x(); // 37
    return 0;
}
```

4. Ex 4
```C++
#include <iostream>
using namespace std;

class B
{
    int x;
public:
    B(int i = 0) { x = i; }
};
class D : public B
{
public:
    D() : B(15) {}
    int f() { return x; }
};
int main()
{
    D d;
    cout << d.f();
    return 0;
}
```
R: GRESIT: eroare de compilare

E: ```x``` este ```private``` in clasa de baza, iar la mostenirea de tip ```public``` este inacesibil in clasa derivata. 

Corect: modificam accesul lui ```x``` in clasa de baza la ```protected```.
```C++
class B
{
protected:
    int x;
public:
    B(int i = 0) { x = i; }
};
class D : public B
{
public:
    D() : B(15) {}
    int f() { return x; }
};
int main()
{
    D d;
    cout << d.f(); // 15
    return 0;
}
```

5. Ex 5
```C++
#include <iostream>
using namespace std;

class A
{
protected:
    int x;
public:
    A(int i = 14) { x = i; }
};
class B : A
{
public:
    B(B &b)
    {
        x = b.x;
    }
    void afisare()
    {
        cout << x;
    }
};
int main()
{
    B b1, b2(b1);
    b2.afisare();
    return 0;
}
```
R: GRESIT: eroare de compilare

E: in clasa ```B``` este definit constructorul ```B(B &b)```, deci compilatorul nu mai ofera constructorul by default (cel fara parametrii). Astfel, secventa ```B b1``` este gresita.

Corect: Adaugam constructorul fara parametrii in clasa ```B``` pentru a putea fi apelat de ```B b1```.
```C++
class A
{
protected:
    int x;
public:
    A(int i = 14) { x = i; }
};
class B : A
{
public:
    B(){}
    B(B &b)
    {
        x = b.x;
    }
    void afisare()
    {
        cout << x;
    }
};
int main()
{
    B b1, b2(b1);
    b2.afisare(); // afiseaza 14
    return 0;
}
```
6. Ex 6
```C++
#include <iostream>
using namespace std;

class A
{
protected:
    int x;
public:
    A(int i = 14) { x = i; }
};
class B : A
{
public:
    B() : A(2) {}
    B(B &b) { x = b.x - 14; }
    void afisare() { cout << x; }
};
int main()
{
    B b1, b2(b1);
    b2.afisare();
    return 0;
}
```
R: CORECT: afiseaza -12

E: la declararea lui ```b1``` se apeleaza constructorul lui ```A``` cu valoarea lui ```i=2```. Apoi la declararea lui ```b2``` se apeleaza constructorul (de copiere) ```B(B &b)``` care primeste ```b1``` ca parametru si calculeaza noua valoare a lui ```x = 2-14```.

7. Ex 7
```C++
#include <iostream>
using namespace std;

class A
{
    int x;
public:
    A(int i) : x(i) {}
    int get_x() { return x; }
};
class B : public A
{
    int y;
public:
    B(int i, int j) : y(i), A(j) {}
    int get_y() { return y; }
};
class C : protected B
{
    int z;
public:
    C(int i, int j, int k) : z(i), B(j, k) {}
    int get_z() { return z; }
};
int main()
{
    C c(1, 2, 3);
    cout << c.get_x() + c.get_y() + c.get_z();
    return 0;
}
```
R: GRESIT: eroare de compilare

Explicatie
```
class B : public A
        x private in A => x inaccesibil in B
        get_x() public in B
        constructorul lui A e public in B
        
class C : protected  B
        constructorul lui A e protected in C
        constructorul lui B e protected  in C
        x private in A  => x inaccesibil in B => x inaccesibil in C
        y private in B +=> y inaccesibil in C
        get_x() devine protected in C => inaccesibil printr-o instanta a lui C
        get_y() devine protected in C => inaccesibil printr-o instanta a lui C
```

Corect: schimb tipul de mostenire intre clasele ```C``` si ```B``` in ```public```.

```C++
class A
{
    int x;
public:
    A(int i) : x(i) {}
    int get_x() { return x; }
};
class B : public A
{
    int y;
public:
    B(int i, int j) : y(i), A(j) {}
    int get_y() { return y; }
};
class C : public B
{
    int z;
public:
    C(int i, int j, int k) : z(i), B(j, k) {}
    int get_z() { return z; }
};
int main()
{
    C c(1, 2, 3);
    cout << c.get_x() + c.get_y() + c.get_z(); // afiseaza: 6
    return 0;
}
```

8. Ex 8
```C++
#include <iostream>
using namespace std;

class Base1
{
public:
    Base1()
    {
        cout << " Base1's constructor called" << endl;
    }
};
class Base2
{
public:
    Base2()
    {
        cout << "Base2's constructor called" << endl;
    }
};
class Derived : public Base2, public Base1
{
public:
    Derived()
    {
        cout << "Derived's constructor called" << endl;
    }
};
int main()
{
    Derived d;
    return 0;
}
```
R: CORECT: afiseaza

```
Base2's constructor called
Base1's constructor called
Derived's constructor called
```

E: constructorii se apeleaza de la baza spre derivata, in ordinea in care sunt specificati la mostenire.

9.  Ex 9
```C++
#include <iostream>
using namespace std;

class Base
{
protected:
    int x;
public:
    Base(int i) { x = i; }
};
class Derived : public Base
{
public:
    Derived(int i) : x(i) {}
    void print() { cout << x; }
};
int main()
{
    Derived d(10);
    d.print();
}
```
R: GRESIT: eroare de compilare

E: Mostenire ```public```, iar x este ```proiected``` deci este accesibil in clasa derivata. Dar, *membrii clasei de bază pot fi inițializați doar printr-un constructor al clasei de bază*.

Corect: In loc de lista de intializare, apelez constructorul clasei de baza.
```C++
class Base
{
protected:
    int x;
public:
    Base(int i) { x = i; }
};
class Derived : public Base
{
public:
    Derived(int i) : Base(i) {}
    void print() { cout << x; }
};
int main()
{
    Derived d(10); //10 
    d.print();
}
```
