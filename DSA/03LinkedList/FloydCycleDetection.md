# Floyd's Cycle Detection Algorithm (Hare & Tortoise)

Floyd's Cycle Detection Algorithm is an optimized pointer-based approach used to determine if a Linked List contains a cycle (a loop where a node points back to a previous node).

## 🚀 How It Works
The algorithm uses two pointers that move through the linked list at different speeds:
1. **Tortoise (Slow Pointer):** Moves forward by **1 node** per step.
2. **Hare (Fast Pointer):** Moves forward by **2 nodes** per step.

### The Core Logic
* **If there is NO cycle:** The `Fast Pointer` (Hare) will eventually reach the end of the list (`None`), proving that the list is linear.
* **If there IS a cycle:** The `Fast Pointer` will enter the loop first and keep running in circles. Eventually, the `Fast Pointer` will catch up to and meet the `Slow Pointer` from behind inside the loop. 

*Analogy: Imagine a running track. A fast runner will eventually lap a slow runner if they keep running in a circle.*

---

## 📊 Complexity Analysis

| Metric | Complexity | Why? |
| :--- | :--- | :--- |
| **Time Complexity** | **O(N)** | In the worst case, the pointers will meet within a few traversals of the loop length. |
| **Space Complexity** | **O(1)** | It uses constant extra space (only two pointer variables), unlike a Hash Set approach which requires $O(N)$ extra memory. |

---

## 🔍 Step-by-Step Cycle Detection & Removal
If you need to find **where the cycle starts** and **break it**, the algorithm extends into three clear phases:

1. **Detection:** Advance `slow` by 1 and `fast` by 2 until they meet.
2. **Find Start of Cycle:** Move `slow` back to the `head` of the list. Keep `fast` at the meeting point. Move **both** forward at the exact same speed (1 step at a time). The node where they meet again is the absolute **start of the cycle**.
3. **Break the Cycle:** Keep one pointer at the start node and advance the other around the loop to find the trailing "tail" node. Change that tail node's `.next` pointer to `None`.
