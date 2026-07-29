# Pascal Triangle
#         1
#       1   1
#     1   2   1
#   1   3   3   1  => sum of above two

# nth row will have n elements

def generateFullTriangle(n):
    # nth row will have n elements
    # we can use ncr formula to calculate
    def betterSol():
        # we can store full array for ans and calculate next line using previous
        ans = [[1]]
        for _ in range(1, n):
            temp = [1] # first element
            prev_row = ans[-1] # TC = O(1), SC = O(1) as we are just storing reference not copying or new arr.
            for j in range(1, len(prev_row)):
                element = prev_row[j] + prev_row[j-1]
                temp.append(element) # TC = O(1)
            temp.append(1) # for last 1
            ans.append(temp[:]) # TC = O(n) to copy all elements
            # ans.append(temp) # TC = O(1) to copy all elements
        print(ans) # TC = O(K) -> total no of elements
        # TC = O(n * (prev_row + (prevrow +1))) + O(K)
        # totalELements = 1 + 2 + 3 + n = n * (n+1)/2 = n^2
        # TC = O(n^2)
        # SC = n^2 to store ans
        return 
    betterSol()

    def bruteSol():
        # use nCr for each row & col 
        ans = []
        def nCr(n, r): # TC = O(r) => max to n//2
            if (n == 0):
                return 1
            res = 1
            r = min(r, n-r)
            for i in range(r):
                res *= (n-i)
                res //= (i+1)
            return res
        
        for row in range(1, n+1): # 
            ans.append([])
            for col in range(1, row+1): # TC = O(row * col) as row times
                element = nCr(row-1, col-1) # TC = O(col)
                ans[-1].append(element)
        print(ans)
        # TC = O(n^3)
        # SC = O(n^2)

    bruteSol()

    def optimalSol():
        # element in each row will start with 1 then next will be multiplied by ((n- col)/col)
        # nCk and nC(k+1) what is difference
        ans = []
        for row in range(1, n+1):
            res = 1
            ans.append([1])
            for col in range(1, row):
                res *= (row - col)
                res //= col
                ans[-1].append(res)
        print(ans)
        # TC = O(n^2)
        # SC = O(n^2)
    optimalSol()

def findElement(row, col):
    # Either we can create a full tree and then for for specific row and col. 
    # OR we can do nCr = (n!)/((r!) * (n-r)!)

    # Here ans will be (R-1)C(c-1)

    def nCr(n, r):
        if (n == 0):
            return 1
        res = 1
        r = min(r, n-r)
        for i in range(r):
            res *= (n-i)
            res //= (i+1)
        return res
    ans = nCr(row-1, col-1)
    print(f"Element at row = {row} and col={col}: ", ans)

    
if __name__=="__main__":
    # Q1. for given row and col find the element r = 5, c= 3
    # Q2; print any nth row of pascal triangle n = 5
    # print the entire triangle.

    findElement(5, 3)

    generateFullTriangle(6)