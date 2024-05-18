#
# *Simple Decorator
# def be_polite(fn):
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")
#     return wrapper


# @be_polite
# def greet():
#     print("Hey Mister, how are you doing?")


# @be_polite
# def rage():
#     print("Haaahaha, your RAGED!")


# greet()
# rage()


# * Decorator with arguments and keyword arguments
# def shout(fn):
#     def wrapper(*args, **kwargs):
#         return fn(*args, **kwargs).upper()
#     return wrapper


# @shout
# def greet(name):
#     return f"Hi, I'm {name}"


# @shout
# def order(main, side):
#     return f"Hi, I'd like the {main}, with a side of {side}, please."


# @shout
# def lol():
#     return "lol"


# print(greet("Mike"))
# print(order("burger", "fries"))
# print(order(main="pizza", side="patty"))
# print(lol())


# *Maintaining the Metadata for a Decorator
# MetaData is nothing but the information about the function that is being decorated.
# from functools import wraps

# def log_function_data(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         print(f"You are calling {fn.__name__}")
#         print(f"You are passing {args} and {kwargs}")
#         print(
#             f"You have defined the function {fn.__name__} in {fn.__module__}")
#         return fn(*args, **kwargs)
#     return wrapper


# @log_function_data
# def add(x, y):
#     # following line is metadata
#     """Adds two numbers together"""
#     return x + y


# print(add.__doc__)
# print(add.__name__)
# print(add)

# * Speed Test
from time import time
from functools import wraps

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Execution time: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums_gen(num):
    return sum(x for x in range(num))

@speed_test
def sum_nums_list(num):
    return sum([x for x in range(num)])

#!Warning: Hardware Resource intensive, may take a while to run if num is large
print(sum_nums_gen(90000000))
print(sum_nums_list(90000000))
