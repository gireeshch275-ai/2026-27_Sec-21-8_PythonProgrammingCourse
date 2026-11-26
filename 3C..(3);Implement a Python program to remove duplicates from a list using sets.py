# Remove duplicates from a list using sets

numbers = [10, 20, 30, 20, 40, 10, 50, 30]

print("Original List:", numbers)

# Convert list into a set
unique_numbers = set(numbers)

# Convert set back into a list
result = list(unique_numbers)

print("List after removing duplicates:", result)