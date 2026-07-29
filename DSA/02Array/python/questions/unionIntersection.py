# Q: Union and Intersection of 2 sorted arrays.
    # Union is uniques elements present in either of array.
    # arr1 = [1, 2, 3, 3], arr2 = [1, 1, 3, 3, 4]
    # union = [1, 2, 3, 4]
#
    # intersection is pair of  common elements present in both array.
    # arr1 = [1, 2, 3, 3], arr2 = [1, 1, 3, 3, 4]
    # intersection = [1, 3, 3] # as 2 pairs of 3 can be pulled from both

def unionBruteForce(arr1, arr2): # TC = O(m log m  + n log n)
    # create set and dump in it
    union_elements = set() # do not use unordered set as it will provide the elements randomly

    for num in arr1:
        union_elements.add(num)
    for num in arr2:
        union_elements.add(num)

    return list(union_elements)

def unionOptimal(arr1, arr2):
    # using 2 pointer
    arr1_pointer = 0
    arr2_pointer = 0
    ans = []

    while((arr1_pointer < len(arr1)) and (arr2_pointer < len(arr2))):
        if (arr1[arr1_pointer] <= arr2[arr2_pointer]):
            if ((not ans) or  (ans[-1] != arr1[arr1_pointer])):
                ans.append(arr1[arr1_pointer])
            arr1_pointer += 1
        else:
            if ((not ans) or (ans[-1] != arr2[arr2_pointer])):
                ans.append(arr2[arr2_pointer])
            arr2_pointer += 1

    while(arr1_pointer < len(arr1)):
        if ((not ans) or  (ans[-1] != arr1[arr1_pointer])):
            ans.append(arr1[arr1_pointer])
        arr1_pointer += 1
    
    while(arr2_pointer < len(arr2)):
        if ((not ans) or (ans[-1] != arr2[arr2_pointer])):
            ans.append(arr2[arr2_pointer])
        arr2_pointer += 1
    
    return ans



############ Intersection
def intersectionBrute(arr1, arr2): # TC = O(m * n), SC = O(min(m, n))
    # traverse throught arr 1. 
    # create visited arr for arr2
    # loop arr2 inside arr1. 
    visited_arr = [False]*(len(arr2))
    ans = []

    for num1 in arr1:
        for j in range(len(arr2)):
            if ((num1 == arr2[j]) and (not visited_arr[j])):
                ans.append(num1)
                visited_arr[j] = True
                break
            if (num1 < arr2[j]):
                break
    return ans

def intersectionOptimal(arr1, arr2): # TC = O(min(m, n)), SC = O(K) = O(min(m, n)) to store ans.
    # using 2 pointers
    i = 0
    j = 0
    ans = []

    while((i < len(arr1)) and (j < len(arr2))):
        if (arr1[i] == arr2[j]):
            # found a pair
            ans.append(arr1[i])
            i += 1
            j += 1
        elif (arr1[i] < arr2[j]):
            i += 1
        else:
            j += 1
    
    return ans


if __name__=="__main__":
    arr1 = [1, 1, 2, 3, 4, 4, 4, 5]
    arr2 = [2, 3, 4, 4, 5, 6]

    unionUsingBrute_ans = unionBruteForce(arr1, arr2)
    print("Union Using Brute: ", unionUsingBrute_ans)

    unionOptimal_ans = unionOptimal(arr1, arr2)
    print("Union Using Optimal: ", unionOptimal_ans)

    intersectionBrute_ans = intersectionBrute(arr1, arr2)
    print("Intersection using Brute: ", intersectionBrute_ans)

    intersectionOptimal_ans = intersectionOptimal(arr1, arr2)
    print("Intersection using Optimal: ", intersectionOptimal_ans)