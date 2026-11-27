# Creating a nested dictionary
students = {
    1: {"name": "Anil", "marks": 85},
    2: {"name": "Bhavana", "marks": 92},
    3: {"name": "Charan", "marks": 78},
    4: {"name": "Divya", "marks": 90}
}

# Printing student names and marks
print("Student Details:")

for student in students.values():
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print()