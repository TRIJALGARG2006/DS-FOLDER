#find of sum of all the digits in a given number

n = int(input("Enter a number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
print("Sum of digits:", sum)
magic_number = 0
while sum > 0 :
    digit = sum % 10
    magic_number = magic_number + digit
    sum //= 10
print("Magic number is :", magic_number)