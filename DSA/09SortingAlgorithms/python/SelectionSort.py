'''
Selection Sort:
    - Select a number, keep it on its right place, it can be min, max or any number.

    - O(n^2) each all cases.
'''

def minOnRightPlace(inputArr):
    n = len(inputArr)
    for i in range(n-1):
        minValIndex = i
        for j in range(i+1, n):
            if (inputArr[j] < inputArr[minValIndex]):
                minValIndex = j
        inputArr[i], inputArr[minValIndex] = inputArr[minValIndex], inputArr[i]
        # print(inputArr)

def maxOnRightPlace(inputArr):
    n = len(inputArr)
    for i in range(n-1, 0, -1):
        maxValIndex = i
        for j in range(i, -1, -1):
            if (inputArr[j] > inputArr[maxValIndex]):
                maxValIndex = j
        inputArr[i], inputArr[maxValIndex] = inputArr[maxValIndex], inputArr[i]


if __name__=="__main__":
    inputArr = [64, 32, 25, 45, 20, 15]

    # minOnRightPlace(inputArr)  
    maxOnRightPlace(inputArr)  
    print(inputArr)
