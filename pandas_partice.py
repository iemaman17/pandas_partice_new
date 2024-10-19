import numpy as np
import pandas as pd

# series with the python functionalities 

runs = pd.read_csv(r"C:\Users\NOA\Downloads\kohli_ipl.csv",index_col="match_no")

if len(runs.columns)==1:
    runs =runs.squeeze("columns")

print(len(runs))
print(max(runs))
print(min(runs))
print(sum(runs))
print(runs.mean())

series_into_list = list(runs)
print(series_into_list)

movie = pd.read_csv(r"C:\Users\NOA\Downloads\bollywood.csv",index_col="movie")

if len(movie.columns)==1:
    movie = movie.squeeze("columns")

print(movie.sample(3)) 

if 'Pihu' in movie:
    print("Yes")
else:
    print('no')

print("Delhi Safari" in movie.index)

print("Tusshar Kapoor" in movie.index) # will give false because i am seraching in the index and this value is the value in the movie 
# and also the by default in operator serach the index in the itration so if we have to find any value so we have use the values method in the series 


print("Tusshar Kapoor" in movie.values)

# using the maths 

marks = {
    "maths": 98,
    "english":57,
    "Hindi":69,
    "sst":78
}

sub_marks = pd.Series(marks,name="Noa's Marks in particular subjects!!")

for s,m in sub_marks.items():
    print(f"{s} = {m} = lost marks {100-m}")

for s,m in sub_marks.items():
    if 70 < m <100:
        print(f"{s} = {m} = lost marks {100-m}")



