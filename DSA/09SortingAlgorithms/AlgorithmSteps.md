# Sorting Algorithms Execution Steps

This document breaks down the operational, step-by-step internal mechanics of key sorting algorithms.

---

## 1. O(n²) Simple Iterative Sorts

### Bubble Sort
*   **Step 1:** Start at the beginning of the array (index 0).
*   **Step 2:** Compare the current element with the immediate next element (`arr[i]` vs `arr[i+1]`).
*   **Step 3:** If the current element is greater than the next element, swap them.
*   **Step 4:** Move the pointer one position right and repeat the comparison for all adjacent pairs.
*   **Step 5:** After completing a full pass, the largest unsorted element settles at the end of the array.
*   **Step 6:** Repeat the entire process for the remaining unsorted subarray until a pass finishes with zero swaps.

### Selection Sort
*   **Step 1:** Divide the array conceptually into a sorted prefix (initially empty) and an unsorted suffix.
*   **Step 2:** Initialize a pointer at the beginning of the unsorted region and assume this is the minimum value.
*   **Step 3:** Scan the remainder of the unsorted region to find the absolute smallest value.
*   **Step 4:** Swap that absolute smallest value with the element at the beginning of the unsorted region.
*   **Step 5:** Shift the sorted boundary pointer one position to the right.
*   **Step 6:** Repeat until the unsorted suffix is completely empty.

### Insertion Sort
*   **Step 1:** Assume the first element (index 0) is a pre-sorted subarray of size one.
*   **Step 2:** Pick the next unsorted element in line; this is your "key".
*   **Step 3:** Compare this key with the elements in the sorted subarray, moving backward from right to left.
*   **Step 4:** Shift each sorted element one position to the right if it is greater than the key.
*   **Step 5:** Insert the key into the empty slot when you find an element smaller than it (or hit the array start).
*   **Step 6:** Move to the next unsorted element and repeat until the entire array is processed.

---

## 2. O(n log n) Advanced Sorts

### Merge Sort
*   **Step 1:** Check if the array contains only one element; if so, consider it sorted and return it.
*   **Step 2:** Find the middle point of the current array index bounds: `mid = low + (high - low) / 2`.
*   **Step 3:** Recursively divide the left half of the array until single-element blocks are isolated.
*   **Step 4:** Recursively divide the right half of the array until single-element blocks are isolated.
*   **Step 5:** Merge the divided segments back together using two moving pointers to pick the smaller available element.
*   **Step 6:** Copy the remaining elements of either segment into the final combined array once one side runs out.

### Quick Sort
*   **Step 1:** Choose an element from the array to act as the "pivot" (e.g., first, last, middle, or random).
*   **Step 2:** Initialize two layout pointers to begin partitioning the array.
*   **Step 3:** Rearrange elements so that everything smaller than the pivot moves to its left side.
*   **Step 4:** Rearrange elements so that everything larger than the pivot moves to its right side.
*   **Step 5:** Place the pivot element securely into its final, absolute sorted position between the two zones.
*   **Step 6:** Recursively apply these steps to the left and right sub-arrays until the base case is met.

### Heap Sort
*   **Step 1:** Build a Max-Heap structure out of the raw input array elements.
*   **Step 2:** Locate the maximum value, which is now sitting at the root node of the heap (index 0).
*   **Step 3:** Swap this root element with the very last available element in the current array bounds.
*   **Step 4:** Decrease the active heap size consideration boundary by 1.
*   **Step 5:** Run a "heapify" operation down from the root node to fix broken heap balance rules.
*   **Step 6:** Repeat steps 2 through 5 until the heap size shrinks down to zero.

### Tim Sort
*   **Step 1:** Divide the raw array space into small segments called "Runs" (usually size 32 or 64).
*   **Step 2:** Sort each individual small Run segment using an optimized **Insertion Sort** routine.
*   **Step 3:** Push the boundaries of these sorted Run segments onto an tracking stack.
*   **Step 4:** Combine the sorted pieces together sequentially using a modified, stable **Merge Sort** procedure.
*   **Step 5:** Utilize "galloping mode" during merges to skip redundant item checks when one Run dominates the other.

---

## 3. Linear Non-Comparison Sorts

### Counting Sort
*   **Step 1:** Scan the array to find the maximum item value ($K$) to determine the overall data range bounds.
*   **Step 2:** Initialize a new temporary tracking count array of size $K + 1$ filled entirely with zeros.
*   **Step 3:** Map through the input array, incrementing the count index that matches the value of each element.
*   **Step 4:** Modify the count array by calculating a running prefix sum of counts across the indices.
*   **Step 5:** Iterate through the original array backward to maintain algorithm stability.
*   **Step 6:** Place elements into their target output positions based on the prefix sums, decrementing the sum value after each placement.

### Radix Sort
*   **Step 1:** Find the absolute maximum numerical value to calculate the total count of digits present.
*   **Step 2:** Initialize a loop that processes numbers digit by digit, starting at the Least Significant Digit (1s place).
*   **Step 3:** Execute a stable subroutine sort (traditionally **Counting Sort**) on the array focused strictly on the active digit.
*   **Step 4:** Shift the focus window leftward to the next significant digit position (10s place, then 100s place, etc.).
*   **Step 5:** Run the stable subroutine sort again on the updated digit values.
*   **Step 6:** Terminate the loop once the Most Significant Digit has been completely processed.

### Bucket Sort
*   **Step 1:** Create an array of empty memory locations called "buckets" based on the data range.
*   **Step 2:** Run a mathematical distribution function to determine which bucket each element belongs to.
*   **Step 3:** Append each element from the original input array into its designated target bucket.
*   **Step 4:** Sort each individual bucket separately (typically using **Insertion Sort**).
*   **Step 5:** Concatenate all the individual sorted buckets together into a single master array.
