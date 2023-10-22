### std::queue

* [cppreference.com/queue](https://en.cppreference.com/w/cpp/container/queue)
* A generic queue implementation.

`std::queue<T>` API (e.g. assume the `std::queue<T> q;` declaration):
* **size()**: e.g. `q.size();` (return the number of elements in the queue - `O(1)`)
* **empty()**: e.g. `q.empty()` (check whether the queue is empty - `O(1)`)
* **front()**: e.g. `auto x = q.front();` (return the first element from queue - `O(1)`).
* **back()**: e.g. `auto x = q.back();` (return the last element from queue - `O(1)`).
* **push()**: e.g. `q.push(some_value);` (insert element at the end - `O(1)`)
* **pop()**: e.g. `q.pop();` (remove the first element element - `O(1)`)
