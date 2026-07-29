# Number of subarrays with xor k.

def bruteSol(arr, target):
    ans = 0

    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            xorVal = 0
            for k in range(i, j+1):
                xorVal ^= arr[k]
            if (xorVal == target):
                ans += 1
    print("Brute: ", ans)
    # TC = O(n^3)
    # SC = O(1)

def betterSol(arr, k):
    ans = 0

    n = len(arr)

    for i in range(n):
        xorVal = 0
        for j in range(i, n):
            xorVal ^= arr[j]
            if (xorVal == k):
                ans += 1
    print("Better: ", ans)
    # TC = O(n^2)
    # SC = O(1)

def optimalSol(arr, target):
    # total_xot = x^y
    # TX = X^target
    # x = TX ^ target
    # find x in hash

    freq = {}
    # freq[0] = 1
    curr_xor = 0
    ans = 0
    for num in arr:
        curr_xor ^= num
        freq[curr_xor] = freq.get(curr_xor, 0) +1
        remain = curr_xor ^ target
        ans += freq.get(remain, 0)
    print("Optimal: ", ans)
    # TC = O(n)
    # SC = O(n) for unquw=e xor values

if __name__=="__main__":
    arr = [4, 2, 2, 6, 4]
    k = 6

    bruteSol(arr, k)
    betterSol(arr, k)
    optimalSol(arr, k)
