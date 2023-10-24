# C++ Tutorial

## TLDR
A short summary for what you need / should use at PA can be found at [PA C++: TLDR](tldr.md).

## Docs

Links:
* [en.cppreference.com](https://en.cppreference.com): main C++ documentation
   * [C++ reference](https://en.cppreference.com/w/cpp): C++ documentation
   * [cppreference/algorithm](https://en.cppreference.com/w/cpp/algorithm): STL algorithms docs
   * [cppreference/container](https://en.cppreference.com/w/cpp/container): STL containers docs
* [C reference](https://en.cppreference.com/w/c): C API also available in C++

C++ has multiple standards (see [cppreference/history](https://en.cppreference.com/w/cpp/language/history)). In this tutorial the C++17 standard (g++ flag: `-std=c++17`) is assumed. The laboratory skeletons use C++17 and we strongly encourage to also do it for homeworks / projects.

## C++ basics

* C++ is a high-level language, sometimes called a superset of C.
* It supports imperative, object-oriented and generic programming.

### Hello Gigel in C++

```cpp
#include <iostream>

int main() {
    int x;
    std::cin >> x;
    std::cout << "Hello, Gigel! I got " << x << " from the PA team!"
    return 0;
}
```

Explanations:
* `io`:
  * The standard C++ input/output library is `<iostream>`.
  * Streams:
    * `std::cin`: reading from `STDIN` with operator `>>`
    * `std::cout`: writing to `STDOUT` with operator `<<`
    * `std::cerr`: writing to `STDERR` with operator `<<`
  * Please check `io.md` for file operations.
* `namespace`
  * >Namespaces provide a method for preventing name conflicts in large projects. ([cppreference/namespace](https://en.cppreference.com/w/cpp/language/namespace))
  * A namespace groups variables, types and functions together.


* To compile any C++ program, use
```bash
# compile
g++ -Wall -Wextra -std=c++17 <source_name> -o <executable_name>
```

* To run any compiled C++ program, use
```bash
./<executable_name>
```

---
Notes for `PA-only`:
  * Compiler flags:
    * always use `-std=c++17`
    * never use optimizations flags (the purpose of this class is to find the solution with the best complexity)
  * It's `encouraged` to use `using namespace std` ([stackoverflow/using-namespace-std](https://stackoverflow.com/questions/1452721/why-is-using-namespace-std-considered-bad-practice)) instead of specifing `std::` everywhere. This tutorial we'll use the second approach.
  * Always use the provided skeleton for the laboratory.

---


### C vs C++
* **struct in C** vs **struct in C++**
    * > "A struct in the C programming language is a composite data type declaration that defines a physically grouped list of variables under one name in a block of memory, allowing the different variables to be accessed via a single pointer or by the struct declared name which returns the same address. The struct data type can contain other data types so is used for mixed-data-type records such as a hard-drive directory entry (file length, name, extension, physical address, etc.), or other mixed-type records (name, address, telephone, balance, etc.)." ([wikipedia/struct (C programming language)](https://en.wikipedia.org/wiki/Struct_(C_programming_language)))
    *  > "A class in C++ is a user-defined type or data structure declared with keywords struct or class that has data and functions (also called member variables and member functions or methods) as its members whose access is governed by the three access specifiers private, protected or public." ([wikpedia/C++ classes](https://en.wikipedia.org/wiki/C%2B%2B_classes)).


* Basic example of C struct conversion to C++ struct

In C we can define a struct and some functions which can process this type.

```cpp
// C struct
typedef struct {
    double re;
    double im;
} complex_t;

void print_complex(complet_t c)
{
    printf("%lf + %lf\n", c.re, c.im);
}

int main()
{
    complex_t c = {1, 2}; // 1 + 2i
    print_complex(c);
    return 0;
}
```

In C++ we can move the functions which process the new type inside the struct.
```cpp
// C++ struct
struct Complex {
    double re, im;

    void print() {
        // the im and re members for the current Complex object are accessed
        std::cout << re << "+" << im << "i" << "\n";
    }
};

int main()
{
    Complex c;
    c.re = 1;
    c.im = 2;
    c.print();
    return 0;
}
```

* **access specifiers**: struct vs class in C++

    Members (data and methods)  can be:
    * **public**    - accessible from anywhere
    * **private**   - only accessible in the class
    * **protected** - only accessible on the inheritance chain (not relevant for PA)

    Notes:
    * **struct** members are **public** by default.
    * **class** members are **private** by default.

```cpp
#include <iostream>

class Gigel {
    int x = 100; // private because is in a class;
                 // if Gigel was struct, x was public.
public:
    void show() {
        std::cout << "x is " << x << "\n";
    }
};

int main() {
    Gigel g;
    g.show(); // print "x is 100"
    return 0;
}
```

### Constructors and destructors
* [cppreference/constructor](https://en.cppreference.com/w/cpp/language/constructor)
* [cppreference/destructor](https://en.cppreference.com/w/cpp/language/destructor)

#### Constructor
A constructor is **a special method** that is **automatically** called `when` an object of a class is created.
* The constructor has the same name as the class name.
* The constructor has **no return type**.
* The constructor can take 0 or more parameters (just like regular functions).
* If no constructor is defined, the compiler "creates" one, which does nothing and it is called **default constructor**.
* A class can have **multiple** constructors with different parameters.

```cpp
#include <iostream>

class Gigel {
 public:
   Gigel() {
      std::cout << "Gigel()\n";
    }

   Gigel(int x) {
      std::cout << "Gigel(" << x << ")\n";
    }
};

int main() {
   Gigel g;         // print "Gigel()"
   Gigel g4(5);     // print "Gigel(5)"
}
```

#### Destructor
A destructor is a **special method** that is called `when` the lifetime of an object ends. The purpose
of the destructor is to free the resources that the object may have acquired during its lifetime.

### Dynamic allocation: C vs C++
* **new / malloc** are used to dynamically allocate memory. A difference is that **new** does call the
constructor and **malloc** does not.

* **delete / free** are used to free the allocate memory. A difference is that **delete** does call the
destructor and **free** does not.

Note: The usage of malloc / free in C++ is considered unsafe and it's forbidden. The new / delete functions should be used instead.

---

During the PA labs you won't used dynamic allocation, because we want to keep the things as simple as possible:
* a single call to `new / delete` will be made in the `main()` function - the skeleton already has the implementation for `main()`.
* when solving the tasks you must use containers from STL (e.g. `std::vector`) which allocate and automatically deallocate memory.

---

### auto keyword
* > "For variables, specifies that the type of the variable that is being declared will be automatically deduced from its initializer. For functions, specifies that the return type will be deduced from its return statements." ([cppreference/auto](https://en.cppreference.com/w/cpp/language/auto))

```cpp
#include <iostream>

// the return type for square() is automaticaly deduce to double because the returned value
// (x * x) is a double
auto square(double x) {
   return x * x;
}

int main() {
   auto x = 10.0; // the type of x is automatically deduced to double because 10.0 it's a double
   std::cout << square(x) << "\n";
   return 0;
}
```

### References in C++
* A pointer is a **variable** that holds a memory address (e.g. `0xCAFEBABE` or the address of another variable).
* Both C and C++ have pointers. Additionally, C++ has references.
* A reference is **an alias** for **an already existing variable**. Once a reference is initialized to a variable, it cannot be changed to refer to another variable (hence, a reference is similar to a fixed pointer). The referenced variable can be changed using the reference.

```cpp
#include <iostream>

// C: if we want to change x in function foo, we need to pass using  a pointer
void modify_c(int *x) {
    *x = 123;
}
// call example:
// int x;
// modify_c(&x);

// C++: we can pass by reference
void modify_cpp(int &x) {
     x = 123; // x it's a reference to the "x" variable from main
}

int main() {
   int x = 0;
   modify_cpp(x);
   std::cout << x << "\n"; // print 123 because x was changed to 123 in modify_cpp()
   return 0;
}
```

### Templates
In C++, templates allow to pass to functions/classes the data type as parameter, so there is no need to write the same code for different data types.

#### template functions
A function which may have generic parameter(s) or return type.
* generic return type

```cpp
template<typename T>
T func(...) {
    // ...
    return T(...);
}
// usage example for int
int x  = func<int>();

// usage example for struct Gigel
Gigel gigel  = func<Gigel>();
// or
auto gigel = func<Gigel>();
```

* generic parameter type(s)
```cpp
// example of template function
// which has 2 parameters of type T (reference to T)
template<typename T>
void func(T& a, T&b) {
    // ...
}
// usage example for int
func<int>(123, 456);
// example of template function
// which has 2 parameters of type K and V
template<typename K, typename V>
void func(K &k, V &v) {
    // ...
}
// usage example for int and struct Gigel
func<int, Gigel>(123, Gigel());
```

```cpp
#include <iostream>

// generic maximum function: a and b have the same template type T
template <typename T>
T my_max (T a, T b) {
    return (a > b ? a : b);
}

int main() {
    //  usage example for T = int
    std::cout << my_max<int>(2, 3) << "\n";
    // or let to compile to automatically determine the T type from the passed values
    std::cout << my_max(2, 3) << "\n";

    // usage example for T = double
    std::cout << my_max(3.4, 5.6) << "\n";

    // usage example for T = char
    std::cout << my_max('a', 'b') << "\n";
    return 0;
}
```

### template classes
Classes which depend of a template type `T` (e.g. a struct with a `T` member which can be an `int` or  ` double`).
Consider the next simple class which has an `int` member;

```cpp
class MyClass {
public:
   int get_member() { return member; }
   void set_member(int new_value) { member = new_value; }
private:
    int member;
};
```

If we want to make a similar class with a member `double` we would copy the class and replace `int` with `double`. We also need to rename the class. If instead we use a template class, we need to:

* replace `int` with `T` (a generic type)
* declare that the class is template (using ```cpp template<typename T>``` before class MyClass)

```cpp
template<typename T>
class MyClass {
public:
   T get_member() { return member; }
   void set_member(T new_value) { member = new_value; }
private:
    T member;
};

// usage example for int
MyClass<int> mc_int;
mc_int.set_member(123); // set an int value
std::cout << mc_int.get_member() << "\n"; // print 123

// usage example for class Gigel
MyClass<Gigel> mc_gigel;
mc_gigel.set_member(Gigel()); // set a Gigel value
std::cout << mc_gigel.get_member() << "\n"; // print the Gigel value
```

## STL
C++ provides implementation for various data types and algorithms which are grouped into the `STL` (the Standard Template Library - generic / template functions and classes).

Please continue the tutorial from the `STL` tree.
