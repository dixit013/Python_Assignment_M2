"""
Write a Python function to insert a string in the middle of a string.
"""
def insert_in_middle(original, to_insert):
    middle_index = len(original) // 2
    new_string = original[:middle_index] + to_insert + original[middle_index:]
    return new_string


original_string = "abcdefgh"
string_to_insert = "1234"
result = insert_in_middle(original_string, string_to_insert)
print(result)  
