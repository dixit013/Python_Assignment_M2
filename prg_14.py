"""

Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.

"""
def swap_first_two_chars(s1, s2):
    if len(s1) < 2 or len(s2) < 2:
        return "Both strings must have at least two characters."

    new_s1 = s2[:2] + s1[2:]
    new_s2 = s1[:2] + s2[2:]

    result = new_s1 + ' ' + new_s2
    return result

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

print(swap_first_two_chars(string1, string2))
