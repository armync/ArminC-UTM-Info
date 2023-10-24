#include <bits/stdc++.h>

int main() {
    std::pair<std::string, int> p = {"gigel", 3}; // a pair with a string and an integer
    std::pair<int, int> p2 = {0, -1}; // a pair with to integers

    p2.first = 1;
    p2.second = 2;

    std::cout << p.first << " " << p.second << "\n"; // print the pair members

    // structured bindings feature: unpack a pair into components
    auto [x, y] = p2; // unpack a pair p into 2 variables: x = p.first, y = p.second
    std::cout << x << " " << y << '\n';
    return 0;
}
