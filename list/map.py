# make doubles
nums = [1, 2, 3, 4, 5]

# *map takes arguments function, iterable -> map(function,iterable)
# using function
# def double(num):
#     return num*2
# doubles=map(double,nums)

# using lambda
# doubles = map(lambda x: x*2, nums)

# #iterate over map object
# for i in doubles:
#     print(i, end=' ')

# *add two lists elements into each other
list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3]
addition_of_two = map(lambda x, y: x+y, list_1, list_2)
print(tuple(addition_of_two))
