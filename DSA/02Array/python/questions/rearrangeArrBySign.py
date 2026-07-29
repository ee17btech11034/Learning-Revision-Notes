# Rearrange array elements alternate by sign. as n//2 are positive.
# arr = [3, 1, -2, -5, 2, -4]  => [3, -2, 1, -5, 2, -4]


## if not sure that n//2 are postive the brute with few twiks is the optimal sol.


def bruteSol(arr):
    # TC = O(n + n/2) = O(n)
    # SC = O(n)
    pos_arr = []
    neg_arr = []

    for num in arr:
        if ( num < 0):
            neg_arr.append(num)
        else:
            pos_arr.append(num)
    
    for i in range(len(arr)//2):
        arr[2*i] = pos_arr[i]
        arr[(2*i) +1] = neg_arr[i]
    

def optimalSol(arr):
    # We can not reduce SC but we can better it in single pass. 
    # TC = O(n)
    # SC = O(n)

    n = len(arr)
    ans = [0]*n
    pos_ind = 0
    neg_ind = 1

    for num in arr:
        if (num < 0):
            ans[neg_ind] = num
            neg_ind += 2
        else:
            ans[pos_ind] = num
            pos_ind += 2
    
    return ans



# When pos, neg are not equal length
def optimalSol2(arr):
    # TC = O(n + n/2) = O(n)
    # SC = O(n)
    pos_arr = []
    neg_arr = []

    for num in arr:
        if ( num < 0):
            neg_arr.append(num)
        else:
            pos_arr.append(num)
    
    # check which is more start with that
    # if    # complete this code

if __name__=="__main__":
    arr = [3, 1, -2, -5, 2, -4]

    # bruteSol(arr)
    # print(arr)

    ans = optimalSol(arr)
    print(ans)