#
# # !Tuples are immutable
# ?Makes code safer and easier to read
# ?Tuples are faster than lists
# ?Usuall used for data that is not going to be changed
# ?dict.items() returns a list of tuples because list item are never going to be changed

calendar_months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

# *Can be use as key in dictionary
# locations = {
#     (35.6895, 39.6917): "Tokyo Office",
#     (40.7128, 74.0060): "New York Office",
#     (37.7749, 122.4194): "San Francisco Office",
# }

# print(locations[(40.7128, 74.0060)])

# *looping over a tuple
# for month in calendar_months:
#     print(month)

# for i in range(len(calendar_months)):
#     print(i+1, calendar_months[i])

# *count() returns the number of times a value appears in a tuple
# month_count = calendar_months.count('Jan')
# print(month_count)

# *index() returns the index of the first item found in a tuple
# month_index = calendar_months.index('Sep')
# print(month_index)

# *Nested tuples
nested_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# *slicing in tuples
nested_tuples_slice = nested_tuples[1:3]
print(nested_tuples_slice)