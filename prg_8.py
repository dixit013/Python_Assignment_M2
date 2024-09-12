"""
Write a Python program that will return true if the two given integer
values are equal or their sum or difference is 5.
"""
def check_integer_condition(a, b):
    if a == b:
        return True
    elif abs(a - b) == 5:
        return True
    elif a + b == 5:
        return True
    else:
        return False


print(check_integer_condition(2, 7))   
print(check_integer_condition(2, 3))   
print(check_integer_condition(2, 7))   
print(check_integer_condition(2, -3))  
print(check_integer_condition(5, 0))   
print(check_integer_condition(7, 2))   
print(check_integer_condition(5, 10))  
