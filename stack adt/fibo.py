def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

count = int(input("How many terms to print: "))

if count <= 0:
    print("enter number :")
else:
    print("Fibonacci:")
    for i in range(count):
        print(fibonacci(i))