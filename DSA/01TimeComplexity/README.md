# Time and Space Complexity Ultimate Cheat Sheet

Complexity analysis measures how an algorithm's execution time and memory usage scale relative to the input size (n).

---

## 1. Asymptotic Notations

Algorithms are evaluated using three primary cases based on input distribution:

*   **Worst Case (O - Big-O):** Maximum resources required. Industry standard because it guarantees a performance floor.
*   **Average Case (Θ - Theta):** Expected resources averaged over all possible inputs.
*   **Best Case (Ω - Omega):** Minimum resources required under ideal conditions.

### Case Comparison Example (Linear Search)
*   **Best Case Ω(1):** Target item is the very first element.
*   **Average Case Θ(n):** Target item is found in the middle.
*   **Worst Case O(n):** Target item is at the end or missing.

---

## 2. Common Complexities (Fastest to Slowest)

\[O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)\]


| Notation | Name | Time Growth Description | Space Growth Description |
| :--- | :--- | :--- | :--- |
| **O(1)** | Constant | Standard arithmetic operations. | No extra memory allocated. |
| **O(log n)**| Logarithmic | Input size cuts in half each step. | Recursion tree depth (Divide & Conquer). |
| **O(n)** | Linear | Proportional to input size. | Allocating a static array of size n. |
| **O(n log n)**| Linearithmic| Efficient sorting steps. | Merge Sort auxiliary array storage. |
| **O(n²)** | Quadratic | Nested iterations over data. | 2D matrix allocation of size n × n. |
| **O(2^n)** | Exponential | Choices double with each input. | Deep recursive call stacks (e.g., subsets).|
| **O(n!)** | Factorial | Every permutation explored. | Storing all possible orderings. |

---

## 3. Memory Breakdown: Space Complexity

Space complexity calculation consists of two distinct components:
\[\text{Total Space} = \text{Auxiliary Space} + \text{Input Space}\]

*   **Input Space:** Memory required to store the input data.
*   **Auxiliary Space:** Extra or temporary memory allocated by the algorithm itself. 
*   **Note:** Interviewers usually care most about **Auxiliary Space**.

---

## 4. Code Reference Examples

### Example A: Linear Search
*   **Time Complexity:** Worst O(n), Average Θ(n), Best Ω(1)
*   **Auxiliary Space:** O(1) (Only uses a single pointer variable `item`)

```python
def find_item(arr, target):
    for item in arr:
        if item == target:
            return True
    return False
```

### Example B: Matrix Pair Generation
*   **Time Complexity:** Worst O(n²) due to nested loops.
*   **Auxiliary Space:** O(n²) because it allocates a new list containing n × n pairs.

```python
def generate_pairs(arr):
    pairs = []
    for i in arr:
        for j in arr:
            pairs.append((i, j))
    return pairs
```

### Example C: Binary Search (Iterative)
*   **Time Complexity:** Worst \(O(\log n)\), Best Ω(1)
*   **Auxiliary Space:** O(1) (Pointers are updated in-place without recursion stack buildup)

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

---

## 5. Practical Analysis Rules

1.  **Drop Lower-Order Terms:** In $O(n^2 + n + 5)$, drop $n$ and $5$ to get $O(n^2)$.
2.  **Drop Constants:** In $O(3n + 10)$, drop coefficients to get $O(n)$.
3.  **Consecutive Steps Add:** Sequential loops perform $O(a + b)$.
4.  **Nested Steps Multiply:** Nested loops perform $O(a \times b)$.
5.  **Track the Call Stack:** Every nested recursive function call adds $O(1)$ to the Space Complexity stack frame.
