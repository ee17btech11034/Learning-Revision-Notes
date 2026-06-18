'''
Bubble Sort:
    - Create a bubble of 2 elements and swap if first is greater. This way, Maximum element will be in the last.
    - 1st iteration => 0 -> n-1 ==> (n-1)
    - 2nd iteration => 1 -> n-1 ==> (n-2)
    ...
    - -----=> (n-1) + (n-2) + .... + 1 = O(n^2)

    --  But if we can track that "if no swap that means already sorted. => omega(n)
'''

if __name__=="__main__":
    inputArr = [64, 32, 25, 45, 20, 15]

    isSwapped = False
    n = len(inputArr)

    for i in range(0, n-1):
        isSwapped = False
        for j in range(0, n-1-i):
            if (inputArr[j] > inputArr[j+1]):
                isSwapped = True
                inputArr[j], inputArr[j+1] = inputArr[j+1], inputArr[j]
        if (not isSwapped):
            break
    
    print(inputArr)
