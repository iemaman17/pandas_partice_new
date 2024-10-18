import numpy as np
import pandas as pd

#series with the dictionaries 

marks = {
    "maths": 100,
    "English":80,
    "science":85,
    "hindi":70
}

marks_series = pd.Series(marks,name="Subject wise Marks")

#in the dictionary we dont have to give the index its auotmatically take keys as index 

print(marks_series)