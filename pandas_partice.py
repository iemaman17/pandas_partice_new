import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# taking out the rows in the dataframes 

students = {
    "Name":["Aman","jayesh","Ram",'Noa'],
    "Marks":[89,55,48,54],
    "Course":["Panda","Matplotlib","Java","AIML"],
    "IQ":[190,89,97,48]
}

s = pd.DataFrame(students)
s.set_index("Name",inplace=True)
print(s)

print(s.loc[["Aman","Noa"],["Marks","IQ"]])