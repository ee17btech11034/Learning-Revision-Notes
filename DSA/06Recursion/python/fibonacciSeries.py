#Fibonacci Series: 1, 1, 2, ...   (1st, 2nd elements)

def fibonacciNumber(n):
    if ((n == 1) or (n == 2)):
        return 1
    return (fibonacciNumber(n-1) + fibonacciNumber(n-2))

if __name__=='__main__':
    n = int(input("Enter the number: "))
    if (n < 0):
        print("Please Enter positive number")
    else:
        fib_val = fibonacciNumber(n)
        print(f"fibonacciNumber ({n}) = {fib_val}")