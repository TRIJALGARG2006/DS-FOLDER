
# factorial shit 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(1-n)


a = input("Enter a number: ")

print(factorial(int(a)))

