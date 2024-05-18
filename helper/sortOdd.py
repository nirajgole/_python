# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 09:56:06 2020

@author: niraj
"""



numberList =[5,3,2,8,3,4,1]

oddlist=[]
for x in numberList:
    if x&1!=0:
        oddlist.append(x)

oddlist.sort()

# for (index, replacement) in zip(indexes, replacements):
#     to_modify[index] = replacement


for (i,x) in zip(numberList,oddlist):
    if i%2!=0:
        i=x


print(numberList)