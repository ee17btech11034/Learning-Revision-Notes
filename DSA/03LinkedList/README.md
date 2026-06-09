# Linked Lists Reference Manual

A linked list is a linear data structure where elements are not stored at contiguous memory locations. Instead, elements are dynamically allocated and linked together using pointers (in c/c++)/reference variables (in python). Each node has 2 parts `data` and address to next node `next`.

---

## 📊 Summary Comparison Matrix

| Data Structure | Access / Search | Insert / Delete (Head) | Insert / Delete (Tail) | Pointer Overhead | Main Advantage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Singly Linked List (SLL)** | $O(n)$ | $O(1)$ | $O(n)$ *($O(1)$ with tail ptr for insert)* | Minimal (1 pointer/node) | Memory efficient, simple |
| **Doubly Linked List (DLL)** | $O(n)$ | $O(1)$ | $O(1)$ *($O(n)$ without tail ptr)* | Medium (2 pointers/node) | Bidirectional traversal, $O(1)$ deletion given node reference |
| **Circular Singly (CSLL)** | $O(n)$ | $O(1)$ *with tail ptr* | $O(n)$ *for delete (needs prev)* | Minimal (1 pointer/node) | Infinite looping, clear end-to-beginning wrap |
| **Circular Doubly (CDLL)** | $O(n)$ | $O(1)$ | $O(1)$ | Medium (2 pointers/node) | Complete elimination of NULL pointers, instant access to both ends |

---

## 🛠️ Data Structure Breakdowns

### 1. Singly Linked List (SLL)

#### Overview
Each node contains a data field and a **single pointer** (`next`) to the subsequent node. The final node points to `NULL`. It only supports forward traversal.

#### Pointer Architecture
```text
[Head] -> [Data | Next] -> [Data | Next] -> [Data | Next] -> NULL
```

#### Best Use Cases
*   Implementing **Stacks** (LIFO) where operations happen exclusively at the head.
*   Simple unidirectional data caching or forward-only history tracking.
*   Systems with highly constrained memory where second-pointer overhead is unacceptable.

#### Operations & Complexities *(Where $n$ is the number of nodes)*
*   **Access / Search element**
    *   **Time Complexity:** $\Omega(1)$ Head element $\rightarrow \Theta(n) \rightarrow O(n)$ Tail or missing element
    *   **Auxiliary Space:** $O(1)$
*   **Insertion at Head**
    *   **Time Complexity:** $\Omega(1) \rightarrow \Theta(1) \rightarrow O(1)$
    *   **Auxiliary Space:** $O(1)$
*   **Insertion at Tail**
    *   **Time Complexity:** $\Omega(1)$ With tail pointer $\rightarrow \Theta(n) \rightarrow O(n)$ Without tail pointer
    *   **Auxiliary Space:** $O(1)$
*   **Insertion at Specific Index / Arbitrary Position**
    *   **Time Complexity:** $\Omega(1)$ Index 0 $\rightarrow \Theta(n) \rightarrow O(n)$ End of list
    *   **Auxiliary Space:** $O(1)$
*   **Deletion at Head**
    *   **Time Complexity:** $\Omega(1) \rightarrow \Theta(1) \rightarrow O(1)$
    *   **Auxiliary Space:** $O(1)$
*   **Deletion at Tail**
    *   **Time Complexity:** $\Omega(1)$ If list has $\le 1$ node $\rightarrow \Theta(n) \rightarrow O(n)$ Must traverse to find second-to-last node
    *   **Auxiliary Space:** $O(1)$
*   **Deletion of a Node by Value / Specific Index**
    *   **Time Complexity:** $\Omega(1)$ Delete head $\rightarrow \Theta(n) \rightarrow O(n)$ Delete tail or missing value
    *   **Auxiliary Space:** $O(1)$
*   **Reverse List (In-place)**
    *   **Time Complexity:** $\Omega(n) \rightarrow \Theta(n) \rightarrow O(n)$
    *   **Auxiliary Space:** $O(1)$ Iterative $\rightarrow O(n)$ Recursive Call Stack

---

### 2. Doubly Linked List (DLL)

#### Overview
Each node contains a data field and **two pointers**: `next` (points forward) and `prev` (points backward). The head's `prev` and the tail's `next` both point to `NULL`. This enables bidirectional traversal and $O(1)$ deletions given a direct node reference.

#### Pointer Architecture
```text
NULL <- [Prev | Data | Next] <-> [Prev | Data | Next] <-> [Prev | Data | Next] -> NULL
```

#### Best Use Cases
*   **Browser Cache Navigation** (Forward and Back buttons).
*   **LRU (Least Recently Used) Cache** implementations (requires fast insertion and deletion at both ends).
*   Text editor buffers managing cursor positions moving left and right.

#### Operations & Complexities *(Where $n$ is the number of nodes)*
*   **Access / Search element**
    *   **Time Complexity:** $\Omega(1)$ Head/Tail elements $\rightarrow \Theta(n) \rightarrow O(n)$ Middle or missing element
    *   **Auxiliary Space:** $O(1)$
*   **Insertion at Head**
    *   **Time Complexity:** $\Omega(1) \rightarrow \Theta(1) \rightarrow O(1)$
    *   **Auxiliary Space:** $O(1)$
*   **Insertion at Tail**
    *   **Time Complexity:** $\Omega(1)$ With tail pointer $\rightarrow \Theta(n) \rightarrow O(n)$ Without tail pointer
    *   **Auxiliary Space:** $O(1)$
*   **Insertion Before / After a Given Node Reference**
    *   **Time Complexity:** $\Omega(1) \rightarrow \Theta(1) \rightarrow O(1)$ Immediate pointer manipulation via `prev`/`next`
    *   **Auxiliary Space:** $O(1)$
