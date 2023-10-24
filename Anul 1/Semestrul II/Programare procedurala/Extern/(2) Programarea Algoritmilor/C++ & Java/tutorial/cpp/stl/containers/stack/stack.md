### std::stack
* [cppreference.com/stack](https://en.cppreference.com/w/cpp/container/stack)
* A generic stack implementation.

`std::stack<T>` API (e.g assume the `std::stack<T> st;` declaration):
* **size()**: e.g. `st.size()` (return the number of elements in the stack - `O(1)`)
* **empty()**: e.g. `st.empty();`(check whether the stack is empty - `O(1)`)
* **top()**: e.g. `auto x = st.top();` (return the top element in the stack - `O(1)`)
* **push()**: e.g. `st.push(some_value)` (insert an element at the top of the stack - `O(1)`)
* **pop()**: e.g. `st.pop()` (remove the top element - `O(1)`)
