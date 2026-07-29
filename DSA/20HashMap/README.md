# Hashing and Maps: Core DSA Notes

## 1. Fundamentals & Definitions

### Hashing
A technique that maps data of arbitrary size to fixed-size values using a mathematical function. 

### Hash Function
A function that converts an input key into a specific numerical index within an array. 

### Collision
An event where two distinct keys produce the exact same hash index.

### Collision Resolution Techniques
* **Chaining:** Linked lists store multiple elements at the same hash index.
* **Open Addressing:** Finds alternative empty slots using linear probing, quadratic probing, or double hashing.

### Map / HashMap
A data structure that stores data sequentially in key-value pairs. 

### Set / HashSet
A data structure that stores unique elements without any duplicate values.

---

## 2. Array Size Restrictions vs. Hashing

When implementing counting or frequency patterns, using a direct frequency array has strict memory limitations imposed by the system stack and heap. Exceeding these limits causes a **Segmentation Fault** (Stack Overflow).

### Direct Frequency Array Limits

* **Integer Arrays (`int arr[]`):**
  * **Inside Local Function (Stack Memory):** Maximum size $\approx 10^6$ elements.
  * **Globally / Statically (Heap/Data Segment):** Maximum size $\approx 10^7$ elements.
* **Boolean Arrays (`bool arr[]`):**
  * **Inside Local Function (Stack Memory):** Maximum size $\approx 10^7$ elements.
  * **Globally / Statically (Heap/Data Segment):** Maximum size $\approx 10^8$ elements.

---

### Handling Large Inputs (e.g., $10^9$)

If your input values can be up to $10^9$, you **cannot** allocate a static array of size `arr[10^9]`. The system will immediately throw a segmentation fault because it requires gigabytes of contiguous memory.

#### The Hashing Solution
To track frequencies or existence for large bounds like $10^9$, you must use a **HashMap (`dict` in Python)** or a **HashSet (`set` in Python)**.

* **Memory Efficiency:** Instead of allocating $10^9$ slots in memory, a Hash Map only allocates memory for the *unique elements actually present* in the input.
* **Example:** If an array contains only 5 distinct numbers (even if those numbers are as large as $1,000,000,000$), a HashMap will only store 5 key-value pairs, keeping the auxiliary space at a safe $O(N)$ instead of an impossible $O(\text{Max Value})$.


---

## 3. Time & Auxiliary Space Complexity

### Time Complexity

#### HashMap / HashSet (Unordered / Hash-Table Based)
* **Insert:** Ω(1) no collision --> Θ(1) uniform distribution --> O(N) when all keys hash to the same bucket (due to collisions).
* **Delete:** Ω(1) when element is found immediately --> Θ(1) with proper load factor management --> O(N) when traversing a long collision chain.
* **Search:** Ω(1) when key sits directly at hash index --> Θ(1) for standard key lookups --> O(N) when bucket behaves like a linear list.

#### TreeMap / TreeSet (Ordered / Balanced BST Based)
* **Insert:** Ω(1) if element matches root or immediate leaf --> Θ(log N) as tree height scales logarithmically --> O(log N) due to strict auto-balancing rules
* **Delete:** Ω(1) if element matches root or immediate leaf --> Θ(log N) to find and rebalance tree --> O(log N) for deep node rotations
* **Search:** Ω(1) if element matches root or immediate leaf --> Θ(log N) as tree height scales logarithmically --> O(log N)  when traversing to deepest leaf node

### Auxiliary Space Complexity
* **HashMap / HashSet (Unordered / Hash-Table Based)** Ω(1) when table is initialized empty --> Θ(N) to scale dynamically with elements --> O(N) allocations for bucket arrays and nodes.
* **TreeMap / TreeSet (Ordered / Balanced BST Based)** Ω(1) before any items are inserted --> Θ(N) to store parent, child, and color pointers --> O(N) overhead for tracking tree structural properties.


---

## 4. Important DSA Patterns

### Frequency Counting
* Uses a hash map to track occurrences of elements.
* Useful for identifying duplicates, majorities, or anagrams.

### Two-Pointer Complement Search
* Stores seen elements in a hash set while iterating.
* Checks if the complement (`target - current`) already exists in the set.

### Sliding Window with HashMap
* Maintains a dynamic window over an array or string.
* Tracks characters or numbers inside the current window to handle substrings or sub-arrays.

### Prefix Sum with HashMap
* Stores cumulative sums and their first occurrence indices.
* Solves problems tracking continuous sub-arrays matching a target sum.

---

## 5. Essential Practice Questions

### Question 1: Two Sum
* **Problem:** Find two numbers in an array that add up to a specific target.
* **Pattern:** Two-Pointer Complement Search.
* **Complexity:** Time: O(N), Space: O(N).

### Question 2: Subarray Sum Equals K
* **Problem:** Find the total number of continuous subarrays whose sum equals K.
* **Pattern:** Prefix Sum with HashMap.
* **Complexity:** Time: O(N), Space: O(N).

### Question 3: Longest Substring Without Repeating Characters
* **Problem:** Find the length of the longest substring without duplicate characters.
* **Pattern:** Sliding Window with HashMap.
* **Complexity:** Time: O(N), Space: O(min(M, N)) where M is alphabet size.

### Question 4: Group Anagrams
* **Problem:** Group a list of strings together if they are anagrams of each other.
* **Pattern:** Frequency Counting / Sorted Key Hashing.
* **Complexity:** Time: O(N * K log K) where K is max string length.
