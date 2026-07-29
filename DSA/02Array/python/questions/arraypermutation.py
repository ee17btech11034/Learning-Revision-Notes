# Q: arr is given, list all the permutations in increasing order. ot find the next permutation of given arr. 

def bruteSol(arr):
    # Use recursion to generate all possible permutations
    # Do a linear search and find arr index in ans
    # next ind element is next permutation

    # TC = O(n * fact(n))   # if n = 15 fact(n) = 10^12
    # SC = O( fact(n))
    result = []
    n = len(arr)

    def backtracking(start_ind):
        if (start_ind > n):
            return 
        if (start_ind == n):
            # we got a new array
            result.append(arr[:])
            return 
        
        for i in range(start_ind, n):
            # swap start_ind element with all other elememnts
            arr[start_ind], arr[i] = arr[i], arr[start_ind]

            # move to next ind
            backtracking(start_ind + 1)

            # backtract undo
            arr[start_ind], arr[i] = arr[i], arr[start_ind]
    
    backtracking(0)
    return result

# def better() # using stl in cpp as it has next_permutation methods, it is also implemented using optimal only

def optimalSol(arr):
    # Let's take a pointer from right and rearrange the right numbers to get the exact next

    n = len(arr)
    pointer = n -1
    max_num = 0


    while(pointer >= 0):
        if (arr[pointer] >= max_num):
            max_num = arr[pointer]
            pointer -= 1
            continue
        
        # pointer num is small that means we can get an permutation
        pointer_num = arr[pointer]
        arr[pointer:] = sorted(arr[pointer:])

        # find the just bigger num
        ind = pointer
        while((ind < n) and (arr[ind] <= pointer_num)):
            ind += 1

        # put it in place of pointer
        temp_num = arr.pop(ind)
        arr.insert(pointer, temp_num)
        print(arr)

        pointer -= 1
        break


if __name__=="__main__":
    arr = [2, 1, 5, 4, 3, 0, 0]

    optimalSol(arr)