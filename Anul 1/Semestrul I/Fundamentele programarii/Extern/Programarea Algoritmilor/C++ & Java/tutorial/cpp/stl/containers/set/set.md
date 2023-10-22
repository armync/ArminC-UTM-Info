### std::set
* [cppreference.com/set](https://en.cppreference.com/w/cpp/container/set)
* an associative container that contains a **sorted** set of unique objects. (a.k.a `sorted set`)

`std::set<T>` API (e.g. assume the `std::set<T> s;` declaration):
* **size()**: e.g. `s.size()` (return the number of elements in the set - `O(1)`)
* **empty()** e.g. `s.empty();` (check whether the set is empty - `O(1)`)
* **insert()** e.g. `s.insert(some_value);` (insert element  - `O(log n)`)
* **find()** e.g. `s.find(some_value);` (return an iterator to the element having the same key or past-the-end() iterator if not found - `O(log n)`).
* **erase()** e.g. `s.erase(some_value);` (remove the element matching a key - `O(log n)`).

Note: If we want to keep duplicates for the elements, we can use `std::multiset<T>` which has the same API.
