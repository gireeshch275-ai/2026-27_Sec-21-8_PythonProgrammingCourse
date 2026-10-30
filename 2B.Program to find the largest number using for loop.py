# Program to find the largest number using for loop

n = int(input("Enter how many numbers: "))

largest = int(input("Enter a number: "))

for i in range(1, n):
    num = int(input("Enter a number: "))

    if num > largest:
        largest = num

print("The largest number is:", largest)
