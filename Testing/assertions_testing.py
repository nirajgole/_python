def add_positive_numbers(a, b):
    """
    Add two positive numbers together.
    """
    assert a > 0 and b > 0, "Both numbers must be positive."
    return a + b


print(add_positive_numbers(1, 2)) # 3
print(add_positive_numbers(1, -2)) # AssertionError: Both numbers must be positive.

