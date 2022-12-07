from turtle import Turtle , Screen
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


t = Turtle()
t.speed(10)
t.pensize(5)
i = 0
t.color(colours[i])
''' moving functions'''
def w():
    t.forward(5)
 
def s():
    t.backward(5)

def d():
    t.right(10)
def a():
    t.left(10)

def c():
    t.clear()

def co(i):
    i+=1
    t.color(colours[i])

def right():
    co()


s= Screen()
s.listen()
s.onkeypress(key= "w", fun= w)
s.onkeypress(key= "d", fun= d)
s.onkey(key= "s", fun= s)
s.onkeypress(key= "a", fun= a)
s.onkey(key= "c", fun= c)
#s.onkey("Right", fun= co)
s.exitonclick()