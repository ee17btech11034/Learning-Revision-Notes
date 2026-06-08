# Ultimate Comprehensive DSA Complexity Cheat Sheet

A complete reference for time and space complexities. This document lists every core data structure, sorting routine, graph traversal, string matcher, and algorithmic pattern formatted clearly as **Best Case $\rightarrow$ Average Case $\rightarrow$ Worst Case**.

---

## 1. Data Structure Operations

### Linear Structures

*   **Array / Static Array**
    *   **Access:** $O(1) \rightarrow O(1) \rightarrow O(1)$
    *   **Search:** $O(1) \rightarrow O(n) \rightarrow O(n)$
    *   **Insertion:** $O(1) \rightarrow O(n) \rightarrow O(n)$
    *   **Deletion:** $O(1) \rightarrow O(n) \rightarrow O(n)$
    *   **Auxiliary Space:** $O(1)$ *(Total Space: $O(n)$)*
*   **Dynamic Array (e.g., Vector/ArrayList)**
    *   **Access:** $O(1) \rightarrow O(1) \rightarrow O(1)$
    *   **Search:** $O(1) \rightarrow O(n) \rightarrow O(n)$
    *   **Insertion (at end):** $O(1) \text{ Amortised} \rightarrow O(1) \text{ Amortised} \rightarrow O(n) \text{ Resizing step}$
    *   **Deletion:** $O(1) \rightarrow O(n) \rightarrow O(n)$
    *   **Auxiliary Space:** $O(1)$ *(Total Space: $O(n)$)*
*   **Singly Linked List**
    *   **Access:** $O(1) \rightarrow O(n) \rightarrow O(n)$
    *   **Search:** $O(1) \rightarrow O(n) \rightarrow O(n)$
    *   **Insertion (at known position/head):** $O(1) \rightarrow O(1) \rightarrow O(1)$
    *   **Deletion (at known position/head):** $O(1) \rightarrow O(1) \rightarrow O(1)$
    *   **Auxiliary Space:** $O(1)$ *(Total Space: $O(n)$)*
*   **Doubly Linked List**
    *   **Access:** $O(1) \rightarrow O(n) \rightarrow O(n)$
    *   **Search:** $O(1) \rightarrow O(n) \rightarrow O(n)$
    *   **Insertion (any position if node reference given):** $O(1) \rightarrow O(1) \rightarrow O(1)$
    *   **Deletion (any position if node reference given):** $O(1) \rightarrow O(1) \rightarrow O(1)$
    *   **Auxiliary Space:** $O(1)$ *(Total Space: $O(n)$)*
*   **Stack**
    *   **Push / Pop / Peek:** $O(1) \rightarrow O(1) \rightarrow O(1)$
    *   **Search:** $O(1) \rightarrow O(n) \rightarrow O(n)$
    *   **Auxiliary Space:** $O(1)$ *(Total Space: $O(n)$)*
*   **Queue / Deque**
    *   **Enqueue / Dequeue:** $O(1) \rightarrow O(1) \rightarrow O(1)$
    *   **Search:** $O(1) \rightarrow O(n) \rightarrow O(n)$
    *   **Auxiliary Space:** $O(1)$ *(Total Space: $O(n)$)*

### Hash-Based Structures

*   **Hash Table / Map / Set**
    *   **Search:** $O(1) \rightarrow O(1) \rightarrow O(n) \text{ High collisions}$
    *   **Insertion:** $O(1) \rightarrow O(1) \rightarrow O(n) \text{ High collisions / resizing}$
    *   **Deletion:** $O(1) \rightarrow O(1) \rightarrow O(n) \text{ High collisions}$
    *   **Auxiliary Space:** $O(1)$ *(Total Space: $O(n)$)*

### Non-Linear Tree Structures

