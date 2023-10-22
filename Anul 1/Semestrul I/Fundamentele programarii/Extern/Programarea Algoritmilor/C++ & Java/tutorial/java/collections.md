**Java Collections** is a framework that provides implementation for various data structures and algorithms for storing and manipulating groups of objects. It provides Interfaces and Classes through the `java.util` package.

## ArrayList
* [docs.oracle.com/ArrayList](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html)

The ArrayList class defines a resizable array container which:
* keeps the insertion order, elements being accessed randomly by index (`arr.get(k), k in [0, arr.size() - 1]`) 
* can have duplicate elements

ArrayList methods:
* **size()** = returns the number of elements in the array (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)
* **get(int index)** = returns the element at the specified index (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)
* **isEmpty()** = returns `true` if the list contains no elements, `false` otherwise (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)
* **add(T element)** = appends an element at the end of the list (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)
* **add(int index, T element)** = inserts the element at the specified index (<img src="https://render.githubusercontent.com/render/math?math=O(n)">)
* **remove(int index)** = removes the element at the specified index (<img src="https://render.githubusercontent.com/render/math?math=O(n)">)

```Java
import java.util.ArrayList;
import java.util.List;

public class ArrayListTest {
	public static void main (String[] args) {
		List<Integer> list = new ArrayList<Integer>();
		System.out.println("Is empty: " + list.isEmpty());
		
		list.add(5);
		list.add(1);
		list.add(3);

		System.out.println("Size: " + list.size());
		System.out.println("The first element: " + list.get(0));

		list.remove(0);

		System.out.println("Size: " + list.size());
		System.out.println("The first element: " + list.get(0));
	}
}
```

Expected output:
```
Is empty: true
Size: 3
The first element: 5
Size: 2
The first element: 1
```

### How to iterate over ArrayList
* **index-based loop**

```Java
import java.util.ArrayList;
import java.util.List;

public class ArrayListTest {
	public static void main (String[] args) {
		List<Integer> list = new ArrayList<Integer>();

		// operations on list - e.g. add elements

		for (int i = 0; i < list.size(); i++) {
			// do stuff with the element at the current index i
		}
	}
}
```

* **for-each loop**
```Java
import java.util.ArrayList;
import java.util.List;

public class ArrayListTest {
	public static void main (String[] args) {
		List<Integer> list = new ArrayList<Integer>();

		// operations on list - e.g. add elements

		for (Integer element : list) {
			// do stuff with the current element
		}

		for (var element : list) {
			// do stuff with the current element
		}
	}
}
```

### Example - ArrayList of integers
```Java
import java.util.ArrayList;
import java.util.List;

public class ArrayListTest {
	public static void main (String[] args) {
		List<Integer> list = new ArrayList<Integer>();
		list.add(5);
		list.add(1);
		list.add(3);

		for (var element : list) {
			// the array will not change - Integer is immutable in Java
			element = element * 2;
			// note: if the list type is mutable, the element in the list would change
		}

		for (int i = 0; i < list.size(); i++) {
			// each element will double its value due to the direct access at the list element
			var element = list.get(i) * 2;
			list.set(i, element); 
		}
	}
}
```
### Java Iterator
An `Iterator` object is also useful for iterating over a collection of elements. It is used universally by any kind of Collection object.
Each Collection object has the special method `iterator()` that returns an iterator to the start of the collection.

Iterator methods:
* **hasNext()** = returns a boolean that is true if there still are elements to iterate and false otherwise
* **next()** = returns the next element in the collection
* **remove()** = removes the current element in the iteration

```Java
import java.util.ArrayList;
import java.util.List;
import java.util.Iterator;

public class IteratorTest {
	public static void main (String[] args) {
		List<Integer> list = new ArrayList<Integer>();
		list.add(10);
		list.add(30);
		list.add(20);
		list.add(70);
		list.add(50);

		// Get the Iterator object of the collection
		Iterator iterator = list.iterator();

        	System.out.println("The elements of the collection are:");
		while (iterator.hasNext()) {
			System.out.print(iterator.next() + " ");
		}
	}
}
```

