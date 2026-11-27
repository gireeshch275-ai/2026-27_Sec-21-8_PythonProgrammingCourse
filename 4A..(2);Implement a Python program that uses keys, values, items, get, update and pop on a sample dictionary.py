# Creating a sample dictionary
student = {
    "name": "Gireesh",
    "age": 18,
    "course": "B.Tech"
}

# Using keys()
print("Keys:", student.keys())

# Using values()
print("Values:", student.values())

# Using items()
print("Items:", student.items())

# Using get()
print("Name:", student.get("name"))

# Using update()
student.update({"age": 19})
print("After update:", student)

# Using pop()
student.pop("course")
print("After pop:", student)