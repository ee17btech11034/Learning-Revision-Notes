def printName(name, times):
    if (times == 0):
        return # base condition
    print(name, end=" ")
    printName(name, times-1)

def countingToN(i, n):
    if (i > n):
        return # base condition
    print(i, end=" ")
    countingToN(i+1, n)

def countingToNBacktrack(n): # Backtracking
    if (n == 0):
        return # base condition
    countingToN(n-1)
    print(n, end=" ")

def reverseCountingToN(n):
    if (n == 0):
        return # base condition
    print(n, end=" ")
    reverseCountingToN(n-1)

def sumOfNnums(n):
    if (n == 0):
        return 0
    return (n + sumOfNnums(n-1))

if __name__=="__main__":
    printName("Raja", 5) # print name 5 times
    print()

    countingToN(1, 6) # 1 to n
    print()

    reverseCountingToN(6) # 1 to n
    print()

    sum_ans = sumOfNnums(6) # sum of nums 1 to n
    print("sum: ", sum_ans)