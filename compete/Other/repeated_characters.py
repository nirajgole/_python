from numpy import sort


print('Hello Word')

def repeated_characters(s):
    temp=set(s)
    return [i for i in temp if s.count(i)>1]

print(repeated_characters('aabbcdf'))