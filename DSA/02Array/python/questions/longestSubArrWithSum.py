# Sub Arr => contigous part of arr.
# Sub Seq => elements picked seq contigous or non-contigous.

# Q: Longest subarr with sum k

######## Q: Longest subarr with sum k (assuming all elements in arr are positive)

def long_subarr_pos_brute1(arr, k): # TC = O(n^3), SC = O(1)
    max_len = 0

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            temp_sum = 0
            for m in range(i, j+1): # calculating sum everytime
                temp_sum += arr[m]
            if (temp_sum == k):
                max_len = max(max_len, (j - i + 1))
            elif (temp_sum > k):
                break
    
    return max_len

def long_subarr_pos_brute2(arr, k): # TC = O(n^2), SC = O(1)
    max_len = 0

    for i in range(len(arr)):
        temp_sum = 0
        for j in range(i, len(arr)):
            temp_sum += arr[j]
            if (temp_sum == k):
                max_len = max(max_len, (j - i + 1))
            elif (temp_sum > k):
                break
    
    return max_len

def long_subarr_pos_better(arr, k):
    # Use hashing:
        # We store sum till (i-1)th index. 
        # when doinf ith inde then 
            # we check (sum_ith - k) present in hash that means this is present.
    
    sum_hash = [] # use hash map not array
    total_sum = 0 # or we can find this by accessing last element of sum_hash
    longest_sub = 0

    for i, num in enumerate(arr):
        # diff = total_sum - k
        total_sum += num
        diff = total_sum - k
        if (diff < 0):
            sum_hash.append(total_sum)
            continue
        if diff in sum_hash:
            ind = sum_hash.index(diff)
            longest_sub = max(longest_sub, (i - ind))
        sum_hash.append(total_sum)

    return longest_sub

def long_subarr_pos_optimal(arr, k): # TC = O(n + n), SC = O(1)
    # 2 pointer or greedy approach
    # when sum exceed k then trim from left
    # TC is 2n because inner while will run only n, it will not run n times for each i. 
    max_len = 0
    left = 0
    window_sum = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        if (window_sum == k):
            max_len = max(max_len, (right - left + 1))
        elif (window_sum > k):
            while((left < right) and (window_sum > k)):
                window_sum -= arr[left]
                left += 1
            if (window_sum == k):
                max_len = max(max_len, (right - left + 1))

    return max_len


############# for neg 
def long_subarr_neg_optimal(arr, k):
    # Use hashing:
        # We store sum till (i-1)th index. 
        # when doinf ith inde then 
            # we check (sum_ith - k) present in hash that means this is present.
    
    sum_hash = {}
    total_sum = 0 # or we can find this by accessing last element of sum_hash
    longest_sub = 0

    for i, num in enumerate(arr):
        # diff = total_sum - k
        total_sum += num
        diff = total_sum - k
        if (diff < 0):
            if total_sum not in sum_hash.keys(): # not updating the index num if sum is same. as for -ve we will diff with latest which is not longest
                sum_hash[total_sum] = i
            continue
        if diff in sum_hash.keys():
            ind = sum_hash[diff]
            longest_sub = max(longest_sub, (i - ind))
        
        if total_sum not in sum_hash.keys():
            sum_hash[total_sum] = i

    return longest_sub


if __name__=="__main__":
    # arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
    arr = [1, 2, 3, 1, 1, 1, 1, 0, 0, 0, 4, 2, 3]
    k = 4 # sum = 3


    long_subarr_pos_brute1_ans = long_subarr_pos_brute1(arr, k)
    print("long_subarr_pos_brute1: ", long_subarr_pos_brute1_ans)

    long_subarr_pos_brute2_ans = long_subarr_pos_brute2(arr, k)
    print("long_subarr_pos_brute2: ", long_subarr_pos_brute2_ans)

    long_subarr_pos_better_ans = long_subarr_pos_better(arr, k)
    print("long_subarr_pos_better: ", long_subarr_pos_better_ans)

    long_subarr_pos_optimal_ans = long_subarr_pos_optimal(arr, k)
    print("long_subarr_pos_optimal: ", long_subarr_pos_optimal_ans)