*   **Binary Search Tree (Unbalanced BST)**
    *   **Search:** $O(1) \rightarrow O(\log n) \rightarrow O(n) \text{ Skewed tree}$
    *   **Insertion:** $O(1) \rightarrow O(\log n) \rightarrow O(n) \text{ Skewed tree}$
    *   **Deletion:** $O(1) \rightarrow O(\log n) \rightarrow O(n) \text{ Skewed tree}$
    *   **Auxiliary Space:** $O(1)$
*   **AVL Tree / Red-Black Tree (Self-Balancing BST)**
    *   **Search:** $O(1) \rightarrow O(\log n) \rightarrow O(\log n)$
    *   **Insertion:** $O(\log n) \rightarrow O(\log n) \rightarrow O(\log n)$
    *   **Deletion:** $O(\log n) \rightarrow O(\log n) \rightarrow O(\log n)$
    *   **Auxiliary Space:** $O(1)$
*   **Binary Heap (Min / Max Heap)**
    *   **Find Min/Max:** $O(1) \rightarrow O(1) \rightarrow O(1)$
    *   **Insert (Push):** $O(1) \text{ Leaf node placement} \rightarrow O(\log n) \rightarrow O(\log n)$
    *   **Extract Min/Max (Pop):** $O(1) \rightarrow O(\log n) \rightarrow O(\log n)$
    *   **Search (Arbitrary element):** $O(1) \rightarrow O(n) \rightarrow O(n)$
    *   **Auxiliary Space:** $O(1)$
*   **Trie (Prefix Tree)**
    *   *Where $L$ is string length, $A$ is alphabet size, $N$ is total strings*
    *   **Search / Insert / Delete:** $O(L) \rightarrow O(L) \rightarrow O(L)$
    *   **Total Space Complexity:** $O(A \cdot L \cdot N)$
*   **Segment Tree**
    *   **Build Tree:** $O(n) \rightarrow O(n) \rightarrow O(n)$
    *   **Range Query:** $O(1) \rightarrow O(\log n) \rightarrow O(\log n)$
    *   **Point Update:** $O(1) \rightarrow O(\log n) \rightarrow O(\log n)$
    *   **Auxiliary Space:** $O(n)$
*   **Fenwick Tree (Binary Indexed Tree - BIT)**
    *   **Range Query:** $O(1) \rightarrow O(\log n) \rightarrow O(\log n)$
    *   **Point Update:** $O(1) \rightarrow O(\log n) \rightarrow O(\log n)$
    *   **Auxiliary Space:** $O(n)$

---

## 2. Searching & Sorting Algorithms

### Searching

*   **Linear Search**
    *   **Time Complexity:** $\Omega(1) \rightarrow \Theta(n) \rightarrow O(n)$
    *   **Auxiliary Space:** $O(1)$
*   **Binary Search**
    *   **Time Complexity:** $\Omega(1) \rightarrow \Theta(\log n) \rightarrow O(\log n)$
    *   **Auxiliary Space:** $O(1) \text{ Iterative} \rightarrow O(\log n) \text{ Recursive Call Stack}$

### Sorting

*   **Bubble Sort**
    *   **Time Complexity:** $\Omega(n) \text{ Optimized swap flag} \rightarrow \Theta(n^2) \rightarrow O(n^2)$
    *   **Auxiliary Space:** $O(1)$ | **Stable:** Yes
*   **Insertion Sort**
    *   **Time Complexity:** $\Omega(n) \text{ Already sorted} \rightarrow \Theta(n^2) \rightarrow O(n^2)$
    *   **Auxiliary Space:** $O(1)$ | **Stable:** Yes
*   **Selection Sort**
    *   **Time Complexity:** $\Omega(n^2) \rightarrow \Theta(n^2) \rightarrow O(n^2)$
    *   **Auxiliary Space:** $O(1)$ | **Stable:** No
*   **Merge Sort**
    *   **Time Complexity:** $\Omega(n \log n) \rightarrow \Theta(n \log n) \rightarrow O(n \log n)$
    *   **Auxiliary Space:** $O(n)$ | **Stable:** Yes
