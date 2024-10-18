import numpy as np
import pandas as pd

#using the pandas with the list ds of python with series ds of pandas

#name = ["Aman","Ram","Noa","Ganesh"]

#print(pd.Series(name))

#example of months 

#months =["jan","feb","march","april","may","june,","july","august","sep","oct","nov","dec"]

#print(pd.Series(months))

# using the index 

runs = [59,32,30,88]
batsman = ['Rohit',"Virat","Hardik","Rinku"]

batsman_info = pd.Series(runs,index=batsman,name="Every Batsman runs ")

print(batsman_info)