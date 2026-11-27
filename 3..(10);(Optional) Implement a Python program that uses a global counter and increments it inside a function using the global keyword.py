# Global Counter
count = 0

# Function to increment the counter
def increment():
    global count
    count = count + 1
    print("Counter:", count)

# Function calls
increment()
increment()
increment()
increment()