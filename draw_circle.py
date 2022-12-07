from turtle import Turtle , Screen, colormode
import random

colormode(255)
def random_co():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    tup = (r,g,b)
    return tup


t1= Turtle()
t1.speed("fastest")
for _ in range(36):
    t1.color(random_co())
    t1.circle(50)
    t1.setheading(i)
    i += 10


'''
t2 = Turtle()
t2.speed("fastest")
t2.setposition(100)
for i in range(360, step = 10):
    t2.color(random_co())
    t2.circle(50)
    t2.setheading(i)
'''





s = Screen()
s.exitonclick()