*   **Quick Sort**
    *   **Time Complexity:** $\Omega(n \log n) \rightarrow \Theta(n \log n) \rightarrow O(n^2) \text{ Poor pivot choices}$
    *   **Auxiliary Space:** $O(\log n) \text{ Avg Stack Frames} \rightarrow O(n) \text{ Worst Stack Frames}$ | **Stable:** No
*   **Heap Sort**
    *   **Time Complexity:** $\Omega(n \log n) \rightarrow \Theta(n \log n) \rightarrow O(n \log n)$
    *   **Auxiliary Space:** $O(1)$ | **Stable:** No
*   **Counting Sort**
    *   *Where $k$ is the range of the non-negative key inputs*
    *   **Time Complexity:** $\Omega(n + k) \rightarrow \Theta(n + k) \rightarrow O(n + k)$
    *   **Auxiliary Space:** $O(n + k)$ | **Stable:** Yes
*   **Radix Sort**
    *   *Where $k$ is the number of digits/bits per element*
    *   **Time Complexity:** $\Omega(n \cdot k) \rightarrow \Theta(n \cdot k) \rightarrow O(n \cdot k)$
    *   **Auxiliary Space:** $O(n + k)$ | **Stable:** Yes

---

## 3. Graph Algorithms

*   *Where $V$ is vertices/nodes and $E$ is edges/connections*

*   **Breadth-First Search (BFS) / Depth-First Search (DFS)**
    *   **Time Complexity:** $\Omega(V + E) \rightarrow \Theta(V + E) \rightarrow O(V + E)$
    *   **Auxiliary Space:** $O(V)$ *(BFS Queue / DFS Recursion Stack)*
*   **Dijkstra's Shortest Path (Using Binary Min-Heap)**
    *   **Time Complexity:** $\Omega((V + E) \log V) \rightarrow \Theta((V + E) \log V) \rightarrow O((V + E) \log V)$
    *   **Auxiliary Space:** $O(V)$
*   **Bellman-Ford Shortest Path**
    *   **Time Complexity:** $\Omega(E) \text{ Early termination flag} \rightarrow \Theta(V \cdot E) \rightarrow O(V \cdot E)$
    *   **Auxiliary Space:** $O(V)$
*   **Floyd-Warshall (All-Pairs Shortest Path)**
    *   **Time Complexity:** $\Omega(V^3) \rightarrow \Theta(V^3) \rightarrow O(V^3)$
    *   **Auxiliary Space:** $O(V^2)$
*   **Kruskal's Minimum Spanning Tree**
    *   **Time Complexity:** $\Omega(E \log E) \rightarrow \Theta(E \log E) \rightarrow O(E \log E)$ or $O(E \log V)$
    *   **Auxiliary Space:** $O(V + E)$ *(For Disjoint Set Union and tracking edge list)*
*   **Prim's Minimum Spanning Tree (Using Binary Min-Heap)**
    *   **Time Complexity:** $\Omega(E \log V) \rightarrow \Theta(E \log V) \rightarrow O(E \log V)$
    *   **Auxiliary Space:** $O(V)$
*   **Kahn's Topological Sort / DFS-Based Topological Sort**
    *   **Time Complexity:** $\Omega(V + E) \rightarrow \Theta(V + E) \rightarrow O(V + E)$
    *   **Auxiliary Space:** $O(V)$
*   **Tarjan's / Kosaraju's Strongly Connected Components**
    *   **Time Complexity:** $\Omega(V + E) \rightarrow \Theta(V + E) \rightarrow O(V + E)$
    *   **Auxiliary Space:** $O(V)$

---

## 4. String Matching Algorithms

*   *Where $n$ is text length, $m$ is pattern length, and $\Sigma$ is alphabet size*

*   **Naive String Matcher**
    *   **Time Complexity:** $\Omega(n) \rightarrow \Theta(n \cdot m) \rightarrow O(n \cdot m)$
    *   **Auxiliary Space:** $O(1)$
