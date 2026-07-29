# values of 3 elements ( i!=j !=k) from arr must be equal to k. find such groups

def bruteSol(arr, target):
    # ans = [] # can not use list as eleent in set, we will have to change it into tuple
    ans = set()
    n = len(arr)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if ((arr[i] + arr[j] + arr[k]) == target):
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    # if temp not in ans:
                    #     ans.append(temp)
                    ans.add(tuple(temp))
    print("brute: ", ans)
    # TC = O(n^3)
    # SC = O(K) to store ans.

def betterSol1(arr, target):
    # i + j + k = target
    # k = target - (i + j)
    # if for i, j;  I can find k in hashmap in better sol. 
    n = len(arr)
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    ans = set()
    for i in range(n-1):
        freq[arr[i]] -=1
        for j in range(i+1, n):
            freq[arr[j]] -= 1 # we do not want to tke element twice
            third_element = target - arr[i] - arr[j]
            freqVal = freq.get(third_element, 0)
            if (freqVal > 0):
                temp = [arr[i], arr[j], third_element]
                temp.sort()
                ans.add(tuple(temp))
            freq[arr[j]] += 1
        freq[arr[i]] += 1
    print("better1: ", ans)
    # TC = O(n + n^2)
    # SC = O(n + k) for freq and ans.

def betterSol2(arr, target):
    # for i < j < k, if i take i, k, then j will be in hashmap. 
    n = len(arr)
    ans = set()
    for i in range(n-1):
        freq = {}
        for k in range(i+1, n):
            jth_ele = target - arr[i] - arr[k]
            isPresent = freq.get(jth_ele, 0)
            if (isPresent):
                temp = [arr[i], arr[k], jth_ele]
                temp.sort()
                ans.add(tuple(temp))
            freq[arr[k]] = freq.get(arr[k], 0) +1
    print("better2: ", ans)
    # TC = O(n^2)
    # SC = O(n + k)

def optimalSol(arr, target):
    # sort the arr and then try to get triblets
    # Use 3 pointers, with 2 pointer moving
    # Like i is fixed and moving i from i_1 to k in the end
    arr.sort()
    n = len(arr)
    i = 0
    j = 0
    k = n -1
    ans = set()
    while(i < (n-2)):
        j = i+1
        k = n-1

        while(j < k):
            sumCal = arr[i] + arr[j] + arr[k]
            if (sumCal ==  target):
                ans.add(tuple([arr[i], arr[j], arr[k]]))
                while((j < k) and (arr[j] == arr[j+1])): # can not compare with i-1 as what is ith and j = I=1 th elem are different then it will not move.
                    j += 1
                j += 1
                while((j < k) and (arr[k] == arr[k-1])):
                    k -= 1
                k -= 1
            elif (sumCal < target):
                while((j < k) and (arr[j] == arr[j+1])):
                    j += 1
                j += 1
            else:
                while((j < k) and (arr[k] == arr[k-1])):
                    k -=1
                k -= 1
        while((i < (n-2)) and (arr[i] == arr[i+1])):
            i += 1
        i += 1
    print("Optimal sol: ", ans)
    # TC = O(nlog n   +  n^2)
    # SC = O(k) to store ans.

if __name__=="__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    target = 0

    # arr = [-2, -1, 0, -2, 2, 2, -2, 2, -1, -1, 0, 0, 2]
    target = 0

    bruteSol(arr, target)
    betterSol1(arr, target)
    betterSol2(arr, target)
    optimalSol(arr, target)