# Q: sort an arr of 0, 1, 2

def sortBrute(arr):
    # use sorting algo
    # TC = O(n log n)
    # SC = O(n) for new arr
    sorted_arr = arr.copy()
    sorted_arr.sort()
    return sorted_arr

def sortBetter(arr):
    # Use counting
    # TC = O(n + n) = O(n)
    # SC = O(n)
    zeroes = 0
    ones = 0
    n = len(arr)
    ans = arr.copy()

    for num in arr:
        if (num == 0):
            zeroes += 1
        elif (num == 1):
            ones += 1
    
    for i in range(n):
        if (i < zeroes):
            ans[i] = 0
        elif(i < (zeroes + ones)):
            ans[i] = 1
        else:
            ans[i] = 2

    return ans


def sortOptimal(arr): # tc = on), SC = O(1)
    # Deutch National Flag Algorithm
    # Use 3 pointers --> low, mid, high
    # [0, low-1] will contan 0
    # [low, mid-1] will contain 1
    # [mid, high] will contain 0/1/2 unsorted
    # [high+1, n-1] will contain 2.
    # we just need to handle unsortedpart

    # Steps:
    # [ 0 0 0 0    1 1 1 1 1    0 2 1 2 1 0    2 2 2 2]
    #              |            |         |
    #              |            |         |
    #             low           mid       high

    # if arr[mid]  = 0
        # swap(low, mid)
        # low += 1
        # mid += 1
    # if (arr[mid]  = 1)
        # mid += 1
    # if arr[mid]  = 2
        # swap(mid, high)
        # high -= 1
    
    low = 0
    mid = 0
    high =len(arr) -1

    while(mid <= high):
        if (arr[mid] == 0):
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif (arr[mid] == 1):
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1


if __name__=="__main__":
    arr = [0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]

    print("Sorted using brute: ", sortBrute(arr))

    print("Sorted using better: ", sortBetter(arr))
    # print("Sorted using optimal: ", sortOptimal(arr))
    print(arr)
