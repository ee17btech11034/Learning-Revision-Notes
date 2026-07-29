# Q: FInd the element that is present more than n//2 times. 
from collections import defaultdict

def bruteSol(arr):
    # Traverse  whole array using 2 llops to check the freq.
    # TC = O(n^2)
    # SC = O(1)
    n = len(arr)

    for i in range(n):
        freq = 0
        for j in range(n):
            if (arr[i] == arr[j]):
                freq += 1
        if (freq > (n//2)):
            return [arr[i], freq]
    
    return [-1, -1]

def betterSol(arr):
    # use hashing to store freq. 
    # TC = O(n log n)
    # SC = O(n//2)
    n = len(arr)
    freq_dict = defaultdict(int) 

    for num in arr:
        freq_dict[num] += 1
        if (freq_dict[num] > (n//2)):
            return [num, freq_dict[num]] # if we break here thn we won't be able to find the exact count as it will stop at (n//2 + 1)
    return [-1, -1]


def optimalSol(arr):
    # Moore's voting algorithm
    # Steps:
        # 2 vars, element= -1, count = 0
        # go through the loop
            # if num == element : count += 1 else count -=1
            # if (count == 0): # means till this point element is not major element not anyone else as well as element will be occuring exactly {j//2} not higher. 
                # element = next num, count = 1
        # Once we get the element we need to check that it must appear > n/2 times.
    
    # TC = O(n + n) = O(n)
    # SC = O(1)
    element = -1
    count = 0
    n = len(arr)
    for num in arr:
        if (count == 0):
            element = num
            count = 1
        elif (num == element):
            count += 1
        else:
            count -= 1
    
    if (count > 0):
        ele_cnt = 0
        for num in arr: # this step is not neded when say thata element exist.
            if (num == element):
                ele_cnt += 1
        if (ele_cnt > (n//2)):
            return [element, ele_cnt]
    return [-1, -1]


if __name__=="__main__":
    arr = [2, 2, 3, 3, 1, 2, 2]
    arr = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5]
    arr = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 1, 1, 1, 1]

    brute_ans = bruteSol(arr)
    print(f"Brute sol: {brute_ans[0]} appeared {brute_ans[1]} times.")

    better_ans = betterSol(arr)
    print(f"Better sol: {better_ans[0]} appeared {better_ans[1]} times.")

    optimal_ans = optimalSol(arr)
    print(f"Better sol: {optimal_ans[0]} appeared {optimal_ans[1]} times.")