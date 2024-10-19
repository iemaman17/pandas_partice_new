import numpy as np
import pandas as pd

a = pd.read_csv(r"C:\Users\NOA\Downloads\kohli_ipl.csv",index_col="match_no")
if len(a.columns) == 1:
    a = a.squeeze("columns")

print(a)

print(type(a))

print(a.head())
print(a.tail())
print(a.sample(5))

# values_count function

movies = pd.read_csv(r"C:\Users\NOA\Downloads\bollywood.csv",index_col="movie")

if len(movies.columns)==1:
    movies = movies.squeeze("columns")

print(movies.value_counts().head(1))

print(a.sort_values(ascending=False).head(1).values)

print(movies.sort_index())

sub = pd.read_csv(r"C:\Users\NOA\Downloads\subs.csv")

if len(sub.columns)==1:
    sub = sub.squeeze("columns")

print(sub.sum())
print(sub.mean())
print(sub.min())
print(sub.max())
print(sub.describe())




