# create screan
import random
from turtle import Turtle , Screen
import pandas as pd

#constants
df = pd.read_csv("./50_states.csv")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
guessed = []

#func
def w(df,user):
    t = Turtle()
    t.penup()
    t.color(random.choice(colours))
    x = int(df["x"].loc[df["state"]== user])
    y = int(df["y"].loc[df["state"]== user])
    t.goto(x,y)
    t.write(f"{user}")



#screan
s = Screen()
s.bgpic("./blank_states_img.gif")




#turtle
app_on = True
user = s.textinput("state", "Enter state name").title()
while app_on:

    if user == "Exit":
        break
    elif user in guessed:
        user = s.textinput("try again , you already wrote it", "Enter state name").title()
        w(df, user)

    elif user in list(df["state"]):
        w(df, user)
        guessed.append(user)




    else :
        user = s.textinput("try again", "Enter state name").title()


s.exitonclick()