from turtle import Turtle, Screen

def line(turt):
    turt.forward(100)
    turt.right(90)

tur = Turtle()
tur.shape("arrow")
tur.color("red")
tur.speed(1)
line(tur)
line(tur)
line(tur)
line(tur)

screen = Screen()
screen.exitonclick()