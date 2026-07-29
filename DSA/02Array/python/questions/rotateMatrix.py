# Rotate Matrix by 90 degree
from math import *
def bruteSol(arr):
    # we will store the ans in seperate arr 
    # we will place each element on right place
    n = len(arr)
    ans = [[0]*n for _ in range(n)]
    # ans_i = 0
    # ans_j = n - 1
    # for row in arr:
    #     ans_i = 0
    #     for element in row:
    #         ans[ans_i][ans_j] = element
    #         ans_i += 1
    #     ans_j -= 1
    for i in range(n):
        for j in range(n):
            ans[j][n-i-1] = arr[i][j]
    print("brute ans: ", ans)
    # TC = O(n^2)
    # SC = O(n^2)


def optimalSol(arr):
    # we can reduce SC by making changes inplace

    # Method 1: Transpose the matrix arr, reverse the rows. 
            # We found as each col is reversed and put as row.
    # Method 2: inplace single traverse

    def transposeMethod():
        # make transpose of arr/matrix
        # We interchange the elements along diagonal

        n = len(arr)
        row = 0
        for _ in range(n):
            for i in range(row, n):
                arr[row][i], arr[i][row] = arr[i][row], arr[row][i]
            row += 1
        # print(arr)

        # reverse rows
        for i in range(n):
            for j in range(n//2):
                arr[i][j], arr[i][n-1-j] = arr[i][n-1-j], arr[i][j]
        print(arr)

    # transposeMethod()

    def singleTraverse():
        # we can say outer loop rotated. 
        # we will rotate corner 4 and then go for next 4. 
        n = len(arr)
        # top_left = [0, 0] # i, j
        # top_right = [0, n-1]
        # bottom_left = [n-1, 0]
        # bottom_right = [n-1, n-1]
        start = 0
        end = n-1
        loop = int(sqrt(n))
        for _ in range(loop):
            for i in range((end - start)):
                # temp = arr[s][s]
                # arr[s][s] = arr[n-1-i][s]
                # arr[n-1-i][s] = arr[n-1-i][n-1-i] # this way it will be complicated
                temp = arr[start][start+i]
                arr[start][start+i] = arr[end-i][start]
                arr[end-i][start] = arr[end][end-i]
                arr[end][end-i] = arr[start+i][end]
                arr[start+i][end] = temp
            start += 1
            end -= 1
        print("Optimal Sol: ", arr)
    
    singleTraverse()


if __name__=="__main__":
    arr = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    # bruteSol(arr)

    optimalSol(arr)