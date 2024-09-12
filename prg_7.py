"""
Write a Python program to test whether a passed letter is a vowel or
not.

"""

def is_vowel(letter):
    vowels = "aeiouAEIOU"
    return letter in vowels

letter_to_check = input("Enter a letter: ")

if len(letter_to_check) == 1 and letter_to_check.isalpha():
    if is_vowel(letter_to_check):
        print(f"The letter '{letter_to_check}' is a vowel.")
    else:
        print(f"The letter '{letter_to_check}' is not a vowel.")
else:
    print("Please enter a single alphabetical character.")
