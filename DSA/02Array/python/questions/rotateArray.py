# Q: Left rotate an array by D places
# Part 1: => If D = 1, then we can store the 0th ind elements in temp and left shift all elements and put the temp element in last place.

# Steps:
    # n = len(arr)
    # d = d%n as rotating by n is arr itself.
    # Solution 1: 
        # store D first elements in a temp arr and 
        # left shift the remaining elements
        # put the temp arr elements in main arr.
        # TC = O(n), SC = O(D)
    # Solution 2: Optimal
        # [1, 2, 3, 4, 5, 6, 7]; d = 3
        # reverse left arr => [3, 2, 1, 4, 5, 6, 7] # reverse first d elements
        # reverse right arr => [3, 2, 1, 7, 6, 5, 4]
        # reverse whole arr => [4, 5, 6, 7, 1, 2, 3]
        # TC = O(d + n-d + n) = O(n), SC = O(1)

def bruteForce(arr, d):
    temp = arr[:d].copy()
    n = len(arr)
    for i in range(n-d):
        arr[i] = arr[i+d]
    
    for i in range(d):
        arr[n-d+i] = temp[i]

def optimalSol(arr, d):
    # reverse first d, reverese remaning elements
    # reverse whole arr. 

    def reverseArr(arr, s, e): # TC = O((e-s)//2)
        while(s < e):
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
    
    
    reverseArr(arr, 0, d-1) # reverse left part => first d elements
    reverseArr(arr, d, n-1) # reverse right part => remaining elements
    reverseArr(arr, 0, n-1) # reverse whole array.


if __name__=="__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 8
    n = len(arr)
    d = d % n

    bruteForce(arr, d)
    print(arr)


    arr2 = [1, 2, 3, 4, 5, 6, 7]

    optimalSol(arr2, d)
    print(arr2)
