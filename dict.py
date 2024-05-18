# first way to create a dictionary
employee = {'image': '👨‍💼', 'name': 'John', 'age': 25, 'salary': 5000}
# second way to create a dictionary
person = dict(image='🧔', name='Mark', age=25, salary=5000)

# *extracting values from a dictionary
# print(employee['name'])
# print(person['image'])

# !while looping over dictionary, there is no guarantee that the order of the keys will be the same
# *accessing all values from a dictionary
# ? value() method returns a list of values
# print(employee.values())
# for value in employee.values():
#     print(value, end=' ')

# *accessing all keys and values from a dictionary
# ? items() method returns a list of tuples (key, value)
# for item in employee.items():
#     print(item)

# for key, value in employee.items():
#     print(key, value)

# *check if a key exists in a dictionary
# ? keys() method returns a list of keys
# print('name' in employee)  # True
# print('phone' in employee)  # False
# print('phone' in employee.keys())  # False

# *check if a value exists in a dictionary
# print(5000 in employee.values())  # True
# print(30 in employee.values())  # False

# *clear all the keys and values from a dictionary
# ?clear() method removes all the keys and values from a dictionary
# !mutates the original dictionary
# employee.clear()
# print(employee)

# * copy a dictionary
# !copy() - shallow copy, deepCopy() - deep copy
# person_clone = person.copy()
# print(person_clone == person)  # True as this only checks if values are equal
# False as this checks if the reference is the same
# print(person_clone is person)

# *fromkeys() method creates a dictionary with the specified keys and values
# !usually used to create default values for a dictionary
# new_person = {}.fromkeys(['name', 'age', 'salary'], 'unknown')
# new_person.fromkeys(['age'], '50')
# new_person.fromkeys(['location'], 'here')
# new_person['name'] = 'John'

# *get() method returns the value of the specified key
# !return None if the key does not exist
# nameKey = new_person.get('name')
# print(new_person, nameKey)

# *pop() method removes the specified key and returns its value
# popped_key = {'a': '1', 'b': 23}.pop('a')
# print(popped_key)

# *popitem() method removes the last inserted key and returns its value
# popped_item = {'a': '1', 'b': 23}.popitem()
# print(popped_item)

# *update() method updates the dictionary with the specified key and value
# person_item = dict(name='John', age=23, department='IT')

# person_item.update(name='Mark', age=25, salary=5000)
# print(person_item)

# * {_:_ for _ in {}}
# example_1 = {key: value**2 for key,
#              value in dict(first=1, second=2, third=3).items()}
# print(example_1)

# example_2 = {num: num**2 for num in range(1, 6)}
# print(example_2)

# str1='ABC'
# str2='123'

# example_3 = {str1[i]: str2[i] for i in range(0,len(str1))}
# print(example_3)

# *conditional logic in dictionaries
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# example_4 = {num: 'even' if num % 2 == 0 else 'odd' for num in num_list}
# print(example_4.items())

# example_5 = {(k if k%2==0 else 'k'):v for k, v in example_4.items()}
# print(example_5)

