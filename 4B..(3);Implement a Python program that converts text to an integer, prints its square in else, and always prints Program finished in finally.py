try:
    text = input("Enter a number: ")
    num = int(text)

except ValueError:
    print("Error: Please enter a valid integer.")

else:
    square = num * num
    print("Square:", square)

finally:
    print("Program finished")