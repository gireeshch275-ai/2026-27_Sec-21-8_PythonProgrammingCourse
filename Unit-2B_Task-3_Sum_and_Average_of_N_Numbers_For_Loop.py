# Program to find sum and average of N numbers using for loop

n = int(input("Enter how many numbers: "))

sum = 0

for i in range(1, n + 1):
    num = int(input("Enter a number: "))
    sum = sum + num

average = sum / n

print("Sum =", sum)
print("Average =", average)
