# Operatorul typeid

- Este utilizat acolo unde este nevoie de tipul dinamic sau tipul de rulare ale unui obiect.
- ```#include<typeinfo>```
- Mai multe detalii puteti gasi [in documentatia oficiala](https://en.cppreference.com/w/cpp/language/typeid)
- Verifica tipurile (ex: x de tip int si y de tip int vor avea acelasi typeid)
- Returneaza un _lvalue_: ``` const type_info```

## Sintaxa
```
typeid(type);
      sau
typeid(expression);
```

## Important !
Dacă expresia este o referință sau un pointer către o clasă polimorfă (are _cel putin_ o metoda _virtual_), 
```typeid``` va returna un obiect de tipul ```type_info``` care reprezintă obiectul pe care referința sau pointerul îl capata la runtime.
Dacă NU este o clasă polimorfă, ```typeid``` va returna un obiect de tipul ```type_info``` care reprezintă tipul referinței sau al indicatorului
dereferențiat. 
  

### Exemplul 1
```C++
 int x = 50;
 string s = "string";
 double *p = nullptr;

 cout << "x has type: " << typeid(x).name() << endl;
 cout  << "s has type: " << typeid(s).name() << endl;
 cout  << "p has type: " << typeid(p).name() << endl;
```

Afiseaza: 
```
x has type: i
s has type: NSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
p has type: Pd
```

### Exemplul 2 - clasa de baza este virtuala
```C++
struct A { virtual ~A() { } };
struct B : A { };

int main() {
    B ob;
    A* p = &ob;
    A& r = ob;
    cout << "pointer: " << typeid(p).name() << endl;
    cout << "deferntiere pointer: " << typeid(*p).name() << endl;
    cout << "referinta: " << typeid(r).name() << endl;
}
```

Afiseaza - tipul la runtime:
```
pointer: P1A
pointer: 1B
referinta: 1B
```

### Exemplul 3 - clasa de baza NU este virtuala
```C++
struct A {};
struct B : A { };

int main() {
    B ob;
    A* p = &ob;
    A& r = ob;
    cout << "pointer: " << typeid(p).name() << endl;
    cout << "deferntiere pointer: " << typeid(*p).name() << endl;
    cout << "referinta: " << typeid(r).name() << endl;
}
```

Afiseaza - tipul declarat:
```
pointer: P1A
deferintiere pointer: 1A
referinta: 1A
```

