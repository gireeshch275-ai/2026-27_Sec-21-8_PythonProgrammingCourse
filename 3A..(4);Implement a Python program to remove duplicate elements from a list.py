# Remove duplicate elements from a list

numbers = [10, 20, 30, 20, 40, 10, 50, 30]

print("Original List:", numbers)

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List after removing duplicates:", unique_numbers)