from  turtle import Turtle, Screen


#t = Turtle("square")
segments_pos = [(0,0),(-20,0),(-40,0)]
segments = []
for i in segments_pos:
    new_segment = Turtle(shape="square")
    new_segment.color("whi")
    new_segment.goto(i)






s = Screen()
s.exitonclick()