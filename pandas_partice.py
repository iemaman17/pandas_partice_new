import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# taking out the single columns from the dataframe

movies = pd.read_csv(r"C:\Users\NOA\Downloads\movies.csv")
print(movies)

a = movies["title_x"] 
print(a.head())

# taking out the more than one columns from the dataframe

b = movies[["title_x","release_date","year_of_release"]]
print(b.sample(3))