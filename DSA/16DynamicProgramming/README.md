# Dynamic Programming (DP) Algorithms

A comprehensive collection of algorithmic solutions based on the **Dynamic Programming** paradigm. This repository highlights how to solve complex optimization problems by breaking them into overlapping subproblems and caching intermediate results.

## 📌 Introduction to Paradigm

**Dynamic Programming (DP)** is an algorithmic technique used to solve problems by combining solutions to subproblems. Unlike Divide and Conquer, DP is specifically used when those subproblems overlap (share the same sub-subproblems).
- DP uses memoization. It tells that remember the output from subproblem and use that in next sub problem.

### Core Concepts
* **Optimal Substructure**: The global optimal solution can be constructed from optimal solutions of its subproblems.
* **Overlapping Subproblems**: The recursive execution visits the exact same subproblems repeatedly rather than generating new ones.

### Implementation Strategies
1. **Top-Down (Memoization)**: Solves problems recursively but caches the results of subproblems in a table to prevent redundant re-computation.
2. **Bottom-Up (Tabulation)**: Avoids recursion by solving the smallest subproblems first and filling up an iterative table system step-by-step.

---

## 🚀 Core Algorithm Implementations

### 1. 0/1 Knapsack Problem
An optimization challenge to maximize value within a strict weight limit, where items cannot be divided.
* **Mechanism**: Evaluates every item by deciding whether to include it or exclude it based on remaining capacity, building a 2D grid of states.
* **Time Complexity**: $O(n \cdot W)$ where $n$ is item count and $W$ is maximum weight capacity.
* **Space Complexity**: $O(n \cdot W)$ for standard tabulation, or $O(W)$ using space-optimized single-row arrays.

### 2. Longest Common Subsequence (LCS)
Finds the longest subsequence present in two distinct strings in the same relative order.
* **Mechanism**: Slices string indices sequentially. If characters match, it increments the state; if they mismatch, it takes the maximum from adjacent states.
* **Time Complexity**: $O(m \cdot n)$ where $m$ and $n$ are the lengths of the two text strings.
* **Space Complexity**: $O(m \cdot n)$ to preserve state coordinates.

### 3. Longest Increasing Subsequence (LIS)
Finds the length of the longest subsequence in a given array such that all elements are sorted in increasing order.
* **Mechanism**: For each index, tracks the longest valid sequence achievable by looking back at all preceding smaller elements.
* **Time Complexity**: $O(n^2)$ via baseline DP, or $O(n \log n)$ optimized using patience sorting and binary search.
* **Space Complexity**: $O(n)$ array allocation.

---

## 📊 Complexity Cheat Sheet

| Algorithm | Time Complexity | Space Complexity | Space Optimized |
| :--- | :--- | :--- | :--- |
| **0/1 Knapsack** | $O(n \cdot W)$ | $O(n \cdot W)$ | $O(W)$ |
| **Longest Common Subsequence** | $O(m \cdot n)$ | $O(m \cdot n)$ | $O(\min(m, n))$ |
| **Longest Increasing Subsequence** | $O(n^2)$ | $O(n)$ | $O(n)$ ($O(n \log n)$ variant) |

---


## 🤝 Contributing
- New DP variants (e.g., Matrix Chain Multiplication, Edit Distance, Coin Change Problem).
