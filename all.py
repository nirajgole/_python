#all: It is built in function
# #!return True if all the elements in the list are true

# #Example 1:
# print(all([True, True, True]))
# print(all([0,12,3,4,5]))


def increment_string(strng):
    intrl=''
    strl=''
    for i in strng:
        if i.isdigit():
            intrl+=i
        else:
            strl+=i

    return f'{strl}{intrl}'

increment_string('foobar001')