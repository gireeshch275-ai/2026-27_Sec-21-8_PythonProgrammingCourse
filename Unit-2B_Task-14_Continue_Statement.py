# Demonstrate continue statement using for loop

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print("Loop completed")

# Demonstrate continue statement using while loop

i = 0

while i < 10:
    i = i + 1

    if i == 5:
        continue

    print(i)

print("Loop completed")
