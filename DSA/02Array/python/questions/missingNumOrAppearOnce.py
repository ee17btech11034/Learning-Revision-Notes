# Q: arris given and n is given. 1 to n nums are present in this but one number is missing find that.

############# Missing number
def missingNumberBrute(arr, n): # TC = O(n^2), SC = O(1)
    for i in range(1, n+1):
        for num in arr:
            if (num == i):
                break
        else: # we can use flag and use another if condition here. set flag in above line
            return i
    return -1

def missingNumBetterSol(arr, n): # TC = O(n + n) = O(n), SC = O(n)
    # create an hash array of length (n+1)
    freq = [0]*(n+1)

    for num in arr:
        freq[num] = 1
    
    for i in range(1, n+1):
        if (freq[i] == 0):
            return i
    return -1


def missingOptimal1(arr, n): # TC = O(n) if use formul for sum else O(2n), SC = O(1)
    # using sum of all numbers
    # Not a good approach for big numbers such as 10^5 or bigger as we can not store sum of these numbers until we use long.
    arr_sum = 0
    for num in arr:
        arr_sum += num
    
    # sum of nums 1 to n
    # num_sum = n*(n+1)/2
    num_sum = 0
    for i in range(1, n+1):
        num_sum += i
    
    return (num_sum - arr_sum)


# def missingOptimal2(arr, n): # TC = O(n + n) = O(n), SC = O(1)
#     # using XOR property.     a XOR a = 0, a XOR 0 = a
#     xor_val = 0
#     for i in range(1, n+1):
#         xor_val ^= i
    
#     for num in arr:
#         xor_val ^= num
    
#     return xor_val

def missingOptimal2(arr, n): # TC = O(n), SC = O(1)
    # using XOR property.     a XOR a = 0, a XOR 0 = a
    # XOR of big numbers will be smaller
    xor_val = n
    for i in range(1, n):
        xor_val ^= (i ^ arr[i-1])
    
    return xor_val


if __name__=="__main__":
    # missing number
    arr = [1, 2, 5, 3]
    n = 5

    missingNumBrute_ans = missingNumberBrute(arr, n)
    print("Missing Num using Brute: ", missingNumBrute_ans)

    missingNumBetter_ans = missingNumBetterSol(arr, n)
    print("Missing Num using Better: ", missingNumBetter_ans)

    missingOptimal1_ans = missingOptimal1(arr, n)
    print("Missing Num using Optimal using sum: ", missingOptimal1_ans)

    missingOptimal2_ans = missingOptimal2(arr, n)
    print("Missing Num using Optimal using XOR: ", missingOptimal2_ans)