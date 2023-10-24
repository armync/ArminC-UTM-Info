# Java tutorial

Links:
* [docs.oracle/tutorial](https://docs.oracle.com/javase/tutorial): main Java documentation
    * [docs.oracle.com/java](https://docs.oracle.com/javase/tutorial/java): Java basics
    * [docs.oracle.com/collections](https://docs.oracle.com/javase/tutorial/collections): containers and algorithms in Java

## Java basics
* Java is a high-level object-oriented programming language.
* It supports primitive data types like `int`, `char` and `boolean`. Most of the types are classes (e.g. `String` or `Integer`).
* Unlike C and C++, Java has no low-level features such as pointers.

### Access modifiers
* [docs.oracle.com/access-modifiers](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html)

The `access modifiers` in Java are: `default`, `private`, `protected` and `public`. They allow access to a class, method or attribute in another class.

| access modifier |                                                visibility                                                 |
| :-------------: | :-------------------------------------------------------------------------------------------------------: |
|   **default**   |       allow access only within the same package, present when no other access modifier is specified       |
|   **private**   |     method and attributes are allowed to be accessed only within the class in which they are declared     |
|  **protected**  | allow access to the methods and attributes in the same package or child classes located in other packages |
|   **public**    | do not impose any access limit, access to methods or attributes can be done from anywhere in the program  |

### Constructors
A constructor is a special method called when an instance of a class is created in order to initialize the object.
* If no user-defined constructor is provided, the compiler automatically generates a **default constructor**.
* The constructor has **no** return type.
* The constructor is named after the class.
* A class can have zero or multiple use-defined constructors with different prototypes.

```Java
class Student {
    public String name;
    public int age;

    public Student() {
        System.out.println("Constructor with no parameters");
        this.name = "Alice";
        this.age = 20;
    }

    public Student(String name, int age) {
        System.out.println("Constructor with parameters");
        this.name = name;
        this.age = age;
    }

    public void display () {
        System.out.println(name + " " + age);
    }
}

public class ConstructorsTest {
    public static void main(String args[]){
        Student student1 = new Student();
        Student student2 = new Student("Bob", 19);

        student1.display();
        student2.display();
    }
}
```

Expected output:
```
Constructor with no parameters
Constructor with parameters
Alice 20
Bob 19
```

### static keyword
The `static` keyword is used for a member that is shared between all instances of a class.

* `static` members
```Java
class Student {
    public String name;
    public int age;
    // public data member shared between all instances of the class
    // note: only one projectCount exists in the entire program!
    public static int projectCount = 0;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void display () {
        System.out.println(name + " " + age + " " + projectCount);
    }
}

public class StaticVariableTest {
    public static void main(String args[]){
        Student student1 = new Student("Alice", 20);
        Student student2 = new Student("Bob", 19);

        student1.display();
        // the value of the static variable is changed for all instances
        Student.projectCount++;
        student2.display();
    }
}
```

Expected output:
```
Alice 20 0
Bob 19 1
```

* `static` methods
A `static` method does not use an instance of the class: it is called by using the `Class.method()` syntax.
```Java
class Student {
    public String name;
    public int age;
    // public data member shared between all instances of the class
    // note: only one projectCount exists in the entire program!
    public static int projectCount = 0;

    Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    void display () {
        System.out.println(name + " " + age + " " + projectCount);
    }

    public static void receiveProjects() {
    	// "this" cannot be accessed here - no available instance
        // only static members or methods can be accessed
    	projectCount++;
    }
}

public class StaticMethodTest {
    public static void main(String args[]){
        System.out.println(Student.projectCount);

        // static method is called without creating an instance of the class
        Student.receiveProjects();

        Student student1 = new Student("Alice", 20);
        student1.display();
    }
}
```

Expected output:
```
0
Alice 20 1
```

## Method call: by value vs by reference
In Java, the parameters can only be **passed by value**.

### Passing primitive types
A copy is always created.

```Java
public class CallByValueTest {
    public static void main(String[] args) {
        int x = 10;
        System.out.println("Before, x = " + x);

        // Call function
        changeX(x);

        System.out.println("After, x = " + x);
    }

    public static void changeX(int x) {
        x = x * 2;
    }
}
```

Expected output:
```
Before, x = 10
After, x = 10
```

### Passing immutable objects
For example, a `String` object is immutable, it cannot be changed because all its fields are final.

```Java
public class CallByValueTest {
	public static void main(String[] args) {
	    String name = "Alice";
	    System.out.println("Before, name = " + name);
	    changeName(name);
	    System.out.println("After, name = " + name);
	}

	public static void changeName(String name) {
            name = "Bob";
	}
}
```

Expected output:
```
Before, name = Alice
After, name = Alice
```

### Passing mutable objects
When passing objects by value, a reference copy is created and it points to the real object in the memory. The changes to the value of the real object are visible.

```Java
class Dog {
    public String breed;
    public Dog(String breed) { this.breed = breed; }
}

public class CallByValueMutableObject {
    public static void main(String []args){
        Dog dog  = new Dog("Bulldog");
        System.out.println("Before, breed = " + dog.breed);
        changeBreed(dog);
        System.out.println("After, breed = " + dog.breed);
     }

     public static void changeBreed(Dog dog) {
        dog.breed = "Poodle";
     }
}
```

Expected output:
```
Before, breed = Bulldog
After, breed = Poodle
```

## var keyword
The `var` keyword allows the feature of local variable type inference. The type of a local variable is no longer declared explicitly, it will be inferred by the compiler.
```Java
List<Integer> numbers = new ArrayList<Integer>();
```
The line above can be replaced by:
```Java
var numbers = new ArrayList<Integer>(); // the type of "numbers" is inferred from the value used in the initialization
```

## Generics
Generics in Java allow to pass to functions or classes the data type as parameter, so there is no need to write the same code for different data types.

### Generic methods
A method may have  generic parameters or return type - the actual type is missing, a placeholder is used: e.g. `<T>` (some type).
* generic parameter type(s)
```Java
public class GenericsTest {
    static <T> void showType (T element) {
        System.out.println(element + " : " + element.getClass());
    }

    public static void main(String[] args) {
        Integer a = 10;
        String b = "abc";
        Boolean c = true;

        showType(a);
        showType(b);
        showType(c);
    }
}
```

Expected output:
```
10 : class java.lang.Integer
abc : class java.lang.String
true : class java.lang.Boolean
```

* generic return type
```Java
public class GenericsTest {
    public static <T extends Comparable<T>> T maxElement(T a, T b) {
        return a.compareTo(b) > 0 ? a : b;
    }

    public static void main(String[] args) {
        System.out.println(maxElement(20, 10));
        System.out.println(maxElement("abc", "xyz"));
    }
}
```

Expected output:
```
20
xyz
```

### Generic classes
Classes which depend of a generic type `T` (e.g. a class with a `T` member - e.g. `T` can be an `Integer` or `String`).

```Java
class GenericObject<T> {
    public T element;

    GenericObject(T element) {
        this.element = element;
    }

    public void showType() {
        System.out.println(element.getClass());
    }
}

public class GenericsTest {
    public static void main (String[] args) {
        GenericObject<Integer> object1 = new GenericObject<Integer>(100);
        GenericObject<String> object2 = new GenericObject<String>("abc");

        object1.showType();
        object2.showType();
    }
}
```

Expected output:
```
class java.lang.Integer
class java.lang.String
```

## Collections
Java Collections is the main group of data structures and algorithms. Please check [Java Collections](./collections.md).
