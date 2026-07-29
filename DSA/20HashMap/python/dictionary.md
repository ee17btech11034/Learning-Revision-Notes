# Mastering Python Dictionaries (`dict`)

## 1. Fundamentals & Core Mechanics

### What is a Dictionary?
A built-in Python data structure that stores data in **key-value pairs**. 

### Key Characteristics
* **Unordered/Ordered:** As of Python 3.7+, dictionaries maintain the **insertion order** of keys.
* **Key Uniqueness:** Keys must be completely unique. Duplicate keys will overwrite existing values.
* **Hashability:** Keys must be **immutable** data types (e.g., `str`, `int`, `float`, `tuple`). Mutable structures like `list` or `set` cannot be used as keys.

### Under the Hood
Python dictionaries are implemented using a highly optimized **Hash Table**. 
* When a key is inserted, Python applies the built-in `hash()` function to compute its index.
* Since Python 3.6, it uses a split-array layout (an uncompact indices array and a dense entries array) which reduced memory usage by up to 25%.

---

## 2. Internal Collision Resolution (How Python Handles Collisions)

No matter how good a hash function is, two different keys can produce the same hash value or map to the same array index. This is a **Hash Collision**.

### Open Addressing (Closed Hashing)
Unlike languages like Java that use *Chaining* (linked lists inside buckets), Python resolves collisions using **Open Addressing**. All elements are stored directly within the main table array itself. If a slot is occupied, Python looks for an alternative empty slot.

### Pseudo-Random Probing
To find the next available slot, Python does not use simple Linear Probing (`index + 1`), because linear probing causes consecutive slots to fill up fast (known as primary clustering). Instead, Python uses a unique formula called **Pseudo-Random Probing**.

The core recurrence relation used by CPython to find the next index is:
```text
next_index = ((5 * current_index) + 1 + (hash_value >> perturb)) % table_size
```

#### Why this formula works:
1. **The `5 * current_index + 1` Multiplier:** Ensures that every single index in the array will eventually be checked before any index is repeated. This completely covers the table size.
2. **The `perturb` Shift Variable:** Initially set to the full `hash_value`. With every collision step, it is bit-shifted right (`perturb >>= 5`). This shifts in the higher-order bits of the original hash value that were initially ignored. 
3. **Clustering Prevention:** Incorporating the original hash bits ensures that two keys colliding at step one will take completely different resolution paths on step two, breaking up clusters instantly.

### Handling Deletions (The `DKIX_EMPTY` / Dummy Flag)
When a key-value pair is deleted from an open-addressed table, Python cannot just leave the slot blank. Doing so would break the lookup chain for other keys that collided past that slot during insertion.
* **The Fix:** Python replaces the deleted key with a special marker token (internally named a dummy entry).
* **During Search:** If Python encounters a dummy marker, it knows to keep probing forward.
* **During Insertion:** Python can reuse and overwrite a dummy marker slot with new data.

---

## 3. Time & Auxiliary Space Complexity

### Time Complexity
* **Search / Lookup:** O(1) average | O(N) worst-case
* **Insert / Update:** O(1) average | O(N) worst-case
* **Delete (`pop`/`del`):** O(1) average | O(N) worst-case

*Note: The O(N) worst-case scenario occurs only during severe hash collisions or when the internal hash table needs to resize.*

### Auxiliary Space Complexity
* **Space:** O(N) where N is the number of unique elements stored.

---

## 4. Essential CRUD Operations

### Create
```python
# Initialization methods
empty_dict = {}
user = {"name": "Alice", "age": 25}
built_in_dict = dict(name="Bob", age=30)
```

### Read
```python
# Direct lookup (Throws KeyError if key does not exist)
name = user["name"]

# Safe lookup (Returns None or custom default if key is missing)
age = user.get("age")
salary = user.get("salary", 0)  # Returns 0 if 'salary' isn't found
```

### Update
```python
# Adding or modifying elements
user["age"] = 26  # Updates existing key
user["city"] = "Delhi"  # Adds new key-value pair

# Batch update
user.update({"status": "Active", "age": 27})
```

### Delete
```python
# Removes key and returns its value (Safe with default parameter)
age = user.pop("age", None)

# Removes last inserted key-value pair as a tuple
last_item = user.popitem()

# Delete keyword (Throws KeyError if key does not exist)
del user["name"]

# Wipe the entire dictionary
user.clear()
```

---

## 5. Advanced & Specialized Dictionary Types

Python's `collections` module provides enhanced dictionary variants built specifically for competitive programming and data science patterns.

### 1. `defaultdict`
Eliminates manual checks for missing keys by automatically initializing them with a default type template.

```python
from collections import defaultdict

# Avoids manual frequency counting checks
freq = defaultdict(int)
for num in:
    freq[num] += 1  # No KeyError! Missing keys default to 0 automatically.

# Grouping elements into lists
graph = defaultdict(list)
graph["A"].append("B")  # Missing keys default to an empty list []
```

### 2. `Counter`
A specialized dictionary subclass specifically engineered for rapid element frequency tracking.

```python
from collections import Counter

items = ["apple", "banana", "apple", "cherry"]
counts = Counter(items)

print(counts)  # Output: Counter({'apple': 2, 'banana': 1, 'cherry': 1})
print(counts.most_common(1))  # Output: [('apple', 2)]
```

---

## 6. Critical DSA Idioms & Performance Tips

### 1. Dictionary Comprehensions
Generate dictionaries elegantly using quick inline iterations.
```python
# Create squares map for even numbers
squares = {x: x**2 for x in range(10) if x % 2 == 0}
```

### 2. Iterating Effectively
```python
my_dict = {"a": 1, "b": 2}

# Loop through keys only (Default behavior)
for key in my_dict:
    pass

# Loop through values only
for val in my_dict.values():
    pass

# Loop through both simultaneously
for key, val in my_dict.items():
    pass
```

### 3. Membership Checking Performance
Always use `if key in my_dict` instead of searching manually. It checks the hash table instantly in **O(1) constant time**. Do **not** use `if key in my_dict.keys()`, as it creates an extra view object and reduces search performance in older versions.
```python
# Correct and fastest way
if "name" in user:
    print("Found!")
```