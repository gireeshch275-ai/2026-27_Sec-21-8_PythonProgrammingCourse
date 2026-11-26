# String Methods

text = "  Hello Python Programming  "

# upper()
print("Uppercase:", text.upper())

# lower()
print("Lowercase:", text.lower())

# strip()
print("Strip:", text.strip())

# split()
words = text.split()
print("Split:", words)

# join()
result = "-".join(words)
print("Join:", result)

# replace()
new_text = text.replace("Python", "Java")
print("Replace:", new_text)

# find()
position = text.find("Python")
print("Find:", position)