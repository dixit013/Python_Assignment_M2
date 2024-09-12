"""
Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero

"""

def sum_of_three_integers(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c


num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

result = sum_of_three_integers(num1, num2, num3)
print(f"Sum of {num1}, {num2}, and {num3} is {result}")
