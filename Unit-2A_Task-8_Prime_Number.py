# Program to check whether a number is prime or not

num = int(input("Enter a number (1 to 100): "))

if num <= 1:
    print("Not a prime number")
else:
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print("Prime number")
    else:
        print("Not a prime number")
