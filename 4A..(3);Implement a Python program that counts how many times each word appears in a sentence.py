# Getting a sentence from the user
sentence = input("Enter a sentence: ")

# Splitting the sentence into words
words = sentence.split()

# Creating an empty dictionary
word_count = {}

# Counting each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Displaying the word counts
print("Word Frequency:")
for word, count in word_count.items():
    print(word, ":", count)