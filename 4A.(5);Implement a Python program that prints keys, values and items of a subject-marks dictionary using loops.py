# Creating a subject-marks dictionary
subjects = {
    "Python": 90,
    "Java": 85,
    "C": 80,
    "HTML": 95,
    "DBMS": 88
}

# Printing keys
print("Subject Names:")
for key in subjects.keys():
    print(key)

# Printing values
print("\nSubject Marks:")
for value in subjects.values():
    print(value)

# Printing items
print("\nSubject Names and Marks:")
for key, value in subjects.items():
    print(key, ":", value)