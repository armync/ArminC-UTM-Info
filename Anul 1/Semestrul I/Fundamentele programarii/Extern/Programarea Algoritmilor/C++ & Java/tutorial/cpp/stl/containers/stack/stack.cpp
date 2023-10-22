#include <bits/stdc++.h>

int main() {
    std::stack<int> st;
    for (int i = 0; i < 5; ++i) {
        st.push(i);
    }

    while (!st.empty()) {
        auto top = st.top(); // get the top element
        st.pop(); // remove the top element
        std::cout << top << " "; // 4 3 2 1 0
    }
    std::cout << "\n";

    return 0;
}
