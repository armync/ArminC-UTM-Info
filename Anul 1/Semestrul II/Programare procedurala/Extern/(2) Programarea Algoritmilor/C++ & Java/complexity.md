## Clase de complexități

- Acest document are ca scop asocierea unor algoritmi / clase de algoritmi cu anumite complexități.
De exemplu, pornind de la limita de timp din enunț, se poate deduce care este complexitatea optimă în funcție de variabilele date, iar de la complexitate se pot deduce câțiva posibili algoritmi pentru a rezolva problema dată.

- Pentru un procesor modern, în **C/C++**, numărul de instrucțiuni executate în 1s este în $[10^6, 10^7]$.
- Pentru **Java**, de obicei, timpul de execuție este cel puțin dublu (în special în problemele în care există input sau output cu dimensiuni foarte mari).

|Ordin de mărime|Complexitate|
|-|-|
|$\left[10^{12}, 10^{18}\right]$|$O(\log{n})$|
|$\left[10^{7}, 10^{12}\right]$|$O(\sqrt{n})$|
|$\left[10^{6}, 10^{7}\right]$|$O(n)$|
|$10^{5}$|$O(n \log{n})$|
|$10^{4}$|$O(n \sqrt{n})$|
|$10^{3}$|$O(n^2)$|
|$10^{2}$ |$O(n^3)$|
|$10$|$O(2^n)/O(3^n)$|
|$15$|$O(n!)/O(2^n)$|
|$30 - 40$ (par)|$O(\frac{n}{2}!)/(2 ^ {\frac{n}{2}})$ (Meet in the middle) |


Concluzie: **Ideal** este să găsim o soluție $O(1)$.
Dacă nu se poate, căutăm $O(\log{n})$. Apoi $O(\sqrt{n})$. Și tot așa urcăm în tabel.

# Algoritmi studiați la PA

|Clasă de complexitate| Algoritmi |
|-|-|
|$O(1)$| - răspunsuri directe (par, impar, etc.)<br> - formule simple (ex: suma numerelor de la 1 la n folosind formula lui Gauss)|
|$O(\log{n})$ | - algoritmi de tipul DEI: căutare binară (normală, lower bound, upper bound), exponențiere logaritimică, exponențiere logaritmică pe matrice (optimizarea de la DP) <br> - cmmdc, cmmmc |
|$O(\sqrt{n})$| - factorizarea numerelor<br>- verificare că un numar e prim |
|$O(n)$ = liniar| - parcurgere de vector<br>- recurențe liniare la DP: SSM, numărare<br>- greedy (ex: pe vector) |
|$O(n \log{n})$| - sortări<br>- n căutări binare pe un vector deja sortat<br>- n = parcurgerea unui șir de n elemente, log n = fiecărui element i se aplică log n operații (ex: push/pop heap, compute power) |
|$O(n ^ 2)$ <br>$O(n m)$| - recurențe la DP mai complexe (ex: SCMAX)<br>- operații pe matrice<br>- BFS pe matrice |
|$O(n ^ 3)$| - recurențe DP de tip PODM |
|||
|**Backtracking**||
|$O(2 ^ n)$|- submulțimile unei mulțimi cu n elemente <br>- combinații în probleme de tipul "mereu se poate face stânga sau dreapta, care este numărul total de posibilități?" |
|$O(C(n, k))$<br>$O(n!)$*| - probleme care se reduc la generarea combinărilor|
|$O(A(n, k))$<br>$O(n!)$*|- probleme care se reduc la generarea aranjamentelor|
|$O(P(n))$<br>$O(n!)$|- probleme care se reduc la generarea permutărilor|
||* = o limită relaxată (de exemplu: numărul de aranjamente este mai mic decât n!)|
|||
|**Grafuri**|
|$O(n + m)$ = liniar| - DFS/BFS<br>- orice algoritm bazat pe una sau câteva parcurgeri: ciclu în graf, TopSort, CC, CTC (SCC), BCC / CV / CE, distanțe pe grafuri particulare (arbore, DAG, costuri egale / fără cost)
|$O(m \log{n})$ |- Dijkstra |
|$O(m \log{m})$| - Kruskal / Prim |
|$O(n \log{n} + m)$| - sortarea nodurilor după un criteriu, apoi o parcurgere a grafului|
|$O(m \log{m} + n)$ | - sortarea muchiilor după un criteriu, apoi o parcurgere a grafului|
|$O(n m)$<br>$O(n ^ 2)$| - Bellman-Ford <br> - n parcurgeri pe un graf $n * O(BFS/DFS)$|
|$O(n ^ 3)$|- Roy-Floyd (grafuri dense)|
|$O(n m \log{n})$| - Johnson (grafuri rare)|
|$O(n m^2)$| - Edmonds-Karp|
|$O(b ^ d)$|- A* <br>- Minimax|
