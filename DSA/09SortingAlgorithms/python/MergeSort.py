'''
Merge Sort:
    - It is an example of "Divide and Conquer".
    - Divide and Conquer tells to divide the big problem into small problems, each small problem is solved in similar fashion. Then we merge all small solutions to solve the bigger problem.
    - We divide array in small parts (mainly half here), until it is sorted (single element).
    - Then we merge them.

    - TC ==> O(n log n) for all cases.
'''

def mergeSortUsingRecursion(inputArr, startInd, endInd):
    # base case -> single element remaining
    if (startInd > endInd):
        print("start Index must be smaller than end index")
        return
    elif (startInd == endInd):
        return
    # Divide
    mid = startInd + ((endInd - startInd)//2)
    mergeSortUsingRecursion(inputArr, startInd, mid) # left half
    mergeSortUsingRecursion(inputArr, mid+1, endInd) # right half

    left_half = inputArr[startInd: mid+1].copy()
    right_half = inputArr[mid+1: endInd+1].copy()

    left_pointer = 0
    right_pointer = 0
    input_arr_ind = startInd

    while((left_pointer < len(left_half)) and (right_pointer < len(right_half))):
        if (left_half[left_pointer] <= right_half[right_pointer]):
            inputArr[input_arr_ind] = left_half[left_pointer]
            left_pointer += 1
        else:
            inputArr[input_arr_ind] = right_half[right_pointer]
            right_pointer += 1
        
        input_arr_ind += 1
    
    while(left_pointer < len(left_half)):
        inputArr[input_arr_ind] = left_half[left_pointer]
        left_pointer += 1
        input_arr_ind += 1
    
    while(right_pointer < len(right_half)):
        inputArr[input_arr_ind] = right_half[right_pointer]
        right_pointer += 1
        input_arr_ind += 1
        

if __name__=="__main__":
    # inputArr = [64, 32, 25, 45, 20, 15]
    inputArr = [64, 32, 25, 45, 20, 15, 1]

    n = len(inputArr)
     
    mergeSortUsingRecursion(inputArr, 0, n-1)

    print(inputArr)
