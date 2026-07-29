# Longest Consecutive sequence
# Q: arr is given, we can reorder them and need to find longest consecutive seq. 

def bruteSol1(arr):
    # for each element will check the next element is present or not
    # TC = O(n^3 + n^2)
    # SC = O(n)
    n = len(arr)
    ans = []
    for i in range(n):
        checkNum = arr[i] +1
        while(True): # TC = O(k) -> k is consecutive seq. 
            for j in range(n): # TC = O(n)
                if (arr[j] == checkNum):
                    checkNum += 1
                    break
            else:
                break
        if ((checkNum - arr[i]) > len(ans)): # O(n)
            ans = [num for num in range(arr[i], checkNum)]
    return ans

def bruteSol2(arr):
    # for each element will check the next element is present or not
    # TC = O(n^3) for worst, O(n^2) for avg/best as seq length is 1.
    # SC = O(n)
    n = len(arr)
    ans = []
    for i in range(n):
        checkNum = arr[i] +1
        while(checkNum in arr): # TC = O(k*n) -> k is consecutive seq. 
                checkNum += 1
        if ((checkNum - arr[i]) > len(ans)): # O(n)
            ans = [num for num in range(arr[i], checkNum)]
    return ans

# def betterSol(arr_original): ==> Wil not work as input = [1,1,2, 2, 3, 3, 3, 4]
#     # sort the arr. 
#     # we can run 2 for loop but better to use counting in single pass
#     arr = arr_original[:]
#     arr.sort()

#     last_ind = 0
#     ans_range = [0, 0]

#     n = len(arr)
#     for i in range(1, n):
#         if (arr[i] != (arr[i-1] +1)):
#             if ((i - last_ind) > (ans_range[1] - ans_range[0])):
#                 ans_range[0] = last_ind
#                 ans_range[1] = i
#             last_ind = i
#     if ((n - last_ind) > (ans_range[1] - ans_range[0])):
#         ans_range[0] = last_ind
#         ans_range[1] = n
#     return arr[ans_range[0] : ans_range[1]]

def betterSol(o_arr):
    # Sort the arr
    # TC = O(n + nlogn + n)
    # SC = O(n)
    arr = o_arr[:] # TC = O(n) to copy
    arr.sort() # TC = O(nlogn) to sort
    ans = []
    ans_len = 1
    last_num = float('-inf')
    longest_len = 1

    for i in range(len(arr)): # TC = O(n) as we are not adding data in ans arr.Even if we do we will be just adding a number and define new arr when no consecutive so that be O(1)
        if (arr[i] == last_num):
            continue
        elif(arr[i] == (last_num +1)):
            longest_len += 1
            last_num = arr[i] # can append if we want arr
        else:
            ans_len = max(ans_len, longest_len)
            longest_len = 1
            last_num = arr[i]
    return ans_len


def optimalSOl(arr):
    # it is optimal in some constraints
    # we will put data into set (unordered set/map for better TC O(1) -> O(log n))
    # we will pick the element and check if element-1 present in set or not.
        # if present that means we can not start the seq here. 
        # if not that means it is starting point of a seq. then run a while loop till consecutive is present.
    numSet = set() # or set(arr), SC = O(n)
    for num in arr: # TC = O(n)
        numSet.add(num)
    
    max_len = 1
    for num in numSet: # O(n)
        if (num -1) in numSet: # TC = O(1)
            continue
        else:
            # means it is start of seq
            checkNum = num+1
            curr_len = 1
            while checkNum in numSet: # TC = O(1 *k) -> k is consequtive lengths, 1 is for lookup
                curr_len += 1
                checkNum += 1
            max_len = max(max_len, (checkNum - num))
    return max_len
    # TC = O(n) not O(n^2)
    # like if all are unique nums then while will never run and it will be O(n) total. 
    # if all in seq, then it will start while loop only from strt num not for each, for this
        # it will be 1+1 + 1 ... (n-1) times + n(total in while loop) => O(2n)
if __name__=="__main__":
    arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
    arr = [100, 102, 100, 101, 101, 4, 3, 2, 3, 2, 1, 1, 1, 2, 5, 6]

    print("brute sol1: ", bruteSol1(arr))
    print("brute sol2: ", bruteSol2(arr))

    print("better sol: ", betterSol(arr))
    print("optimal sol: ", optimalSOl(arr))