#include <bits/stdc++.h>

int main() {
    std::multiset<int> ms;
    ms.insert(1);
    ms.insert(2);
    ms.insert(3);
    ms.insert(3);
    ms.insert(2);
    ms.insert(1);

    // iterate a set
    for (const auto& elem : ms) {
        std::cout << elem << " ";
    }
    std::cout << "\n";

    return 0;
}

// Compile:
// $ make
//
// Run:
// ./multiset
// 1 1 2 2 3 3
//
