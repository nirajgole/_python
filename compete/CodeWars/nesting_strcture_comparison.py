# my solution
# def get_length(arr):
#     return [get_length(i)if isinstance(i, list) else 'K' for i in arr]

# def same_structure_as(original, other):
#     if(isinstance(original, list) and isinstance(other, list)):
#         return get_length(original) == get_length(other)
#     else:
#         return False

# solution from codewars
# def same_structure_as(original, other):
#     if type(original) == list == type(other):
#         return len(original) == len(other) and all(map(same_structure_as, original, other))
#     else:
#         return type(original) != list != type(other)


# solution from codewars
def same_structure_as(original, other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2):
                return False
        else:
            return True
    else:
        return not isinstance(original, list) and not isinstance(other, list)


# should return True
same_structure_as([1, '[', ']'], ['[', ']', 1])

# # should return True
# same_structure_as([1, 1, -1], [2, 2, 2])

# # should return True
# same_structure_as([1, 1, 1], [2, 2, 2])
# same_structure_as([1, [1, 1]], [2, [2, 2]])

# # should return False
same_structure_as([1, [1, 1]], [[2, 2], 2])
same_structure_as([1, [1, 1]], [[2], 2])

# # should return True
same_structure_as([[[], []]], [[[], []]])

# # should return False
same_structure_as([[[], []]], [[1, 1]])

# should return False
same_structure_as([], 1)

# a_string = str([1, 2, 3, -4, 5, 6, -7, 8, 9, 10])
# new_string = re.sub("-?\d+", "K", a_string)
# print(new_string)


print(list(zip([1, 2, 3], [4, 5, 6])))