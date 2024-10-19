import numpy as np
import pandas as pd

# series with the python functionalities 

runs = pd.read_csv(r"C:\Users\NOA\Downloads\kohli_ipl.csv",index_col="match_no")

if len(runs.columns)==1:
    runs =runs.squeeze("columns")

#for m,s in runs.items():
    #if s>50:
       # count+=1
        #print(f'{m} ={s}')


movie = pd.read_csv(r"C:\Users\NOA\Downloads\bollywood.csv",index_col="movie")

if len(movie.columns)==1:
    movie =movie.squeeze("columns")

a = movie.value_counts()
a = a[a>20]

print(a)