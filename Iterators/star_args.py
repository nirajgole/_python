#
# * (*args) is a parameter that accepts any number of arguments and stores them in a tuple

#we passed *args as a parameter to the function which will store the arguments in a tuple

#Example 1
# sum_all_numbers = lambda *args: sum(args)
# print(sum_all_numbers(1, 2, 3, 4, 5))

#Example 2
# sum_all_numbers = lambda param1,*args: f'{param1}: {sum(args)}'
# print(sum_all_numbers('Total',1, 2, 3, 4, 5))

#Example 3
# sum_all_numbers = lambda **args: "".join([f' जय श्री {value}\n' for key, value in args.items()])
# print(sum_all_numbers(name2='Ram', name3='Lakshman', name4='Sita' , name5='Hanuman'))

# *Parameter Ordering
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs

# def display_info(a, b, *args, instructor='Colt', **kwargs):
#     return [a, b, args, instructor, kwargs]
# print(display_info(1,2,45,67,name='John',age=23))

# *Tuple Unpacking
# !The * operator unpacks the tuple into positional arguments
# def sum_of_all_sums(*args):
#     return sum(args)
# nums=(1,2,3,4,5)
# print(sum_of_all_sums(*nums))

# **Dictionary Unpacking
# !The ** operator unpacks the dictionary into keyword arguments
def sum_of_all_sums(**args):
    print({**args})
    return sum(args.values())
nums={'a':1,'b':2,'c':3,'d':4,'e':5}
print(sum_of_all_sums(**nums))

