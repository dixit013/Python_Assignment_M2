"""

Write a Python program to get the Fibonacci series of given range.

"""


def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    while a <= n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

range_limit = 50
fib_series = fibonacci_series(range_limit)

print(f"Fibonacci series up to {range_limit}:")
print(fib_series)
