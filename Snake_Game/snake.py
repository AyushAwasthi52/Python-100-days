from turtle import Turtle
MOVE_DISTANCE = 20
START_POSITION = [[0,0],[20,0],[40,0]]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []

        for i in START_POSITION:
            turtleObj = Turtle()
            turtleObj.shape("square")
            turtleObj.color("white")
            turtleObj.hideturtle()
            turtleObj.penup()
            turtleObj.goto(i[0], i[1])
            turtleObj.showturtle()
            self.segments.append(turtleObj)
        
        self.head = self.segments[0]

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].xcor(), self.segments[i-1].ycor())
        
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def add_segments(self):
        if self.head.heading() == UP:
            new_x = self.segments[-1].xcor()
            new_y = self.segments[-1].ycor()-20
        elif self.head.heading() == DOWN:
            new_x = self.segments[-1].xcor()
            new_y = self.segments[-1].ycor()+20
        elif self.head.heading() == LEFT:
            new_x = self.segments[-1].xcor()+20
            new_y = self.segments[-1].ycor()
        else:
            new_x = self.segments[-1].xcor()-20
            new_y = self.segments[-1].ycor()
        turtleObj = Turtle()
        turtleObj.shape("square")
        turtleObj.color("white")
        turtleObj.hideturtle()
        turtleObj.penup()
        turtleObj.goto(new_x, new_y)
        turtleObj.showturtle()
        self.segments.append(turtleObj)