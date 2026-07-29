
def largestElementUsingBruteForce(arr):
    # sort the arr
    arr.sort()

    return arr[-1] # TC = O( n + (n log n)) = O(n log n)

def largestElementUsingOptimized(arr):
    max_val_ind = 0

    for i in range(len(arr)):
        if (arr[i] > arr[max_val_ind]):
            max_val_ind = i
    return arr[max_val_ind]

def secLargestUsingBrute(arr): # TC => O( n + (n log n))
    arr.sort()
    # elements can repeat so not sure about -2
    j = len(arr) -1

    while((j >= 0) and (arr[j] == arr[-1])):
        j -= 1
    
    if (j < 0):
        return -1
    return arr[j]

def secLargestUsingOptimized(arr):
    # // we can not achieve using index as what is first element is largest
    # largest_ind = 0 # 
    # sec_largest_ind = 1

    # for i in range(len(arr)):
    #     if (arr[i] > arr[largest_ind]):
    #         sec_largest_ind = largest_ind
    #         largest_ind = i
    #     if (arr[i] > arr[sec_largest_ind]):
    #         sec_largest_ind = i
    
    # return arr[sec_largest_ind]

    largest = float('-inf')
    seclargest = float('-inf')

    for num in arr:
        if (num > largest):
            seclargest = largest
            largest = num
        elif ((num > seclargest) and (num != largest)):
            seclargest = num
    return seclargest

if __name__=="__main__":
    arr = [3, 2, 1, 5, 2]
    largestVal = largestElementUsingOptimized(arr)
    print(largestVal)


    arr2= [3, 2, 1, 5, 2, 7, 7] # better approach is in first pass find the largest element and in second time find the sec largest.
    # seclargestVal = secLargestUsingBrute(arr2)
    seclargestVal = secLargestUsingOptimized(arr2)
    print(seclargestVal)
