# Tuple Operations

# Create two tuples
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

print("First Tuple:", tuple1)
print("Second Tuple:", tuple2)

# Tuple Concatenation
result = tuple1 + tuple2
print("Concatenation:", result)

# Tuple Slicing
print("First Three Elements:", result[0:3])
print("Last Three Elements:", result[3:6])

# Tuple Unpacking
a, b, c = tuple1

print("Tuple Unpacking:")
print("a =", a)
print("b =", b)
print("c =", c)