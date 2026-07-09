# Armstrong Number => An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
import math

def isArmstrongNumber(num):
    # calculate sum of digits
    digitSquareSum = 0
    numCopy = num
    noOfDigits = int(math.log10(num)) +1
    while(numCopy > 0):
        # get digit
        digit = numCopy % 10
        digitSquareSum += (digit ** noOfDigits)
        numCopy //= 10
    
    if (num == digitSquareSum):
        return True
    return False

if __name__=="__main__":
    num = int(input("Enter number: ")) #371, 1634

    result = isArmstrongNumber(num)
    if (result):
        print(f"{num} is armstrong number.")
    else:
        print(f"{num} is not armstrong number.")


    
    