# Write a code to accept dictionary values from user and print the sum of values
print('Dictionary elements should be in format of key-value pair')

user_dict = {}

while True:
    isExit = input('Add item to dictionary? y/n : ')
    if str(isExit) == 'n':
        break
    user_input_key = input('Key:')
    user_input_value = input('Value:')
    # *TO-DO: raise exception if user_input is not a number
    user_dict[user_input_key] = user_input_value

print(user_dict)
dict_sum = sum(int(v) for _, v in user_dict.items())
print(f'Sum of dictionary values: {dict_sum}')
