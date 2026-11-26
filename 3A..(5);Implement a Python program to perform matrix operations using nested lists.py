# Matrix Operations Using Nested Lists

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print("Matrix A:")
for row in A:
    print(row)

print("Matrix B:")
for row in B:
    print(row)

# Matrix Addition
addition = [
    [A[i][j] + B[i][j] for j in range(2)]
    for i in range(2)
]

print("\nMatrix Addition:")
for row in addition:
    print(row)

# Matrix Subtraction
subtraction = [
    [A[i][j] - B[i][j] for j in range(2)]
    for i in range(2)
]

print("\nMatrix Subtraction:")
for row in subtraction:
    print(row)

# Matrix Multiplication
multiplication = [
    [sum(A[i][k] * B[k][j] for k in range(2))
     for j in range(2)]
    for i in range(2)
]

print("\nMatrix Multiplication:")
for row in multiplication:
    print(row)