name = 'Mohan'  # string/iterable

# iter() returns an iterator object
# it = iter(name)

# next() returns the next item of an iterator
# print(next(it))  # M
# print(next(it))  # o
# print(next(it))  # h
# print(next(it))  # a
# print(next(it))  # n
# print(next(it))  # StopIteration error

# custom iterator


def my_for(iterable, func):
    it = iter(iterable)
    while True:
        try:
            element = next(it)
        except StopIteration:
            break
        else:
            func(element)


def square(x):
    print(x * x)


my_for(name, print)
my_for([1, 2, 3, 4], square)

