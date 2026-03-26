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

tim = Turtle()
tim.speed(0);
tim.pensize(2)

degree_of_seperation = 3

for _ in range(int(360/degree_of_seperation)):
    tim.color(random_rgb_color())
    tim.circle(100)
    tim.left(degree_of_seperation)

screen = Screen()
screen.exitonclick()