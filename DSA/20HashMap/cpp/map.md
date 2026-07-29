# Mastering C++ Hashing and Maps: Core DSA Reference Notes

## 1. Fundamentals & Core Definitions

In C++, associative containers come in two distinct architectural designs: **Hash Table-based** (Unordered) and **Balanced Binary Search Tree-based** (Ordered).

### 1. `std::unordered_map` / `std::unordered_set`
* **Under the Hood:** Implemented natively as a **Hash Table** with an array of buckets.
* **Ordering:** Elements are completely unordered. Their positions depend entirely on their generated hash values.
* **Key Requirement:** Keys must be hashable via `std::hash<Key>` and support equality checking via the `==` operator. key will always be single data type.

### 2. `std::map` / `std::set`
* **Under the Hood:** Implemented natively as a **Red-Black Tree** (a self-balancing binary search tree).
* **Ordering:** Elements are strictly ordered by key using strict weak ordering (the `<` operator).
* **Key Requirement:** Keys must support the `<` operator. They do not require a hash function.

---

## 2. Mathematically Precise Complexity Notations

Rather than using Big-O as a loose blanket term for all performance states, we track algorithmic runtime using precise asymptotic boundaries:
* **$\Omega(f(n))$ (Best Case / Lower Bound):** The absolute minimum operational steps required.
* **$\Theta(f(n))$ (Average Case / Tight Bound):** The true typical performance expected during standard runtime execution.
* **$O(f(n))$ (Worst Case / Upper Bound):** The maximum threshold constraint if things go completely wrong (e.g., severe hash collisions).

### Time Complexity Matrix

| Container Type | Operation | Best Case ($\Omega$) | Average Case ($\Theta$) | Worst Case ($O$) |
| :--- | :--- | :--- | :--- | :--- |
| **`std::unordered_map`**<br>**`std::unordered_set`** | **Insert**<br>**Delete**<br>**Search** | $\Omega(1)$<br>$\Omega(1)$<br>$\Omega(1)$ | $\Theta(1)$<br>$\Theta(1)$<br>$\Theta(1)$ | $O(N)$ (All keys hit one bucket)<br>$O(N)$ (Traversing full bucket)<br>$O(N)$ |
| **`std::map`**<br>**`std::set`** | **Insert**<br>**Delete**<br>**Search** | $\Omega(1)$<br>$\Omega(\log N)$<br>$\Omega(1)$ | $\Theta(\log N)$<br>$\Theta(\log N)$<br>$\Theta(\log N)$ | $O(\log N)$<br>$O(\log N)$<br>$O(\log N)$ |

### Auxiliary Space Complexity Matrix

| Container Type | Best Case ($\Omega$) | Average Case ($\Theta$) | Worst Case ($O$) | Details / Structural Overhead |
| :--- | :--- | :--- | :--- | :--- |
| **`std::unordered_map`** | $\Omega(1)$ | $\Theta(N)$ | $O(N)$ | Footprint scales dynamically to track bucket arrays and linked list nodes. |
| **`std::map`** | $\Omega(1)$ | $\Theta(N)$ | $O(N)$ | Fixed overhead per node for 3 pointers (`Left`, `Right`, `Parent`) and 1 `Color` bit flag. |

---

## 3. Collision Resolution Mechanics Reference

Unlike languages that utilize Open Addressing, standard C++ library implementations (like GNU `libstdc++` used by GCC/g++) resolve hash collisions using **Separate Chaining (Closed Addressing)**.

```text
       BUCKET ARRAY
      ┌───────────┐
      │ Bucket 0  │ ───► Empty (nullptr)
      ├───────────┤
      │ Bucket 1  │ ───► [ Hash A | Key A | Val A ] ───► [ Hash B | Key B | Val B ] (Collision Chain)
      ├───────────┤
      │ Bucket 2  │ ───► Empty (nullptr)
      └───────────┘
```

### The Chaining Flow under the Hood
When you insert a key-value pair:
1. **Hash Generation:** C++ invokes `std::hash<Key>{}(key)` to generate a `size_t` hash code integer.
2. **Bucket Mapping:** The hash code is compressed to match the current bucket count using modulo arithmetic: `bucket_index = hash_code % bucket_count`.
3. **Collision Handling:** If the bucket already contains data, the new node is appended to the linked list assigned to that specific bucket.

