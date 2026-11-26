# Display student details using **kwargs

def student_details(**kwargs):
    print("Student Details:")

    for key, value in kwargs.items():
        print(key, ":", value)

# Function call
student_details(
    name="Krishna",
    Python=85,
    Java=90,
    Mathematics=95
)