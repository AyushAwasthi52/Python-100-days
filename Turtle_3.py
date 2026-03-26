from turtle import Turtle, Screen

def draw(tim, angle):
    tim.forward(5)
    tim.right(angle)

tim = Turtle()
tim.shape("arrow")
tim.color("SpringGreen4")
tim.speed(0)
tim.pensize(5)
tim.penup()
tim.goto(-100, 200)
tim.pendown()

for i in range(3, 100000):
    angle = ((i-2)*180)/i
    for j in range(i):
        draw(tim, 180-angle)

screen = Screen()
screen.exitonclick()