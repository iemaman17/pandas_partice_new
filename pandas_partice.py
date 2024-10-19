import numpy as np
import pandas as pd

# adding the items in the Series 

state = {
    "Gujarat":"Gujarati",
    "Rajasthan":"Rajasthani",
    "Kerala":"Kanada"
}

state_lang = pd.Series(state)
state_lang["kerala"] = "Kanda & Telegu"

print(state_lang)

state_lang["haryana"] = "Haryanvi & Hindi"
print(state_lang)

state_lang["Gujarat":"Rajasthan"] = ["Gujarati & Hindi","Rajasthani & hindi"]
print(state_lang)





