"""
Write a Python program to count the number of characters (character
frequency) in a string
"""
def count_characters(input_string):
    
    char_frequency = {}

    
    for char in input_string:
        
        if char in char_frequency:
            char_frequency[char] += 1
        
        else:
            char_frequency[char] = 1

    return char_frequency


input_string = "Hello, World!"
frequency_dict = count_characters(input_string)


print(f"Character frequencies in '{input_string}':")
for char, count in frequency_dict.items():
    print(f"Character '{char}' occurs {count} times")
