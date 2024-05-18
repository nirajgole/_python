def current_beat():
    """
    This is a generator function that yields the current beat
    """
    nums = (1, 2, 3, 4, 5)
    i = 0
    while True:
        if i >= len(nums):
            i = 0
        yield nums[i]
        i += 1


current = current_beat()
print(next(current))
print(next(current))
print(next(current))
print(next(current))
print(next(current))
print(next(current))


# Generator functions are a way to create iterators.

# write a program that will return first 1000000 fibonacci numbers
# !WARNING 🔴🔴🔴 terminal may crash if you run this code 🔴🔴🔴

# function
#!following code will eat up significant amount of memory
# def fibonacci(max):
#     nums=[]
#     a,b=0,1
#     while len(nums) < max:
#         nums.append(a)
#         a,b=b,a+b
#     return nums

# for i in fibonacci(1000):
#     print(i)


# generator function
# * As compared to above function, this function will not eat up memory
def fibonacci_generator(max):
    a, b = 0, 1
    count = 0
    while count < max:
        a, b = b, a+b
        yield a
        count += 1


for i in fibonacci_generator(10000):
    print(i)
