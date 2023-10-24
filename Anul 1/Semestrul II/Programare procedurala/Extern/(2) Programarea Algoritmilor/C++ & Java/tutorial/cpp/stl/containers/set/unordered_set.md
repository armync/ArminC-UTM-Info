### std::unordered_set
* [cppreference.com/unordered_set](https://en.cppreference.com/w/cpp/container/unordered_set)
* an associative container that contains a set of unique objects. (a.k.a. `unsorted set`)

`std::unordered_set<T>` API (e.g. assume the `std::unordered_set<T> us;` declaration):
* **size()**: e.g. `us.size();` (return the number of elements in the unordered_set - `O(1)`)
* **empty()** e.g. `us.empty();` (check whether the set is empty - `O(1)`)
* **insert()** e.g. `us.insert(some_value);` (insert element  - `O(1)`)
* **find()** e.g. `us.find(some_value);` (return an iterator to the element having the same key or past-the-end() iterator if not found - `O(1)`).
* **erase()** e.g. `us.erase(some_value);` (remove the element matching a key - `O(1)`).
