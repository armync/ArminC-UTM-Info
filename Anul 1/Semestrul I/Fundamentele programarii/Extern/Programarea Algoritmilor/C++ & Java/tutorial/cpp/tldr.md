# PA C++ - TLDR

## PA skel
During the PA laboratories, you'll receive a skeleton for each task.

NOTE: `should` on this page it's considered to be something like tips & tricks for PA (it may not be applicable in other contexts).

```cpp
#include <bits/stdc++.h>
using namespace std;

class Task {
public:
    void solve() {
        read_input();
        get_result();
        print_output();
    }

private:
    // TODO: define members

    void read_input() {
        ifstream fin("in");
        // TODO: read input
        fin.close();
    }

    void get_result() {
        // TODO: implement the solution
    }

    void print_output() {
        ofstream fout("out");
        // TODO: write the solution
        fout.close();
    }
};

// [ATENTIE] NU modifica functia main!
int main() {
    // * se aloca un obiect Task pe heap
    // (se presupune ca e prea mare pentru a fi alocat pe stiva)
    // * se apeleaza metoda solve()
    // (citire, rezolvare, printare)
    // * se distruge obiectul si se elibereaza memoria
    auto* task = new (std::nothrow) Task(); // hint: cppreference/nothrow
    if (!task) {
        std::cerr << "new failed: WTF are you doing? Throw your PC!\n";
        return -1;
    }
    task->solve();
    delete task;
    return 0;
}
```

Notes:
* You `don't` need to include other libraries. `<bits/stdc++.h>` includes everything!
* You `don't` need to ever change the `main()` function!
* You `need` to complete the implementation for the `Task` class.
  * The reading/writing must be done with `<fstream>` for performance reasonse.
    * Usually, the skeleton already implements the `read_input()` and `print_output()` methods.
  * You need to implement the `get_result()` method.
  * Optionally, you can add other helper methods to the class.
* The `check` command compiles and runs the tasks.
  ```bash
  # compile and run all tasks for C++
  ./check cpp

  # compile and run task-1 for C++
  ./check cpp task-1

  # compile and run test 1 for task-1 for C++
  ./check cpp task-1 1
  ```

## C++ tweaks
### IO
You should always use the C++ `skel`.

```cpp
// reading example: assume the input stream is named fin
int x;
fin >> x; // read integer x from file

int x, y;
fin >> x >> y; // read integers x and y from file

int x;
char c;
std::string s;
fin >> x >> c >> s; // read integer x, char c and string s from file
```

```cpp
// writing example: assume the output stream is named fout
int x;
fout << x; // write integer x to file

int x, y;
fout << x << " " << y << "\n"; // write a line: x, space, y, newline

int x;
char c;
std::string s;
fout << x " " << c << " " << s << "\n"; // write a line: x, space, y, space, s, newline
```

### arrays
You should always use `std::vector<T>`.

```cpp
// unitialized vector:
// * use this when you don't know the size
// * use push_back and pop_back to insert/remove elements
std::vector<int> v;
// read example
for (int i = 0; i < n; ++i) {
    int x;
    fin >> x;
    v.push_back(x);
}

// vector with n zeros (0-indexed)
std::vector<int> v(n, 0); // use: v[0], v[1], ... , v[n - 1]
// read example
for (int i = 0; i < n; ++i) {
    fin >> v[i];
}

// vector with n zeros (1-indexed)
std::vector<int> v(n + 1, 0); // use: v[1], v[2], ..., v[n] - e.g. for dynamic programming
// note: v[0] it's allocated, but not used
// read example:
for (int i = 1; i <= n; ++i) {
    fin >> v[i];
}
```

### matrix
You should always use `std::vector<std::vector<T>>`.

```cpp
// most common usage at PA it's 1-indexed matrix for DP
// n x m matrix filled with zeros
std::vector<std::vector<int>> dp(n + 1, std::vector<int>(m + 1, 0));
// use:
// dp[1][1], dp[1][2], ..., dp[1][m]
// ...
// dp[n][1], dp[n][2], ..., dp[n][m]
// note: row 0 and column 0 are not used!
// traversal example:
for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= m; ++j) {
        // do something with dp[i][j]
    }
}
```

### stack
You should always use `std::stack<T>`.

```cpp
std::stack<int> st;
st.push(1);
st.push(2);
st.push(3);

while (!st.empty()) {
    auto top = st.top();
    st.pop();
    std::cout << top << "\n";
}
// print: 3 2 1
```

### queue
You should always use `std::queue<T>`.

```cpp
std::queue<int> q;
q.push(1);
q.push(2);
q.push(3);

while (!st.empty()) {
    auto top = st.top();
    st.pop();
    std::cout << top << "\n";
}
// print: 1 2 3
```

### hashtable
You should always use `std::unordered_map<K, V>`.

```cpp
std::unordered_map<std::string, int> frequency;
frequency["gigel"]++;
frequency["gigel"]++;
frequency["gigel"]++;
frequency["gigel"]++;
frequency["gigel"]++;
frequency["not_gigel"]++;

for (auto& [name, count] : frequency) {
    std::cout << name << " " << count << "\n";
}
// possible output (because it's unordered):
// not_gigel 1
// gigel 5
//
// if using `std::map` the output is guaranteed to be (sorted keys):
// gigel 5
// not_gigel 1
```

### set

#### ordered set
You should always use `std::set<T>` (ascending element order) or `std::set<T, std::greater<T>>` (descending element ordere).

#### unordered set
You should always use `std::unordered_set<T>`.

#### example
```cpp
std::set<int> s;
s.insert(1);
s.insert(12);
s.insert(12);
s.insert(6);
s.insert(6);
s.insert(1);

for (auto x : s) {
    std::cout << s << "\n";
}
// print: 1 6 12
```

### minheap
You should always use `std::multiset<T>`.

```cpp
std::multiset<int> minheap;
minheap.insert(1);
minheap.insert(12);
minheap.insert(6);
minheap.insert(1);

while (!minheap.empty()) {
    auto top = *minheap.begin();
    minheap.erase(minheap.begin());
    std::cout << top << "\n";
}
// print: 1 1 6 12
```

### maxheap
You should always use `std::multiset<T, std::greater<T>>`.

```cpp
std::multiset<int, std::greater<int>> maxheap;
    maxheap.insert(1);
    maxheap.insert(12);
    maxheap.insert(6);
    maxheap.insert(1);

    while (!maxheap.empty()) {
        auto top = *maxheap.begin();
        maxheap.erase(maxheap.begin());
        std::cout << top << "\n";
    }
// print: 12 6 1 1
```
