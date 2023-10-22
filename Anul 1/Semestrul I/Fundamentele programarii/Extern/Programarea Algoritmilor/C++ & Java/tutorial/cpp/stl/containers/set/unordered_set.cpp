#include <bits/stdc++.h>

int main() {
    std::unordered_set<int> s;

    // insert element in an unordered_set
    for (int i = 0; i < 5; ++i) {
        s.insert(i);
    }

    // erase one element from unordered_set
    s.erase(4);

    // add another element to see that elements are not sorted
    s.insert(-2);

    // iterate an unordered_set
    for (const auto& elem : s) {
        std::cout << elem << " ";
    }
    std::cout << "\n";

    return 0;
}
