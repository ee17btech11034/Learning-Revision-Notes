def invertNumber(num):
    reversedNum = 0

    while(num > 0):
        lastDigit = num % 10
        reversedNum = (reversedNum * 10) + lastDigit
        num //= 10
    
    return reversedNum

def isPalindrome(num):
    num = str(num)
    n = len(num)
    for i in range(n//2):
        if (num[i] != num[n - i - 1]):
            return False
    return True

if __name__=="__main__":
    num = int(input("Enter number: "))
    
    reversedNum = invertNumber(num)

    if (num == reversedNum):
        print(f"number {num} is palindrome.")
    else:
        print(f"number {num} is not palindrome.")

    if (isPalindrome(num)):
        print(f"number {num} is palindrome.")
    else:
        print(f"number {num} is not palindrome.")
    # TC => O(log10 (n))