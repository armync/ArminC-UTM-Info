### std::unordered_map
* [cppreference.com/unordered_map](https://en.cppreference.com/w/cpp/container/unordered_map)
*  associative container that contains **key-value** pairs with **unique keys**. (a.k.a `unordered keys`)

`std::unordered_map<K, V>` API (e.g. assume the `std::unordered_map<K, V> um;` declaration):
* **size()**: e.g. `um.size();` (return the number of elements in the unordered_map - `O(1)`)
* **operator[]** e.g. `um[key] = value;` (return the value mapped to a key, performing an insertion if such key does not exist - `O(1)`).
* **find()**: e.g. `auto it = um.find(some_value);` (return an iterator to the element having the same key or past-the-end iterator if not found - `O(1)`).
* **erase()**: e.g. `um.erase(some_value);` (remove the element matching a key - `O(1)`).
