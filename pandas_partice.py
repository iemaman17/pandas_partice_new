import numpy as np
import pandas as pd

# maing the dataframes using the list 
student_data = [
    ["Aman",17,"Pandas"],
    ["Noa",1,"PostgresQl"],
    ["Ram",3,"Java"],
    ["Jayesh",20,"Matplotlib"]
]

columns_data = ["Name","Fav_no","Cousre"]

a = pd.DataFrame(student_data,columns=columns_data,index=[1,2,3,4])

# making the dataframes uing the dictionaries 

country_info = {
    "Country":["USA","India","China","Russia"],
    "Militry_Rank":[1,4,3,2],
    "Population":["34 cr","140 Cr","130 Cr","14 Cr"],
    "Status":["Rich","Medium","Rich","Rich"]
}

b = pd.DataFrame(country_info)

# usually we imprt the data in real world

movies = pd.read_csv(r"C:\Users\NOA\Downloads\movies.csv")

ipl = pd.read_csv(r"C:\Users\NOA\Downloads\ipl-matches.csv")
