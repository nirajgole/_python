#module - random
# *importing standard library
# import random
# print(random.choice(['apple', 'pear', 'banana']))
# print(random.randint(5, 20))

# *import module as alias
# import random as rand
# print(rand.choice(['apple', 'pear', 'banana']))
# print(rand.randint(5, 20))

# *importing from module and alias methods
from random import choice as selected, randint as random_int
print(selected(['apple', 'pear', 'banana']))
print(random_int(5, 20))

# * using keyword form to extract module individual methods
# from random import choice, randint
# print(choice(['apple', 'pear', 'banana']))
# print(randint(5, 20))

# * import all methods from module
# from random import *
