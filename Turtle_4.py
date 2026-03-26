from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)

def random_rgb_color():
    """Generates a random RGB color tuple."""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color

def turn_left(tim):
    tim.left(90)

def turn_right(tim):
    tim.right(90)

def turn_back(tim):
    tim.right(90)
    tim.right(90)

tim = Turtle()
tim.shape("circle")
tim.pensize(5)

for _ in range(1000):
    color = random_rgb_color()
    speed = randint(0, 11)
    direction = randint(0, 4)
    steps = randint(1, 50)
    if direction == 1:
        turn_left(tim)
    if direction == 2:
        turn_right(tim)
    if direction == 3:
        turn_back(tim)
    tim.speed(speed)
    tim.color(color)
    tim.forward(steps)

screen = Screen()
screen.exitonclick()