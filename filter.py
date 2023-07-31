# filter: filters out the elements based on true or false that are not in the list

# *filter even numbers
# nums=[1,2,3,4,5,6,7,8,9,10]
# even_nums=filter(lambda x: x%2==0, nums)
# print(list(even_nums))

#  *#filter names that start with 'a'
# names=['adam','bob','alice','bob','carol','arthur']
# names_starts_with_a=list(filter(lambda x: x[0]=='a', names))
# print(names_starts_with_a)

# *find out people who are older than 18
people = [{'name': 'adam', 'age': 16}, {'name': 'bob', 'age': 31}, {
    'name': 'alice', 'age': 19}, {'name': 'carol', 'age': 17}, {'name': 'arthur', 'age': 13}]
# adults=list(filter(lambda x:x['age'] >= 18, people))
# print(adults)

# *chaining map and filter
# getting only name of people who are older than 18
# adults=list(map(lambda x:x['name'],filter(lambda x:x['age'] >= 18, people)))
# print(adults)

# *alternative way
adults = [x['name'] for x in people if x['age'] >= 18]
print(adults)
