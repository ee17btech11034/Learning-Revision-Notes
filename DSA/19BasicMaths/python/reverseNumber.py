def invertNumber(num):
    reversedNum = 0

    while(num > 0):
        lastDigit = num % 10
        reversedNum = (reversedNum * 10) + lastDigit
        num //= 10
    
    return reversedNum

if __name__=="__main__":
    num = int(input("Enter number: "))
    
    reversedNum = invertNumber(num)

    print(f"{num} ==> {reversedNum}")
    # TC => O(log10 (n))