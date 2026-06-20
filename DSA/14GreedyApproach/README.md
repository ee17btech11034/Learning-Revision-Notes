# Greedy Approach Algorithms

A comprehensive collection of algorithmic solutions based on the **Greedy Paradigm**. This repository demonstrates how making locally optimal choices at each step can lead to efficient solutions for complex optimization problems.

## 📌 Introduction to Paradigm

The **Greedy Approach** is an algorithmic strategy used to solve optimization problems. It builds up a solution piece by piece, always choosing the next option that offers the most immediate, local benefit.
- Find the local Best Solution and this will lead to Global Best. Like max run on each ball will lead to max score in match.
- It will think for best at that time. (this may lead to less as well). 
### Core Characteristics
* **Irreversible**: Decisions made at any step are final and never reconsidered.
* **Top-Down Choice**: Picks the local optimum without worrying about future consequences.
* **Optimal Substructure**: A global optimal solution contains optimal solutions to its subproblems.
* **Greedy Choice Property**: A global optimal solution can be reached by making local greedy choices.

---

## 🚀 Core Algorithm Implementations

### 1. Fractional Knapsack
An optimization problem to maximize value within a weight limit, where items can be broken into smaller pieces.
* **Mechanism**: Calculates the value-to-weight ratio for each item. It then sorts items in descending order of this ratio and packs them greedily.
* 0/1 knapSack problem (Solved by DP) is either item will be picked fully or not but in fractional Knapsack we can pick the fraction of item as well. 
* **Time Complexity**: $O(n \log n)$ due to the initial sorting step.
* **Space Complexity**: $O(1)$ auxiliary space if sorted in place.

### 2. Huffman Coding
A lossless data compression algorithm that assigns variable-length codes to characters.
* **Mechanism**: Counts character frequencies and builds a binary tree from the bottom up. It greedily pairs the two lowest-frequency nodes at each step.
* **Time Complexity**: $O(n \log n)$ using a priority queue/min-heap.
* **Space Complexity**: $O(n)$ to store the tree nodes.

### 3. Dijkstra's Algorithm
A single-source shortest path algorithm for graphs with non-negative edge weights.
* **Mechanism**: Maintains a set of visited nodes and greedily selects the unvisited node with the absolute smallest tentative distance.
* **Time Complexity**: $O((V + E) \log V)$ when implemented with a binary heap.
* **Space Complexity**: $O(V)$ to store distances and the priority queue.

---

## 📊 Complexity Cheat Sheet

| Algorithm | Best Time | Average Time | Worst Time | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Fractional Knapsack** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ |
| **Huffman Coding** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ |
| **Dijkstra's Algorithm** | $O((V + E) \log V)$ | $O((V + E) \log V)$ | $O((V + E) \log V)$ | $O(V)$ |

---

## 🤝 Contributing
Read more about new greedy solutions (e.g., Prim's Algorithm, Kruskal's Algorithm, Activity Selection Problem).

## Questions:
- Q1. min and max diff of sum of 2 arrays. (max diff = larger elements are in single arr, min means diff of consecutive in sorted )
- Q2. Coin change problem. getting bigger notes first