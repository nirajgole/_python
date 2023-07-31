# access documention
print(print.__doc__)

# """ """ used to document a function


def sum_of_two_numbers(a, b):
    """
    This function will add two numbers
    :param a: first number
    :param b: second number
    :return: sum of two numbers
    """
    return a+b


print(sum_of_two_numbers.__doc__)
