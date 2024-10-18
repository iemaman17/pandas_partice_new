import numpy as np
import pandas as pd

#series attributes 

country = ["india","nepal","England","usa","russia"]

nums = [1,2,3,4,5,6,9,1,4]

a = pd.Series(country,name="Countries Name")
b = pd.Series(nums,name="Numbers")
print(a.size) # this is for the size of ur series

print(a.dtype) # this is for data type of ur series

print(a.name) # this will give the name which u given to the series 

print(a.is_unique) # True because no dupliactes in it 
print(b.is_unique) # False because  dupliactes in it 

print(a.index) # this will give the indexs

marks = {
    "maths":89,
    "science":98,
    "english":58
}

sub_marks = pd.Series(marks,name="Noa's Marks")

for i in sub_marks.index:
    print(i) # means i use the series index which is key to print in th line wise 
    
for i in sub_marks.values:
    print(i)# means i use the series index which is values to print in th line wise 

for i,a in sub_marks.items():
    print(f"{i}={a}")