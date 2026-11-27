# Global bank balance
balance = 1000

# Function to deposit money
def deposit(amount):
    global balance
    balance = balance + amount
    print("Amount deposited:", amount)
    print("Updated balance:", balance)

# Function using a local balance
def local_balance():
    balance = 500
    print("Local balance:", balance)

# Display initial balance
print("Initial bank balance:", balance)

# Deposit money
deposit(500)

# Display local balance
local_balance()

# Display actual bank balance
print("Final bank balance:", balance)