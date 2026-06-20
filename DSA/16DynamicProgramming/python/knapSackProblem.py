'''
Q1. A thief has a knapsack (bori) of weith W. an arr is given with weight with value (price). maximum picked item.
Can not pick fraction of weight.
Sol:
    - Find the per kg price. 
    - sort on decresasing order on per kg price. 
    - now do the loop and add item.
'''

'''
0/1 knapsack: either pick that or do not pick, no partial allowed
'''


def knapSackRecursion(arr, ind, capacity, n):
    # Base cases
    if ((n==0) or (capacity == 0) or (ind == n)):
        return 0
    
    if (arr[ind][1] > capacity ):
        return knapSackRecursion(arr, ind+1, capacity, n) # if bigger than capacity then won't include
    
    include = arr[ind][0] + knapSackRecursion(arr, ind+1, capacity - arr[ind][0], n)
    exclude = knapSackRecursion(arr, ind+1, capacity, n)

    return max(include, exclude)

def knapSackDP(arr, capacity, n):
    # 2D array
    dp = [[0]*(capacity +1) for _ in range(n+1)]

    for row in range(1, n+1):
        for col in range(1, capacity+1):
            if (col >= arr[row -1][1]):
                dp[row][col] = max(dp[row -1][col], (dp[row -1][(col - arr[row -1][1])] + arr[row -1][0]))
            else:
                dp[row][col] = dp[row-1][col]
    
    for row in dp:
        print(row)
    return dp[n][capacity]


if __name__=="__main__":
    #[price, weight]-> weight available
    arr = [[21, 7], [24, 4], [12, 6], [40, 5], [30, 6]]
    # arr = [[24, 7], [21, 3], [12, 4], [10, 5]]
    knapSackWeight = 20

    '''
    arr.sort(key=lambda x: (x[0] / x[1]), reverse=True) # sort on decresasing order on per kg price. 

    print(arr)

    totalValues = 0
    for [price, weight] in arr:
        if (weight <= knapSackWeight):
            totalValues += price
        knapSackWeight -= weight
    
    print(totalValues)
    '''
    '''
    Above code may give the correct ans but not sure. We will have to check all possibilities here. 
    To code it like we can pick it or not pick it. By recursion TC = O(2^n) 
    '''
    # totalValue = knapSackRecursion(arr, 0, knapSackWeight, len(arr))

    # print(totalValue)



    '''
    Memoization Technique:
        - When we have single parameter then we create 1D DP array. But when we have 2 params then we use 2D array,

    Steps:
        - here we have price, weight, capacity.
        - we create 2D array of       (weight + 1) X (Capacity +1)
        - Colums represent the capacity. 
            - col = 0 tells that right now capacity is zero
            - col = 1 tells that right now capacity is one, etc.
        - Row represent the ith ind element included. 
            - row = 0 tells that no element is included.
            - row = 1 tells that 1st element is included, etc.
        
            - To fill the dp[i][j]:
                -> if i==0 or j==0 then fill 0.
                -> above row with same col tells that val was this when ith was not included dp[i-1][j]
                -> above row with col-weight tells that to include this element, we will have to empty the bag by this weight. dp[i-1][j-weight] + price
                -> max(dp[i-1][j], dp[i-1][j-weight] + price)
    '''

    arr2 = [[3, 2], [4, 3], [5, 4], [6, 5]]
    knapSackWeight = 5
    # totalValue = knapSackDP(arr, knapSackWeight, len(arr))
    totalValue = knapSackDP(arr2, knapSackWeight, len(arr2))
    print(totalValue)