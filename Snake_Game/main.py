from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen._resize(400, 500)
screen.bgcolor("black")

screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segments()

screen.exitonclick()