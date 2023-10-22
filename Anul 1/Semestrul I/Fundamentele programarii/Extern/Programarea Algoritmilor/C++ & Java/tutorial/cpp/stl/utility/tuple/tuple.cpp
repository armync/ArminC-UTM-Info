#include <bits/stdc++.h>

int main() {
    std::tuple<int, int> t1 = {1, 2};
    std::tuple<int, int, int> t2 = {1, 2, 3};
    std::tuple<int, char, bool, std::string, int> t3 = {1, '2', false, "gigel", -1};

    // example: a 3D position -> tuple of coordinates (e.g. integer coordinates)
    auto [x, y, z]
        = t2; // unpack a tuple into 3 variables: x is the 1st member, y is the 2nd member, z is the 3rd member
    std::cout << x << " " << y << " " << z << "\n";
    return 0;
}
// the members from a std::tuple can also be accessed via std::get
// std::cout << std::get<0>(position) << " " << std::get<1>(position) << " " << std::get<2>(position) << "\n";
// we encourage you to use the structure binding pattern