*   **Deletion at Head**
    *   **Time Complexity:** $\Omega(1) \rightarrow \Theta(1) \rightarrow O(1)$
    *   **Auxiliary Space:** $O(1)$
*   **Deletion at Tail**
    *   **Time Complexity:** $\Omega(1)$ With tail pointer, instantly access prev node $\rightarrow \Theta(n) \rightarrow O(n)$ Without tail pointer
    *   **Auxiliary Space:** $O(1)$
*   **Deletion of a Given Node Reference**
    *   **Time Complexity:** $\Omega(1) \rightarrow \Theta(1) \rightarrow O(1)$ No traversal needed to look up the previous node
    *   **Auxiliary Space:** $O(1)$
*   **Reverse List (In-place)**
    *   **Time Complexity:** $\Omega(n) \rightarrow \Theta(n) \rightarrow O(n)$ Swapping `next` and `prev` pointers for all nodes
    *   **Auxiliary Space:** $O(1)$

---

### 3. Circular Singly Linked List (CSLL)

#### Overview
A modified SLL where the `next` pointer of the **last node points back to the head node**, forming a continuous loop. There is no `NULL` terminator.

#### Pointer Architecture
```text
+-------------------------------------------------+

|                                                 |
v                                                 |
[Head] -> [Data | Next] -> [Data | Next] -> [Data | Next]
```

#### Best Use Cases
*   **Round-Robin Scheduling** in Operating Systems (allocating CPU time to processes sequentially in a loop).
*   Multiplayer gaming loops where turns rotate continuously from the last player back to the first player.

#### Operations & Complexities *(Where $n$ is the number of nodes)*
*   **Access / Search element**
    *   **Time Complexity:** $\Omega(1)$ Head element $\rightarrow \Theta(n) \rightarrow O(n)$ Full cycle traversal
    *   **Auxiliary Space:** $O(1)$
*   **Insertion at Head**
    *   **Time Complexity:** $\Omega(1)$ With tail pointer $\rightarrow \Theta(n) \rightarrow O(n)$ Without tail pointer *(must traverse to update last node's next)*
    *   **Auxiliary Space:** $O(1)$
*   **Insertion at Tail**
    *   **Time Complexity:** $\Omega(1)$ With tail pointer $\rightarrow \Theta(n) \rightarrow O(n)$ Without tail pointer
    *   **Auxiliary Space:** $O(1)$
*   **Deletion at Head**
    *   **Time Complexity:** $\Omega(1)$ With tail pointer $\rightarrow \Theta(n) \rightarrow O(n)$ Without tail pointer
    *   **Auxiliary Space:** $O(1)$
*   **Deletion at Tail**
    *   **Time Complexity:** $\Omega(n) \rightarrow \Theta(n) \rightarrow O(n)$ Always requires traversal to locate the second-to-last node
    *   **Auxiliary Space:** $O(1)$

---

### 4. Circular Doubly Linked List (CDLL)

#### Overview
A hybrid configuration where the **last node's `next` points to the head**, and the **head's `prev` points to the last node**. This structure completely eliminates `NULL` pointers and provides instantaneous $O(1)$ access to both ends of the list using just the head pointer.

#### Pointer Architecture
```text
+-------------------------------------------------------+

|                                                       |
v                                                       |
[Head] <-> [Prev | Data | Next] <-> [Prev | Data | Next]+
^                                                       |

|                                                       |
+-------------------------------------------------------+
```

#### Best Use Cases
*   **Media Playlists** supporting continuous looped playback alongside immediate "Previous Track" and "Next Track" capabilities.
*   Advanced buffer management inside real-time operating systems.

#### Operations & Complexities *(Where $n$ is the number of nodes)*
*   **Access / Search element**
    *   **Time Complexity:** $\Omega(1)$ Head/Tail elements $\rightarrow \Theta(n) \rightarrow O(n)$
    *   **Auxiliary Space:** $O(1)$
*   **Insertion at Head**
    *   **Time Complexity:** $\Omega(1) \rightarrow \Theta(1) \rightarrow O(1)$ Instantly achieved via `head->prev`
    *   **Auxiliary Space:** $O(1)$
*   **Insertion at Tail**
    *   **Time Complexity:** $\Omega(1) \rightarrow \Theta(1) \rightarrow O(1)$ Instantly achieved via `head->prev`
    *   **Auxiliary Space:** $O(1)$
*   **Deletion at Head**
    *   **Time Complexity:** $\Omega(1) \rightarrow \Theta(1) \rightarrow O(1)$ Updates head pointer and links new head with the last node
    *   **Auxiliary Space:** $O(1)$
*   **Deletion at Tail**
    *   **Time Complexity:** $\Omega(1) \rightarrow \Theta(1) \rightarrow O(1)$ Bypasses the last node using `head->prev->prev`
    *   **Auxiliary Space:** $O(1)$

---

## 🎯 Essential Algorithmic Patterns

When handling linked list technical questions, keep these patterns in mind:

1.  **Fast & Slow Pointers (Two-Pointer / Floyd's Cycle):** Move one pointer twice as fast as the other. Used to find the middle of a list ($O(n)$ time, $O(1)$ space) or detect cycles.
2.  **Dummy Head Node:** Always use a dummy node (`dummy = Node(0)`) when structural mutations happen at the head of the list (e.g., merging lists, deleting nodes). This eliminates edge-case conditional logic.
3. **Pointer Swap Order:** When inserting into a DLL/CDLL, always bind the new node's outgoing pointers first before severing existing structural pointers to avoid breaking the chain.


## Questions:
1. Josephus Problem.