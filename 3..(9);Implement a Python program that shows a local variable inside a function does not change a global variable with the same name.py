# Global Variable
x = 100

def display():
    # Local Variable
    x = 50
    print("Local Variable:", x)

# Display global variable
print("Global Variable before function call:", x)

# Function call
display()

# Display global variable again
print("Global Variable after function call:", x)