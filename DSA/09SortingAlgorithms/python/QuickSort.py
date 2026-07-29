'''
Quick Sort:
    - It is an example of "Divide and Conquer".
    - Divide and Conquer tells to divide the big problem into small problems, each small problem is solved in similar fashion. Then we merge all small solutions to solve the bigger problem.
    
    - Select an pivot element. We can choose any element for pivot.
    - then put this pivot on its correct position. 
    - Left elements to this pivot location will be smaller than this pivot but can be unsorted. 
    - Right elements to this pivot location will be greater than this pivot but can be unsorted. 
    - now solve left and right arr in same way.
    
    - TC ==> O(n log n) -> O(n log n) -> O (n^2).
    - Worst Case: (O(n^2)) when the array is already sorted (or reverse sorted) and the first element is always chosen as the pivot.
    - To advance check :
        - how to implement Randomised Quick Sort to avoid the worst-case (O(n^2)) time complexity.
        - the alternative Lomuto Partition Scheme which uses a cleaner single-loop approach. Our approach (2 pinter opposite direction) is called "Hoare Scheme".
'''

def quickSort(inputArr, startInd, endInd):
    # print("pivot ind: ", startInd, " with start arr: ", inputArr[startInd: endInd+1])
    # Base case
    if (endInd <= startInd):
        return

    # pick pivot -> picking `startInd element as pivot here
    pivotInd = startInd

    # two pointer
    left = startInd +1
    right = endInd

    while(left <= right):
        while((left <= endInd) and (inputArr[left] <= inputArr[pivotInd])):
            left += 1
        
        while((startInd < right) and (inputArr[pivotInd] < inputArr[right])):
            right -= 1
        
        if (left < right):
            inputArr[left], inputArr[right] = inputArr[right], inputArr[left]
    
    # swap pivot with right
    inputArr[pivotInd], inputArr[right] = inputArr[right], inputArr[pivotInd]

    # print("pivot ind: ", startInd, " with after while arr: ", inputArr[startInd: endInd+1])

    quickSort(inputArr, startInd, right-1)
    quickSort(inputArr, right+1, endInd)


def quickSort2(inputArr, startInd, endInd):
    if (endInd <= startInd):
        return
    
    start = startInd
    end = endInd
    pivot_ind = start

    while(start <= end):
        while((start <= end) and (inputArr[start] <= inputArr[pivot_ind])):
            start += 1
        while((start <= end) and (inputArr[pivot_ind] < inputArr[end])):
            end -= 1
        if (start < end):
            inputArr[start], inputArr[end] = inputArr[end], inputArr[start]
    
    pivot_ind = end
    inputArr[pivot_ind], inputArr[startInd] = inputArr[startInd], inputArr[pivot_ind]  # swap pivot
    quickSort2(inputArr, startInd, pivot_ind-1)
    quickSort2(inputArr, pivot_ind+1, endInd)


if __name__=="__main__":
    inputArr = [64, 32, 25, 45, 20, 15]
    # inputArr = [64, 32, 25, 45, 20, 15, 1]

    n = len(inputArr)
    
    # quickSort(inputArr, 0, n-1)
    print(inputArr)
    
    quickSort2(inputArr, 0, n-1)
    print(inputArr)
