from turtle import Turtle , Screen

s = Screen()
s.screensize(400 ,400, "black")

#constants

segments_pos = [(0,0)]
segments = []
t = Turtle()
for i in segments_pos:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(i)
    segments.append(new_segment)


game_on = True
while game_on:
  t.forward(1)








s.exitonclick()



