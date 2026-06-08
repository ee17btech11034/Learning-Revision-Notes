# Comprehensive Data Structures and Algorithms Complexity Cheat Sheet

A comprehensive reference for time and space complexities of core data structures, algorithms, advanced design patterns, and domain-specific techniques.

---

## 1. Data Structure Complexities

### Basic Operations


| Data Structure | Access | Search | Insertion | Deletion | Space Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Array** | $O(1)$ | $O(n)$ | $O(n)$ | $O(n)$ | $O(n)$ |
| **Dynamic Array** | $O(1)$ | $O(n)$ | $O(1)$ Amortised | $O(n)$ | $O(n)$ |
| **Singly Linked List** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ | $O(n)$ |
| **Doubly Linked List** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ | $O(n)$ |
| **Stack** | $O(n)$ | $O(n)$ | $O(1)$ (Push) | $O(1)$ (Pop) | $O(n)$ |
| **Queue** | $O(n)$ | $O(n)$ | $O(1)$ (Enqueue) | $O(1)$ (Dequeue) | $O(n)$ |
| **Hash Table** | N/A | $O(1)$ Avg / $O(n)$ Worst | $O(1)$ Avg / $O(n)$ Worst | $O(1)$ Avg / $O(n)$ Worst | $O(n)$ |

### Tree and Graph Structures


| Structure | Access | Search | Insertion | Deletion | Space Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Binary Search Tree (BST)** | $O(\log n)$ Avg<br>$O(n)$ Worst | $O(\log n)$ Avg<br>$O(n)$ Worst | $O(\log n)$ Avg<br>$O(n)$ Worst | $O(\log n)$ Avg<br>$O(n)$ Worst | $O(n)$ |
| **AVL Tree (Balanced BST)**| $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| **Red-Black Tree** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| **Min/Max Heap** | N/A | $O(n)$ | $O(\log n)$ | $O(\log n)$ (Extract) | $O(n)$ |
| **Trie (Prefix Tree)** | N/A | $O(L)$ | $O(L)$ | $O(L)$ | $O(A \cdot L \cdot N)$ |
| **Segment Tree** | N/A | $O(\log n)$ (Query) | $O(\log n)$ (Update) | N/A | $O(n)$ |
| **Fenwick Tree (BIT)** | N/A | $O(\log n)$ (Query) | $O(\log n)$ (Update) | N/A | $O(n)$ |
| **Graph (Adjacency List)** | N/A | $O(V + E)$ | $O(1)$ | $O(V + E)$ | $O(V + E)$ |
| **Graph (Adjacency Matrix)** | N/A | $O(V)$ | $O(1)$ | $O(1)$ | $O(V^2)$ |

*Note: For Trie, $L$ is string length, $A$ is alphabet size, $N$ is total strings. For Fenwick/Segment trees, $n$ is array size.*

---

## 2. Sorting and Searching Algorithms


