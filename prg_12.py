"""
Write a Python program to count occurrences of a substring in a string.
"""
def count_substring_occurrences(main_string, substring):
    count = main_string.count(substring)
    return count


main_string = "hello, hello, how"
substring = "hello"

occurrences = count_substring_occurrences(main_string, substring)
print(f"The substring '{substring}' occurs {occurrences} times in the string.")
