import sys

# ==============================================================================
# 1. UNDERSTANDING AND ADJUSTING SYSTEM RECURSION LIMITS
# ==============================================================================
def manage_system_stack():
    """
    Demonstrates how to view and modify the Python system call stack limit.
    By default, Python sets this limit to 1000 to prevent infinite recursion
    from consuming all system memory and crashing the OS.
    """
    print("=== System Call Stack Monitoring ===")
    
    # Get current default limit
    default_limit = sys.getrecursionlimit()
    print(f"Default Python maximum recursion depth limit: {default_limit}")
    
    # Safely increase the limit for deep tree/graph traversals
    new_limit = 2000
    sys.setrecursionlimit(new_limit)
    print(f"Updated maximum recursion depth limit: {sys.getrecursionlimit()}")
    
    # Restoring default limit to remain clean
    sys.setrecursionlimit(default_limit)


# ==============================================================================
# 2. LINEAR (NON-TAIL) RECURSION
# ==============================================================================
def factorial_linear(n):
    """
    Calculates factorial using standard Linear Recursion.
    
    Time Complexity:  Ω(n) -> Θ(n) -> O(n)
    Space Complexity: Ω(n) -> Θ(n) -> O(n) (Due to pending operations on stack)
    
    Why it is Non-Tail:
    The final instruction is `n * factorial_linear(n - 1)`. The computer 
    CANNOT drop the current stack frame because it must wait for the child 
    call to resolve before multiplying the result by 'n'.
    """
    # Base Case: The absolute termination anchor
    if n <= 1:
        return 1
        
    # Recursive Case with a PENDING arithmetic operation (*)
    return n * factorial_linear(n - 1)


# ==============================================================================
# 3. TAIL-OPTIMISED RECURSION (Using an Accumulator)
# ==============================================================================
def factorial_tail_helper(n, accumulator=1):
    """
    Calculates factorial using Tail Recursion.
    
    Time Complexity:  Ω(n) -> Θ(n) -> O(n)
    Space Complexity: O(1) in languages with TCO / O(n) in standard Python
    
    Why it is Tail Recursive:
    The final instruction is purely the self-call itself. All mathematical 
    computations are calculated upfront and passed down into the `accumulator`. 
    There are zero pending operations left on the current stack frame.
    """
    # Base Case: Return the calculated total sitting in the accumulator
    if n <= 1:
        return accumulator
        
    # Recursive Case: Perfect tail-call. No pending operations here!
    return factorial_tail_helper(n - 1, n * accumulator)

def factorial_tail(n):
    """Clean wrapper interface for the tail recursive function."""
    return factorial_tail_helper(n, 1)


# ==============================================================================
# RUNTIME ARCHITECTURE VERIFICATION
# ==============================================================================
if __name__ == "__main__":
    # 1. Test and view stack limits
    manage_system_stack()
    print("\n" + "="*50 + "\n")

    # 2. Trace Linear vs Tail results
    target_number = 5
    print(f"Calculating Factorial for: {target_number}!")
    
    linear_result = factorial_linear(target_number)
    tail_result = factorial_tail(target_number)
    
    print(f"Linear Recursion Result: {linear_result}")
    print(f"Tail Recursion Result:   {tail_result}")

    # 3. Visualizing Stack Safety / Exception Handling
    print("\n=== Testing Stack Overflow Limit Safety ===")
    try:
        # Intentionally triggering a depth that violates the default limit
        # safely intercepted by Python's internal tracker
        invalid_depth = 1500 
        print(f"Attempting a linear call of depth {invalid_depth}...")
        factorial_linear(invalid_depth)
    except RecursionError as error:
        print(f"Successfully caught crash! System Note: {error}")

'''
Even though factorial_tail_helper is written in perfect tail-recursive form, standard Python (CPython) does not natively execute Tail Call Optimisation (TCO). 
The core developers intentionally left TCO out of the compiler layout to ensure that complete system stack traces remain completely readable for debugging purposes.

Therefore, for massive calculations in Python that would require more than a few thousand stack frames, you should always rewrite the logic into a standard iterative loop (while / for) to reduce the space complexity to a perfect O(1) constant boundary.

'''