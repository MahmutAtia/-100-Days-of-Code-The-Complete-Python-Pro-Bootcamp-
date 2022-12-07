from turtle import Turtle , Screen

#constants
heading = False



snake = Turtle(shape= "square")
snake.shapesize(1,4)
snake.color("DeepSkyBlue")


def up():
    snake.setheading(90)
def down():
    snake.setheading(270)
def right():
    snake.setheading(0)
def left():
    snake.setheading(180)
def moving():
    while True  :
        snake.forward(1)


s = Screen()
s.bgcolor("black")
s.screensize(400,400)
s.exitonclick()
#moving the snake
s.listen()
s.onkey(fun= up , key= "Up")
s.onkey(fun= down , key= "Down")
s.onkey(fun= left , key= "Left")
s.onkey(fun= right , key= "Right")













#The game
while True:
    snake.forward(1)