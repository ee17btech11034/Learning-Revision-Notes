'''
Insertion Sort:
    - Start from i=0, like one element sorted arr.
    - insert elements at i, in right side or sorted arr by right shifting the greater elements.

    - Best case when arr is already sorted then only single traversal is needed.

    - TC ==> O(n) --> O(n^2)
'''


if __name__=="__main__":
    inputArr = [64, 32, 25, 45, 20, 15]

    n = len(inputArr)
    for i in range(1, n):
        temp = inputArr[i]
        j = i
        while((j > 0) and (inputArr[j-1] > temp)):
            # print("while hit")
            inputArr[j] = inputArr[j-1]
            j -= 1
        inputArr[j] = temp
        # print(inputArr)


    print(inputArr)
