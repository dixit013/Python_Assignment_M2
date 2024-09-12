"""
Write python program that swap two number with temp variable and
without temp variable.


"""

#with temp variable

def swap_with_temp(a, b):
    print(f"Before swapping: a = {a}, b = {b}")

    
    temp = a
    a = b
    b = temp
    
    print(f"After swapping: a = {a}, b = {b}")

num1 = 5
num2 = 10
swap_with_temp(num1, num2)




