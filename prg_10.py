"""
Write a Python program to calculate the length of a string.
"""

def calculate_string_length(input_string):
    length = len(input_string)
    return length


input_string = "Hello, python!"
length_of_string = calculate_string_length(input_string)
print(f"The length of the string '{input_string}' is {length_of_string}")
