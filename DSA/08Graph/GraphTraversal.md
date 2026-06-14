# Graph Traversal: BFS and DFS

Graph traversal algorithms are fundamental techniques used to visit all the vertices (nodes) of a graph in a systematic order. 

---

## 1. Breadth-First Search (BFS)

BFS explores the graph layer by layer, visiting all neighbors of a node before moving to the next level. It uses a **Queue** data structure (FIFO).

### Steps to Follow
* **Step 1**: Initialize an empty queue and a `visited` tracking structure (array or set) of size $V$.
* **Step 2**: Enqueue the starting vertex and mark it as visited.
* **Step 3**: Loop while the queue is not empty.
* **Step 4**: Dequeue the front vertex from the queue.
* **Step 5**: Process the dequeued vertex (e.g., print it, check for target).
* **Step 6**: For each unvisited neighbor of this vertex, mark it as visited and enqueue it.

### Complexity Analysis (Standard Adjacency List)
* **Time Complexity (TC)**: $\Omega(V) \rightarrow O(V + E) \rightarrow O(V + E)$ *(Best $\rightarrow$ Avg $\rightarrow$ Worst)*
    * *Detail:* Best case occurs when the graph contains no edges ($E=0$), meaning the algorithm only spends time iterating through the initial vertex list.
* **Space Complexity (SC)**: $\Omega(V) \rightarrow O(V) \rightarrow O(V)$ *(Best $\rightarrow$ Avg $\rightarrow$ Worst)*
    * *Detail:* Bounded by the explicit `visited` tracker of size $V$ and the dynamic queue allocation.

---

## 2. Depth-First Search (DFS)

DFS explores the graph by going as deep as possible along each branch before backtracking. It uses a **Stack** data structure (LIFO), typically implemented via recursion.

### Steps to Follow
* **Step 1**: Initialize a `visited` tracking structure (array or set) of size $V$.
* **Step 2**: Create a recursive function that takes the current vertex.
* **Step 3**: Mark the current vertex as visited and process it.
* **Step 4**: Iterate through all the neighbors of the current vertex.
* **Step 5**: If a neighbor is unvisited, recursively call the function for that neighbor.
* **Step 6**: Repeat until all reachable vertices are visited.

### Complexity Analysis (Standard Adjacency List)
* **Time Complexity (TC)**: $\Omega(V) \rightarrow O(V + E) \rightarrow O(V + E)$ *(Best $\rightarrow$ Avg $\rightarrow$ Worst)*
    * *Detail:* Best case occurs when the graph contains no edges ($E=0$), forcing the traversal loop to instantly skip neighbors for each vertex.
* **Space Complexity (SC)**: $\Omega(V) \rightarrow O(V) \rightarrow O(V)$ *(Best $\rightarrow$ Avg $\rightarrow$ Worst)*
    * *Detail:* Bounded by the explicit `visited` tracker of size $V$ and the depth of the recursive call stack.

---

## Comparison Summary

| Feature | BFS | DFS |
| :--- | :--- | :--- |
| **Data Structure** | Queue (FIFO) | Stack (LIFO / Recursion) |
| **Exploration** | Level-by-level | Branch-by-branch |
| **Shortest Path** | Guarantees shortest path in unweighted graphs | Does not guarantee shortest path |
| **Memory Footprint** | High for broad, shallow graphs (wide levels) | High for narrow, highly deep graphs |
