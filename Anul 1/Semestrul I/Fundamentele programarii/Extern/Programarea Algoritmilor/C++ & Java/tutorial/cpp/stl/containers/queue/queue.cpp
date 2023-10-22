#include <bits/stdc++.h>

int main() {
    std::queue<int> q;
    for (int i = 0; i < 5; ++i) {
        q.push(i);
    }

    while (!q.empty()) {
        auto front = q.front();
        q.pop();
        std::cout << front << " "; // 0 1 2 3 4
    }
    std::cout << "\n";
    return 0;
}
