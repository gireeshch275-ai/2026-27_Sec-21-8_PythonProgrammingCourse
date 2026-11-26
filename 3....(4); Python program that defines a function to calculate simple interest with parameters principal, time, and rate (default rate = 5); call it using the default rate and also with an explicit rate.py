# Function to calculate simple interest

def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

# Get principal and time from the user
p = float(input("Enter Principal Amount: "))
t = float(input("Enter Time in Years: "))

# Function call using default rate
result1 = simple_interest(p, t)
print("Simple Interest with Default Rate (5%):", result1)

# Get rate from the user
r = float(input("Enter Rate of Interest: "))

# Function call using explicit rate
result2 = simple_interest(p, t, r)
print("Simple Interest with Given Rate:", result2)