*   **Rabin-Karp Algorithm**
    *   **Time Complexity:** $\Omega(n + m) \rightarrow \Theta(n + m) \rightarrow O(n \cdot m) \text{ Worst case hash collisions}$
    *   **Auxiliary Space:** $O(1)$
*   **Knuth-Morris-Pratt (KMP)**
    *   **Time Complexity:** $\Omega(n + m) \rightarrow \Theta(n + m) \rightarrow O(n + m)$
    *   **Auxiliary Space:** $O(m)$ *(Prefix/$\pi$ array)*
*   **Boyer-Moore Algorithm**
    *   **Time Complexity:** $\Omega(n / m) \text{ Ideal character skips} \rightarrow \Theta(n + m) \rightarrow O(n \cdot m)$
    *   **Auxiliary Space:** $O(m + \Sigma)$ *(Bad character & good suffix shift tables)*

---

## 5. Advanced Design Paradigms

### Dynamic Programming (DP)

*   **0/1 Knapsack Problem** *(Where $W$ is maximum weight capacity)*
    *   **Time Complexity:** $\Omega(n \cdot W) \rightarrow \Theta(n \cdot W) \rightarrow O(n \cdot W)$
    *   **Auxiliary Space:** $\Omega(n \cdot W) \rightarrow \Theta(n \cdot W) \rightarrow O(W) \text{ with space optimization}$
*   **Longest Common Subsequence (LCS)**
    *   **Time Complexity:** $\Omega(n \cdot m) \rightarrow \Theta(n \cdot m) \rightarrow O(n \cdot m)$
    *   **Auxiliary Space:** $\Omega(n \cdot m) \rightarrow \Theta(n \cdot m) \rightarrow O(\min(n, m)) \text{ with row-optimization}$
*   **Edit Distance (Levenshtein Distance)**
    *   **Time Complexity:** $\Omega(n \cdot m) \rightarrow \Theta(n \cdot m) \rightarrow O(n \cdot m)$
    *   **Auxiliary Space:** $\Omega(n \cdot m) \rightarrow \Theta(n \cdot m) \rightarrow O(\min(n, m)) \text{ with row-optimization}$
*   **Matrix Chain Multiplication**
    *   **Time Complexity:** $\Omega(n^3) \rightarrow \Theta(n^3) \rightarrow O(n^3)$
    *   **Auxiliary Space:** $\Omega(n^2) \rightarrow \Theta(n^2) \rightarrow O(n^2)$

### Divide and Conquer & Math

*   **Binary Exponentiation (`pow(x, n)`)**
    *   **Time Complexity:** $\Omega(1) \text{ Power of 0 or 1} \rightarrow \Theta(\log n) \rightarrow O(\log n)$
    *   **Auxiliary Space:** $O(1) \text{ Iterative} \rightarrow O(\log n) \text{ Recursive Call Stack}$
*   **Euclidean Algorithm (Greatest Common Divisor)**
    *   **Time Complexity:** $\Omega(1) \text{ Direct division} \rightarrow \Theta(\log(\min(a, b))) \rightarrow O(\log(\min(a, b)))$
    *   **Auxiliary Space:** $O(1) \text{ Iterative} \rightarrow O(\log(\min(a, b))) \text{ Recursive Call Stack}$
*   **Sieve of Eratosthenes (Prime generation up to $n$)**
    *   **Time Complexity:** $\Omega(n \log \log n) \rightarrow \Theta(n \log \log n) \rightarrow O(n \log \log n)$
    *   **Auxiliary Space:** $\Omega(n) \rightarrow \Theta(n) \rightarrow O(n)$ Boolean tracking array
*   **Karatsuba Integer Multiplication**
    *   **Time Complexity:** $\Omega(n^{\log_2 3}) \rightarrow \Theta(n^{\log_2 3}) \rightarrow O(n^{1.585})$
    *   **Auxiliary Space:** $\Omega(\log n) \rightarrow \Theta(\log n) \rightarrow O(\log n)$ recursion stack frames

