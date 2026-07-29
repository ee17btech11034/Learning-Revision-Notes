# Q: Sorted non desc arr is given. Modify the inplace array with all distinct elements in start and return no of distinct elements.


def bruteForce(arr): # TC = O(n log n) & SC = O(n) for worst case
    # using set
    unique_elements_set = set()

    for num in arr:
        unique_elements_set.add(num) # TC = O(1) for avg but O(n) or O(log n)-> based on creation method for worst case collision as uses hash table
    
    for i, num in enumerate(unique_elements_set):
        arr[i] = num
    
    return len(unique_elements_set)

def optimizedUsing2pointer(arr): # TC = O(n), SC = O(1)
    unique_ind = 1 # first element is unique
    loop_ind = 1

    while(loop_ind < len(arr)):
        if (arr[loop_ind] != arr[loop_ind -1]):
            arr[unique_ind] = arr[loop_ind]
            unique_ind += 1
        loop_ind += 1
    
    return unique_ind


if __name__=="__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    noOfUniqueElements = bruteForce(arr)
    for i in range(noOfUniqueElements):
        print(arr[i], end=" ")
    print()

    arr2 = [1, 1, 2, 2, 2, 3, 3]
    noOfUniqueElements2 = optimizedUsing2pointer(arr2)
    for i in range(noOfUniqueElements2):
        print(arr[i], end=" ")
    print()