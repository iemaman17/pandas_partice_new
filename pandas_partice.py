import numpy as np
import pandas as pd


# using the csv files

a = pd.read_csv(r"C:\Users\NOA\Downloads\subs.csv")

if len(a.columns) == 1:
    a = a.squeeze("columns")
print(a)
print(type(a))

b = pd.read_csv(r"C:\Users\NOA\Downloads\kohli_ipl.csv",index_col="match_no")

if len(b.columns) ==1:
    b = b.squeeze("columns")

print(b)

c = pd.read_csv(r"C:\Users\NOA\Downloads\bollywood.csv",index_col="movie")

if len(c.columns) ==1:
    c= c.squeeze("columns")

print(c)

