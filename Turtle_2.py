from turtle import Turtle, Screen

def draw(tom):
    tom.penup()
    tom.forward(10)
    tom.pendown()
    tom.forward(10)

def line(tim):
    for _ in range(1, 20):
        draw(tim)
    tim.right(90)

tim = Turtle()
tim.shape("arrow")
tim.color("RosyBrown")

for _ in range(4):
    line(tim)

screen = Screen()
screen.exitonclick()