import colorgram
from turtle import Turtle ,Screen ,colormode
import random

colormode(255)
rgb_colors = []
c = colorgram.extract("94bbb2f93e3e52de8507fbd22957b97c.jpg", 50)
for i in range(len (c)):
    color = c[i]
    rgb = color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    tup = (r,g,b)
    rgb_colors.append(tup)


t = Turtle()
t.hideturtle()
t.penup()
t.setheading(200)
t.forward(400)
t.setheading(0)
for _ in range(10):
    for _ in range(10):
        t.penup()
        t.forward(50)
        t.pendown()
        t.dot(10 , random.choice(rgb_colors))
    t.penup()
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)















s = Screen()
s.exitonclick()