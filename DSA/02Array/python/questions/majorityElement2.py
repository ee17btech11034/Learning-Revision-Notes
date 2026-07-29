#  majority elements that appreaed > n//3 times.
# at max we can have 2 integers as ans. as n/3 + n/3 ==>  > 2n/3 

def bruteSol(arr):
    n = len(arr)
    ans = []

    for num in arr:
        if num not in ans: # TC = O(1)f for this as max 2 elements can be there
            count = 0
            for j in range(n):
                if (arr[j] == num):
                    count += 1
            if (count > (n//3)):
                ans.append(num)
        if (len(ans) > 1):
            break # as we found 2 elements
    # TC = O(n^2) as for n/3 elements we are running full loop inside. suppose intial n/3 elements are distinct
    # SC = O(2)
    print(ans)

def betterSol(arr):
    n = len(arr)
    freq = {}
    ans = []
    for num in arr:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
        if (freq[num] > (n//3)):
            ans.append(num)
        if (len(ans) > 1):
            break
    print(ans)
    # TC = O(n)
    # SC = O(n/3) = O(n) 

def optimalSol(arr):
    #cancelation logic
    ele_1 = 0
    cnt_1 = 0
    ele_2 = 0
    cnt_2 = 0

    for num in arr:
        if ((cnt_1 == 0) and (ele_2 != num)):
            ele_1 = num
            cnt_1 = 1
        elif ((cnt_2 == 0) and (ele_1 != num)):
            ele_2 = num
            cnt_2 = 1
        elif (ele_1 == num):
            cnt_1 += 1
        elif (ele_2 == num):
            cnt_2 += 1
        else:
            cnt_1 -= 1
            cnt_2 -= 1
    
    # check if these 2 can be ans or not
    cnt_1 = 0
    cnt_2 = 0
    ans = []
    for num in arr:
        if (num == ele_1):
            cnt_1 += 1
        elif(num == ele_2):
            cnt_2 += 1
    if (cnt_1 > (n//3)):
        ans.append(ele_1)
    if (cnt_2 > (n//3)):
        ans.append(ele_2)
    print(ans)
    # TC = O(n + n) = O(n)
    # SC = O(1)
    
if __name__=="__main__":
    arr = [1, 1, 1, 3, 3, 2, 2, 2]
    n = 8

    bruteSol(arr)
    betterSol(arr)
    optimalSol(arr)