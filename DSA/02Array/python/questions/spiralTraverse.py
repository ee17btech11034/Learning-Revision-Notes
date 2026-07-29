# Spiral Traversal of Matrix of n*m way


def optimalSol(arr):
    # it does not have multiple sol as we just need to print spiral format
    n = len(arr)
    m = len(arr[0])
    top = 0
    bottom = n-1
    left = 0
    right = n-1

    # while((top <= bottom) or (left <= right)): This will not work for arr =[[1]] as we never ran any singlr loop
    #     # print top left -> right
    #     for j in range(left, right):
    #         print(arr[top][j], end=" ")
        
    #     # right top -> bopttom
    #     for i in range(top, bottom):
    #         print(arr[i][right], end=" ")
        
    #     top += 1

    #     # bottom right -> left
    #     for j in range(right, left, -1):
    #         print(arr[bottom][j], end=" ")
        
    #     right -= 1

    #     # left bottom -> top
    #     for i in range(bottom, top-1, -1): # we shift top so we need to include this element
    #         print(arr[i][left], end=" ")
        
    #     left += 1
    #     bottom -= 1

    while((top <= bottom) or (left <= right)):
        # print top left -> right
        for j in range(left, right+1):
            print(arr[top][j], end=" ")
        
        top += 1
        # right top -> bopttom
        for i in range(top, bottom+1):
            print(arr[i][right], end=" ")
        
        right -= 1

        # bottom right -> left
        if (top <= bottom):
            for j in range(right, left-1, -1):
                print(arr[bottom][j], end=" ")
            
            bottom -= 1

        # left bottom -> top
        if (left <= right):
            for i in range(bottom, top-1, -1): # we shift top so we need to include this element
                print(arr[i][left], end=" ")
            
            left += 1



if __name__=="__main__":
    arr = [
        [1, 2, 3, 4, 5, 6],
        [20, 21, 22, 23, 24, 7],
        [19, 32, 33, 34, 25, 8],
        [18, 31, 36, 35, 26, 9],
        [17, 30, 29, 28, 27, 10],
        [16, 15, 14, 13, 12, 11]
    ]

    # arr = [[1]]

    optimalSol(arr)