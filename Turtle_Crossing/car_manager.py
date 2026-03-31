from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

START_X = 320
END_X = -320

CAR_Y_VALUES = [-250, -220, -190, -160, -130, -100, -70, -40, -10, 20, 30, 80, 110, 140, 170, 200, 230]

class CarManager:
    def __init__(self):
        self.cars = []
        self.generate_cars()

    def generate_cars(self):
        for i in CAR_Y_VALUES:
            random_number = random.randint(0, 10)
            if random_number == 0:
                temp_turtle_obj = Turtle("square")
                temp_turtle_obj.penup()
                temp_turtle_obj.color(random.choice(COLORS))
                temp_turtle_obj.goto(320, i)
                temp_turtle_obj.left(180)
                self.cars.append(temp_turtle_obj)

    def move_cars(self):
        for i in self.cars:
            i.forward(STARTING_MOVE_DISTANCE)

    def remove_cars(self):
        temp_list = []
        for i in self.cars:
            if i.xcor() > -320:
                temp_list.append(i)
            else:
                i.hideturtle()
        self.cars = temp_list

    def check_collision(self, player):
        for i in self.cars:
            if i.distance(player) < 15:
                return True
        return False
    
    def level_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
    