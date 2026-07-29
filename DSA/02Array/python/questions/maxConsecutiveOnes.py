# find the max consecutive 1's in arr.

def maxConsecutiveOnes(arr):
    count = 0
    max_count = 0

    for num in arr:
        if (num == 1):
            count += 1
        else:
            max_count = count if (count > max_count) else max_count
            count = 0
    max_count = count if (count > max_count) else max_count
    return max_count

if __name__=="__main__":
    arr = [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1]
    # arr = [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]

    max_Ones = maxConsecutiveOnes(arr)
    print("max 1's: ", max_Ones)