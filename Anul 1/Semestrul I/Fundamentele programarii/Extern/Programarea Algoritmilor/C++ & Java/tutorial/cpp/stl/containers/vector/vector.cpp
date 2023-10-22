#include <bits/stdc++.h>

int main() {
    std::vector<int> v; // a vector of ints
    v.push_back(5);
    v.push_back(1);
    v.push_back(3);
    std::cout << v.size() << "\n"; // 3 elements
    std::cout << v.back() << "\n"; // the last element is 3
    v.pop_back();
    std::cout << v.size() << "\n"; // the size is 2
    std::cout << v.back() << "\n"; // the last element is 1
    return 0;
}
