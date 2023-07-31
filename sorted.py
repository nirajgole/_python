#Sorted: function that sorts a list,tuples,dictionaries
print(sorted([1,2,3,4,5,6,7,8,9,10]))
print(sorted([10,1,2,45,8,-4,23.56],reverse=True))
print(sorted(['a','b','c','d','e','f','g','h','i','j']))


users=[{'name':'John','age':30},{'name':'Bob','age':25},{'name':'Sam','age':40},{'name':'Sara','age':35}]
#arrange the users by name in ascending order

sorted_by_name=sorted(users,key=lambda x:x['name'])
print(sorted_by_name)