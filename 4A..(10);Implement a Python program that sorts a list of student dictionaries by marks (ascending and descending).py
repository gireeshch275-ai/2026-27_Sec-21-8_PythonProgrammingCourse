# Creating a list of student dictionaries
students = [
    {"name": "Anil", "marks": 85},
    {"name": "Bhavana", "marks": 92},
    {"name": "Charan", "marks": 78},
    {"name": "Divya", "marks": 95}
]

# Sorting in ascending order
ascending = sorted(students, key=lambda x: x["marks"])

print("Ascending Order:")
for student in ascending:
    print(student)

# Sorting in descending order
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("\nDescending Order:")
for student in descending:
    print(student)