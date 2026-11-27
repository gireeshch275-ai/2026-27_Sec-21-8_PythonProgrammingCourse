# Creating two dictionaries
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"d": 40, "e": 50}

# Creating a copy of the first dictionary
merged_dict = dict1.copy()

# Merging the second dictionary
merged_dict.update(dict2)

# Printing the dictionaries
print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged_dict)