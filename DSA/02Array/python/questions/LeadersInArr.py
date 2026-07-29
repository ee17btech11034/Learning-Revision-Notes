# return the list of leaders of arr. 
# leader: -> everything on the right is smaller.

def bruteForce(arr):
    # we will check the all right lement for ith. 
    # TC = O(n^2), SC = O(n) to store the val
    n = len(arr)
    ans = []
    for i in range(n):
        for j in range(i+1, n):
            if (arr[j] >= arr[i]): # not leader
                break
        else:
            ans.append(arr[i])

    return ans

def optimalSol(arr):
    # We are just checking the right side, so lets keep a pointer for it.
    # TC = O(n), SC = O(n) for ans 
    maxVal = float('-inf')

    i = len(arr) -1
    ans = []

    while(i >= 0 ):
        if (arr[i] > maxVal):
            ans.append(arr[i])
            maxVal = arr[i]
        i -= 1
    
    return ans
        
if __name__=="__main__":
    arr = [10, 22, 12, 3, 0, 6]

    print("leaders using brute: ", bruteForce(arr))
    print("leaders using optimal: ", optimalSol(arr))