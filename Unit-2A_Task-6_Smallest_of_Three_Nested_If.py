# Program to find the smallest of three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b:
    if a < c:
        print("The smallest number is", a)
    else:
        print("The smallest number is", c)
else:
    if b < c:
        print("The smallest number is", b)
    else:
        print("The smallest number is", c)
