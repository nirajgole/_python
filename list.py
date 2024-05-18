# fruits = ['banana', 'apple', 'mango', 'orange',
#           'kiwi', 'grapes', 'pear', 'watermelon']

# this line is suggested by copilot
fruits = ['🍌', '🍎', '🍊', '🍋', '🥝', '🍇', '🍐', ]

# *print list of fruits
# for fruit in fruits:
#     print(f'{fruit}\n')

# *check if a fruit is in the list
# isExist = '🍌' in fruits
# print(isExist)

# *negative index
# print(fruits[-1])
# print(fruits[-3])


# *len - length of the list
# print(len(fruits))

# range - exclusive of the last number in the range
# print(fruits[1:3])
# print(range(4, len(fruits)))
# for i in range(4, len(fruits)):
#     print(fruits[i])

# append - add only SINGLE to the list
# fruits.append('🥭')
# print(fruits)

# extend - add MULTIPLE elements to the end of the list
# fruits.extend(['🍓', '🍍'])
# print(fruits)

# insert - add element at a specific index
# fruits.insert(2, '🍉')
# print(fruits)

# clear - remove all elements from the list
# fruits.clear()
# print(fruits)

# pop - remove the last element from the list
# popped_fruit = fruits.pop()
# popped_fruit_at_index = fruits.pop(2)
# print({popped_fruit, popped_fruit_at_index})

# remove - remove the first element that matches the argument
# removed_fruit = fruits.remove('🍇')
# print({removed_fruit})  # doesn't capture the removed fruit

# index - returns the index of the first element that matches the argument
# index_of_fruit = fruits.index('🍋', 0)
# print(f'Index of 🍋: {index_of_fruit}')

# count - returns the count of elements that match the argument
# count_of_bananas = fruits.count('🍌')
# print(f'Count of 🍌: {count_of_bananas}')

# reverse - reverse the order of the list
# fruits.reverse()  # it mutates the list and makes it reversed
# print(fruits)

# sort - sort the list
# fruits.sort()
# it mutates the list and makes it sorted in ascending order
# for ex. string values will be sorted alphabetically
# print(fruits)

# *join - join the list elements into a string
# print('--'.join(fruits))

# *slice - returns a new list with the elements from the specified range
# [start:stop:step]
# print(fruits[1:3])
# print(fruits[::2])
# print(fruits[::-1])  # reverse the list
# print(fruits[::-2])  # reverse the list and skip every other element
# fruits[1:3] = ['🍉,', '🥭']  # replace the elements in the range
# print(fruits)
# sliced_and_reversed_list = fruits[0:5][::-1]
# print(sliced_and_reversed_list)

# *swapping two elements in the list
# fruits[0], fruits[1] = fruits[1], fruits[0]
# print(fruits)

# *LIST COMPREHENSION
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print([i*10 for i in nums])
# print([num/2 for num in (range(1, 6))])
# print([num*5 if num % 2 == 0 else num/5 for num in nums])

# characters = 'This is so simple'
# print([char for char in characters])
# print(''.join([char for char in characters if char not in 'aeiou']))

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print(num) for num in nested_list[i]] for i in range(len(nested_list))]
