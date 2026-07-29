# Easy Q: Buy and sell stock only once.

def bruteSol(arr):
    n = len(arr)
    profit = 0

    for i in range(n-1):
        for j in range(i+1, n):
            profit = max(profit, (arr[j] - arr[i]))
    
    return profit

def optimalSol(arr):
    # if we want to sell it on ith ind, that means we must have bought it on minimum on the left.
    n = len(arr)
    min_bought_val = arr[0]
    max_profit = 0

    for i in range(1, n):
        temp = arr[i] - min_bought_val
        max_profit = max(max_profit, temp)
        min_bought_val = min(min_bought_val, arr[i])
    return max_profit



if __name__=="__main__":
    arr = [7, 1, 5, 3, 6, 4]

    print("Profit using brute: ", bruteSol(arr))

    print("Profit using optimal: ", optimalSol(arr))
