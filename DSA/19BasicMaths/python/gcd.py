# GCD/HCF => Greatest common divisor.
# common factors.

# gcd(a,b) = gcd(a, b-a) =....= gcd(k, 0) => k is the common factor.

def gcdUsingSimple(a, b):
    gcdAns = 1
    for i in range(1, min(a, b) +1): # TC => O(min(m, n))
        if ((a % i == 0) and (b % i == 0)):
            gcdAns *= i
    
    return gcdAns

def gcdUsingDiff(a, b): # Euclidean Theorem
    if (a == 0):
        return b
    if (b == 0):
        return a
    if (a < b):
        return gcdUsingDiff(a, b-a)
    return gcdUsingDiff(a-b, b)

if __name__=="__main__":
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    gcdVal = gcdUsingSimple(num1, num2)

    print(f"GCD({num1}, {num2}) => {gcdVal}")


    gcdVal2 = gcdUsingDiff(num1, num2)
    print(f"GCD({num1}, {num2}) => {gcdVal2}")
