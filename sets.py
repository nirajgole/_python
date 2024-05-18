#
# *lighter than list and tuple*
# !Every item in a set is unique
# *No order is guaranteed (unordered)
# *Cannot access items by index(like list)

s = {1, 2, 2, 2, 2, 3.3, 4, 4, 4, 4, 5, 6, 7}
# print(s)

# *looping over a set
# for item in s:
#     print(item)

# list_with_duplicates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_without_duplicates = list(set(list_with_duplicates))
# print(list_without_duplicates)
s1 = {1, 2, 2, 3, 4, 4, 4, 3, 3, 2, 3, 3, }
print({x**2 for x in range(10)})
print({char.upper() for char in 'hello'})

# *Joining two sets
# ?UNION -  of set
print(s1.union(s))

# *union of sets operator (|)

print(f'union of sets: {s | s1}')

# ?INTERSECTION of set
print(s1.intersection(s))

# *intersection of set operator (&)
print(f'intersection of sets: {s&s1}')

# ?UPDATE set
# !need iterator object to be passed as argument to update set, for ex. list, set, tuple
s1.update({'abcd', 132})  # passing tuple as argument
print(s1)


# *difference between sets operator(-)
print(f'{s-s1}')

# *subset of sets operator(<)
s3 = {1, 2}
print(s3 < s1)  # is s3 subset of s1
print(s3 > s1)  # is s1 subset of s3

# * frozen set
frozen_set = frozenset({1, 2, 2, 3})
print(frozen_set)

# * ADD - elements in SET
s.add('🚗')
print(s)

# *REMOVE - elements from set
# !if element is not present, it will raise error
s.remove(1)
s.discard(2)
print(s)

# *LEN - number of elements in a set
print(len(s))
