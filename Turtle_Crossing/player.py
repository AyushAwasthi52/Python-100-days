from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.player = Turtle("turtle")
        self.player.penup()
        self.player.goto(STARTING_POSITION[0], STARTING_POSITION[1])
        self.player.left(90)

    def up(self):
        self.player.forward(MOVE_DISTANCE)

    def reached_finished_line(self):
        return self.player.ycor() >= FINISH_LINE_Y
    
    def return_to_start(self):
        self.player.goto(STARTING_POSITION)