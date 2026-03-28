from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(randint(-180,180), randint(-180, 180))
