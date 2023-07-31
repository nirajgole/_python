#Python Error Types
# 1.Syntax Error
# 2.Name Error
# 3.Value Error
# 4.Index Error
# 5.Type Error
# 6.Key Error
# 7.Attribute Error

# foobar # this line will throw name error

#Raise error
# raise ValueError('This is value error info.') #this line will throw error and next line(s) won't execute

#Example
def sum_of_two(a,b):
    if type(a) or type(b) is not int:
        # raise TypeError # throwing error without description
        raise TypeError('Please enter valid integer.')
    return a+b

sum_of_two('10',45) # this line will throw error for type