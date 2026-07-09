import math
def divisorpairs(num):
    limit = int(math.sqrt(num))
    ans = []
    for i in range(1, limit+1): # inlcude num for perfect square
        if (num % i == 0):
            ans.append((i, num//i))
    return ans

if __name__=="__main__":
    num = int(input("Enter number: "))
    ans = divisorpairs(num)
    print(ans)