### Why Storing the Hash with Each Node Matters
Every individual node inside a bucket chain stores `[Hash, Key, Value, NextPointer]`. The raw hash integer is explicitly saved inside the node for two critical performance enhancements:
1. **Instant Collision Filtering:** During a lookup (`map[key]`), C++ steps through the linked list. It compares the target hash against the stored node hash using an integer check first. If hashes do not match, it skips evaluating the heavy `Key1 == Key2` structural comparison entirely.
2. **Re-Hashing During Expansion:** When the load factor exceeds its threshold (typically `1.0`), the bucket array doubles in size. C++ reallocates the grid and calculates new indexes instantly using `stored_hash % new_bucket_count` without having to slowly re-execute the original key hashing algorithm.

#### Alternative Formats For Reference: Open Addressing Techniques
* **Linear Probing:** $h(x, i) = (h'(x) + i) \pmod{\text{Size}}$. Suffers heavily from **Primary Clustering** where consecutive slots group together, ruining $\Theta(1)$ speeds.
* **Quadratic Probing:** $h(x, i) = (h'(x) + c_1 \cdot i + c_2 \cdot i^2) \pmod{\text{Size}}$. Eliminates primary clustering but creates **Secondary Clustering** if keys share initial hashes.
* **Double Hashing:** $h(x, i) = (h_1(x) + i \cdot h_2(x)) \pmod{\text{Size}}$. Uses a secondary hash function for the step interval size, clearing out both types of clustering.

---

## 4. Array Memory Constraints vs. Hashing Necessity

When implementing counting patterns, using a direct frequency array has strict memory limitations imposed by the system stack and heap. Exceeding these limits causes a **Segmentation Fault (Stack Overflow)**.

### Memory Allocation Limitations
* **Integer Frequency Arrays (`int arr[]`):**
  * *Declared locally inside a function (Stack Memory):* Maximum size $\approx 10^6$ elements.
  * *Declared globally / statically (Heap/Data segment):* Maximum size $\approx 10^7$ elements.
* **Boolean Frequency Arrays (`bool arr[]`):**
  * *Declared locally inside a function (Stack Memory):* Maximum size $\approx 10^7$ elements.
  * *Declared globally / statically (Heap/Data segment):* Maximum size $\approx 10^8$ elements.

### The $10^9$ Bound Problem Matrix
If your input values can be up to $10^9$, you **cannot** allocate a static array of size `arr[10^9]`. The system will instantly crash because it requires gigabytes of contiguous RAM.

#### The C++ Map Solution:
To track frequencies or existence for large bounds like $10^9$, you must use `std::unordered_map` or `std::unordered_set`. Instead of allocating $10^9$ slots in memory, a Map only allocates memory for the *unique elements actually present* in the input. If an array contains only 5 distinct numbers (even if those numbers are as large as $1,000,000,000$), the map will only store 5 entries, keeping the space at a safe $\Theta(N)$.

---

## 5. Essential C++ Operations & Customs

### 1. Basic CRUD Operations
```cpp
#include <iostream>
#include <unordered_map>
#include <string>

int main() {
    // CREATE
    std::unordered_map<std::string, int> userAge;
    userAge["Alice"] = 25;        // Insertion via operator[]
    userAge.insert({"Bob", 30});   // Insertion via pair initialization

    // READ
    // Safe lookup using find() to prevent accidental default insertions
    auto it = userAge.find("Alice");
    if (it != userAge.end()) {
        std::cout << "Age: " << it->second << std::endl;
    }

    // UPDATE
    userAge["Alice"] = 26; // Overwrites original value

    // DELETE
    userAge.erase("Bob"); // Removes key-value entry completely
    
    return 0;
}
```

### 2. Custom Key Hashing (Example: Storing Pairs `std::pair<int, int>`)
By default, C++ does not provide a hash function for `std::pair`. To use pairs as keys inside an `std::unordered_map`, you must create a custom hashing functor.

```cpp
#include <unordered_map>
#include <utility>
#include <string>

// Custom hash functor for std::pair<int, int>
struct PairHash {
    std::size_t operator()(const std::pair<int, int>& p) const {
        auto h1 = std::hash<int>{}(p.first);
        auto h2 = std::hash<int>{}(p.second);
        // Combines hashes using a bitwise shift and prime multiplier to minimize collisions
        return h1 ^ (h2 + 0x9e3779b9 + (h1 << 6) + (h1 >> 2));
    }
};

int main() {
    // Declaring unordered_map with the custom hash rules
    std::unordered_map<std::pair<int, int>, std::string, PairHash> coordinateMap;
    
    coordinateMap[{2, 3}] = "Point A";
    coordinateMap[{5, 8}] = "Point B";
    
    return 0;
}
```

---

## 6. Critical DSA Coding Patterns

### Pattern 1: Frequency Counting
Tracks occurrences of elements to analyze duplicates, majorities, or string permutations. Pre-allocate buckets upfront using `.reserve(N)` for massive inputs to bypass intermediate resizing migrations.

### Pattern 2: Two-Pointer Complement Search (Two-Sum Pattern)
Finds structural pairings by tracking previously evaluated elements in a set and matching against a targeted formula complement (`complement = target - current`).

### Pattern 3: Sliding Window with HashMap
Tracks variable boundary arrays or substring elements by dynamically adjusting window pointers (`left` and `right`) alongside real-time frequency map state changes.

### Pattern 4: Prefix Sum with HashMap
Finds continuous target subarrays by storing cumulative calculations (`current_sum`) and their historical occurrence snapshots.

---

## 7. Essential Practice Questions

### Question 1: Two Sum
* **Problem:** Return indices of two numbers that add up to a specific target.
* **Pattern:** Two-Pointer Complement Search.

```cpp
#include <vector>
#include <unordered_map>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> seen;
    for (int i = 0; i < nums.size(); ++i) {
        int complement = target - nums[i];
        if (seen.find(complement) != seen.end()) {
            return {seen[complement], i};
        }
        seen[nums[i]] = i;
    }
    return {};
}
```

---

### Question 2: Subarray Sum Equals K
* **Problem:**  Find the total number of continuous subarrays whose sum equals K.
* **Pattern:** Prefix Sum with HashMap.

```cpp
#include 
#include <unordered_map>int subarraySum(std::vector& nums, int k) {std::unordered_map<int, int> prefixMap;prefixMap[0] = 1;
int currentSum = 0;
int count = 0;
for (int num : nums) {
    currentSum += num;
    if (prefixMap.find(currentSum - k) != prefixMap.end()){
        count += prefixMap[currentSum - k];
    }
    prefixMap[currentSum]++;
}
return count;}
```

### Question 3: Longest Substring Without Repeating Characters
* **Problem:** Find the length of the longest substring without duplicate characters.
* **Pattern:** Sliding Window with HashMap.

```cpp
#include 
#include <unordered_map>#include int lengthOfLongestSubstring(std::string s) {std::unordered_map<char, int> charMap;
int left = 0, maxLen = 0;
for (int right = 0; right < s.length(); ++right) {
    if (charMap.find(s[right]) != charMap.end() && charMap[s[right]] >= left) {
        left = charMap[s[right]] + 1;
    }
    charMap[s[right]] = right;maxLen = std::max(maxLen, right - left + 1);
}
return maxLen;
}
```

### Question 4: Group Anagrams
* **Problem:** Group a list of strings together if they are anagrams of each other.
* **Pattern:** Frequency Counting / Sorted Key Hashing.

```cpp
#include 
#include #include <unordered_map>#include std::vector<std::vectorstd::string> groupAnagrams(std::vectorstd::string& strs) {std::unordered_map<std::string, std::vectorstd::string> anagramMap;
for (const std::string& s : strs) {
    std::string key = s;std::sort(key.begin(), key.end());anagramMap[key].push_back(s);
}
std::vector<std::vectorstd::string> result;
for (auto& pair : anagramMap) {
    result.push_back(pair.second);
    }
return result;
}
```

## 8. Critical Performance Pitfalls
* **Avoid operator[] For Conditional Existence Checks** Using if `(myMap[key] == 5)` when the key is completely missing will automatically insert the key into the map with a default value of 0 before evaluating. Always prioritize `.find()` or `.count()` for tracking clean lookups.

```cpp
// Bad Approach (Causes accidental insertions)
if (myMap[missing_key] == 5) { ... }

// Correct Approach
if (myMap.find(missing_key) != myMap.end()) { ... }

```