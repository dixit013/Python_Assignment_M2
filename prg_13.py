"""
Write a Python program to count the occurrences of each word in a
given sentence
"""
def count_word_occurrences(sentence):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in sentence:
        if char in punctuation:
            sentence = sentence.replace(char, "")

    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Split the sentence into words
    words = sentence.split()

    # Initialize an empty dictionary to store word counts
    word_count = {}

    # Count the occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Print the word counts
    for word, count in word_count.items():
        print(f"{word}: {count}")
        
sentence = "Hello world and hello universe, hello again."
count_word_occurrences(sentence)
