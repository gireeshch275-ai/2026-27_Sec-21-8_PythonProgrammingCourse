
# Diamond Pattern of Stars

n = int(input("Enter number of rows: "))

# Upper part of diamond
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)

# Lower part of diamond
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print("* " * i)
