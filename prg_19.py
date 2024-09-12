"""
Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string.
"""
def extract_chars(s):
    # Check if the length of the string is less than 2
    if len(s) < 2:
        return ''
    # Extract the first 2 and last 2 characters
    first_two = s[:2]
    last_two = s[-2:]
    # Concatenate and return the result
    return first_two + last_two


input_string = input("Enter a string: ")
result = extract_chars(input_string)
print("Result:", result)
