# Check whether a string is a palindrome

text = input("Enter a string: ")

reverse = text[::-1]

print("Original String:", text)
print("Reversed String:", reverse)

if text == reverse:
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")