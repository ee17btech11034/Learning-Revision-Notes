# Prime =>  A number that has exact 2 factors 1 & itself.
import math
def isPrimeUsingSimpleLoop(num):
    if (num == 1):
        return False
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

def isPrimeUsingSQRT(num):
    if (num == 1):
        return False
    # all factors lie in sqrt(N)
    limit = int(math.sqrt(num)) +1
    for i in range(2, limit):
        if (num % i == 0):
            return False
    return True

if __name__=="__main__":
    num = int(input("Enter number: "))
    # isPrime = isPrimeUsingSimpleLoop(num)
    isPrime = isPrimeUsingSQRT(num)
    if (isPrime):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")