"""
Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string

"""

def replace_not_poor_with_good(s):
    poor_index = s.find('poor')
    
    if poor_index == -1:
        return s
    
    not_index = s.find('not', poor_index)
    
    if not_index == -1 or not_index < poor_index:
        return s
    
    return s[:poor_index] + 'good' + s[not_index + len('not'):]


input_string = "The weather is not poor, but it will be better."
result = replace_not_poor_with_good(input_string)
print(result)
