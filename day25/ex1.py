import pandas as pd
import numpy as np
file = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

list= ['Gray' ,'Cinnamon' ,'Black']
list_count = []
df = pd.DataFrame({"color": [], "count" : []})
for i in list:
    c = file['Primary Fur Color'][file['Primary Fur Color'] == i ]
    df.loc[len(df.index)] = (i, c.count())

df.to_csv("./df.csv")

