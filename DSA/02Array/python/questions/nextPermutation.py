# Q: arr is given find next permutation. if it is last max then return smallest lexical.


# Brute force => Generate all of them in sorted manner.

#  Stirling's approximation, log(n!) =~= n log n.
def bruteForce(arr):
    # TC = -> permutation O(n * fact(n)), sort O(n* K lon K), binarysearch  O(n*Log (k)), K = factorial(n)
    # TC = O(  (n * n!) + (n* n! * log n!) + (n log n!) 
    # TC = O(  (n * n!) + (n! * n^2 log n) + (n^2 * log n) = O( n! * n^2 log n )
    # SC = copy input arr O(n) + recursion call stack (O(n)) +  to store ans O(n* n!) as each arr len is n.
    # SC = O(n* n!)
    arr2 = arr.copy()
    n = len(arr2)

    ans = []

    # either we can run loop for factorial(n) or use recursion. 

    # let's use recursion here
    def recursionToGenerateAll(start): #TC = O(n * fact(n)) -> n is because of copy.

        # base
        if (start == n):
            ans.append(arr2[:]) # it takes O(n) time to copy
        for i in range(start, n):
            # swap
            arr2[i], arr2[start] = arr2[start], arr2[i]

            # backtrack
            recursionToGenerateAll(start+1)

            # revert 
            arr2[i], arr2[start] = arr2[start], arr2[i]
    
    # create all and sort them and search using Binary as first word will be in sorting, then second, etc.
    # TC for sorting is    Klog(k) but if first element is sorted then sort according to last element. multiply by n.


def betterSol(arr):
    # Sort the initial array once: (O(n log n)) time
    # Find the next sequential sorted permutation by working from the right to find the first decreasing element, swapping it, and reversing the suffix. This single step takes \(O(n)\) time.
    # Repeat step 2 until the array is fully reversed.

    # we are printing ans not storing then

    # TC = O(n log n ) + O(n * n!) = O(n * n!)
    # SC = O(1) if we are not including array copy, else O(n)

    current = arr.copy()

    current.sort()
    ans = []

    n = len(arr)
    while True:
        # Step : Find the first element from the right that is smaller than its neighbor
        pivot_index = -1
        for i in range(n - 2, -1, -1): #TC = O(n)
            if current[i] < current[i + 1]:
                pivot_index = i
                break
                
        # If no such element is found, the array is fully reversed (e.g., [3, 2, 1])
        # This means we have successfully generated all permutations!
        if pivot_index == -1:
            break
            
        # Step 4: Find the smallest element to the right of pivot that is larger than current[pivot_index]
        for i in range(n - 1, pivot_index, -1):
            if current[i] > current[pivot_index]:
                # Swap them
                current[pivot_index], current[i] = current[i], current[pivot_index]
                break
                
        # Step 5: Reverse the entire suffix sequence to the right of the pivot_index
        current[pivot_index + 1:] = reversed(current[pivot_index + 1:]) # takes O(n) TC
        
        # Append the next valid sorted permutation
        ans.append(current[:])
        
    return ans


def optimalSol(arr):
    # find only next increasing permutation if not provided sorted one.
    # we will use better sol approach. 

    # lets change in arr only

    # Steps:
        # find the decresing element from right
        # swap it with just bigger number in right portion and sort the remaining elements. 

    # TC = O(n + n + n) = O(n)
    # SC = O(1)
    
    # find the decresing element from right
    pivot = -1
    n = len(arr)
    for i in range(n-2, -1, -1):
        if (arr[i] < arr[i+1]):
            pivot = i
            break
    
    if (pivot == -1): # if arr is sorted dec, [4, ,3 ,2 ,1]
        arr.sort() # it takes O(n) time for dec sorted arr else O(n log n) as python uses Timsort/Powersort
        return 
    
    # now if I look at the arr then right side of pivot must be sorted. 

    # to swap with just bigger num, we just need to traverse from right and swap with first big.
    for j in range(n-1, pivot, -1):
        if (arr[j] > arr[pivot]):
            arr[j], arr[pivot] = arr[pivot], arr[j]
            break
    
    # here, we placed the number and in right of pivot it is still sorted. 

    # We want the right part sorted in increasing order, just reverse it. 
    arr[pivot+1:] = reversed(arr[pivot+1:])
    # current[pivot_index + 1:].sort() # slicing creates a brand new copy of arr.

    # print(arr)
    return


def generate_all_sorted_permutations(arr): # TC = O(n * n!), SC = O(1) or O(n)
    # Step A: Sort the array first to start from the absolute lowest lexicographical order
    current = list(arr)
    current.sort()
    
    ans = []
    # Store the first sorted permutation
    ans.append(current[:]) 
    
    def optimalSol(arr):
        """Your exact optimized Next Permutation logic."""
        pivot = -1
        n = len(arr)
        
        # 1. Find the first decreasing element from the right
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break
                
        # If pivot is -1, the array is fully reversed (e.g., [3, 2, 1]).
        # We return False to signal to our loop that we are completely done!
        if pivot == -1:
            return False
            
        # 2. Find the successor and swap
        for j in range(n - 1, pivot, -1):
            if arr[j] > arr[pivot]:
                arr[j], arr[pivot] = arr[pivot], arr[j]
                break
                
        # 3. Reverse the right suffix sequence
        arr[pivot + 1:] = reversed(arr[pivot + 1:])
        return True

    # Step B: Keep calling optimalSol to advance to the next permutation in-place
    # The loop breaks automatically when optimalSol returns False
    while optimalSol(current):
        ans.append(current[:])
        
    return ans
if __name__=="__main__":
    # arr = [3, 1, 2]
    arr = [3, 2, 1]

    optimalSol(arr)
    print(arr)
