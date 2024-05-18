def add(a, b):
    """
    >>> add(2, 3)
    5
    >>> add(100, 200)
    300
    """
    # return a * b #for this doctest will fail
    return a * b #for this doctest will success


print(add(2, 3))
print(add(100, 200))

# doctest.testmod()
# *Enter below code in the console
# py -m doctest -v doc_test.py
