# Set Matrix Zeroes
#an m*n matrix is given with only 0/1. 
# find the zero and make entire col & row and make it zero.


def bruteSol(arr):
    # SOl1 => we can create a new arr and then do the following otr follow the below steps. 

    unique_mark = -1 # if we do not mark unique then on run time we will be changing zeroes and we will find then in next iterations.
    # traverse the i,j aand if find 0 then mark all elements in that row and col as unique so that we can make changes in main arr.
    m = len(arr)
    n = len(arr[0]) # m*n

    def markUnique(row, col):
        # mark row elements
        for j in range(n):
            if (arr[row][j] != 0):
                arr[row][j] = unique_mark
        for i in range(m):
            if (arr[i][col] != 0):
                arr[i][col] = unique_mark
        
    for i in range(m): #TC = O(m*n*(m+n))
        for j in range(n):
            if (arr[i][j] == 0):
                markUnique(i, j) #TC = O(m + n)
    
    for i in range(m): #TC = O(m*n)
        for j in range(n):
            if (arr[i][j] == unique_mark):
                arr[i][j] = 0 # revert as first changing step is completed.
    # TC = O(m*n*(m+n)) + O(m*n) = O(n^3)
    # SC = O(1)

def betterSol(arr):
    # if we can keep track of zeroes in rows and cols then we can do it.
    m = len(arr)
    n = len(arr[0]) # 
    zero_row = [False]*m
    zero_col = [False]*n

    for i in range(m):
        for j in range(n):
            if (arr[i][j] == 0):
                zero_row[i] = True
                zero_col[j] = True
    for i in range(m):
        for j in range(n):
            if (zero_row[i] or zero_col[j]):
                arr[i][j] = 0
    # TC = O(m*n + m*n)
    # SC = O(m+n)


def optialSol(arr):
    # we can not optimize TC as we need that to traverse. 
    # we are keeping track of zeroes in 2 different araays. Let's use first row and col  to behave like that.
    # but issue here is 90, 0) will collapse for both row and col. So, lets keep a new variable for col_0
    # part is when we do the changes make if sub porttion first and then top row and then col. As arr[0][n-1] will depend on itself and arr[0][0]
    # if we make changes for arr[0][0] first that depends on col_0. Then it will affect upper line. 

    col_0 = 1
    m = len(arr)
    n = len(arr[0]) # 

    for i in range(m):
        for j in range(n):
            if (arr[i][j] == 0):
                if (j == 0):
                    col_0 = 0
                else:
                    arr[0][j] = 0
                arr[i][0] = 0
    
    # lets go my way ==> i am saying that we will traverse backward like last element to origin
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            isColZero = col_0 if j == 0 else arr[0][j]
            # isColZero = False
            # if (j == 0):
            #     if (col_0 == 0):
            #         isColZero = True
            # else:
            #     if (arr[0][j] == 0):
            #         isColZero = True
            # if ((isColZero) or (arr[i][0] == 0)):
            if ((isColZero == 0) or (arr[i][0] == 0)):
                arr[i][j] = 0
    # TC = O(m*n + m*n)
    # SC = O(1)


if __name__=="__main__":
    arr = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
          ]
    # bruteSol(arr)
    # print("brute ans: ", arr)

    # betterSol(arr)
    # print("better ans: ", arr)

    optialSol(arr)
    print("optimal ans: ", arr)