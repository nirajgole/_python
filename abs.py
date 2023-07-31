#abs: function that returns the absolute value of a number
#i.e. if the number is negative, it returns the positive value
from math import floor


print(abs(-5))
print(abs(5))
print(abs(0))
print(abs(5.5))
print(abs(-5.5))
print(abs(5+3j))
print(abs(-5+3j))
print(abs(float(-5)))

import math
#fabs: function that floors and then returns absolute value of a number
print(math.fabs(-10))
