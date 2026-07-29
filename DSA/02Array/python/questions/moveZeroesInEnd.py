def bruteForce(arr): # TC = O(n + n) = O(n), SC = O(k)= O(n) if all elements are non zero.
    # Store non-zero numbers in a new arr.
    non_zeroes = []

    for num in arr:
        if (num != 0):
            non_zeroes.append(num)
    
    for i in range(len(arr)):
        if (i < len(non_zeroes)):
            arr[i] = non_zeroes[i]
        else:
            arr[i] = 0

def betterSol(arr):
    # count zeroes
    count_zeroes = 0
    insert_ind = 0

    for i in range(len(arr)):
        if (arr[i] == 0):
            count_zeroes += 1
            continue
        elif (i != insert_ind):
            arr[insert_ind] = arr[i]
        insert_ind += 1
    # Now put last k elements to zero. ====> COmplete it.


def optimalSol(arr):
    # 2 pointer approach
    zero_found = -1
    n = len(arr)

    for i in range(n):
        if ((arr[i] == 0) and (zero_found == -1)):
            zero_found = i
        elif (arr[i] != 0):
            # 
            if (zero_found >= 0):
                # swap
                arr[i], arr[zero_found] = arr[zero_found], arr[i]
                zero_found += 1 # because next element will always be zero you can draw.

if __name__=="__main__":
    arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
    # order of elements must maintain

    # bruteForce(arr)
    print(arr)

    optimalSol(arr)
    print(arr)