import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ploting the graphs in the series 

runs = pd.read_csv(r"C:\Users\NOA\Downloads\kohli_ipl.csv",index_col="match_no")

if len(runs.columns)==1:
    runs = runs.squeeze("columns")

#runs[runs>80].plot()
#print(plt.show())

movie = pd.read_csv(r"C:\Users\NOA\Downloads\bollywood.csv",index_col="movie")

if len(movie.columns)==1:
    movie =movie.squeeze("columns")

a = movie.value_counts()
a = a[a>15]
print(a)

a.plot(kind="pie")
print(plt.show())
