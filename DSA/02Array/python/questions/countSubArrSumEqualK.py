# Count subarray sum equals k
#

def bruteSol(arr, k): # TC = O(n^3)
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i, n):
            curr_sum = 0
            for k in range(i, j+1):
                curr_sum += arr[k]
            if (curr_sum == k):
                count += 1
    print("Brute sol: ", count)

def betterSol(arr, k): # TC = O(n^2)
    n = len(arr)
    count = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if (curr_sum == k):
                count += 1
    print("Better sol: ", count)


def optimalSol(arr, k):
    # using prefix sum
    # we say till ith ind sum = x
    # till jth index sum = y; j < i
    # if (x-k) present in prefixSum arr that means it is avalable.
    freq = {}
    n = len(arr)
    last_sum = 0
    count = 0
    freq[0] = 1
    for i in range(n):
        last_sum += arr[i]
        if last_sum in freq.keys():
            freq[last_sum] += 1
        else:
            freq[last_sum] = 1

        if (last_sum - k) in freq.keys():
            count += freq[(last_sum - k)]
    print("Optimal Sol: ", count)

if __name__=="__main__":
    arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
    k = 3

    bruteSol(arr, k)
    betterSol(arr, k)
    optimalSol(arr, k)