"""
Write python program that swap two number with temp variable and
without temp variable.

"""

#without temp variable

def swap_without_temp(a, b):
    print(f"Before swapping: a = {a}, b = {b}")

    
    a = a + b
    b = a - b
    a = a - b
    
    print(f"After swapping: a = {a}, b = {b}")

num1 = 5
num2 = 10
swap_without_temp(num1, num2)
