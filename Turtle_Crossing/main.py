import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

i = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.move_cars()
    cars.remove_cars()

    if cars.check_collision(player.player):
        score.gameOver()
        game_is_on = False

    if i==10:
        cars.generate_cars()
        i = 0

    if (player.reached_finished_line()):
        player.return_to_start()
        cars.level_up()
        score.update_Score()

    i = i+1

screen.exitonclick()
