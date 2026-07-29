# Q: find the two nums whose sum is level.
from collections import defaultdict 


def twoSumBrute(arr, level): # Here I am returning all pairs.
    # TC = O(n^2), SC = O(n//2) for storing ans
    n = len(arr)
    all_pairs = []
    for i in range(n-1):
        for j in range(i+1, n):
            if ((arr[i] + arr[j]) == level):
                all_pairs.append([i, j])
    return all_pairs

def twoSumBetter(arr, level):
    # Use hashing
    # TC = O(n log n), SC = O(n) for hash + O(n//2) for ans = O(n)
    hash_map = defaultdict(lambda: -1)
    all_pairs = []

    for i in range(len(arr)):
        diff = level - arr[i]
        ind = hash_map[diff]
        if (ind > -1):
            all_pairs.append([ind, i])
        hash_map[arr[i]] = i
    return all_pairs


def twoSumOptimal(arr, level):
    # Greedy or 2 pointer approach
    # TC will be same as above but slightly better
    # TC = O(n + n log n) but changing the input array. SC = O(1)

    arr.sort() # sort the array
    left = 0
    right = len(arr) -1
    all_pairs = []

    while(left < right):
        if ((arr[left] + arr[right]) < level):
            left += 1
        elif ((arr[left] + arr[right]) > level):
            right -= 1
        else:
            all_pairs.append([left, right])
            left += 1

    return all_pairs


if __name__=="__main__":
    arr = [2, 6, 5, 8, 11, 10, 4, 6, 8]
    level = 14

    twoSum_brute_ans = twoSumBrute(arr, level)
    print("Two sum Brute ans: ", twoSum_brute_ans)

    twoSum_better_ans = twoSumBetter(arr, level)
    print("Two sum Better ans: ", twoSum_better_ans)

    twoSum_optimal_ans = twoSumOptimal(arr, level) # these are in sorted as we sorted array 
    print("Two sum Better ans: ", twoSum_optimal_ans)