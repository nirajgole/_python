#Generator Expressions
#Generator expressions are a way to create iterators.
#Syntactically they are written as a function call with a for loop.
import sys
#Here we are checking memory size of the system using sys.getsizeof
list_comp=sys.getsizeof([x * 10 for x in range(1000)])
generator_expression=sys.getsizeof(x * 10 for x in range(1000))

print(f'List Comprehension: {list_comp}')
print(f'Generator Expression: {generator_expression}')