Expected output:
```
The elements of the collection are:
10 30 20 70 50
```

### Which iteration method is best?
* choose the `index-based loop` if you need to use the index of the element (e.g. dynamic programming algorithms)
* choose the `iterator-based loop` to easily change the collection that we loop through
* otherwise, always use the `for-each` loop

## Stack
* [docs.oracle.com/Stack](https://docs.oracle.com/javase/10/docs/api/java/util/Stack.html)

The Stack class defines a generic stack implementation container which:
* is based on the principle of LIFO (last-in-first-out)

Stack methods:
* **push(T element)** = adds the element at the top of the stack (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)
* **pop()** = removes the top element and returns it (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)
* **peek()** = returns the top element of the stack without removing it (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)
* **empty()** = returns a boolean value that is true if there are no elements and false otherwise (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)

```Java
import java.util.Stack;

public class StackTest {
    public static void main(String[] args) {
        Stack<Integer> stack= new Stack<Integer>();
        System.out.println("Stack is empty: " + stack.empty());

        stack.push(100);
        stack.push(200);
        stack.push(500);
        System.out.println("Stack is empty: " + stack.empty());
        System.out.println("The top element is: " + stack.pop());
        System.out.println("The top element is: " + stack);
    }
}
```

Expected output:
```
Stack is empty: true
Stack is empty: false
The top element is: 500
The top element is: [100, 200]
```

## LinkedList

* [docs.oracle.com/LinkedList](https://docs.oracle.com/javase/7/docs/api/java/util/LinkedList.html)

The LinkedList class provides a container that implements a doubly linked list which:
* implements both `Queue` and `List` interfaces
* it is not suitable for frequent random access of the elements in the container

LinkedList methods:
* **size()** = returns the number of elements in the container (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)
* **addFirst(T element)**/**addLast(T element)** = adds an element to the first/last position in the list (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)
* **getFirst()**/**getLast()** = returns the first/last element of the list (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)
* **removeFirst()**/**removeLast()** = removes the first/last element of the list (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)

```Java
import java.util.LinkedList;

public class LinkedListTest {
    public static void main (String[] args) {
        LinkedList<Integer> list = new LinkedList<Integer>();
        System.out.println("Size: " + list.size());

        list.addFirst(1);
        list.addFirst(5);
        list.addLast(9);
        list.addLast(7);
        System.out.println("Size: " + list.size());
        System.out.println("The elements of the list are: " + list);

        list.removeFirst();
        list.removeLast();
        System.out.println("First element: " + list.getFirst());
        System.out.println("Last element: " + list.getLast());
    }
}
```

Expected output:
```
Size: 0
Size: 4
The elements of the list are: [5, 1, 9, 7]
First element: 1
Last element: 9
```

Notes:
* To utilize the Queue interface in Java, the LinkedList class could be used as a FIFO data structure.
  
```Java
public class QueueTest {

    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<String>();
        queue.add("James");
        queue.add("Jane");
        queue.add("Alice");
        queue.add("Bob");
        System.out.println("The elements of the queue are: " + queue);

		// removes and returns the head of the list
        System.out.println("Head element of the queue" + queue.poll());
        System.out.println("Size: " + queue.size());
		
		// returns the head of the list without removing it
        System.out.println("Head element of the queue" + queue.peek());
        System.out.println("Size: " + queue.size());
    }
}
```

Expected output:
```
The elements of the queue are: [James, Jane, Alice, Bob]
Head element of the queue: James
Size: 3
Head element of the queue: Jane
Size: 3
```

## PriorityQueue
* [docs.oracle.com/PriorityQueue](https://docs.oracle.com/javase/7/docs/api/java/util/PriorityQueue.html)

The PriorityQueue class stores and manipulates objects based on their priority:
* implements the `Queue` interface
* based on the implementation of a priority heap

PriorityQueue methods:
* **size()** = returns the number of items in the priority queue (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)
* **add(T e)** = adds the given element to the priority queue (<img src="https://render.githubusercontent.com/render/math?math=O(\log{n})">)
* **peek()** = returns the top element of the queue without removing it (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)
* **poll()** = returns and removes the top element of the queue (<img src="https://render.githubusercontent.com/render/math?math=O(\log{n})">)

```Java
import java.util.PriorityQueue;
import java.util.Queue;

public class PriorityQueueTest {

    public static void main(String[] args) {
        Queue<String> queue = new PriorityQueue<>();
        queue.add("James");
        queue.add("Jane");
        queue.add("Alice");
        queue.add("Bob");
        System.out.println("The elements of the queue are: " + queue);

        // removes and returns the head of the list
        System.out.println("Head element of the queue: " + queue.poll());
        System.out.println("Size: " + queue.size());

        // returns the head of the list without removing it
        System.out.println("Head element of the queue: " + queue.peek());
        System.out.println("Size: " + queue.size());
    }
}

```

Expected output:
```
The elements of the queue are: [Alice, Bob, James, Jane]
Head element of the queue: Alice
Size: 3
Head element of the queue: Bob
Size: 3
```

## HashMap
* [docs.oracle.com/HashMap](https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html)

The HashMap class provides a container that contains key-value pairs with unique keys:
*  it does not provide constant order of the elements over time

HashMap methods:
* **put(K key, V value)** = creates a new entry in the map (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)
* **get(K key)** = returns the value that is mapped to the specified key, or null if the key does not exit (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)
* **remove(K key)** = removes the key-value pair if the key exists in the map (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)
* **size()** = returns the number of items in the map (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)

```Java
import java.util.HashMap;
import java.util.Map;

public class HashMapTest {
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<String, String>();
        System.out.println("The size of the map is: " + map.size());

        map.put("Greece", "Athens");
        map.put("Germany", "Berlin");
        map.put("Ireland", "Dublin");

        System.out.println("The size of the map is: " + map.size());
        System.out.println("The capital of Germany is: " + map.get("Germany"));
        map.remove("Germany");
        System.out.println("The capital of Germany is: " + map.get("Germany"));
    }
}
```

Expected output:
```
The size of the map is: 0
The size of the map is: 3
The capital of Germany is: Berlin
The capital of Germany is: null
```

## TreeMap
* [docs.oracle.com/TreeMap](https://docs.oracle.com/javase/8/docs/api/java/util/TreeMap.html)

The TreeMap class offers a container that contains **sorted** key-value pairs with unique keys:
* it provides a collection of sorted items based on the natural ordering of its keys or by a specified `Comparator`

TreeMap methods:
* **put(K key, V value)** = creates a new entry in the map (<img src="https://render.githubusercontent.com/render/math?math=O(\log{n})">)
* **get(K key)** = returns the value that is mapped to the specified key, or null if the key does not exit (<img src="https://render.githubusercontent.com/render/math?math=O(\log{n})">)
* **remove(K key)** = removes the key-value pair if the key exists in the map (<img src="https://render.githubusercontent.com/render/math?math=O(\log{n})">)
* **size()** = returns the number of items in the map (<img src="https://render.githubusercontent.com/render/math?math=O(1)">)

```Java
import java.util.Map;
import java.util.TreeMap;

public class TreeMapTest {
    public static void main(String[] args) {
        Map<String, String> map = new TreeMap<String, String>();
        System.out.println("The size of the map is: " + map.size());
	
        map.put("Greece", "Athens");
        map.put("Germany", "Berlin");
        map.put("Ireland", "Dublin");
        System.out.println("The size of the map is: " + map.size());
        System.out.println("The capital of Germany is: " + map.get("Germany"));
	
        map.remove("Germany");
        System.out.println("The capital of Germany is: " + map.get("Germany"));
    }
}
```

Expected output:
```
The size of the map is: 0
The size of the map is: 3
The capital of Germany is: Berlin
The capital of Germany is: null
```

