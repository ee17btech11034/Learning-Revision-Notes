import math

def digitCount(num):
    if (num == 0):
        return 1
    
    counter = 0
    while(num > 0):
        counter += 1
        num //= 10
    
    return counter

def digitCount2(num):
    if (num == 0):
        return 1
    return (int(math.log10(num)) + 1) # ceil does not work when num=10

if __name__=="__main__":
    num = int(input("Enter number: "))
    
    noOfDigits1 = digitCount(num)
    noOfDigits2 = digitCount2(num)

    print(f"{noOfDigits1} digits are present in number {num}.")
    print(f"{noOfDigits2} digits are present in number {num}.")
    # TC => O(log10 (n))
