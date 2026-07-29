# maximum subarray sum
# subarr -> contigous part

def bruteSol(arr):
    # TC = O(n^3)
    # SC = O(1)
    max_sum = 0

    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            temp_sum = 0
            for k in range(i, j+1):
                temp_sum += arr[k]
            max_sum = max(max_sum, temp_sum)
    return max_sum

def betterSol(arr):
    # TC = O(n^2)
    # SC = O(1)
    max_sum = 0

    n = len(arr)
    for i in range(n):
        temp_sum = 0
        for j in range(i, n):
            temp_sum += arr[j]
            if (temp_sum < 0):
                break
            max_sum = max(max_sum, temp_sum)
    return max_sum

def optimalSol(arr):
    # Kadane algorithm.
    max_sum = float('-inf')
    curr_sum = 0

    for num in arr:
        curr_sum += num
        if (curr_sum < 0):
            curr_sum = 0
            continue
        max_sum = max_sum if (max_sum > curr_sum) else curr_sum
    return max_sum

if __name__=="__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    # arr = [-4, -2, -3] # return 0 if no pos ans. # need to modify the above code with return max(0, max_val)

    print("max sum brute: ", bruteSol(arr))

    print("max sum better: ", betterSol(arr))

    print("max sum optimal: ", optimalSol(arr))