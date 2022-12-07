from turtle import Turtle , Screen
import random
from turtle import colormode
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
colormode(255)
def random_co():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    tup = (r,g,b)
    return tup



t1 = Turtle()


dirc = [0, 90, 180, 270]
for _ in range(200):
     t1.color(random_co())
     t1.pensize(5)
     t1.forward(30)
     t1.speed("fastest")
     t1.setheading(random.choice(dirc))








s = Screen()

s.exitonclick()
