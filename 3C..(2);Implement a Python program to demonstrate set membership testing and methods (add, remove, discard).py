# Set Membership Testing and Methods

# Create a set
numbers = {10, 20, 30, 40, 50}

print("Original Set:", numbers)

# Membership Testing
print("Is 20 present?", 20 in numbers)
print("Is 60 present?", 60 in numbers)

# Add an element
numbers.add(60)
print("After Add:", numbers)

# Remove an element
numbers.remove(30)
print("After Remove:", numbers)

# Discard an element
numbers.discard(40)
print("After Discard:", numbers)