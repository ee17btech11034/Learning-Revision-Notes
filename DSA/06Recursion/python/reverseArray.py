def reverseArrUsingIterative(arr): # using loops/ iterations
    n = len(arr)

    for i in range(n//2):
        # temp = arr[i]
        # arr[i] = arr[n-i-1]
        # arr[n-i-1] = temp

        arr[n-i-1], arr[i] = arr[i], arr[n-i-1]

def reverseArrUsing2pointer(arr): # using loops/ iterations
    s = 0
    e = len(arr) -1

    while(s < e):
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1

def reverseArrUsingRecursion(arr, ind):
    if (ind >= len(arr)):
        return []
    
    response = reverseArrUsingRecursion(arr, ind+1)
    response.append(arr[ind])
    return response

def reverseArrUsingRecursionInplace(arr, ind):
    n = len(arr)
    if (ind >= n//2):
        return 
    
    arr[ind], arr[n-ind-1] = arr[n-ind-1], arr[ind]
    reverseArrUsingRecursionInplace(arr, ind+1)

if __name__=="__main__":
    arr = [1, 2, 3, 4, 5]

    reverseArrUsingIterative(arr)
    print(arr)

    reverseArrUsing2pointer(arr)
    print(arr)

    reverseArrUsingRecursionInplace(arr, 0)
    print(arr)
    
    new_arr = reverseArrUsingRecursion(arr, 0)
    print(new_arr)