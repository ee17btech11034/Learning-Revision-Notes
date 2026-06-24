'''
Binary Search:
    - works in sorted arr.
    - find the mid and compare key with mid
    - take the left sub arr or right sub arr based on that.
    - repeat above 

    - TC => Ω(1) -> Θ(log n) -> O(log n)
    - SC => Ω(1) -> Θ(1) -> O(1) for Iteration
    - SC => O(log n) for Recursion as call stack

1. Python Does Not Have Blocks-Level Scope:
    - In languages like C, C++, or Java, variables declared inside a block ({ ... }) are allocated on the stack and destroyed when the block exits.
    - Python does not have block scope. Variables defined inside a while loop or if statement belong to the entire function scope. 
        Whether you write mid = ... before the loop or inside the loop, the variable name mid is registered in the function's local symbol table exactly once when the function compiles. 
        No names are deleted or re-registered on each iteration.
    
2. Immutability and Reassignment Cost
    - In Python, integers are immutable objects.
    - You cannot change the value at a specific memory address for an integer.
    - Every time you calculate a new value with start + (end - start) // 2, Python creates a brand-new integer object somewhere in memory.
    - The variable mid is simply a label (pointer) that switches to reference this new memory address.
'''

def binarySearchUsingRecursion(arr, start, end, key):
    if (start > end):
        return -1
    mid = start + ((end - start)//2)
    if(arr[mid] == key):
        return mid
    elif (arr[mid] < key):
        return binarySearchUsingRecursion(arr, mid+1, end, key)
    else:
        return binarySearchUsingRecursion(arr, start, mid-1, key)
    
def binarySearchUsingIteration(arr, key):
    start = 0
    end = len(arr) -1
    if (end < start):
        return -1

    while(start <= end):
        mid = start + (end - start)//2
        if (arr[mid] == key):
            return mid
        elif (arr[mid] < key):
            start = mid+1
        else:
            end = mid-1
    return -1

if __name__=="__main__":
    arr = [3, 6, 7, 8, 10, 50, 52, 55]

    keys = [3, 5, 6, 8, 55]
    n = len(arr)

    print("Arr is: ", end=" ")
    print(arr)
    for val in keys:
        key_indusingRec = binarySearchUsingRecursion(arr, 0, n-1, val)
        key_indusingIt = binarySearchUsingIteration(arr, val)

        if (key_indusingIt > -1):
            print(f"Iteration ==> {val} is present in arr at ind: {key_indusingIt}")
        else:
            print(f"Iteration ==> {val} is not present in arr.")

        if (key_indusingRec > -1):
            print(f"Recursion ==> {val} is present in arr at ind: {key_indusingRec}")
        else:
            print(f"Recursion ==> {val} is not present in arr.")