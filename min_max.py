#min: this function returns the minimum value in a list
print(min([1,2,3,4,5,6,7,8,9,10])) #list
print(min(1,-45,56,78,90)) #generator expression

#max: this function returns the maximum value in a list
print(max([1,2,3,4,5,6,7,8,9,10])) #list
print(max(1,-45,56,78,90)) #generator expression

#find longest string in a list
names=['hippopotamus','lion','tiger','elephant','giraffe','aligator','penguin']
longest_name=max(names,key=len)
print(longest_name)

#find a song with the longest duration
songs=[{'name':'song1','duration':3.5},{'name':'song2','duration':4.5},{'name':'song3','duration':5.5},{'name':'song4','duration':6.5}]
lengthy_song=max(songs,key=lambda x:x['duration'])['name']
print(lengthy_song)