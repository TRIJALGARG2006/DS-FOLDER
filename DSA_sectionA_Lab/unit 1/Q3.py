def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1: # Base case
        return 1
    return n * factorial(n - 1) # Recursive case

print(f"Factorial of 4 is: {factorial(4)}")