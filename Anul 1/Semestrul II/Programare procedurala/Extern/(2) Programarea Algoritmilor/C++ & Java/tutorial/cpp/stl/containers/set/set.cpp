#include <bits/stdc++.h>

int main() {
    std::set<int> s;

    // insert element in set
    for (int i = 0; i < 5; ++i) {
        s.insert(i);
    }

    // erase one element from set
    s.erase(4);

    // add another element to see that elements are sorted
    s.insert(-2);

    // iterate a set
    for (const auto& elem : s) {
        std::cout << elem << " ";
    }
    std::cout << "\n";

    return 0;
}
