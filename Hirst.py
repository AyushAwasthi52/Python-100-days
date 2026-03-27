from turtle import Turtle, Screen, colormode
from random import choice

colormode(255)

colors = [(245, 239, 228), (236, 240, 247), (248, 238, 244), (235, 246, 241), (196, 158, 124), (64, 95, 125), (142, 87, 62), (139, 162, 184), (216, 209, 128), (184, 147, 159), (23, 36, 54), (122, 78, 93), (138, 179, 153), (46, 23, 16), (68, 114, 84), (54, 23, 34), (130, 25, 39), (20, 38, 29), (169, 156, 50), (188, 98, 85), (220, 174, 188), (125, 34, 25), (173, 99, 116), (226, 176, 168), (46, 59, 96), (163, 209, 179), (79, 156, 109), (113, 122, 157), (180, 187, 214), (31, 86, 62)]

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.goto(-225, -225)

def draw_line():
    tim.pendown()
    for _ in range(10):
        tim.dot(20, choice(colors))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)

for _ in range(10):
    draw_line()

screen = Screen()
screen.exitonclick()