| Algorithm | Best Time | Average Time | Worst Time | Auxiliary Space | Stable? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Linear Search** | $\Omega(1)$ | $\Theta(n)$ | $O(n)$ | $O(1)$ | N/A |
| **Binary Search** | $\Omega(1)$ | $\Theta(\log n)$ | $O(\log n)$ | $O(1)$ Iterative<br>$O(\log n)$ Recursive | N/A |
| **Bubble Sort** | $\Omega(n)$ | $\Theta(n^2)$ | $O(n^2)$ | $O(1)$ | Yes |
| **Insertion Sort** | $\Omega(n)$ | $\Theta(n^2)$ | $O(n^2)$ | $O(1)$ | Yes |
| **Selection Sort** | $\Omega(n^2)$ | $\Theta(n^2)$ | $O(n^2)$ | $O(1)$ | No |
| **Merge Sort** | $\Omega(n \log n)$ | $\Theta(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes |
| **Quick Sort** | $\Omega(n \log n)$ | $\Theta(n \log n)$ | $O(n^2)$ | $O(\log n)$ Avg stack frames | No |
| **Heap Sort** | $\Omega(n \log n)$ | $\Theta(n \log n)$ | $O(n \log n)$ | $O(1)$ | No |
| **Counting Sort** | $\Omega(n + k)$ | $\Theta(n + k)$ | $O(n + k)$ | $O(n + k)$ | Yes |
| **Radix Sort** | $\Omega(nk)$ | $\Theta(nk)$ | $O(nk)$ | $O(n + k)$ | Yes |

---

## 3. Graph and Network Algorithms


| Algorithm | Domain / Problem Solved | Worst-Case Time | Auxiliary Space |
| :--- | :--- | :--- | :--- |
| **Breadth-First Search (BFS)** | Unweighted shortest path / Traversal | $O(V + E)$ | $O(V)$ |
| **Depth-First Search (DFS)** | Topological sort / Connectivity / Traversal | $O(V + E)$ | $O(V)$ stack |
| **Dijkstra's (Min-Heap)** | Single-source shortest path (no negative weights) | $O((V + E) \log V)$ | $O(V)$ |
| **Bellman-Ford** | Single-source shortest path (supports negative weights)| $O(VE)$ | $O(V)$ |
| **Floyd-Warshall** | All-pairs shortest path | $O(V^3)$ | $O(V^2)$ |
| **Kruskal's (with DSU)** | Minimum Spanning Tree (Edge-focused) | $O(E \log E)$ or $O(E \log V)$ | $O(V + E)$ |
| **Prim's (Min-Heap)** | Minimum Spanning Tree (Vertex-focused) | $O(E \log V)$ | $O(V)$ |
| **Kosaraju's** | Strongly Connected Components (2 DFS passes) | $O(V + E)$ | $O(V)$ |
| **Tarjan's** | Strongly Connected Components (1 DFS pass) | $O(V + E)$ | $O(V)$ |
| **Kahn's Algorithm** | Topological Sort (Indegree/Queue-based) | $O(V + E)$ | $O(V)$ |
| **Ford-Fulkerson** | Maximum Network Flow | $O(E \cdot f)$ *(f = max flow)* | $O(V)$ |
| **Edmonds-Karp** | Maximum Network Flow (BFS-based) | $O(V \cdot E^2)$ | $O(V + E)$ |

---

## 4. String Matching Algorithms


| Algorithm | Best Time | Average Time | Worst Time | Auxiliary Space |
| :--- | :--- | :--- | :--- | :--- |
| **Naive Approach** | $\Omega(n)$ | $\Theta(n \cdot m)$ | $O(n \cdot m)$ | $O(1)$ |
| **Rabin-Karp** | $\Omega(n + m)$ | $\Theta(n + m)$ | $O(n \cdot m)$ spurious hits | $O(1)$ |
| **Knuth-Morris-Pratt (KMP)**| $\Omega(n + m)$ | $\Theta(n + m)$ | $O(n + m)$ | $O(m)$ pi-array |
| **Boyer-Moore** | $\Omega(n / m)$ | $\Theta(n + m)$ | $O(n \cdot m)$ | $O(m + \Sigma)$ |
| **Aho-Corasick** | $O(n + m + z)$ | $O(n + m + z)$ | $O(n + m + z)$ | $O(m \cdot \Sigma)$ |

*Note: $n$ = text length, $m$ = pattern length, $z$ = total match occurrences, $\Sigma$ = alphabet size.*

---

## 5. Algorithmic Paradigms & Famous Sub-Algorithms

### Dynamic Programming (DP) & Memoization
*   **0/1 Knapsack:** Time: $O(n \cdot W)$ | Space: $O(n \cdot W)$ optimization to $O(W)$
*   **Longest Common Subsequence (LCS):** Time: $O(n \cdot m)$ | Space: $O(n \cdot m)$
*   **Matrix Chain Multiplication:** Time: $O(n^3)$ | Space: $O(n^2)$
*   **Edit Distance (Levenshtein):** Time: $O(n \cdot m)$ | Space: $O(n \cdot m)$

### Greedy & Divide and Conquer
*   **Fractional Knapsack:** Time: $O(n \log n)$ sorting cost | Space: $O(1)$
*   **Huffman Coding:** Time: $O(n \log n)$ | Space: $O(n)$
*   **Binary Exponentiation:** Time: $O(\log n)$ | Space: $O(1)$ or $O(\log n)$ recursive stack
*   **Karatsuba Multiplication:** Time: $O(n^{\log_2 3}) \approx O(n^{1.585})$ | Space: $O(\log n)$

### Mathematical & Cryptographic / Geometric
*   **Sieve of Eratosthenes (Primes):** Time: $O(n \log \log n)$ | Space: $O(n)$
*   **Euclidian GCD:** Time: $O(\log(\min(a, b)))$ | Space: $O(1)$
*   **Graham Scan (Convex Hull):** Time: $O(n \log n)$ | Space: $O(n)$

---

## 6. Advanced Coding Patterns Reference


| Pattern Design | Key Indicator | Core Complexity Behavior |
| :--- | :--- | :--- |
| **Sliding Window** | Subarray/Substring constraints (Max, Min, K-distinct) | Time: $O(n)$ sliding pointers. Space: $O(1)$ or $O(k)$ for frequency tracking. |
| **Two Pointers** | Sorted arrays, pair hunting, reversing data arrays | Time: $O(n)$ linear traversal. Space: $O(1)$ scalar manipulation. |
| **Fast & Slow Pointers**| Linked list cycles, midpoints, loop tracking | Time: $O(n)$ cycle bounding. Space: $O(1)$ node tracking variables. |
| **Merge Intervals** | Overlapping periods, calendar schedules, range splits| Time: $O(n \log n)$ initial sort bottleneck. Space: $O(n)$ or $O(1)$ sorting array mutation. |
| **Top K Elements** | Find the $K$ largest, smallest, or most frequent items | Time: $O(n \log k)$ heap streaming limit. Space: $O(k)$ heap footprint container. |
| **Monotonic Stack/Queue** | Next greater element, histogram areas, sliding maximums| Time: $O(n)$ amortised push/pop cycles. Space: $O(n)$ index tracker boundary array. |

---

## 7. Analysis Cheat Rules for Interview Mastery

1.  **Bitwise Shortcuts:** Basic bit manipulation (`AND`, `OR`, `XOR`, shifts) runs in $O(1)$ time and $O(1)$ space.
2.  **Backtracking Matrix Boundary:** Generating state trees (like N-Queens or Permutations) scales at exponential rates ($O(2^n)$ or $O(n!)$) with tree structural bounds matching recursion trace depth $O(n)$.
3.  **Amortised Dynamic Scaling:** Resizing continuous array structures doubles sizes step-wise. Single inserts trigger $O(n)$ copies rarely, yielding true $O(1)$ across sequential loops.
4.  **Tree Paths Rule:** Balanced tree options split work cleanly down tree branching lines, lowering item lookups to exact mathematical heights of $O(\log n)$. Unbalanced tree links fail this rule, collapsing back down into long $O(n)$ linear lines.
