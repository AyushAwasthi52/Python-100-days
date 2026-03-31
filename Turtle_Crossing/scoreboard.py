from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.current_level = 1
        self.level = Turtle()
        self.level.penup()
        self.level.hideturtle()
        self.level.goto(-300, 300)
        self.level.write(f"Level: {self.current_level}", font=FONT)

    def gameOver(self):
        self.game_over = Turtle()
        self.game_over.penup()
        self.game_over.hideturtle()
        self.game_over.write("Game Over", font=FONT)

    def update_Score(self): 
        self.current_level += 1
        self.level.clear()
        self.level.write(f"Level: {self.current_level}", font=FONT)