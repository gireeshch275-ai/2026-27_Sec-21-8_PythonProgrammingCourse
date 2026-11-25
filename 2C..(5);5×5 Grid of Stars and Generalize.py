
# Print a star grid using user input

n = int(input("Enter grid size: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
