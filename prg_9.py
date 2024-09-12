"""
Write a python program to sum of the first n positive integers
"""

def sum_first_n_integers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


n = 7
result = sum_first_n_integers(n)
print(f"The sum of the first {n} positive integers is: {result}")
